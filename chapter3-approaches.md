# ISTQB CTAL-TAE - Chapter 3 continued

## Test Automation Approaches

### Data Driven Testing (DDT)
- Test logic is separated from test data
- Same test script runs with multiple data sets
- Data stored in external files (CSV, Excel, JSON)
- Reduces script duplication

### Keyword Driven Testing (KDT)
- Test actions represented as keywords
- Keywords implemented separately from test data
- Testers can write tests without programming knowledge
- Example keywords: OpenBrowser, Login, VerifyText

### BDD (Behaviour Driven Development)
- Tests written in natural language (Gherkin)
- Format: Given / When / Then
- Bridges gap between business and technical teams
- Tools: Cucumber, SpecFlow, Playwright with Cucumber

## Comparison
| Approach | Skill needed | Reusability | Maintenance |
|----------|-------------|-------------|-------------|
| DDT      | Medium      | High        | Low         |
| KDT      | Low         | Very High   | Medium      |
| BDD      | Low-Medium  | Medium      | Medium      |
