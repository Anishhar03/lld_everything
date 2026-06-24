package com.anish.lld.patterns.structural;

import java.util.HashMap;
import java.util.Map;

record MarkerIcon(String type, String imagePath) {}

class MarkerIconFactory {
    private final Map<String, MarkerIcon> cache = new HashMap<>();
    MarkerIcon getIcon(String type) {
        return cache.computeIfAbsent(type, key -> new MarkerIcon(key, "/icons/" + key + ".png"));
    }
}

public class FlyweightDemo {
    public static void run() {
        MarkerIconFactory factory = new MarkerIconFactory();
        MarkerIcon restaurant1 = factory.getIcon("restaurant");
        MarkerIcon restaurant2 = factory.getIcon("restaurant");
        System.out.println("Flyweight shared: " + (restaurant1 == restaurant2));
    }
}
