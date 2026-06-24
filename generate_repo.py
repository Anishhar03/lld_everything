from pathlib import Path


ROOT = Path(__file__).resolve().parent


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content.strip() + "\n", encoding="utf-8")


def slug(name: str) -> str:
    return name.lower().replace(" ", "-")


overview = """
# LLD Everything

A complete, beginner-friendly Low Level Design repository inspired by the playlist:

https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW

The goal of this repo is to make LLD easy to revise for interviews and practical machine-coding rounds. It includes:

- OOP fundamentals
- UML basics
- SOLID principles
- GoF design patterns
- Concurrency and practical engineering patterns
- Classic LLD interview problems
- Runnable Java implementations
- Easy explanations, tradeoffs, and interview notes

## How To Use This Repo

1. Start with `docs/00-roadmap.md`.
2. Revise OOP and SOLID from `docs/01-oop-basics.md` and `docs/02-solid-principles.md`.
3. Study patterns category-wise from `design-patterns/`.
4. Run Java demos from `src/main/java/com/anish/lld`.
5. Practice system designs from `case-studies/`.

## Run Examples

```bash
mvn test
mvn exec:java -Dexec.mainClass="com.anish.lld.Main"
```

If Maven is not installed, the source files are still readable as standalone Java examples.

## Repository Map

```text
docs/                 Core LLD notes
design-patterns/      Pattern-wise README explanations
src/main/java/         Java implementations
case-studies/          LLD interview problems and workflows
interview-prep/        Revision sheets and questions
```
"""


roadmap = """
# LLD Roadmap

Low Level Design is the skill of converting requirements into classes, interfaces, objects, relationships, and maintainable code.

## Learning Order

1. Understand requirements and use cases.
2. Identify nouns and verbs.
3. Convert nouns into entities/value objects/services.
4. Convert verbs into methods and workflows.
5. Define relationships: association, aggregation, composition, inheritance, dependency.
6. Apply SOLID principles.
7. Use design patterns only where they reduce real complexity.
8. Think about concurrency, extensibility, testing, and failure cases.

## Interview Flow

For any LLD problem:

1. Clarify requirements.
2. Define scope and assumptions.
3. Identify actors and core use cases.
4. Define entities and relationships.
5. Design APIs/classes.
6. Explain patterns used.
7. Discuss edge cases.
8. Discuss scaling and concurrency.
9. Write clean code.
10. Add tests or sample flows.

## What Interviewers Check

- Can you convert vague requirements into clear objects?
- Do you avoid overengineering?
- Do your classes have single responsibility?
- Can your design support new features?
- Do you understand tradeoffs?
- Can you code the design cleanly?
"""


oop = """
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
"""


solid = """
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
"""


uml = """
# UML Basics For LLD

UML diagrams help explain class relationships quickly.

## Class Box

```text
+------------------+
|      User        |
+------------------+
| - id: String     |
| - name: String   |
+------------------+
| + login(): void  |
+------------------+
```

## Visibility

- `+` public
- `-` private
- `#` protected
- `~` package-private

## Relationships

### Association

`User --> Order`

User knows about Order.

### Aggregation

`Team o-- Player`

Weak ownership.

### Composition

`Order *-- OrderItem`

Strong ownership.

### Inheritance

`Car --|> Vehicle`

Car is a Vehicle.

### Dependency

`CheckoutService ..> PaymentGateway`

CheckoutService temporarily uses PaymentGateway.
"""


requirements = """
# Requirement Gathering In LLD

Most LLD failures happen before coding: unclear requirements create confused classes.

## Ask These Questions

- Who are the actors?
- What are the main use cases?
- What is in scope?
- What is out of scope?
- What are the constraints?
- Are there concurrency requirements?
- Are there persistence requirements?
- What should happen on failure?
- What extension points are expected?

## Convert Requirements To Design

Example requirement:

"Users should be able to book movie tickets."

Nouns:

- User
- Movie
- Theatre
- Show
- Seat
- Ticket
- Payment

Verbs:

- search movie
- select show
- lock seat
- make payment
- confirm booking
- cancel booking

Possible classes:

- `User`
- `Movie`
- `Theatre`
- `Show`
- `Seat`
- `Booking`
- `Payment`
- `BookingService`
- `SeatLockService`
"""


patterns = [
    ("Singleton", "Creational", "Ensure a class has only one instance and provide a global access point.", "Configuration manager, logger, connection registry."),
    ("Factory Method", "Creational", "Let subclasses or factory methods decide which object to create.", "Notification sender, parser selection, payment type creation."),
    ("Abstract Factory", "Creational", "Create families of related objects without binding code to concrete classes.", "UI widgets for Windows/Mac, cloud provider resources."),
    ("Builder", "Creational", "Construct complex objects step by step while keeping construction readable.", "HTTP request, user profile, immutable config."),
    ("Prototype", "Creational", "Create new objects by copying existing objects.", "Game objects, document templates, expensive object cloning."),
    ("Adapter", "Structural", "Make incompatible interfaces work together.", "Integrating third-party payment or SMS APIs."),
    ("Bridge", "Structural", "Separate abstraction from implementation so both can vary independently.", "Remote controls and devices, notification channel and message type."),
    ("Composite", "Structural", "Represent part-whole trees and treat leaf and group uniformly.", "File system, organization hierarchy, menu tree."),
    ("Decorator", "Structural", "Add behavior dynamically without changing the original class.", "Coffee add-ons, stream wrappers, middleware."),
    ("Facade", "Structural", "Provide a simple interface over a complex subsystem.", "Checkout facade hiding inventory, payment, invoice, notification."),
    ("Flyweight", "Structural", "Share common immutable state to reduce memory usage.", "Text editor characters, map markers, game particles."),
    ("Proxy", "Structural", "Control access to another object.", "Caching proxy, security proxy, lazy loading proxy."),
    ("Chain Of Responsibility", "Behavioral", "Pass a request through handlers until one handles it.", "Logging pipeline, support escalation, validation chain."),
    ("Command", "Behavioral", "Encapsulate a request as an object.", "Undo/redo, job queues, button actions."),
    ("Iterator", "Behavioral", "Traverse a collection without exposing internal structure.", "Custom collections, paginated data traversal."),
    ("Mediator", "Behavioral", "Centralize communication between many objects.", "Chat room, UI dialog controls, air traffic control."),
    ("Memento", "Behavioral", "Capture and restore object state without exposing internals.", "Undo, editor snapshots, game save points."),
    ("Observer", "Behavioral", "Notify subscribers when state changes.", "Event systems, stock price alerts, pub-sub."),
    ("State", "Behavioral", "Change behavior when internal state changes.", "Order lifecycle, vending machine, document workflow."),
    ("Strategy", "Behavioral", "Select an algorithm at runtime.", "Payment strategy, sorting strategy, pricing strategy."),
    ("Template Method", "Behavioral", "Define algorithm skeleton while subclasses customize steps.", "Report generation, data import workflows."),
    ("Visitor", "Behavioral", "Add operations to object structures without changing their classes.", "AST processing, tax calculation across item types."),
]


main_java = """
package com.anish.lld;

import com.anish.lld.patterns.behavioral.ObserverDemo;
import com.anish.lld.patterns.behavioral.StrategyDemo;
import com.anish.lld.patterns.creational.BuilderDemo;
import com.anish.lld.patterns.creational.FactoryMethodDemo;
import com.anish.lld.patterns.structural.AdapterDemo;
import com.anish.lld.patterns.structural.DecoratorDemo;

public class Main {
    public static void main(String[] args) {
        System.out.println("LLD Everything demos");
        FactoryMethodDemo.run();
        BuilderDemo.run();
        AdapterDemo.run();
        DecoratorDemo.run();
        StrategyDemo.run();
        ObserverDemo.run();
    }
}
"""


pom = """
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.anish</groupId>
    <artifactId>lld-everything</artifactId>
    <version>1.0.0</version>
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>5.10.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>
            <plugin>
                <groupId>org.codehaus.mojo</groupId>
                <artifactId>exec-maven-plugin</artifactId>
                <version>3.3.0</version>
            </plugin>
        </plugins>
    </build>
</project>
"""


factory_java = """
package com.anish.lld.patterns.creational;

interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    public void send(String message) {
        System.out.println("Email: " + message);
    }
}

class SmsNotification implements Notification {
    public void send(String message) {
        System.out.println("SMS: " + message);
    }
}

class NotificationFactory {
    static Notification create(String type) {
        return switch (type.toLowerCase()) {
            case "email" -> new EmailNotification();
            case "sms" -> new SmsNotification();
            default -> throw new IllegalArgumentException("Unknown notification type: " + type);
        };
    }
}

public class FactoryMethodDemo {
    public static void run() {
        Notification notification = NotificationFactory.create("email");
        notification.send("Factory Method demo");
    }
}
"""


builder_java = """
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
"""


singleton_java = """
package com.anish.lld.patterns.creational;

public final class SingletonDemo {
    private static volatile SingletonDemo instance;

    private SingletonDemo() {
    }

    public static SingletonDemo getInstance() {
        if (instance == null) {
            synchronized (SingletonDemo.class) {
                if (instance == null) {
                    instance = new SingletonDemo();
                }
            }
        }
        return instance;
    }

    public static void run() {
        System.out.println("Singleton same instance: " + (getInstance() == getInstance()));
    }
}
"""


adapter_java = """
package com.anish.lld.patterns.structural;

interface PaymentProcessor {
    void pay(int amount);
}

class LegacyPaymentApi {
    void makePaymentInPaise(int amountInPaise) {
        System.out.println("Legacy payment processed: " + amountInPaise + " paise");
    }
}

class LegacyPaymentAdapter implements PaymentProcessor {
    private final LegacyPaymentApi legacyPaymentApi;

    LegacyPaymentAdapter(LegacyPaymentApi legacyPaymentApi) {
        this.legacyPaymentApi = legacyPaymentApi;
    }

    public void pay(int amount) {
        legacyPaymentApi.makePaymentInPaise(amount * 100);
    }
}

public class AdapterDemo {
    public static void run() {
        PaymentProcessor processor = new LegacyPaymentAdapter(new LegacyPaymentApi());
        processor.pay(250);
    }
}
"""


decorator_java = """
package com.anish.lld.patterns.structural;

interface Coffee {
    int cost();
    String description();
}

class SimpleCoffee implements Coffee {
    public int cost() {
        return 50;
    }

    public String description() {
        return "Coffee";
    }
}

abstract class CoffeeDecorator implements Coffee {
    protected final Coffee coffee;

    CoffeeDecorator(Coffee coffee) {
        this.coffee = coffee;
    }
}

class MilkDecorator extends CoffeeDecorator {
    MilkDecorator(Coffee coffee) {
        super(coffee);
    }

    public int cost() {
        return coffee.cost() + 10;
    }

    public String description() {
        return coffee.description() + ", milk";
    }
}

public class DecoratorDemo {
    public static void run() {
        Coffee coffee = new MilkDecorator(new SimpleCoffee());
        System.out.println("Decorator: " + coffee.description() + " costs " + coffee.cost());
    }
}
"""


strategy_java = """
package com.anish.lld.patterns.behavioral;

interface PricingStrategy {
    int finalPrice(int basePrice);
}

class RegularPricing implements PricingStrategy {
    public int finalPrice(int basePrice) {
        return basePrice;
    }
}

class FestivalPricing implements PricingStrategy {
    public int finalPrice(int basePrice) {
        return (int) (basePrice * 0.8);
    }
}

class Cart {
    private PricingStrategy pricingStrategy;

    Cart(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    void setPricingStrategy(PricingStrategy pricingStrategy) {
        this.pricingStrategy = pricingStrategy;
    }

    int checkout(int basePrice) {
        return pricingStrategy.finalPrice(basePrice);
    }
}

public class StrategyDemo {
    public static void run() {
        Cart cart = new Cart(new RegularPricing());
        System.out.println("Strategy regular: " + cart.checkout(1000));
        cart.setPricingStrategy(new FestivalPricing());
        System.out.println("Strategy festival: " + cart.checkout(1000));
    }
}
"""


observer_java = """
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
"""


case_studies = {
    "parking-lot": "Design a parking lot with multiple floors, spot types, tickets, pricing, entry gates, exit gates, and payment.",
    "elevator-system": "Design elevators that handle requests, direction, scheduling, floors, doors, and emergency behavior.",
    "bookmyshow": "Design movie ticket booking with theatres, shows, seats, seat locking, booking, payment, and cancellation.",
    "splitwise": "Design expense sharing with groups, users, expenses, splits, balances, and settlement.",
    "snake-and-ladder": "Design a board game with dice, players, snakes, ladders, and win conditions.",
    "chess": "Design chess with board, pieces, moves, validations, check, checkmate, and turn handling.",
    "logger": "Design a logger with log levels, appenders, formatters, and chain of responsibility.",
    "cache": "Design an in-memory cache with eviction policies like LRU and TTL.",
    "vending-machine": "Design a vending machine with states, inventory, coins, selection, dispense, and refund.",
    "atm": "Design an ATM with authentication, withdrawal, deposit, balance inquiry, cash dispenser, and transaction history.",
}


def pattern_readme(name: str, category: str, intent: str, examples: str) -> str:
    return f"""
# {name} Pattern

Category: {category}

## Intent

{intent}

## The Problem

Without this pattern, code often becomes tightly coupled, hard to extend, or full of conditional logic.

## The Solution

Use a small abstraction that separates the part that changes from the part that stays stable.

## When To Use

Use {name} when:

- You see repeated conditional logic.
- You need extensibility.
- You want client code to depend on an abstraction.
- The pattern makes the design simpler to reason about.

## Real Examples

{examples}

## Interview Explanation

"The {name} pattern is useful when {intent.lower()} It improves maintainability by reducing direct dependency on changing implementation details."

## Common Mistakes

- Applying the pattern when simple code is enough.
- Creating too many classes without real benefit.
- Hiding business logic behind unnecessary abstractions.

## Implementation

See the Java examples under `src/main/java/com/anish/lld/patterns`.
"""


def case_study_readme(title: str, description: str) -> str:
    pretty = title.replace("-", " ").title()
    return f"""
# {pretty} LLD

## Problem Statement

{description}

## Clarifying Questions

- What are the main actors?
- What is in scope for this design?
- What is out of scope?
- Are concurrent requests possible?
- Do we need persistence?
- What failure cases should be handled?

## Core Entities

- User or actor
- Domain object
- Service class
- Repository or storage abstraction
- Strategy or policy class where rules vary

## Design Approach

1. Start with use cases.
2. Identify nouns and verbs.
3. Define entities and value objects.
4. Move business workflows into services.
5. Use interfaces for variable behavior.
6. Add validations and edge cases.
7. Discuss concurrency and consistency.

## Patterns Commonly Useful

- Strategy for variable policies.
- Factory for object creation.
- State for lifecycle-heavy objects.
- Observer for notifications/events.
- Repository for storage abstraction.

## Interview Tips

- Keep the first design simple.
- Add complexity only after interviewer asks.
- Explain tradeoffs.
- Mention concurrency risks if shared resources exist.
- Use clean names and small methods.
"""


def main() -> None:
    write("README.md", overview)
    write("docs/00-roadmap.md", roadmap)
    write("docs/01-oop-basics.md", oop)
    write("docs/02-solid-principles.md", solid)
    write("docs/03-uml-basics.md", uml)
    write("docs/04-requirement-gathering.md", requirements)
    write("pom.xml", pom)
    write("src/main/java/com/anish/lld/Main.java", main_java)
    write("src/main/java/com/anish/lld/patterns/creational/FactoryMethodDemo.java", factory_java)
    write("src/main/java/com/anish/lld/patterns/creational/BuilderDemo.java", builder_java)
    write("src/main/java/com/anish/lld/patterns/creational/SingletonDemo.java", singleton_java)
    write("src/main/java/com/anish/lld/patterns/structural/AdapterDemo.java", adapter_java)
    write("src/main/java/com/anish/lld/patterns/structural/DecoratorDemo.java", decorator_java)
    write("src/main/java/com/anish/lld/patterns/behavioral/StrategyDemo.java", strategy_java)
    write("src/main/java/com/anish/lld/patterns/behavioral/ObserverDemo.java", observer_java)

    write("design-patterns/README.md", "# Design Patterns\n\nThis folder contains notes for creational, structural, and behavioral design patterns.\n")
    for name, category, intent, examples in patterns:
        write(f"design-patterns/{category.lower()}/{slug(name)}/README.md", pattern_readme(name, category, intent, examples))

    for name, description in case_studies.items():
        write(f"case-studies/{name}/README.md", case_study_readme(name, description))

    write("interview-prep/revision-sheet.md", """
# LLD Revision Sheet

## Must Know

- Encapsulation, abstraction, inheritance, polymorphism
- Association, aggregation, composition
- SOLID principles
- Creational, structural, behavioral patterns
- Requirement clarification
- Class diagrams
- Thread safety basics
- Clean code principles

## Design Checklist

- Are responsibilities separated?
- Are abstractions meaningful?
- Can new behavior be added without modifying too much code?
- Are edge cases handled?
- Is concurrency discussed?
- Is the code testable?
""")

    write("interview-prep/questions.md", """
# LLD Interview Questions

1. Explain SOLID with examples.
2. Difference between aggregation and composition.
3. Factory vs Abstract Factory.
4. Strategy vs State.
5. Decorator vs Proxy.
6. Observer vs Pub/Sub.
7. How would you design Parking Lot?
8. How would you design BookMyShow?
9. How would you design Splitwise?
10. How would you design an LRU Cache?
11. How do you handle concurrent seat booking?
12. How do you avoid overengineering?
13. When should you use interfaces?
14. How do you test an LLD design?
15. How do you explain tradeoffs?
""")


if __name__ == "__main__":
    main()
