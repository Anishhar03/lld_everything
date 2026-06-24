package com.anish.lld.patterns.behavioral;

interface Command { void execute(); void undo(); }

class Light {
    void on() { System.out.println("Light on"); }
    void off() { System.out.println("Light off"); }
}

class LightOnCommand implements Command {
    private final Light light;
    LightOnCommand(Light light) { this.light = light; }
    public void execute() { light.on(); }
    public void undo() { light.off(); }
}

public class CommandDemo {
    public static void run() {
        Command command = new LightOnCommand(new Light());
        command.execute();
        command.undo();
    }
}
