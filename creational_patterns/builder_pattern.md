# Builder Pattern

## Category
Creational

## Purpose
Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

## When to Use
- Object requires many steps to create
- Need different representations of the same construction process
- Want to isolate complex construction logic from business logic

## Structure

```
┌─────────────────┐       ┌─────────────────────┐
│    Director     │──────▶│   Builder (ABC)     │
├─────────────────┤       ├─────────────────────┤
│ construct()     │       │ build_step_a()      │
└─────────────────┘       │ build_step_b()      │
                          │ get_result()        │
                          └─────────────────────┘
                                    ▲
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
          ┌─────────────────┐             ┌─────────────────┐
          │ ConcreteBuilder1│             │ ConcreteBuilder2│
          ├─────────────────┤             ├─────────────────┤
          │ build_step_a()  │             │ build_step_a()  │
          │ build_step_b()  │             │ build_step_b()  │
          │ get_result()    │             │ get_result()    │
          └─────────────────┘             └─────────────────┘
                    │                               │
                    ▼                               ▼
            ┌─────────────┐                 ┌─────────────┐
            │  Product A  │                 │  Product B  │
            └─────────────┘                 └─────────────┘
```

## Components

| Component | Role |
|-----------|------|
| Director | Orchestrates the build sequence |
| Builder (ABC) | Declares abstract building steps |
| ConcreteBuilder | Implements steps for specific product |
| Product | The complex object being constructed |


## Advantages
- Isolates construction code from product representation
- Same construction process creates different products
- Fine control over construction steps
- Single Responsibility Principle

## Disadvantages
- Increases code complexity with multiple new classes