# 📅 Daily Study Streak Tracker & Exam Flashcards

> **Automated Cloud Service:** This log updates automatically every single day via GitHub Actions, even if your laptop is closed. It serves daily bite-sized exam concepts, K-level questions, and keeps your learning streak alive!

| Current Streak | Status | Target Exam |
| :---: | :---: | :---: |
| 🔥 **Day 7** | 🟢 Active | ISTQB CTAL-TAE |

---

## 📖 Daily Study History


### Day 7 — 2026-11-26: The Dual-Running Strategy
- **Priority:** 🟡 Priority 2 (Medium Weight)
- **Syllabus Chapter:** Chapter 6: Transitioning to Automation
- **Deep-Dive Notes:** [The Dual-Running Strategy](docs/priority-2-medium-weight/07-chapter6-transitioning-manual-to-auto.md)
- **Daily Key Takeaway:**
  > Dual-running executes manual and automated tests side-by-side during the transition phase. This builds confidence, calibrates false results, and ensures release quality before turning off manual regression.
- **❓ Exam Question of the Day:**
  > *When can a team safely stop dual-running?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** When the automated suite runs deterministically with near-zero false alarms for consecutive releases.
  </details>

---

### Day 6 — 2026-11-25: Mitigating Vendor Lock-in
- **Priority:** 🟡 Priority 2 (Medium Weight)
- **Syllabus Chapter:** Chapter 4: Implementation Risks
- **Deep-Dive Notes:** [Mitigating Vendor Lock-in](docs/priority-2-medium-weight/06-chapter4-risks-and-contingencies.md)
- **Daily Key Takeaway:**
  > Vendor lock-in happens when tests depend directly on proprietary tool features. Mitigation: encapsulate all proprietary tool calls inside Layer 4 (Test Adaptation Layer), keeping business test scripts in standard open formats.
- **❓ Exam Question of the Day:**
  > *How does the gTAA architecture protect against commercial tool vendor lock-in?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** By isolating tool-specific APIs in Layer 4 adapters, so replacing the tool only requires rewriting adapters.
  </details>

---

### Day 5 — 2026-11-24: Internal vs External Metrics
- **Priority:** 🟡 Priority 2 (Medium Weight)
- **Syllabus Chapter:** Chapter 5: Reporting & Metrics
- **Deep-Dive Notes:** [Internal vs External Metrics](docs/priority-2-medium-weight/05-chapter5-reporting-and-metrics.md)
- **Daily Key Takeaway:**
  > External metrics measure business and product value (time-to-market, defects caught before release). Internal metrics measure TAS health (execution duration, flakiness rate, false positive ratio, script maintenance hours).
- **❓ Exam Question of the Day:**
  > *Is 'Flakiness Rate' an internal or external metric?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** Internal metric—it measures the reliability of the test automation solution itself.
  </details>

---

### Day 4 — 2026-11-23: False Positives vs False Negatives
- **Priority:** 🔴 Priority 1 (High Weight)
- **Syllabus Chapter:** Chapter 7: Verifying the TAS
- **Deep-Dive Notes:** [False Positives vs False Negatives](docs/priority-1-high-weight/04-chapter7-verifying-the-tas.md)
- **Daily Key Takeaway:**
  > False Positive: Test reports FAIL, but SUT is working fine (wastes triage time, destroys trust). False Negative: Test reports PASS, but SUT has a defect (dangerous, defects leak to production).
- **❓ Exam Question of the Day:**
  > *Why are False Positives dangerous to an automation team?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** They cause 'cry wolf syndrome'—engineers start ignoring test failures, allowing real defects to pass through.
  </details>

---

### Day 3 — 2026-11-22: Proof of Concept (PoC) vs Pilot Project
- **Priority:** 🔴 Priority 1 (High Weight)
- **Syllabus Chapter:** Chapter 2: Preparing for Test Automation
- **Deep-Dive Notes:** [Proof of Concept (PoC) vs Pilot Project](docs/priority-1-high-weight/03-chapter2-preparing-for-automation.md)
- **Daily Key Takeaway:**
  > A PoC verifies technical feasibility (Can the tool click our custom dropdown?). A Pilot Project tests process, standards, naming rules, effort estimation, and team adoption on a real, non-critical project.
- **❓ Exam Question of the Day:**
  > *What is the primary objective of a test automation Pilot Project?*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** To learn the tool in depth, establish guidelines and standards, and evaluate organizational fit and ROI.
  </details>

---

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
