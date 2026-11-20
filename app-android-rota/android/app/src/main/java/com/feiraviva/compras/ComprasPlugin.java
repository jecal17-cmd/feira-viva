package com.feiraviva.compras;

import android.util.Base64;
import android.util.Log;

import com.android.billingclient.api.AcknowledgePurchaseParams;
import com.android.billingclient.api.BillingClient;
import com.android.billingclient.api.BillingClient.BillingResponseCode;
import com.android.billingclient.api.BillingClientStateListener;
import com.android.billingclient.api.BillingFlowParams;
import com.android.billingclient.api.BillingResult;
import com.android.billingclient.api.ConsumeParams;
import com.android.billingclient.api.PendingPurchasesParams;
import com.android.billingclient.api.ProductDetails;
import com.android.billingclient.api.Purchase;
import com.android.billingclient.api.PurchasesUpdatedListener;
import com.android.billingclient.api.QueryProductDetailsParams;
import com.android.billingclient.api.QueryPurchasesParams;
import com.getcapacitor.JSArray;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

import java.security.KeyFactory;
import java.security.PublicKey;
import java.security.Signature;
import java.security.spec.X509EncodedKeySpec;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * Compras com dinheiro real pela Google Play (Play Billing 8), para o jogo em HTML.
 * Mesmo arquivo nos dois apps (Quitanda e Rota das Feiras).
 *
 * Métodos chamados pelo jogo (window.Capacitor.Plugins.Compras):
 *   produtos({ids})          → {itens:[{id, preco, micros, moeda, titulo}]}   preços na moeda do jogador
 *   comprar({id})            → {codigo, msg}   abre a tela de pagamento; a compra chega pelo aviso "compras"
 *   pendentes()              → {compras:[...]}  compras que o jogador tem e ainda não foram consumidas
 *   concluir({token, consumir}) → {codigo}       consome (consumíveis) ou reconhece (permanentes)
 * Aviso "compras": {codigo, compras:[{token, ids, estado, reconhecida, pedido, qtd, valida}]}
 *
 * Se a chave de licença do app (Play Console → Monetizar → Configuração de monetização) estiver no recurso
 * play_license_key, a assinatura de cada compra é conferida aqui (valida=false = compra falsificada).
 */
@CapacitorPlugin(name = "Compras")
public class ComprasPlugin extends Plugin implements PurchasesUpdatedListener {

    private static final String TAG = "Compras";

    private interface Pronto {
        void ok();
        void falhou(BillingResult r);
    }

    private BillingClient cliente;
    private final Map<String, ProductDetails> detalhes = new ConcurrentHashMap<>();
    private final List<Pronto> fila = new ArrayList<>();
    private boolean conectando = false;
    private String chave = "";

    @Override
    public void load() {
        int id = getContext().getResources().getIdentifier("play_license_key", "string", getContext().getPackageName());
        if (id != 0) chave = getContext().getString(id).trim();
        cliente = BillingClient.newBuilder(getContext())
                .setListener(this)
                .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
                .enableAutoServiceReconnection()
                .build();
    }

    @Override
    protected void handleOnDestroy() {
        if (cliente != null) cliente.endConnection();
    }

    // ---------- conexão com a Google Play ----------

    private void conectar(Pronto p) {
        if (cliente.isReady()) {
            p.ok();
            return;
        }
        boolean iniciar;
        synchronized (fila) {
            fila.add(p);
            iniciar = !conectando;
            conectando = true;
        }
        if (!iniciar) return;
        cliente.startConnection(new BillingClientStateListener() {
            @Override
            public void onBillingSetupFinished(BillingResult r) {
                for (Pronto x : esvaziar()) {
                    if (r.getResponseCode() == BillingResponseCode.OK) x.ok();
                    else x.falhou(r);
                }
            }

            @Override
            public void onBillingServiceDisconnected() {
                BillingResult r = BillingResult.newBuilder()
                        .setResponseCode(BillingResponseCode.SERVICE_DISCONNECTED)
                        .setDebugMessage("Google Play desconectada").build();
                for (Pronto x : esvaziar()) x.falhou(r);
            }
        });
    }

    private List<Pronto> esvaziar() {
        synchronized (fila) {
            List<Pronto> l = new ArrayList<>(fila);
            fila.clear();
            conectando = false;
            return l;
        }
    }

    private static void recusar(PluginCall call, BillingResult r) {
        call.reject(r.getDebugMessage() == null ? "erro da Google Play" : r.getDebugMessage(), String.valueOf(r.getResponseCode()));
    }

    // ---------- métodos do jogo ----------

    @PluginMethod
    public void produtos(PluginCall call) {
        JSArray ids = call.getArray("ids");
        final List<String> lista = new ArrayList<>();
        try {
            if (ids != null) for (Object o : ids.toList()) lista.add(String.valueOf(o));
        } catch (Exception e) {
            call.reject("ids inválidos");
            return;
        }
        if (lista.isEmpty()) {
            JSObject ret = new JSObject();
            ret.put("itens", new JSArray());
            call.resolve(ret);
            return;
        }
        conectar(new Pronto() {
            @Override
            public void ok() {
                List<QueryProductDetailsParams.Product> ps = new ArrayList<>();
                for (String id : lista) {
                    ps.add(QueryProductDetailsParams.Product.newBuilder()
                            .setProductId(id)
                            .setProductType(BillingClient.ProductType.INAPP)
                            .build());
                }
                QueryProductDetailsParams params = QueryProductDetailsParams.newBuilder().setProductList(ps).build();
                cliente.queryProductDetailsAsync(params, (r, resultado) -> {
                    if (r.getResponseCode() != BillingResponseCode.OK) {
                        recusar(call, r);
                        return;
                    }
                    JSArray itens = new JSArray();
                    for (ProductDetails d : resultado.getProductDetailsList()) {
                        ProductDetails.OneTimePurchaseOfferDetails o = d.getOneTimePurchaseOfferDetails();
                        if (o == null) continue;
                        detalhes.put(d.getProductId(), d);
                        JSObject j = new JSObject();
                        j.put("id", d.getProductId());
                        j.put("preco", o.getFormattedPrice());
                        j.put("micros", o.getPriceAmountMicros());
                        j.put("moeda", o.getPriceCurrencyCode());
                        j.put("titulo", d.getName());
                        itens.put(j);
                    }
                    JSObject ret = new JSObject();
                    ret.put("itens", itens);
                    call.resolve(ret);
                });
            }

            @Override
            public void falhou(BillingResult r) {
                recusar(call, r);
            }
        });
    }

    @PluginMethod
    public void comprar(PluginCall call) {
        final String id = call.getString("id");
        final ProductDetails d = id == null ? null : detalhes.get(id);
        if (d == null) {
            JSObject ret = new JSObject();
            ret.put("codigo", BillingResponseCode.ITEM_UNAVAILABLE);
            ret.put("msg", "produto não carregado: " + id);
            call.resolve(ret);
            return;
        }
        conectar(new Pronto() {
            @Override
            public void ok() {
                BillingFlowParams params = BillingFlowParams.newBuilder()
                        .setProductDetailsParamsList(Collections.singletonList(
                                BillingFlowParams.ProductDetailsParams.newBuilder().setProductDetails(d).build()))
                        .build();
                getActivity().runOnUiThread(() -> {
                    BillingResult r = cliente.launchBillingFlow(getActivity(), params);
                    JSObject ret = new JSObject();
                    ret.put("codigo", r.getResponseCode());
                    ret.put("msg", r.getDebugMessage());
                    call.resolve(ret);
                });
            }

            @Override
            public void falhou(BillingResult r) {
                JSObject ret = new JSObject();
                ret.put("codigo", r.getResponseCode());
                ret.put("msg", r.getDebugMessage());
                call.resolve(ret);
            }
        });
    }

    @PluginMethod
    public void pendentes(PluginCall call) {
        conectar(new Pronto() {
            @Override
            public void ok() {
                QueryPurchasesParams params = QueryPurchasesParams.newBuilder()
                        .setProductType(BillingClient.ProductType.INAPP).build();
                cliente.queryPurchasesAsync(params, (r, lista) -> {
                    if (r.getResponseCode() != BillingResponseCode.OK) {
                        recusar(call, r);
                        return;
                    }
                    JSObject ret = new JSObject();
                    ret.put("compras", emJson(lista));
                    call.resolve(ret);
                });
            }

            @Override
            public void falhou(BillingResult r) {
                recusar(call, r);
            }
        });
    }

    @PluginMethod
    public void concluir(PluginCall call) {
        final String token = call.getString("token");
        final boolean consumir = Boolean.TRUE.equals(call.getBoolean("consumir", true));
        if (token == null || token.isEmpty()) {
            call.reject("token vazio");
            return;
        }
        conectar(new Pronto() {
            @Override
            public void ok() {
                if (consumir) {
                    ConsumeParams p = ConsumeParams.newBuilder().setPurchaseToken(token).build();
                    cliente.consumeAsync(p, (r, t) -> responder(call, r));
                } else {
                    AcknowledgePurchaseParams p = AcknowledgePurchaseParams.newBuilder().setPurchaseToken(token).build();
                    cliente.acknowledgePurchase(p, r -> responder(call, r));
                }
            }

            @Override
            public void falhou(BillingResult r) {
                responder(call, r);
            }
        });
    }

    private static void responder(PluginCall call, BillingResult r) {
        JSObject ret = new JSObject();
        ret.put("codigo", r.getResponseCode());
        ret.put("msg", r.getDebugMessage());
        call.resolve(ret);
    }

    // ---------- avisos da Google Play ----------

    @Override
    public void onPurchasesUpdated(BillingResult r, List<Purchase> lista) {
        JSObject ev = new JSObject();
        ev.put("codigo", r.getResponseCode());
        ev.put("compras", emJson(lista));
        notifyListeners("compras", ev, true);   // guarda o aviso se o jogo ainda não estiver ouvindo
    }

    private JSArray emJson(List<Purchase> lista) {
        JSArray arr = new JSArray();
        if (lista == null) return arr;
        for (Purchase p : lista) {
            JSObject j = new JSObject();
            JSArray ids = new JSArray();
            for (String id : p.getProducts()) ids.put(id);
            int st = p.getPurchaseState();
            j.put("token", p.getPurchaseToken());
            j.put("ids", ids);
            j.put("estado", st == Purchase.PurchaseState.PURCHASED ? "comprado" : st == Purchase.PurchaseState.PENDING ? "pendente" : "outro");
            j.put("reconhecida", p.isAcknowledged());
            j.put("pedido", p.getOrderId() == null ? "" : p.getOrderId());
            j.put("qtd", p.getQuantity());
            j.put("valida", assinaturaOk(p.getOriginalJson(), p.getSignature()));
            arr.put(j);
        }
        return arr;
    }

    /** Confere a assinatura da compra com a chave de licença do app. Sem chave configurada, aceita. */
    private boolean assinaturaOk(String dados, String assinatura) {
        if (chave.isEmpty()) return true;
        try {
            byte[] k = Base64.decode(chave, Base64.DEFAULT);
            PublicKey pub = KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(k));
            Signature s = Signature.getInstance("SHA1withRSA");
            s.initVerify(pub);
            s.update(dados.getBytes("UTF-8"));
            return s.verify(Base64.decode(assinatura, Base64.DEFAULT));
        } catch (Exception e) {
            Log.w(TAG, "Não deu para conferir a assinatura", e);
            return false;
        }
    }
}
