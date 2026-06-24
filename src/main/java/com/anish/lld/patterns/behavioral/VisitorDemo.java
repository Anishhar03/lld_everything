package com.anish.lld.patterns.behavioral;

interface CartItem { int accept(TaxVisitor visitor); }
class BookItem implements CartItem { public int accept(TaxVisitor visitor) { return visitor.tax(this); } }
class ElectronicsItem implements CartItem { public int accept(TaxVisitor visitor) { return visitor.tax(this); } }

interface TaxVisitor {
    int tax(BookItem item);
    int tax(ElectronicsItem item);
}

class IndiaTaxVisitor implements TaxVisitor {
    public int tax(BookItem item) { return 5; }
    public int tax(ElectronicsItem item) { return 18; }
}

public class VisitorDemo {
    public static void run() {
        TaxVisitor visitor = new IndiaTaxVisitor();
        System.out.println("Visitor book tax: " + new BookItem().accept(visitor));
        System.out.println("Visitor electronics tax: " + new ElectronicsItem().accept(visitor));
    }
}
