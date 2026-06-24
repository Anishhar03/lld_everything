package com.anish.lld.patterns.behavioral;

interface PricingStrategy {
    int finalPrice(int basePrice);
}

class RegularPricing implements PricingStrategy {
    public int finalPrice(int basePrice) {
        return basePrice;
    }
}

class FestivalPricing implements PricingStrategy {
    public int finalPrice(int basePrice) {
        return (int) (basePrice * 0.8);
    }
}

class Cart {
    private PricingStrategy pricingStrategy;

    Cart(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    void setPricingStrategy(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    int checkout(int basePrice) {
        return pricingStrategy.finalPrice(basePrice);
    }
}

public class StrategyDemo {
    public static void run() {
        Cart cart = new Cart(new RegularPricing());
        System.out.println("Strategy regular: " + cart.checkout(1000));
        cart.setPricingStrategy(new FestivalPricing());
        System.out.println("Strategy festival: " + cart.checkout(1000));
    }
}
