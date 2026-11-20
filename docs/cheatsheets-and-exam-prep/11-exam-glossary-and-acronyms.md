# 📖 CTAL-TAE Exam Glossary & Official Terminology

A quick-reference dictionary of official ISTQB terms and acronyms essential for the Certified Tester Advanced Level — Test Automation Engineer examination.

---

## 🔤 Core Acronyms

| Acronym | Full Definition | Context |
| :--- | :--- | :--- |
| **SUT** | **System Under Test** | The software application, microservice, or hardware being verified. |
| **TAF** | **Test Automation Framework** | Generic, reusable architectural foundation, rules, and libraries (independent of SUT). |
| **TAS** | **Test Automation Solution** | The live, operational deployment combining TAF + test cases + test data + SUT connection. |
| **gTAA** | **Generic Test Automation Architecture** | The official 4-layer reference model (Generation, Definition, Execution, Adaptation). |
| **DDT** | **Data-Driven Testing** | Separating test logic from external input datasets (CSV, JSON, SQL). |
| **KDT** | **Keyword-Driven Testing** | Expressing test steps using high-level action words (keywords) and parameters. |
| **BDD** | **Behavior-Driven Development** | Describing system behaviors in plain human language using Gherkin (`Given/When/Then`). |
| **MBT** | **Model-Based Testing** | Generating test cases automatically from mathematical state models or transition tables. |
| **POM** | **Page Object Model** | Design pattern encapsulating UI locators and actions within dedicated classes. |
| **PoC** | **Proof of Concept** | Short technical experiment verifying if a tool can physically interact with the SUT. |
| **ROI** | **Return on Investment** | The financial ratio comparing cost savings from automation against total development/maintenance costs. |

---

## 📚 Essential Official Definitions

### Architecture & Framework
- **Test Harness:** An execution environment containing drivers, stubs, and harnesses needed to execute a test suite automatically.
- **Test Adapter (Layer 4):** A translator component that converts generic commands from the Test Execution Layer into protocol-specific actions on the SUT (e.g., HTTP requests, Selenium clicks).
- **Service Virtualization:** Simulating the behavior and responses of unavailable, costly, or third-party downstream services (e.g., credit card payment gateway).
- **Test Hook (Backdoor):** Dedicated programmatic access points built into the SUT code specifically to enable automated inspection or state setting.

### Testability & Quality
- **Controllability:** The degree to which an SUT can be placed into a known, pre-conditioned initial state (e.g., resetting database records via an API endpoint).
- **Observability:** The degree to which the internal state, outputs, and behaviors of the SUT can be inspected by the test automation suite.
- **Determinism:** The principle that a test should yield the identical pass/fail result whenever executed against an unchanged SUT.
- **Flakiness (Intermittent Test):** A test that produces both passing and failing results over multiple runs without any changes to the code or environment.

### Verification & Metrics
- **False Positive (Type I Error):** A test result reporting **FAIL** when the SUT is actually functioning correctly (often due to timing, locators, or environment issues).
- **False Negative (Type II Error):** A test result reporting **PASS** when the SUT actually contains a software defect (often due to missing or weak assertions).
- **Mutation Testing:** A technique to evaluate test suite quality by intentionally injecting syntactic bugs ("mutants") into the SUT and checking if the tests detect ("kill") them.
- **Dual-Running:** Running manual and automated regression suites in parallel during transition to validate automation accuracy and build confidence.
- **Pesticide Paradox:** The phenomenon where repeating the same automated regression tests ceases to find new defects over time.
