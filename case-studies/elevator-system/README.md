# Elevator System LLD

## Problem Statement

Design elevators that handle requests, direction, scheduling, floors, doors, and emergency behavior.

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
