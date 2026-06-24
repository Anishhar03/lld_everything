# Design URL Shortener

## Problem

Design URL Shortener at high level.

## Functional Requirements

- Create short URLs.
- Redirect to long URLs.
- Support expiry.
- Track analytics.

## Non-Functional Requirements

- High availability for user-facing reads.
- Low latency for core user actions.
- Horizontal scalability.
- Fault tolerance.
- Observability.
- Secure APIs.

## Scale Assumptions

These numbers are interview assumptions. Always state them clearly.

- Daily active users: 10M to 100M depending on product.
- Read/write ratio: usually read-heavy unless noted.
- Peak QPS: 3x to 10x average QPS.
- Data retention: define by product.

## API Sketch

```http
POST /v1/urls
GET /v1/urls/{id}
GET /v1/urls/{id}/status
```

## Data Model

```text
User(id, name, email, created_at)
Entity(id, owner_id, status, created_at, updated_at)
Event(id, entity_id, type, payload, created_at)
```

## High-Level Architecture

```mermaid
flowchart LR
    Client --> CDN[CDN]
    Client --> Gateway[API Gateway]
    Gateway --> Auth[Auth Service]
    Gateway --> Service[Core Service]
    Service --> Cache[(Redis Cache)]
    Service --> DB[(Primary Database)]
    Service --> Queue[(Message Queue)]
    Queue --> Worker[Async Workers]
    Worker --> Search[(Search/Analytics Store)]
    Service --> ObjectStore[(Object Storage)]
```

## Request Flow

1. Client sends request to API Gateway.
2. Gateway authenticates and rate-limits request.
3. Core service validates input.
4. Core service reads/writes cache and database.
5. Non-critical work goes to queue.
6. Workers process async tasks.
7. Metrics/logs/traces are emitted.

## Deep Dive Areas

### Data Partitioning

Choose partition key based on access pattern. Common choices:

- `user_id`
- `tenant_id`
- `region`
- hash of entity id

Avoid shard keys that create hot partitions.

### Caching

Cache read-heavy objects with TTL. Use cache-aside unless there is a strong reason for write-through.

### Consistency

Decide which flows need strong consistency and which can be eventual.

### Failure Handling

- Timeouts for remote calls.
- Retries with exponential backoff.
- Idempotency keys for writes.
- Dead letter queue for failed async events.
- Circuit breaker for unstable dependencies.

## Bottlenecks

- Hot keys.
- Database write throughput.
- Queue backlog.
- Search indexing lag.
- External dependency latency.

## Tradeoffs

- Strong consistency improves correctness but may reduce availability.
- Caching improves latency but introduces staleness.
- Async processing improves responsiveness but introduces eventual consistency.
- Sharding improves scale but complicates queries.

## Interview Summary

"The design uses stateless services behind a gateway/load balancer, cache for hot reads, durable database for source of truth, queue for asynchronous processing, and observability across the system. The key tradeoff is balancing consistency, latency, and operational complexity."
## Problem-Specific Deep Dive

### Short Code Generation

Options:

1. Hash long URL.
2. Generate random base62 string.
3. Use auto-increment ID and encode to base62.
4. Pre-generate codes using a key generation service.

Best interview answer:

Use a key generation service that creates unique base62 codes in batches. App servers consume pre-generated keys. This avoids collisions during user request path.

### Redirect Flow

```mermaid
sequenceDiagram
    participant User
    participant Gateway
    participant URLService
    participant Cache
    participant DB
    participant Queue
    User->>Gateway: GET /abc123
    Gateway->>URLService: resolve abc123
    URLService->>Cache: get abc123
    alt cache hit
        Cache-->>URLService: long URL
    else cache miss
        URLService->>DB: lookup abc123
        DB-->>URLService: long URL
        URLService->>Cache: set abc123
    end
    URLService->>Queue: publish click event
    URLService-->>User: 301/302 redirect
```

### 301 vs 302

- 301 means permanent redirect. Browser may cache aggressively.
- 302 means temporary redirect. Better when analytics and dynamic controls matter.

### Data Model

```text
UrlMapping(short_code PK, long_url, user_id, expires_at, created_at, status)
ClickEvent(id, short_code, timestamp, ip_hash, user_agent, referrer)
```

### Bottlenecks

- Hot short URLs.
- DB lookup latency.
- Analytics write volume.

### Improvements

- Cache hot mappings.
- Async click analytics.
- CDN/edge redirect for extremely hot links.
