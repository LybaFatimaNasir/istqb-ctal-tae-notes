# ISTQB CTAL-TAE - Chapter 4: Test Automation Design Patterns

## Why Design Patterns Matter in Test Automation

- Reusable solutions to recurring problems in automation design
- Improve maintainability, readability, and scalability of the automation solution
- Reduce duplication and coupling between test logic and implementation details
- Map onto gTAA layers (mainly Test Definition and Test Execution layers)

## Core Design Patterns

### 1. Page Object Model (POM)
- Encapsulates UI elements and interactions of a single page/screen in a dedicated class
- Test scripts call methods on the page object instead of interacting with locators directly
- **Benefits:** if UI changes, only the page object needs updating, not every test
- **Drawback:** can grow bloated on large apps if not paired with component-level objects

### 2. Screenplay Pattern
- Focuses on **actors** performing **tasks** using **abilities** and **interactions**
- More behavior-driven and composable than POM
- Better suited for complex user journeys and readability at the business level
- Steeper learning curve than POM

### 3. Data-Driven Testing Pattern
- Separates test logic from test data (data stored externally: CSV, Excel, JSON, DB)
- Same test script runs multiple times with different data sets
- **Benefits:** easy to expand coverage without duplicating scripts
- **Drawback:** test logic can become harder to trace back to specific scenarios

### 4. Keyword-Driven Testing Pattern
- Test steps expressed as keywords/actions (e.g., "Login", "ClickButton") mapped to underlying automation code
- Enables non-technical stakeholders to design test cases
- Keyword interpreter layer translates keywords into executable code
- **Drawback:** extra abstraction layer adds maintenance overhead

### 5. Factory Pattern
- Centralizes object creation (e.g., creating browser/driver instances, test data objects)
- Decouples object creation from usage
- Useful for supporting multiple environments/browsers/platforms from one config point

### 6. Singleton Pattern
- Ensures only one instance of a class exists (commonly used for driver/session management)
- Prevents resource conflicts (e.g., multiple browser instances unintentionally spawned)
- Use carefully in parallel test execution — can cause shared-state issues if misapplied

### 7. Facade Pattern
- Provides a simplified interface over a complex subsystem (e.g., wrapping multiple API calls into one method)
- Hides implementation complexity from test scripts
- Common in API test automation and framework utility layers

## How Patterns Map to gTAA Layers

| Pattern | Primary gTAA Layer |
|---|---|
| Page Object Model | Test Definition / Test Execution |
| Screenplay | Test Definition |
| Data-Driven | Test Data / Test Definition |
| Keyword-Driven | Test Definition |
| Factory | Test Execution |
| Singleton | Test Execution / Adaptation |
| Facade | Adaptation Layer |

## Choosing a Pattern — Key Considerations

- Complexity and size of the SUT
- Team's technical skill level (business-readable vs code-heavy)
- Maintainability goals (how often UI/API changes)
- Reusability needs across multiple test suites/projects
- Parallel execution requirements (thread-safety matters — e.g., Singleton risk)

## Exam Tip
- Questions often present a **scenario** (e.g., "UI changes frequently" or "non-technical stakeholders need to write tests") and ask which pattern best fits — practice mapping scenario → pattern rather than memorizing definitions alone.
