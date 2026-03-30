# Prototype Pattern

## Category
Creational

## Purpose
Creates new objects by cloning existing instances instead of using constructors.

## When to Use
- Object creation is expensive (database calls, API requests, complex calculations)
- Need copies of objects with similar state
- Want to avoid subclasses of an object creator
- Runtime configuration of objects

## Structure

```
┌─────────────────────────────────┐
│         Prototype (ABC)         │
├─────────────────────────────────┤
│ + clone(): Prototype            │
└─────────────────────────────────┘
                 ▲
                 │
     ┌───────────┴───────────┐
     │                       │
┌─────────────┐       ┌─────────────┐
│ ConcreteA   │       │ ConcreteB   │
├─────────────┤       ├─────────────┤
│ + clone()   │       │ + clone()   │
└─────────────┘       └─────────────┘
      │                     │
      ▼                     ▼
┌─────────────┐       ┌─────────────┐
│   Copy A    │       │   Copy B    │
└─────────────┘       └─────────────┘
```

## Components

| Component | Role |
|-----------|------|
| Prototype | Declares the cloning interface |
| ConcretePrototype | Implements cloning operation |
| Client | Creates new objects by asking prototype to clone itself |


## Shallow vs Deep Copy

| Type | Behavior | Use Case |
|------|----------|----------|
| Shallow | Copies object, shares nested references | Simple objects without nested data |
| Deep | Copies object and all nested objects | Objects with nested mutable data |


## Advantages
- Avoids expensive object creation
- Clone objects without coupling to their classes
- Get rid of repeated initialization code
- Produce complex objects more conveniently

## Disadvantages
- Cloning complex objects with circular references can be tricky
- Deep copying can be expensive for heavily nested objects