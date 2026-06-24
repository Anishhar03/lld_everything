# HLD Answer Frameworks

Use these frameworks when practicing system design interview questions.

## Universal 40-Minute Interview Plan

| Time | Activity |
|---|---|
| 0-5 min | Clarify requirements and scope |
| 5-10 min | Estimate scale and define APIs |
| 10-15 min | Define data model |
| 15-25 min | Draw high-level architecture |
| 25-35 min | Deep dive into bottlenecks |
| 35-40 min | Tradeoffs, failures, summary |

## Requirement Clarification Script

"Before jumping into architecture, I want to clarify the scope. Are we designing only the core flow or also admin, analytics, and notifications? What scale should I assume? Is the system read-heavy or write-heavy? Are we optimizing for low latency, strong consistency, or high availability?"

## API Design Script

"I will keep the public APIs minimal and design them around user actions. For writes, I will consider idempotency keys so retries do not create duplicate side effects."

## Data Model Script

"I will first define the source-of-truth tables, then add derived stores like cache, search index, or analytics store where needed. I will design indexes based on query patterns."

## Cache Script

"I would use cache-aside for hot read paths. The cache improves latency and reduces database load, but it introduces stale data risk. I would set TTL based on freshness needs and use invalidation for critical objects."

## Queue Script

"I would move non-critical or slow work to a queue. This keeps user-facing latency low and allows retries. Since queues often provide at-least-once delivery, consumers must be idempotent."

## Consistency Script

"This system has mixed consistency needs. The core transaction needs strong consistency, while analytics/search/notifications can be eventually consistent."

## Failure Handling Script

"I would add timeouts, retries with exponential backoff, circuit breakers for unstable dependencies, dead letter queues for failed async jobs, and idempotency keys for retry-safe writes."

## Final Summary Script

"The design uses stateless services behind an API gateway, durable storage as source of truth, cache for hot reads, queue for async processing, and observability across services. The main tradeoff is between latency, consistency, and operational complexity."
