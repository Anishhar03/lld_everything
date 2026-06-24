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
