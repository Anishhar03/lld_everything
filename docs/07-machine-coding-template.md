# Machine Coding Template

Machine-coding rounds test whether you can convert design into working code quickly.

## Suggested Package Structure

```text
model/          Entities and value objects
service/        Business workflows
repository/     In-memory or DB abstraction
strategy/       Variable algorithms
exception/      Domain exceptions
dto/            Input/output request objects
Main.java       Demo runner
```

## Coding Order

1. Create enums and value objects.
2. Create core entities.
3. Create repositories or in-memory stores.
4. Create services.
5. Add strategies/policies.
6. Add validations.
7. Write a demo flow.
8. Add edge cases.

## What Good Code Looks Like

- Small classes.
- Clear names.
- No giant if-else blocks.
- Business rules in the right place.
- Interfaces for behavior that changes.
- No unnecessary frameworks.
- Easy to test.

## Demo Flow Example

For parking lot:

1. Create parking lot.
2. Add floors.
3. Add spots.
4. Park vehicle.
5. Generate ticket.
6. Unpark vehicle.
7. Calculate fee.
8. Free the spot.

## Last 10-Minute Checklist

- Does code compile?
- Is there a main method or tests?
- Are edge cases handled?
- Did you explain assumptions?
- Are class names interview-readable?
- Did you mention concurrency?
