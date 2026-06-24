package com.anish.lld.patterns.creational;

interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}

class SmsNotification implements Notification {
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}

class NotificationFactory {
    static Notification create(String type) {
        return switch (type.toLowerCase()) {
            case "email" -> new EmailNotification();
            case "sms" -> new SmsNotification();
            default -> throw new IllegalArgumentException("Unknown notification type: " + type);
        };
    }
}

public class FactoryMethodDemo {
    public static void run() {
        Notification notification = NotificationFactory.create("email");
        notification.send("Factory Method demo");
    }
}
