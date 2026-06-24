package com.anish.lld.patterns.structural;

import java.util.ArrayList;
import java.util.List;

interface FileSystemNode { int size(); }

class FileNode implements FileSystemNode {
    private final int size;
    FileNode(int size) { this.size = size; }
    public int size() { return size; }
}

class FolderNode implements FileSystemNode {
    private final List<FileSystemNode> children = new ArrayList<>();
    void add(FileSystemNode node) { children.add(node); }
    public int size() { return children.stream().mapToInt(FileSystemNode::size).sum(); }
}

public class CompositeDemo {
    public static void run() {
        FolderNode root = new FolderNode();
        root.add(new FileNode(10));
        FolderNode nested = new FolderNode();
        nested.add(new FileNode(20));
        root.add(nested);
        System.out.println("Composite size: " + root.size());
    }
}
