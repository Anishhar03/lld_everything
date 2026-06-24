package com.anish.lld.patterns.creational;

class DocumentTemplate implements Cloneable {
    private final String title;
    private final String body;

    DocumentTemplate(String title, String body) {
        this.title = title;
        this.body = body;
    }

    DocumentTemplate copyWithTitle(String newTitle) {
        return new DocumentTemplate(newTitle, body);
    }

    public String toString() {
        return "DocumentTemplate{title='" + title + "', body='" + body + "'}";
    }
}

public class PrototypeDemo {
    public static void run() {
        DocumentTemplate base = new DocumentTemplate("Base NDA", "Standard legal body");
        DocumentTemplate custom = base.copyWithTitle("Client NDA");
        System.out.println("Prototype: " + custom);
    }
}
