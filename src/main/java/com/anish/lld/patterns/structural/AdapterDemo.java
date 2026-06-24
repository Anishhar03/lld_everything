package com.anish.lld.patterns.structural;

interface PaymentProcessor {
    void pay(int amount);
}

class LegacyPaymentApi {
    void makePaymentInPaise(int amountInPaise) {
        System.out.println("Legacy payment processed: " + amountInPaise + " paise");
    }
}

class LegacyPaymentAdapter implements PaymentProcessor {
    private final LegacyPaymentApi legacyPaymentApi;

    LegacyPaymentAdapter(LegacyPaymentApi legacyPaymentApi) {
        this.legacyPaymentApi = legacyPaymentApi;
    }

    public void pay(int amount) {
        legacyPaymentApi.makePaymentInPaise(amount * 100);
    }
}

public class AdapterDemo {
    public static void run() {
        PaymentProcessor processor = new LegacyPaymentAdapter(new LegacyPaymentApi());
        processor.pay(250);
    }
}
