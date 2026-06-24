# Template Method Pattern

Category: Behavioral

## Intent

Define algorithm skeleton while subclasses customize steps.

## The Problem

Without this pattern, code often becomes tightly coupled, hard to extend, or full of conditional logic.

## The Solution

Use a small abstraction that separates the part that changes from the part that stays stable.

## When To Use

Use Template Method when:

- You see repeated conditional logic.
- You need extensibility.
- You want client code to depend on an abstraction.
- The pattern makes the design simpler to reason about.

## Real Examples

Report generation, data import workflows.

## Interview Explanation

"The Template Method pattern is useful when define algorithm skeleton while subclasses customize steps. It improves maintainability by reducing direct dependency on changing implementation details."

## Common Mistakes

- Applying the pattern when simple code is enough.
- Creating too many classes without real benefit.
- Hiding business logic behind unnecessary abstractions.

## Implementation

See the Java examples under `src/main/java/com/anish/lld/patterns`.
