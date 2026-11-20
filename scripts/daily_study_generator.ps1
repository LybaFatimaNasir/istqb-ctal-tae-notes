# daily_study_generator.ps1
# Generates daily study streak entries for ISTQB CTAL-TAE on Windows native

$logFile = "DAILY_STUDY_LOG.md"
$todayStr = (Get-Date).ToUniversalTime().ToString("yyyy-MM-dd")

$topics = @(
    @{
        day = 1
        priority = "🔴 Priority 1 (High Weight)"
        chapter = "Chapter 3: Generic Architecture (gTAA)"
        title = "The 4 Layers of gTAA & Layer Boundaries"
        doc_link = "docs/priority-1-high-weight/01-chapter3-gTAA-architecture.md"
        summary = "The gTAA divides automation into 4 layers: Generation (test design/models), Definition (business test cases & data), Execution (runner & logging), and Adaptation (protocols, drivers, Selenium/HTTP adapters). Layer 4 absorbs all technical and locator changes!"
        question = "If an application UI changes from Angular to React, which layer of the gTAA must be modified?"
        answer = "Layer 4 (Test Adaptation Layer) only. High-level test definitions in Layer 2 remain untouched."
    },
    @{
        day = 2
        priority = "🔴 Priority 1 (High Weight)"
        chapter = "Chapter 3: Automation Approaches"
        title = "Data-Driven (DDT) vs Keyword-Driven (KDT)"
        doc_link = "docs/priority-1-high-weight/02-chapter3-test-automation-approaches.md"
        summary = "DDT separates test logic from external data fixtures (CSV, JSON). KDT represents test steps using action words (Keywords) like LOGIN, CLICK, ASSERT, allowing non-programmers to author tests via spreadsheets while engineers maintain keyword libraries."
        question = "Which approach is optimal when business analysts with no programming background need to author test cases?"
        answer = "Keyword-Driven Testing (KDT)."
    },
    @{
        day = 3
        priority = "🔴 Priority 1 (High Weight)"
        chapter = "Chapter 2: Preparing for Test Automation"
        title = "Proof of Concept (PoC) vs Pilot Project"
        doc_link = "docs/priority-1-high-weight/03-chapter2-preparing-for-automation.md"
        summary = "A PoC verifies technical feasibility (Can the tool click our custom dropdown?). A Pilot Project tests process, standards, naming rules, effort estimation, and team adoption on a real, non-critical project."
        question = "What is the primary objective of a test automation Pilot Project?"
        answer = "To learn the tool in depth, establish guidelines and standards, and evaluate organizational fit and ROI."
    },
    @{
        day = 4
        priority = "🔴 Priority 1 (High Weight)"
        chapter = "Chapter 7: Verifying the TAS"
        title = "False Positives vs False Negatives"
        doc_link = "docs/priority-1-high-weight/04-chapter7-verifying-the-tas.md"
        summary = "False Positive: Test reports FAIL, but SUT is working fine (wastes triage time, destroys trust). False Negative: Test reports PASS, but SUT has a defect (dangerous, defects leak to production)."
        question = "Why are False Positives dangerous to an automation team?"
        answer = "They cause 'cry wolf syndrome'—engineers start ignoring test failures, allowing real defects to pass through."
    },
    @{
        day = 5
        priority = "🟡 Priority 2 (Medium Weight)"
        chapter = "Chapter 5: Reporting & Metrics"
        title = "Internal vs External Metrics"
        doc_link = "docs/priority-2-medium-weight/05-chapter5-reporting-and-metrics.md"
        summary = "External metrics measure business and product value (time-to-market, defects caught before release). Internal metrics measure TAS health (execution duration, flakiness rate, false positive ratio, script maintenance hours)."
        question = "Is 'Flakiness Rate' an internal or external metric?"
        answer = "Internal metric—it measures the reliability of the test automation solution itself."
    }
)

$currentStreak = 1
if (Test-Path $logFile) {
    $raw = Get-Content $logFile -Raw
    $matches = [regex]::Matches($raw, "### Day ")
    $currentStreak = $matches.Count + 1
}

$topicIdx = ($currentStreak - 1) % $topics.Count
$topic = $topics[$topicIdx]

$entry = @"

### Day $currentStreak — $todayStr`: $($topic.title)
- **Priority:** $($topic.priority)
- **Syllabus Chapter:** $($topic.chapter)
- **Deep-Dive Notes:** [$($topic.title)]($($topic.doc_link))
- **Daily Key Takeaway:**
  > $($topic.summary)
- **❓ Exam Question of the Day:**
  > *$($topic.question)*
  <details>
  <summary>🔍 Click to Reveal Answer</summary>
  
  **Answer:** $($topic.answer)
  </details>

---
"@

$header = @"
# 📅 Daily Study Streak Tracker & Exam Flashcards

> **Automated Cloud Service:** This log updates automatically every single day via GitHub Actions, even if your laptop is closed. It serves daily bite-sized exam concepts, K-level questions, and keeps your learning streak alive!

| Current Streak | Status | Target Exam |
| :---: | :---: | :---: |
| 🔥 **Day $currentStreak** | 🟢 Active | ISTQB CTAL-TAE |

---

## 📖 Daily Study History

"@

if (!(Test-Path $logFile)) {
    Set-Content -Path $logFile -Value ($header + $entry) -Encoding UTF8
} else {
    $existing = Get-Content $logFile -Raw
    $updatedHeader = [regex]::Replace($existing, "🔥 \*\*Day \d+\*\*", "🔥 **Day $currentStreak**")
    $marker = "## 📖 Daily Study History`r`n`r`n"
    if ($updatedHeader.Contains($marker)) {
        $parts = $updatedHeader.Split($marker)
        $newContent = $parts[0] + $marker + $entry + $parts[1]
    } else {
        $newContent = $updatedHeader + $entry
    }
    Set-Content -Path $logFile -Value $newContent -Encoding UTF8
}

Write-Output "✅ Generated Daily Study Entry for Day $currentStreak`: $($topic.title)"
