# SOLID Principles

SOLID helps create maintainable, extensible designs.

## S - Single Responsibility Principle

A class should have one reason to change.

Bad: `Invoice` calculates total, saves to DB, and sends email.

Better:

- `Invoice`
- `InvoiceRepository`
- `InvoiceEmailService`

## O - Open Closed Principle

Code should be open for extension but closed for modification.

Use interfaces and polymorphism.

Example: Add `UPIPayment` without changing existing `PaymentProcessor`.

## L - Liskov Substitution Principle

Subclasses should be replaceable wherever the parent is expected.

Bad example: `Square extends Rectangle` if setting width/height breaks expected rectangle behavior.

## I - Interface Segregation Principle

Clients should not depend on methods they do not use.

Bad:

```java
interface Machine {
    void print();
    void scan();
    void fax();
}
```

Better:

- `Printer`
- `Scanner`
- `FaxMachine`

## D - Dependency Inversion Principle

High-level modules should depend on abstractions, not concrete classes.

Bad:

```java
class CheckoutService {
    private MySqlOrderRepository repo;
}
```

Better:

```java
class CheckoutService {
    private OrderRepository repo;
}
```
