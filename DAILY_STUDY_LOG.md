# 📅 Daily Study Streak Tracker & Exam Flashcards

> **Automated Cloud Service:** This log updates automatically every single day via GitHub Actions, even if your laptop is closed. It serves daily bite-sized exam concepts, K-level questions, and keeps your learning streak alive!

| Current Streak | Status | Target Exam |
| :---: | :---: | :---: |
| 🔥 **Day 2** | 🟢 Active | ISTQB CTAL-TAE |

---

## 📖 Daily Study History


### Day 2 — 2026-11-21: Data-Driven (DDT) vs Keyword-Driven (KDT)
- **Priority:** 🔴 Priority 1 (High Weight)
- **Syllabus Chapter:** Chapter 3: Automation Approaches
- **Deep-Dive Notes:** [Data-Driven (DDT) vs Keyword-Driven (KDT)](docs/priority-1-high-weight/02-chapter3-test-automation-approaches.md)
- **Daily Key Takeaway:**
  > DDT separates test logic from external data fixtures (CSV, JSON). KDT represents test steps using action words (Keywords) like LOGIN, CLICK, ASSERT, allowing non-programmers to author tests via spreadsheets while engineers maintain keyword libraries.
- **❓ Exam Question of the Day:**
  > *Which approach is optimal when business analysts with no programming background need to author test cases?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** Keyword-Driven Testing (KDT).
  </details>

---
### Day 1 — 2026-11-20: The 4 Layers of gTAA & Layer Boundaries
- **Priority:** 🔴 Priority 1 (High Weight)
- **Syllabus Chapter:** Chapter 3: Generic Architecture (gTAA)
- **Deep-Dive Notes:** [The 4 Layers of gTAA & Layer Boundaries](docs/priority-1-high-weight/01-chapter3-gTAA-architecture.md)
- **Daily Key Takeaway:**
  > The gTAA divides automation into 4 layers: Generation (test design/models), Definition (business test cases & data), Execution (runner & logging), and Adaptation (protocols, drivers, Selenium/HTTP adapters). Layer 4 absorbs all technical and locator changes!
- **❓ Exam Question of the Day:**
  > *If an application UI changes from Angular to React, which layer of the gTAA must be modified?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** Layer 4 (Test Adaptation Layer) only. High-level test definitions in Layer 2 remain untouched.
  </details>

---
