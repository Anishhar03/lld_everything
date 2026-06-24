package com.anish.lld.patterns.structural;

interface Coffee {
    int cost();
    String description();
}

class SimpleCoffee implements Coffee {
    public int cost() {
        return 50;
    }

    public String description() {
        return "Coffee";
    }
}

abstract class CoffeeDecorator implements Coffee {
    protected final Coffee coffee;

    CoffeeDecorator(Coffee coffee) {
        this.coffee = coffee;
    }
}

class MilkDecorator extends CoffeeDecorator {
    MilkDecorator(Coffee coffee) {
        super(coffee);
    }

    public int cost() {
        return coffee.cost() + 10;
    }

    public String description() {
        return coffee.description() + ", milk";
    }
}

public class DecoratorDemo {
    public static void run() {
        Coffee coffee = new MilkDecorator(new SimpleCoffee());
        System.out.println("Decorator: " + coffee.description() + " costs " + coffee.cost());
    }
}
