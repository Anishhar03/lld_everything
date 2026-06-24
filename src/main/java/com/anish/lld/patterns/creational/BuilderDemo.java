package com.anish.lld.patterns.creational;

public class BuilderDemo {
    static class HttpRequest {
        private final String method;
        private final String url;
        private final String body;
        private final int timeoutMs;

        private HttpRequest(Builder builder) {
            this.method = builder.method;
            this.url = builder.url;
            this.body = builder.body;
            this.timeoutMs = builder.timeoutMs;
        }

        static class Builder {
            private String method = "GET";
            private String url;
            private String body = "";
            private int timeoutMs = 3000;

            Builder url(String url) {
                this.url = url;
                return this;
            }

            Builder method(String method) {
                this.method = method;
                return this;
            }

            Builder body(String body) {
                this.body = body;
                return this;
            }

            Builder timeoutMs(int timeoutMs) {
                this.timeoutMs = timeoutMs;
                return this;
            }

            HttpRequest build() {
                if (url == null || url.isBlank()) {
                    throw new IllegalStateException("URL is required");
                }
                return new HttpRequest(this);
            }
        }

        public String toString() {
            return method + " " + url + " timeout=" + timeoutMs + " body=" + body;
        }
    }

    public static void run() {
        HttpRequest request = new HttpRequest.Builder()
                .url("https://example.com/orders")
                .method("POST")
                .body("{orderId: 101}")
                .timeoutMs(5000)
                .build();
        System.out.println("Builder: " + request);
    }
}
