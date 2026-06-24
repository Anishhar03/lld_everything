# Case Study Checklist

Use this checklist for every HLD problem.

## 1. Requirements

- Who are the users?
- What are the top 3 core features?
- What is out of scope?
- Is this read-heavy or write-heavy?
- Is real-time behavior required?

## 2. Scale

- DAU/MAU
- Requests per second
- Peak traffic
- Storage per day
- Bandwidth
- Cache size

## 3. APIs

- Create APIs
- Read APIs
- Update APIs
- Delete/cancel APIs
- Status APIs
- Idempotency keys for writes

## 4. Data

- Source-of-truth database
- Cache
- Search index
- Object storage
- Analytics store
- Queue events

## 5. Architecture

- Client
- CDN
- API Gateway
- Load balancer
- Services
- Cache
- Database
- Queue
- Workers
- Search/analytics

## 6. Deep Dive

Pick 2-3:

- DB sharding
- Cache invalidation
- Feed generation
- Seat locking
- Message delivery
- Video transcoding
- Payment idempotency
- Search ranking
- Rate limiting

## 7. Failure Handling

- Dependency timeout
- Retry
- Circuit breaker
- DLQ
- Idempotency
- Fallback
- Multi-region failover

## 8. Final Tradeoffs

Mention:

- Latency vs consistency
- Cost vs availability
- Simplicity vs scalability
- Sync vs async
- SQL vs NoSQL
