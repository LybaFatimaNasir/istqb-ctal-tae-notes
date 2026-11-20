#!/usr/bin/env python3
"""
daily_study_generator.py
Automated Daily Study Streak & Exam Flashcard Generator for ISTQB CTAL-TAE.
Executes daily via GitHub Actions in the cloud (even if your laptop is closed).
"""

import os
import sys
from datetime import datetime, timezone

STUDY_TOPICS = [
    {
        "day": 1,
        "priority": "🔴 Priority 1 (High Weight)",
        "chapter": "Chapter 3: Generic Architecture (gTAA)",
        "title": "The 4 Layers of gTAA & Layer Boundaries",
        "doc_link": "docs/priority-1-high-weight/01-chapter3-gTAA-architecture.md",
        "summary": "The gTAA divides automation into 4 layers: Generation (test design/models), Definition (business test cases & data), Execution (runner & logging), and Adaptation (protocols, drivers, Selenium/HTTP adapters). Layer 4 absorbs all technical and locator changes!",
        "question": "If an application UI changes from Angular to React, which layer of the gTAA must be modified?",
        "answer": "Layer 4 (Test Adaptation Layer) only. High-level test definitions in Layer 2 remain untouched."
    },
    {
        "day": 2,
        "priority": "🔴 Priority 1 (High Weight)",
        "chapter": "Chapter 3: Automation Approaches",
        "title": "Data-Driven (DDT) vs Keyword-Driven (KDT)",
        "doc_link": "docs/priority-1-high-weight/02-chapter3-test-automation-approaches.md",
        "summary": "DDT separates test logic from external data fixtures (CSV, JSON). KDT represents test steps using action words (Keywords) like LOGIN, CLICK, ASSERT, allowing non-programmers to author tests via spreadsheets while engineers maintain keyword libraries.",
        "question": "Which approach is optimal when business analysts with no programming background need to author test cases?",
        "answer": "Keyword-Driven Testing (KDT)."
    },
    {
        "day": 3,
        "priority": "🔴 Priority 1 (High Weight)",
        "chapter": "Chapter 2: Preparing for Test Automation",
        "title": "Proof of Concept (PoC) vs Pilot Project",
        "doc_link": "docs/priority-1-high-weight/03-chapter2-preparing-for-automation.md",
        "summary": "A PoC verifies technical feasibility (Can the tool click our custom dropdown?). A Pilot Project tests process, standards, naming rules, effort estimation, and team adoption on a real, non-critical project.",
        "question": "What is the primary objective of a test automation Pilot Project?",
        "answer": "To learn the tool in depth, establish guidelines and standards, and evaluate organizational fit and ROI."
    },
    {
        "day": 4,
        "priority": "🔴 Priority 1 (High Weight)",
        "chapter": "Chapter 7: Verifying the TAS",
        "title": "False Positives vs False Negatives",
        "doc_link": "docs/priority-1-high-weight/04-chapter7-verifying-the-tas.md",
        "summary": "False Positive: Test reports FAIL, but SUT is working fine (wastes triage time, destroys trust). False Negative: Test reports PASS, but SUT has a defect (dangerous, defects leak to production).",
        "question": "Why are False Positives dangerous to an automation team?",
        "answer": "They cause 'cry wolf syndrome'—engineers start ignoring test failures, allowing real defects to pass through."
    },
    {
        "day": 5,
        "priority": "🟡 Priority 2 (Medium Weight)",
        "chapter": "Chapter 5: Reporting & Metrics",
        "title": "Internal vs External Metrics",
        "doc_link": "docs/priority-2-medium-weight/05-chapter5-reporting-and-metrics.md",
        "summary": "External metrics measure business and product value (time-to-market, defects caught before release). Internal metrics measure TAS health (execution duration, flakiness rate, false positive ratio, script maintenance hours).",
        "question": "Is 'Flakiness Rate' an internal or external metric?",
        "answer": "Internal metric—it measures the reliability of the test automation solution itself."
    },
    {
        "day": 6,
        "priority": "🟡 Priority 2 (Medium Weight)",
        "chapter": "Chapter 4: Implementation Risks",
        "title": "Mitigating Vendor Lock-in",
        "doc_link": "docs/priority-2-medium-weight/06-chapter4-risks-and-contingencies.md",
        "summary": "Vendor lock-in happens when tests depend directly on proprietary tool features. Mitigation: encapsulate all proprietary tool calls inside Layer 4 (Test Adaptation Layer), keeping business test scripts in standard open formats.",
        "question": "How does the gTAA architecture protect against commercial tool vendor lock-in?",
        "answer": "By isolating tool-specific APIs in Layer 4 adapters, so replacing the tool only requires rewriting adapters."
    },
    {
        "day": 7,
        "priority": "🟡 Priority 2 (Medium Weight)",
        "chapter": "Chapter 6: Transitioning to Automation",
        "title": "The Dual-Running Strategy",
        "doc_link": "docs/priority-2-medium-weight/07-chapter6-transitioning-manual-to-auto.md",
        "summary": "Dual-running executes manual and automated tests side-by-side during the transition phase. This builds confidence, calibrates false results, and ensures release quality before turning off manual regression.",
        "question": "When can a team safely stop dual-running?",
        "answer": "When the automated suite runs deterministically with near-zero false alarms for consecutive releases."
    },
    {
        "day": 8,
        "priority": "🟢 Priority 3 (Foundational)",
        "chapter": "Chapter 8: Continuous Improvement",
        "title": "Managing Automation Technical Debt",
        "doc_link": "docs/priority-3-foundational/08-chapter8-continuous-improvement.md",
        "summary": "Technical debt in automation comes from hardcoded sleeps, duplicated locators, and unmaintained tests. Over time, tests become flaky. Fix it by allocating 15-20% capacity for refactoring and retiring obsolete tests.",
        "question": "When should an automated test be retired from the regression suite?",
        "answer": "When the feature is removed from SUT, coverage is redundant with lower-level tests, or maintenance exceeds value."
    },
    {
        "day": 9,
        "priority": "🟢 Priority 3 (Foundational)",
        "chapter": "Chapter 1: Intro & Objectives",
        "title": "Realistic Goals & The Pesticide Paradox",
        "doc_link": "docs/priority-3-foundational/09-chapter1-intro-and-objectives.md",
        "summary": "Test automation is designed for fast, repeatable regression feedback. It does not replace manual exploratory testing. Over time, repeating the exact same tests catches fewer new bugs (Pesticide Paradox).",
        "question": "Does automating 100% of all test cases yield the highest ROI?",
        "answer": "No! 100% automation is economically infeasible; complex edge cases and usability tests should remain manual."
    },
    {
        "day": 10,
        "priority": "🔴 Priority 1 (High Weight)",
        "chapter": "Chapter 7: Verifying the TAS",
        "title": "Mutation Testing & Fault Injection",
        "doc_link": "docs/priority-1-high-weight/04-chapter7-verifying-the-tas.md",
        "summary": "Mutation testing injects deliberate bugs ('mutants') into SUT code. If the test suite fails, the mutant is 'killed' (good!). If the test suite passes, the mutant 'survives' (reveals missing test assertions).",
        "question": "What does a survived mutant indicate in mutation testing?",
        "answer": "It reveals a deficiency or missing assertion in the test suite—the deliberate bug went unnoticed!"
    }
]

def update_daily_log():
    log_file = "DAILY_STUDY_LOG.md"
    today_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # Calculate streak from existing log
    current_streak = 1
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            content = f.read()
            # Count previous streak entries
            current_streak = content.count("### Day ") + 1

    topic_idx = (current_streak - 1) % len(STUDY_TOPICS)
    topic = STUDY_TOPICS[topic_idx]

    entry = f"""
### Day {current_streak} — {today_str}: {topic['title']}
- **Priority:** {topic['priority']}
- **Syllabus Chapter:** {topic['chapter']}
- **Deep-Dive Notes:** [{topic['title']}]({topic['doc_link']})
- **Daily Key Takeaway:**
  > {topic['summary']}
- **❓ Exam Question of the Day:**
  > *{topic['question']}*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** {topic['answer']}
  </details>

---
"""

    header = """# 📅 Daily Study Streak Tracker & Exam Flashcards

> **Automated Cloud Service:** This log updates automatically every single day via GitHub Actions, even if your laptop is closed. It serves daily bite-sized exam concepts, K-level questions, and keeps your learning streak alive!

| Current Streak | Status | Target Exam |
| :---: | :---: | :---: |
| 🔥 **Day {streak}** | 🟢 Active | ISTQB CTAL-TAE |

---

## 📖 Daily Study History

""".format(streak=current_streak)

    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(header + entry)
    else:
        with open(log_file, "r", encoding="utf-8") as f:
            existing = f.read()
        
        # Update streak counter in header
        import re
        updated_header = re.sub(r"🔥 \*\*Day \d+\*\*", f"🔥 **Day {current_streak}**", existing)
        
        # Append new daily entry right below the Daily Study History header
        marker = "## 📖 Daily Study History\n\n"
        if marker in updated_header:
            parts = updated_header.split(marker, 1)
            new_content = parts[0] + marker + entry + parts[1]
        else:
            new_content = updated_header + entry
            
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(new_content)

    print(f"✅ Generated Daily Study Entry for Day {current_streak}: {topic['title']}")
    return current_streak, topic

if __name__ == "__main__":
    streak, topic = update_daily_log()
