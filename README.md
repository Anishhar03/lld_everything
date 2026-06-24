# System Design Everything: LLD + HLD

This repository is a deep system design learning resource covering both:

- Low Level Design (LLD)
- High Level Design (HLD)

It is inspired by these playlists:

- LLD playlist: https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW
- HLD playlist: https://www.youtube.com/playlist?list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7
- HLD beginner playlist: https://www.youtube.com/playlist?list=PLlvkTvW25FtjlM61SIOcLS05SfwoYgMit
- System design interview questions: https://www.youtube.com/playlist?list=PLPtUyMfD0mNJDZg50fg2CptjLBavHot47

## What Is Inside

### LLD

- OOP fundamentals
- SOLID principles
- UML basics
- Requirement gathering
- All 22 GoF design patterns
- Java implementation for every GoF pattern
- Classic LLD case studies

### HLD

- HLD roadmap
- Interview approach
- Networking and protocols
- Scalability and load balancing
- Database design
- Caching
- Message queues
- CAP and consistency
- Storage, search, and indexing
- Observability and reliability
- Security and rate limiting
- Capacity estimation
- HLD case studies
- System design practice questions

## Learning Path

1. Start with `hld/00-hld-roadmap.md` for HLD.
2. Read `hld/01-how-to-approach-hld-interviews.md`.
3. Study each HLD building block under `hld/`.
4. Practice HLD case studies from `hld/case-studies/`.
5. Study LLD from `docs/` and `design-patterns/`.
6. Practice LLD case studies from `case-studies/`.

## Run Java LLD Pattern Demos

```bash
mvn exec:java -Dexec.mainClass="com.anish.lld.Main"
```

Without Maven, use JDK directly:

```powershell
$files = Get-ChildItem -Path src\main\java -Recurse -Filter *.java | ForEach-Object { $_.FullName }
javac -d target\classes $files
java -cp target\classes com.anish.lld.Main
```
