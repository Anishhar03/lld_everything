package com.anish.lld.patterns.behavioral;

import java.util.ArrayList;
import java.util.List;

interface Subscriber {
    void update(String event);
}

class EmailSubscriber implements Subscriber {
    private final String email;

    EmailSubscriber(String email) {
        this.email = email;
    }

    public void update(String event) {
        System.out.println(email + " received: " + event);
    }
}

class EventPublisher {
    private final List<Subscriber> subscribers = new ArrayList<>();

    void subscribe(Subscriber subscriber) {
        subscribers.add(subscriber);
    }

    void publish(String event) {
        for (Subscriber subscriber : subscribers) {
            subscriber.update(event);
        }
    }
}

public class ObserverDemo {
    public static void run() {
        EventPublisher publisher = new EventPublisher();
        publisher.subscribe(new EmailSubscriber("anish@example.com"));
        publisher.publish("Observer demo event");
    }
}
