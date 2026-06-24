# Networking And Protocols

HLD requires knowing how requests travel through the system.

## DNS

DNS converts a domain name into an IP address.

Flow:

```text
browser -> recursive resolver -> root DNS -> TLD DNS -> authoritative DNS -> IP
```

In HLD:

- Use DNS for domain routing.
- Use geo-DNS for routing users to nearest region.
- DNS TTL affects failover speed.

## HTTP vs HTTPS

HTTP is application-layer request/response. HTTPS is HTTP over TLS.

Key points:

- HTTPS provides encryption and server authentication.
- TLS termination often happens at load balancer or reverse proxy.
- Internal service traffic may use mTLS in zero-trust systems.

## REST

REST uses resources and HTTP verbs.

Examples:

```http
GET /users/123
POST /orders
PATCH /orders/123
DELETE /sessions/current
```

Good for public APIs and CRUD-heavy systems.

## gRPC

gRPC is efficient service-to-service communication using HTTP/2 and Protocol Buffers.

Use when:

- Internal microservices need low latency.
- Contracts are strongly typed.
- Streaming is needed.

## WebSockets

WebSockets keep a persistent bidirectional connection.

Use for:

- Chat
- Live gaming
- Stock ticks
- Collaboration apps

## Long Polling vs Server-Sent Events vs WebSocket

| Technique | Use Case |
|---|---|
| Long polling | Simple near-real-time updates |
| SSE | Server-to-client event stream |
| WebSocket | Bidirectional real-time communication |

## API Gateway

An API gateway is the entry point for clients.

Responsibilities:

- Authentication
- Routing
- Rate limiting
- Request validation
- TLS termination
- Response transformation

Do not put core business logic in the gateway.
