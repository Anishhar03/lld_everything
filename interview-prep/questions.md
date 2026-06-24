# LLD Interview Questions With Answer Hints

## Fundamentals

1. What is LLD?
   - Converting requirements into classes, APIs, relationships, and code-level design.
2. Entity vs value object?
   - Entity has identity; value object is defined by fields.
3. Aggregation vs composition?
   - Composition has stronger lifecycle ownership.
4. Interface vs abstract class?
   - Interface defines capability; abstract class shares partial implementation.
5. Why SOLID?
   - To reduce coupling and make change safer.

## Design Patterns

1. Factory vs Abstract Factory?
   - Factory creates one product hierarchy; Abstract Factory creates families of related products.
2. Strategy vs State?
   - Strategy selects algorithm; State changes behavior based on lifecycle.
3. Decorator vs Proxy?
   - Decorator adds behavior; Proxy controls access.
4. Observer vs Pub/Sub?
   - Observer often direct in-process; Pub/Sub usually broker-mediated.
5. Template Method vs Strategy?
   - Template uses inheritance; Strategy uses composition.

## Case Studies

1. How do you prevent double booking in BookMyShow?
   - Seat lock with expiry, atomic update, confirmation only after payment.
2. How do you allocate parking spots?
   - SpotAllocationStrategy, atomic check-and-occupy.
3. How do you design LRU cache?
   - HashMap plus doubly linked list, lock around mutation.
4. How do you dispatch elevators?
   - SchedulingStrategy based on direction, distance, load, and request type.
5. How do you settle Splitwise balances?
   - Maintain net balances and simplify debts using creditors/debtors.

## Deep Discussion

For every answer, mention:

- Requirements
- Entities
- Services
- Patterns
- Concurrency
- Edge cases
- Tradeoffs
