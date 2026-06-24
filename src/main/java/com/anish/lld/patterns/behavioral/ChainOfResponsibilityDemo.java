package com.anish.lld.patterns.behavioral;

abstract class RequestHandler {
    private RequestHandler next;
    RequestHandler linkWith(RequestHandler next) { this.next = next; return next; }
    void handle(String request) {
        if (process(request) && next != null) next.handle(request);
    }
    protected abstract boolean process(String request);
}

class AuthHandler extends RequestHandler {
    protected boolean process(String request) { System.out.println("Auth passed"); return true; }
}

class ValidationHandler extends RequestHandler {
    protected boolean process(String request) { System.out.println("Validation passed for " + request); return true; }
}

public class ChainOfResponsibilityDemo {
    public static void run() {
        RequestHandler chain = new AuthHandler();
        chain.linkWith(new ValidationHandler());
        chain.handle("CREATE_ORDER");
    }
}
