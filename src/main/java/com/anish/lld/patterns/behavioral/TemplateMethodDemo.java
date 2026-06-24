package com.anish.lld.patterns.behavioral;

abstract class DataImporter {
    final void importData() {
        read();
        validate();
        save();
    }
    abstract void read();
    void validate() { System.out.println("Common validation"); }
    abstract void save();
}

class CsvImporter extends DataImporter {
    void read() { System.out.println("Read CSV"); }
    void save() { System.out.println("Save CSV rows"); }
}

public class TemplateMethodDemo {
    public static void run() {
        new CsvImporter().importData();
    }
}
