package com.anish.lld;

import com.anish.lld.patterns.behavioral.ObserverDemo;
import com.anish.lld.patterns.behavioral.StrategyDemo;
import com.anish.lld.patterns.creational.BuilderDemo;
import com.anish.lld.patterns.creational.FactoryMethodDemo;
import com.anish.lld.patterns.structural.AdapterDemo;
import com.anish.lld.patterns.structural.DecoratorDemo;

public class Main {
    public static void main(String[] args) {
        System.out.println("LLD Everything demos");
        FactoryMethodDemo.run();
        BuilderDemo.run();
        AdapterDemo.run();
        DecoratorDemo.run();
        StrategyDemo.run();
        ObserverDemo.run();
    }
}
