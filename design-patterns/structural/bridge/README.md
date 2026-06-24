# Bridge Pattern

Category: Structural

## Intent

Separate abstraction from implementation so both can vary independently.

## The Problem

Without this pattern, code often becomes tightly coupled, hard to extend, or full of conditional logic.

## The Solution

Use a small abstraction that separates the part that changes from the part that stays stable.

## When To Use

Use Bridge when:

- You see repeated conditional logic.
- You need extensibility.
- You want client code to depend on an abstraction.
- The pattern makes the design simpler to reason about.

## Real Examples

Remote controls and devices, notification channel and message type.

## Interview Explanation

"The Bridge pattern is useful when separate abstraction from implementation so both can vary independently. It improves maintainability by reducing direct dependency on changing implementation details."

## Common Mistakes

- Applying the pattern when simple code is enough.
- Creating too many classes without real benefit.
- Hiding business logic behind unnecessary abstractions.

## Implementation

See the Java examples under `src/main/java/com/anish/lld/patterns`.
