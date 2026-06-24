# Singleton Pattern

Category: Creational

## Intent

Ensure a class has only one instance and provide a global access point.

## The Problem

Without this pattern, code often becomes tightly coupled, hard to extend, or full of conditional logic.

## The Solution

Use a small abstraction that separates the part that changes from the part that stays stable.

## When To Use

Use Singleton when:

- You see repeated conditional logic.
- You need extensibility.
- You want client code to depend on an abstraction.
- The pattern makes the design simpler to reason about.

## Real Examples

Configuration manager, logger, connection registry.

## Interview Explanation

"The Singleton pattern is useful when ensure a class has only one instance and provide a global access point. It improves maintainability by reducing direct dependency on changing implementation details."

## Common Mistakes

- Applying the pattern when simple code is enough.
- Creating too many classes without real benefit.
- Hiding business logic behind unnecessary abstractions.

## Implementation

See the Java examples under `src/main/java/com/anish/lld/patterns`.
