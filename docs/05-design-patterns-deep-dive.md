# Design Patterns Deep Dive

Design patterns are reusable solutions to recurring object-oriented design problems.

They are not rules. They are vocabulary. A good engineer uses them when they simplify the design, not to make code look impressive.

## Pattern Categories

### Creational Patterns

Creational patterns solve object creation problems.

Use them when:

- Constructor logic is complex.
- Creation depends on input.
- Client code should not know concrete classes.
- Families of related objects must be created together.

Patterns:

- Singleton
- Factory Method
- Abstract Factory
- Builder
- Prototype

### Structural Patterns

Structural patterns solve object composition problems.

Use them when:

- Existing interfaces do not match.
- You need wrappers.
- You need tree structures.
- You need access control.
- You need to reduce memory by sharing state.

Patterns:

- Adapter
- Bridge
- Composite
- Decorator
- Facade
- Flyweight
- Proxy

### Behavioral Patterns

Behavioral patterns solve communication and responsibility flow problems.

Use them when:

- Multiple algorithms are interchangeable.
- Requests flow through handlers.
- Objects need notification.
- State controls behavior.
- You need undo/redo.
- You need to decouple many objects.

Patterns:

- Chain of Responsibility
- Command
- Iterator
- Mediator
- Memento
- Observer
- State
- Strategy
- Template Method
- Visitor

## How To Explain A Pattern In Interviews

Use this structure:

1. Problem: What design issue appears?
2. Intent: What does the pattern solve?
3. Structure: What classes/interfaces are involved?
4. Example: Where have you seen it?
5. Tradeoff: What complexity does it add?

Example:

"Strategy is useful when an algorithm varies independently from the object using it. We define a strategy interface, create multiple implementations, and inject the required strategy at runtime. It avoids large if-else blocks and follows Open Closed Principle, but it introduces more classes."

## Pattern Selection Cheat Sheet

| Need | Pattern |
|---|---|
| Only one shared instance | Singleton |
| Create object based on type | Factory Method |
| Create related objects | Abstract Factory |
| Build complex object step by step | Builder |
| Clone existing object | Prototype |
| Convert one interface to another | Adapter |
| Separate abstraction and implementation | Bridge |
| Tree of objects | Composite |
| Add behavior dynamically | Decorator |
| Simplify subsystem | Facade |
| Share repeated immutable state | Flyweight |
| Control access to object | Proxy |
| Pipeline of handlers | Chain of Responsibility |
| Request as object | Command |
| Traverse collection | Iterator |
| Central coordinator | Mediator |
| Snapshot state | Memento |
| Subscribe to events | Observer |
| State-specific behavior | State |
| Runtime algorithm selection | Strategy |
| Fixed algorithm skeleton | Template Method |
| Add operation over object structure | Visitor |
