# High Level Design

This section is an in-depth HLD/System Design guide inspired by these playlists:

- High Level Design from Basics to Advanced: https://www.youtube.com/playlist?list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7
- System Design Tutorials (HLD) for Beginners: https://www.youtube.com/playlist?list=PLlvkTvW25FtjlM61SIOcLS05SfwoYgMit
- System Design Interview Question: https://www.youtube.com/playlist?list=PLPtUyMfD0mNJDZg50fg2CptjLBavHot47

The playlists expose their titles/descriptions publicly, but individual video titles were not available through the static YouTube page data in this environment. So this section is built as a complete HLD curriculum aligned with the usual flow of those playlists: fundamentals first, then architecture building blocks, then deep case studies and interview practice.

## Learning Path

1. `00-hld-roadmap.md`
2. `01-how-to-approach-hld-interviews.md`
3. `02-networking-and-protocols.md`
4. `03-scalability-and-load-balancing.md`
5. `04-database-design.md`
6. `05-caching.md`
7. `06-message-queues-and-event-driven-design.md`
8. `07-consistency-availability-partitioning.md`
9. `08-storage-search-and-indexing.md`
10. `09-observability-reliability-and-sre.md`
11. `10-security-rate-limiting-and-abuse-prevention.md`
12. `11-capacity-estimation.md`
13. `case-studies/`

## How HLD Differs From LLD

| Area | HLD | LLD |
|---|---|---|
| Focus | System architecture | Class/code architecture |
| Main units | Services, databases, queues, caches | Classes, interfaces, methods |
| Questions | Scale, availability, consistency | Responsibilities, patterns, extensibility |
| Output | Architecture diagram, APIs, data model, tradeoffs | Class diagram, methods, implementation |

## HLD Interview Answer Shape

```text
Requirements -> Scale -> APIs -> Data model -> Architecture -> Deep dives -> Bottlenecks -> Tradeoffs
```

Never jump directly to microservices. Start with requirements and constraints.
