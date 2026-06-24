package com.anish.lld.patterns.creational;

interface Button { void render(); }
interface Checkbox { void render(); }
interface UiFactory { Button createButton(); Checkbox createCheckbox(); }

class WindowsButton implements Button { public void render() { System.out.println("Windows button"); } }
class WindowsCheckbox implements Checkbox { public void render() { System.out.println("Windows checkbox"); } }
class MacButton implements Button { public void render() { System.out.println("Mac button"); } }
class MacCheckbox implements Checkbox { public void render() { System.out.println("Mac checkbox"); } }

class WindowsFactory implements UiFactory {
    public Button createButton() { return new WindowsButton(); }
    public Checkbox createCheckbox() { return new WindowsCheckbox(); }
}

class MacFactory implements UiFactory {
    public Button createButton() { return new MacButton(); }
    public Checkbox createCheckbox() { return new MacCheckbox(); }
}

public class AbstractFactoryDemo {
    public static void run() {
        UiFactory factory = new MacFactory();
        factory.createButton().render();
        factory.createCheckbox().render();
    }
}
