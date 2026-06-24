package com.anish.lld.patterns.behavioral;

import java.util.ArrayList;
import java.util.List;

class ChatRoom {
    private final List<User> users = new ArrayList<>();
    void join(User user) { users.add(user); }
    void send(User from, String message) {
        for (User user : users) if (user != from) user.receive(from.name(), message);
    }
}

record User(String name, ChatRoom room) {
    void send(String message) { room.send(this, message); }
    void receive(String from, String message) { System.out.println(name + " received from " + from + ": " + message); }
}

public class MediatorDemo {
    public static void run() {
        ChatRoom room = new ChatRoom();
        User anish = new User("Anish", room);
        User interviewer = new User("Interviewer", room);
        room.join(anish);
        room.join(interviewer);
        anish.send("Hello");
    }
}
