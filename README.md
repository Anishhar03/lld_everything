# LLD Everything

This repository is a deep Low Level Design learning resource inspired by the LLD playlist:

https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW

It is built for interview preparation, machine-coding rounds, and real engineering design discussions. The repo goes beyond short definitions: every major concept explains why it exists, when to use it, how to implement it, what tradeoffs matter, and how to speak about it in interviews.

## What Is Inside

- Deep LLD roadmap and thinking process
- OOP fundamentals with design examples
- SOLID principles with before/after reasoning
- UML and relationship modeling
- Requirement gathering templates
- All 22 GoF design patterns
- Java implementation for every GoF design pattern
- Concurrency notes for LLD interviews
- Machine-coding templates
- Deep case-study documents for common LLD problems
- Interview question bank and revision sheet

## Recommended Learning Order

1. `docs/00-roadmap.md`
2. `docs/08-how-to-think-in-lld.md`
3. `docs/01-oop-basics.md`
4. `docs/02-solid-principles.md`
5. `docs/03-uml-basics.md`
6. `docs/04-requirement-gathering.md`
7. `docs/05-design-patterns-deep-dive.md`
8. `docs/06-concurrency-for-lld.md`
9. `docs/07-machine-coding-template.md`
10. `design-patterns/`
11. `case-studies/`

## Run Java Pattern Demos

```bash
mvn exec:java -Dexec.mainClass="com.anish.lld.Main"
```

If Maven is unavailable, use JDK directly:

```powershell
$files = Get-ChildItem -Path src\main\java -Recurse -Filter *.java | ForEach-Object { $_.FullName }
javac -d target\classes $files
java -cp target\classes com.anish.lld.Main
```

## Repository Structure

```text
docs/                 Deep LLD theory and interview method
design-patterns/      Pattern-by-pattern explanation, UML, tradeoffs
src/main/java/         Runnable Java implementations
case-studies/          Full LLD problem breakdowns
interview-prep/        Revision sheets and question bank
```

## How To Answer Any LLD Problem

Use this mental model:

1. Clarify requirements.
2. Identify actors and use cases.
3. Define core entities and value objects.
4. Define services that coordinate workflows.
5. Decide relationships between objects.
6. Apply SOLID principles.
7. Use design patterns only where they solve a real design pressure.
8. Discuss concurrency and consistency.
9. Add APIs and class-level code.
10. Explain tradeoffs and future extensions.
