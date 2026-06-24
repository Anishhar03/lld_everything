package com.anish.lld.patterns.structural;

class InventoryService { boolean reserve(String sku) { System.out.println("Reserved " + sku); return true; } }
class PaymentService { boolean charge(int amount) { System.out.println("Charged " + amount); return true; } }
class InvoiceService { void generate() { System.out.println("Invoice generated"); } }

class CheckoutFacade {
    private final InventoryService inventory = new InventoryService();
    private final PaymentService payment = new PaymentService();
    private final InvoiceService invoice = new InvoiceService();

    void checkout(String sku, int amount) {
        if (inventory.reserve(sku) && payment.charge(amount)) {
            invoice.generate();
        }
    }
}

public class FacadeDemo {
    public static void run() {
        new CheckoutFacade().checkout("BOOK-1", 499);
    }
}
