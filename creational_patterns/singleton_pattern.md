# Singleton Pattern

## Category
Creational

## Purpose
Ensures a class has only one instance and provides a global access point to it.

## When to Use
- Exactly one instance needed (database connection, logger, config)
- Need global access to that instance
- Want to control shared resources

## Structure

```
┌─────────────────────────────────┐
│           Singleton             │
├─────────────────────────────────┤
│ - __instance: Singleton = None  │
├─────────────────────────────────┤
│ + __new__(): Singleton          │
│ + operation()                   │
└─────────────────────────────────┘
              │
              │ returns same instance
              ▼
        ┌───────────┐
        │ Instance  │ ◀─── All clients share this
        └───────────┘
```

## Components

| Component | Role |
|-----------|------|
| __instance | Class-level variable storing the single instance |
| __new__ | Intercepts object creation, returns existing instance |
| Client | Gets the same instance on every call |


## Advantages
- Guarantees single instance
- Global access point
- Lazy initialization (created only when needed)

## Disadvantages
- Violates Single Responsibility Principle
- Can mask bad design (hidden dependencies)
- Difficult to unit test
- Requires special handling in multithreaded environments