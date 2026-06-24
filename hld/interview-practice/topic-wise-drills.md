# Topic-Wise HLD Drills

## Scalability Drills

1. A service handles 1K QPS. How do you scale it to 100K QPS?
2. How do you remove a single point of failure?
3. How do you make app servers stateless?
4. What can go wrong with sticky sessions?
5. When would you use L4 vs L7 load balancing?

## Database Drills

1. SQL vs NoSQL for payments?
2. How do read replicas help?
3. What is replication lag?
4. How do you pick a shard key?
5. Why can a bad shard key create a hot partition?
6. When should you denormalize?
7. How do indexes affect writes?

## Caching Drills

1. Explain cache-aside.
2. What is cache penetration?
3. What is cache avalanche?
4. What is cache stampede?
5. How do you decide TTL?
6. When should you invalidate cache manually?
7. Redis vs CDN?

## Queue Drills

1. Queue vs pub/sub?
2. What is at-least-once delivery?
3. Why do consumers need idempotency?
4. What is a dead letter queue?
5. How do you handle queue backlog?
6. How do you preserve ordering?

## Consistency Drills

1. Explain CAP theorem.
2. Strong vs eventual consistency?
3. Which parts of Instagram can be eventually consistent?
4. Which parts of payment system require strong consistency?
5. How do you handle duplicate payment callbacks?

## Reliability Drills

1. Timeout vs retry?
2. Why can retries make an outage worse?
3. What is exponential backoff?
4. What is circuit breaker?
5. What is graceful degradation?
6. What metrics would you track?

## Security Drills

1. Authentication vs authorization?
2. JWT vs session?
3. How does rate limiting prevent abuse?
4. Token bucket vs sliding window?
5. How do you protect sensitive data?
