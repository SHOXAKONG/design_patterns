# Factory Design Patterns

## Factory Method Pattern

**What it does**: Defines an interface for creating objects, but lets subclasses decide which class to instantiate.

**Structure**:
- **Product Interface**: Common interface for all products (e.g., `IProduct`)
- **Concrete Products**: Actual implementations (e.g., `Car`, `Truck`)
- **Creator Interface**: Declares factory method (e.g., `IWorkShop.create()`)
- **Concrete Creators**: Implement factory method (e.g., `CreateCar`, `CreateTruck`)

**Benefits**:
- Decouples client code from concrete classes
- Easy to add new product types without changing existing code
- Separates creation logic from business logic

**Real-world examples**:
- Payment gateways (Stripe, PayPal, Square)
- Document exporters (PDF, Excel, Word)
- Database connections (MySQL, PostgreSQL, MongoDB)
- Notification channels (Email, SMS, Push)

---

## Abstract Factory Pattern

**What it does**: Provides an interface for creating families of related objects without specifying their concrete classes.

**Structure**:
- **Abstract Product Interfaces**: Interfaces for each product type (e.g., `IEngine`, `ICar`)
- **Concrete Products**: Implementations organized into families (e.g., `JapaneseEngine`, `JapaneseCar`)
- **Abstract Factory**: Declares creation methods for each product (e.g., `IFactory.create_engine()`, `IFactory.create_car()`)
- **Concrete Factories**: Create complete product families (e.g., `JapaneseFactory`, `RussianFactory`)

**Benefits**:
- Ensures all products from the same factory are compatible
- Easy to swap entire product families
- Prevents mixing incompatible products

**Real-world examples**:
- UI themes (Dark/Light mode with matching Button, Input, Dialog)
- Cross-platform UI (Windows/Mac/Linux native components)
- Cloud providers (AWS/Azure/GCP services)
- Game difficulty levels (Enemy + Weapon + PowerUp combinations)

---

## Key Differences

| Aspect | Factory Method | Abstract Factory |
|--------|----------------|------------------|
| **Creates** | ONE product type | FAMILIES of products |
| **Methods** | One creation method | Multiple creation methods |
| **Example** | Car factory OR Truck factory | Japanese factory (Engine + Car) |
| **Purpose** | Choose implementation | Ensure compatibility |

**Simple analogy**:
- **Factory Method**: Restaurant specializing in one dish (Pizza place → Pizza)
- **Abstract Factory**: Restaurant serving complete cuisine (Italian → Pasta + Pizza + Tiramisu)

---

## When to Use

**Use Factory Method when**:
- You have multiple variants of a similar object
- Object type is determined at runtime
- You want flexibility without tight coupling

**Use Abstract Factory when**:
- You need related objects that work together
- You want to swap entire product families easily
- Compatibility between products matters

**Avoid both when**:
- Object creation is simple and won't change
- You only have one variant
- The abstraction adds unnecessary complexity