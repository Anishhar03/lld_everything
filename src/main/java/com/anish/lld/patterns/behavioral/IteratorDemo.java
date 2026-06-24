package com.anish.lld.patterns.behavioral;

import java.util.List;

class Playlist {
    private final List<String> songs = List.of("Intro", "LLD", "Patterns");
    java.util.Iterator<String> iterator() { return songs.iterator(); }
}

public class IteratorDemo {
    public static void run() {
        java.util.Iterator<String> iterator = new Playlist().iterator();
        while (iterator.hasNext()) {
            System.out.println("Iterator song: " + iterator.next());
        }
    }
}
