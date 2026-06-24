# Consistency, Availability, And Partitioning

Distributed systems must make tradeoffs.

## CAP Theorem

During a network partition, a distributed system must choose between:

- Consistency
- Availability

Partition tolerance is required in real distributed systems.

## Strong Consistency

After a write completes, all reads see the latest value.

Use for:

- Banking
- Inventory
- Ticket booking
- Payments

## Eventual Consistency

Reads may be stale temporarily, but system converges.

Use for:

- Feed counts
- Analytics
- Search index updates
- Notifications

## Consistency Examples

### Payment

Needs strong consistency because double charge or lost money is unacceptable.

### Like Count

Can be eventually consistent because a small delay is acceptable.

### Seat Booking

Needs strong consistency for seat ownership.

### Search Index

Can lag behind primary database.

## Quorum

In replicated systems:

```text
R + W > N
```

Where:

- N = number of replicas
- R = read quorum
- W = write quorum

## Conflict Resolution

Strategies:

- Last write wins
- Version vectors
- Manual merge
- CRDTs
- Application-specific rules

## Interview Sentence

"For this feature, I would choose strong consistency because incorrect data causes user-visible correctness issues. For analytics and notifications, eventual consistency is acceptable because delay is tolerable."
