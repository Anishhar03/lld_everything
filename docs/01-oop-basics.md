# OOP Basics For LLD

Object-oriented programming helps model real-world systems as objects with state and behavior.

## Class

A class is a blueprint. It defines fields and methods.

Example:

```java
class User {
    private String name;
    public String getName() { return name; }
}
```

## Object

An object is an instance of a class.

## Encapsulation

Encapsulation means hiding internal state and exposing controlled behavior.

Bad:

```java
user.balance = -100;
```

Better:

```java
account.withdraw(100);
```

## Abstraction

Abstraction hides implementation details and exposes what matters.

Example: `PaymentGateway` can expose `pay()` while hiding Stripe/Razorpay/PayPal details.

## Inheritance

Inheritance models an "is-a" relationship. Use it carefully.

Example:

```java
class Car extends Vehicle {}
```

Prefer composition when behavior varies frequently.

## Polymorphism

Polymorphism allows the same interface to have different implementations.

Example:

```java
Payment payment = new CardPayment();
payment.pay(500);
```

## Association

One object uses or knows another object.

Example: A `Driver` is associated with a `Car`.

## Aggregation

A weak whole-part relationship. The part can exist independently.

Example: A `Team` has `Players`; players can exist without the team.

## Composition

A strong whole-part relationship. The part's lifecycle belongs to the whole.

Example: An `Order` has `OrderItems`; items usually do not exist independently outside the order.
