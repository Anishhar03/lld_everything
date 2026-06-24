package com.anish.lld.patterns.structural;

interface Device {
    void enable();
    void disable();
    boolean isEnabled();
}

class Tv implements Device {
    private boolean enabled;
    public void enable() { enabled = true; }
    public void disable() { enabled = false; }
    public boolean isEnabled() { return enabled; }
}

class Remote {
    protected final Device device;
    Remote(Device device) { this.device = device; }
    void togglePower() {
        if (device.isEnabled()) device.disable(); else device.enable();
    }
}

public class BridgeDemo {
    public static void run() {
        Device tv = new Tv();
        Remote remote = new Remote(tv);
        remote.togglePower();
        System.out.println("Bridge TV enabled: " + tv.isEnabled());
    }
}
