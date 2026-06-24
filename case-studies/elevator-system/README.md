# Elevator System Low Level Design

## Problem Statement

Design an elevator system with multiple elevators, floors, internal requests, external requests, scheduling, direction, door state, and emergency behavior.

## How To Start In Interview

Say:

"I will first clarify scope, then identify entities and workflows. After that I will discuss class design, patterns, concurrency, and edge cases."

## Functional Requirements

- Support the main user workflow end to end.
- Validate invalid operations.
- Keep domain state consistent.
- Return meaningful success/failure results.
- Allow future extension without rewriting the core model.

## Non-Functional Requirements

- Correctness over cleverness.
- Simple APIs.
- Thread safety for shared mutable resources.
- Clear separation between models, services, repositories, and strategies.
- Testable code.

## Core Entities

- `Elevator`
- `Floor`
- `Request`
- `Button`
- `Door`
- `Display`
- `ElevatorCar`

## Core Services

- `ElevatorController`
- `Dispatcher`
- `SchedulingStrategy`
- `DoorService`

## High-Level Workflow

```mermaid
flowchart TD
    A[User request] --> B[Validate input]
    B --> C[Load domain state]
    C --> D[Apply business rules]
    D --> E[Update state atomically]
    E --> F[Return result]
```

## Class Relationship Sketch

```mermaid
classDiagram
    class Controller
    class DomainService
    class Repository
    class Entity
    class Strategy
    Controller --> DomainService
    DomainService --> Repository
    DomainService --> Entity
    DomainService --> Strategy
```

## Suggested Patterns

- Strategy for scheduling
- State for elevator movement/door state
- Command for button requests

## Detailed Design Steps

1. Write down actors and use cases.
2. Model entities that have identity.
3. Model value objects for immutable concepts.
4. Put workflow orchestration inside services.
5. Put variable rules behind strategies.
6. Keep repositories as storage abstractions.
7. Make state transitions explicit.
8. Add concurrency protection around shared resources.
9. Write demo flows or unit tests.

## Concurrency Discussion

Requests can arrive concurrently from many floors. Queue updates must be thread-safe. The dispatcher should atomically assign requests to elevators.

## Edge Cases

- Invalid ID or missing object.
- Duplicate request.
- Expired lock or stale state.
- Payment failure or external service failure.
- Concurrent modification.
- Cancellation after partial success.
- Retry after timeout.

## API Sketch

```java
class ElevatorSystemService {
    // validate request
    // load current state
    // apply domain rules
    // persist or update state
    // return response
}
```

## Interview Deep-Dive Points

- Explain why each class exists.
- Mention which rules are likely to change.
- Use Strategy for changeable policies.
- Use State when lifecycle behavior changes.
- Use Factory when object creation depends on type.
- Keep concurrency discussion concrete.

## What To Say If Asked For Production Scale

"For production, I would move in-memory repositories to durable storage, use transactions or optimistic locking for consistency, add idempotency keys for retries, and expose APIs through controllers. For distributed deployments, I would avoid local-only locks and rely on database constraints, distributed locks, or message-driven workflows depending on the exact consistency requirement."

## Domain-Specific Deep Dive

### Elevator States

```mermaid
stateDiagram-v2
    [*] --> IDLE
    IDLE --> MOVING_UP
    IDLE --> MOVING_DOWN
    MOVING_UP --> DOOR_OPEN
    MOVING_DOWN --> DOOR_OPEN
    DOOR_OPEN --> DOOR_CLOSED
    DOOR_CLOSED --> IDLE
```

### Scheduling Strategies

Common options:

- nearest elevator
- same direction first
- least loaded elevator
- zoning based dispatch
- destination control system

### Key Design Decision

The `Dispatcher` should not hardcode scheduling. Put scheduling behind `SchedulingStrategy` so the algorithm can change.
