package com.anish.lld.patterns.behavioral;

record EditorSnapshot(String text) {}

class Editor {
    private String text = "";
    void type(String value) { text += value; }
    EditorSnapshot save() { return new EditorSnapshot(text); }
    void restore(EditorSnapshot snapshot) { text = snapshot.text(); }
    String text() { return text; }
}

public class MementoDemo {
    public static void run() {
        Editor editor = new Editor();
        editor.type("LLD");
        EditorSnapshot snapshot = editor.save();
        editor.type(" advanced");
        editor.restore(snapshot);
        System.out.println("Memento: " + editor.text());
    }
}
