package com.feiraviva.rota;

import android.os.Bundle;

import com.feiraviva.compras.ComprasPlugin;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(ComprasPlugin.class);   // compras pela Google Play (plugin próprio, não vem do npm)
        super.onCreate(savedInstanceState);
    }
}
