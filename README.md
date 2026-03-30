# Creational Design Patterns

## Overview
Creational patterns deal with object creation mechanisms. They abstract the instantiation process, making systems independent of how objects are created, composed, and represented.

## Patterns

| Pattern | Purpose |
|---------|---------|
| [Builder](#builder) | Step-by-step construction of complex objects |
| [Singleton](#singleton) | Ensures only one instance exists |
| [Prototype](#prototype) | Creates objects by cloning existing instances |
| [Factory Method](#factory-method) | Delegates instantiation to subclasses |
| [Abstract Factory](#abstract-factory) | Creates families of related objects |

---

## Builder

### Intent
Separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

### Structure

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
          └─────────────────┘             └─────────────────┘
```

### When to Use
- Object requires many steps to create
- Need different representations of the same construction process
- Want to isolate complex construction logic

### Advantages
- Fine control over construction steps
- Same process creates different products
- Single Responsibility Principle

### Disadvantages
- Increases code complexity with multiple classes

---

## Singleton

### Intent
Ensures a class has only one instance and provides a global access point to it.

### Structure

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

### When to Use
- Exactly one instance needed (database connection, logger, config)
- Need global access to that instance
- Want to control shared resources

### Advantages
- Guarantees single instance
- Global access point
- Lazy initialization

### Disadvantages
- Violates Single Responsibility Principle
- Difficult to unit test
- Requires thread-safety handling

---

## Prototype

### Intent
Creates new objects by cloning existing instances instead of using constructors.

### Structure

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
```

### When to Use
- Object creation is expensive
- Need copies of objects with similar state
- Runtime configuration of objects

### Advantages
- Avoids expensive object creation
- Clone without coupling to concrete classes
- Produce complex objects conveniently

### Disadvantages
- Cloning objects with circular references is tricky
- Deep copying can be expensive

---

## Factory Method

### Intent
Defines an interface for creating objects, but lets subclasses decide which class to instantiate.

### Structure

```
┌─────────────────────────┐
│    Creator (ABC)        │
├─────────────────────────┤
│ + factory_method()      │
│ + operation()           │
└─────────────────────────┘
            ▲
            │
  ┌─────────┴─────────┐
  │                   │
┌─────────────┐ ┌─────────────┐
│ CreatorA    │ │ CreatorB    │
├─────────────┤ ├─────────────┤
│ factory()   │ │ factory()   │
└─────────────┘ └─────────────┘
      │               │
      ▼               ▼
┌─────────────┐ ┌─────────────┐
│  ProductA   │ │  ProductB   │
└─────────────┘ └─────────────┘
```

### When to Use
- Class can't anticipate the type of objects it needs
- Want subclasses to specify objects they create
- Need to localize knowledge of helper classes

### Advantages
- Loose coupling between creator and products
- Single Responsibility Principle
- Open/Closed Principle

### Disadvantages
- May require many subclasses

---

## Abstract Factory

### Intent
Provides an interface for creating families of related objects without specifying their concrete classes.

### Structure

```
┌───────────────────────────┐
│   AbstractFactory (ABC)   │
├───────────────────────────┤
│ + create_product_a()      │
│ + create_product_b()      │
└───────────────────────────┘
            ▲
            │
  ┌─────────┴─────────┐
  │                   │
┌─────────────┐ ┌─────────────┐
│ FactoryA    │ │ FactoryB    │
├─────────────┤ ├─────────────┤
│ create_a()  │ │ create_a()  │
│ create_b()  │ │ create_b()  │
└─────────────┘ └─────────────┘
      │               │
      ▼               ▼
┌─────────────┐ ┌─────────────┐
│ Family A    │ │ Family B    │
│ Products    │ │ Products    │
└─────────────┘ └─────────────┘
```

### When to Use
- System should be independent of product creation
- Need to work with families of related products
- Want to enforce product compatibility

### Advantages
- Ensures compatibility between products
- Loose coupling
- Single Responsibility Principle

### Disadvantages
- Adding new product types requires interface changes

---

## Comparison

| Pattern | Creates | Key Mechanism | Complexity |
|---------|---------|---------------|------------|
| Builder | Complex objects step-by-step | Director + Builder | Medium |
| Singleton | Single instance | `__new__` override | Low |
| Prototype | Clones of existing objects | `clone()` method | Low |
| Factory Method | Objects via subclasses | Override factory method | Medium |
| Abstract Factory | Families of objects | Multiple factory methods | High |

---

## When to Choose

| Scenario | Pattern |
|----------|---------|
| Object needs many configuration steps | Builder |
| Only one instance should exist | Singleton |
| Creating objects is expensive, clone instead | Prototype |
| Subclasses should decide what to create | Factory Method |
| Need families of related objects | Abstract Factory |