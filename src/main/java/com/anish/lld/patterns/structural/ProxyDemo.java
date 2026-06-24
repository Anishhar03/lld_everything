package com.anish.lld.patterns.structural;

interface ReportDownloader { String download(String reportId); }

class RealReportDownloader implements ReportDownloader {
    public String download(String reportId) { return "Report data for " + reportId; }
}

class SecureReportProxy implements ReportDownloader {
    private final ReportDownloader real = new RealReportDownloader();
    private final boolean admin;

    SecureReportProxy(boolean admin) { this.admin = admin; }

    public String download(String reportId) {
        if (!admin) throw new SecurityException("Only admin can download reports");
        return real.download(reportId);
    }
}

public class ProxyDemo {
    public static void run() {
        System.out.println("Proxy: " + new SecureReportProxy(true).download("R-101"));
    }
}
