package com.anish.lld.patterns.creational;

public final class SingletonDemo {
    private static volatile SingletonDemo instance;

    private SingletonDemo() {
    }

    public static SingletonDemo getInstance() {
        if (instance == null) {
            synchronized (SingletonDemo.class) {
                if (instance == null) {
                    instance = new SingletonDemo();
                }
            }
        }
        return instance;
    }

    public static void run() {
        System.out.println("Singleton same instance: " + (getInstance() == getInstance()));
    }
}
