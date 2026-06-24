# Concurrency For LLD

Many LLD interviews become serious when concurrency appears.

Examples:

- Two users try to book the same seat.
- Two cars enter the same parking spot.
- Multiple threads update an LRU cache.
- Elevator requests arrive from different floors.
- ATM withdrawal and account balance update happen together.

## Core Concepts

### Race Condition

A race condition happens when correctness depends on timing.

Example:

1. User A checks seat S1 is available.
2. User B checks seat S1 is available.
3. Both create booking.

Now the same seat is double-booked.

### Critical Section

A critical section is code that must not be executed by multiple threads at the same time for the same shared resource.

Example:

```java
synchronized (seat) {
    if (seat.isAvailable()) {
        seat.lock(userId);
    }
}
```

### Lock Granularity

Coarse lock:

- Easy to reason about.
- Lower concurrency.

Fine-grained lock:

- Better throughput.
- Harder to avoid deadlocks.

### Optimistic Locking

Assume conflicts are rare. Use a version number.

Example:

```text
UPDATE seats
SET status = 'LOCKED', version = version + 1
WHERE id = ? AND version = ? AND status = 'AVAILABLE'
```

If zero rows are updated, someone else changed the seat first.

### Pessimistic Locking

Lock the resource before updating.

Used when conflicts are common or correctness is critical.

## Common Interview Scenarios

### BookMyShow Seat Locking

Need:

- Prevent double booking.
- Release expired locks.
- Handle payment timeout.

Design:

- `SeatLock`
- `SeatLockService`
- lock expiry time
- per-show seat lock map
- atomic lock operation

### Parking Lot Spot Assignment

Need:

- Avoid assigning same spot to two vehicles.

Design:

- synchronize per floor or spot manager
- choose spot and mark occupied atomically

### LRU Cache

Need:

- Get and put should update map and linked list consistently.

Design:

- one lock around map/list mutation
- or concurrent structures plus careful ordering

## How To Discuss In Interview

Say:

"The shared resource here is [seat/spot/cache/account]. The race condition is [double booking/double assignment/lost update]. I would make the check-and-update atomic using [synchronized block/database transaction/optimistic locking/distributed lock], depending on whether this is in-memory or production distributed design."
