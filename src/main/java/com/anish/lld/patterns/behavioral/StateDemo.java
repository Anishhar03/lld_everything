package com.anish.lld.patterns.behavioral;

interface OrderState { void next(OrderContext order); String name(); }

class CreatedState implements OrderState {
    public void next(OrderContext order) { order.setState(new PaidState()); }
    public String name() { return "CREATED"; }
}

class PaidState implements OrderState {
    public void next(OrderContext order) { order.setState(new ShippedState()); }
    public String name() { return "PAID"; }
}

class ShippedState implements OrderState {
    public void next(OrderContext order) { System.out.println("Already shipped"); }
    public String name() { return "SHIPPED"; }
}

class OrderContext {
    private OrderState state = new CreatedState();
    void setState(OrderState state) { this.state = state; }
    void next() { state.next(this); }
    String state() { return state.name(); }
}

public class StateDemo {
    public static void run() {
        OrderContext order = new OrderContext();
        order.next();
        order.next();
        System.out.println("State: " + order.state());
    }
}
