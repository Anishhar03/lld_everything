package com.anish.lld;

import com.anish.lld.patterns.behavioral.*;
import com.anish.lld.patterns.creational.*;
import com.anish.lld.patterns.structural.*;

public class Main {
    public static void main(String[] args) {
        System.out.println("LLD Everything: running all design pattern demos");
        SingletonDemo.run();
        FactoryMethodDemo.run();
        AbstractFactoryDemo.run();
        BuilderDemo.run();
        PrototypeDemo.run();
        AdapterDemo.run();
        BridgeDemo.run();
        CompositeDemo.run();
        DecoratorDemo.run();
        FacadeDemo.run();
        FlyweightDemo.run();
        ProxyDemo.run();
        ChainOfResponsibilityDemo.run();
        CommandDemo.run();
        IteratorDemo.run();
        MediatorDemo.run();
        MementoDemo.run();
        ObserverDemo.run();
        StateDemo.run();
        StrategyDemo.run();
        TemplateMethodDemo.run();
        VisitorDemo.run();
    }
}
