# LLD Everything

A complete, beginner-friendly Low Level Design repository inspired by the playlist:

https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW

The goal of this repo is to make LLD easy to revise for interviews and practical machine-coding rounds. It includes:

- OOP fundamentals
- UML basics
- SOLID principles
- GoF design patterns
- Concurrency and practical engineering patterns
- Classic LLD interview problems
- Runnable Java implementations
- Easy explanations, tradeoffs, and interview notes

## How To Use This Repo

1. Start with `docs/00-roadmap.md`.
2. Revise OOP and SOLID from `docs/01-oop-basics.md` and `docs/02-solid-principles.md`.
3. Study patterns category-wise from `design-patterns/`.
4. Run Java demos from `src/main/java/com/anish/lld`.
5. Practice system designs from `case-studies/`.

## Run Examples

```bash
mvn test
mvn exec:java -Dexec.mainClass="com.anish.lld.Main"
```

If Maven is not installed, the source files are still readable as standalone Java examples.

## Repository Map

```text
docs/                 Core LLD notes
design-patterns/      Pattern-wise README explanations
src/main/java/         Java implementations
case-studies/          LLD interview problems and workflows
interview-prep/        Revision sheets and questions
```
