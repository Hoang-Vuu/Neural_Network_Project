# Sprint 1 Backlog

## Sprint Goal

Deliver a working weather-aware trip planner assistant that combines a SQLite attractions database, a live weather API, and a Groq-hosted Qwen model to recommend suitable outdoor attractions.

---

## Scrum Roles

### Product Owner

Responsibilities:
- Defined the product vision.
- Prioritized backlog items.
- Verified that implemented features provided value to end users.

### Scrum Master

Responsibilities:
- Tracked sprint progress.
- Monitored blockers and technical issues.
- Coordinated testing and integration activities.

### Developers
All team members

Responsibilities:
- Database implementation.
- Tool development.
- API integration.
- Agent integration.
- Testing and evaluation.
- Documentation.

---

## Sprint Backlog

| Product Backlog Item | Sprint Task | Owner(s) | Estimate | Status | Acceptance Evidence |
|----------------------|-------------|-----------|----------|---------|--------------------|
| PBI-01 | Implement attraction search tool using SQLite database | Hoang Vu | 4h | Done | Successful database queries for Stockholm, Berlin, and Munich |
| PBI-02 | Implement weather forecast API tool using Open-Meteo | Hoang Vu | 3h | Done | Weather forecast data successfully returned |
| PBI-03 | Register LangChain tools and tool schemas |  | 2h | Done | Tools available and callable by the model |
| PBI-04 | Integrate Groq-hosted Qwen model |  | 3h | Done | Model generated valid tool calls |
| PBI-05 | Implement multi-tool agent workflow |  | 4h | Done | Agent successfully used database and API together |
| PBI-06 | Create command-line user interface |  | 1h | Done | User can enter requests and receive recommendations |
| PBI-07 | Evaluate assistant using representative test scenarios |  | 2h | Done | Evaluation report completed |
| PBI-08 | Prepare documentation and repository structure |  | 2h | Done | Required Sprint 1 documents completed |

---

## Sprint Planning

### Selected Work

- SQLite database integration
- Weather API integration
- LangChain tool implementation
- Groq-hosted Qwen integration
- Evaluation and documentation

### Scope Decisions

Included:
- Tool calling
- Database filtering
- Weather-based recommendations
- Evaluation and traces

Excluded:
- Streamlit GUI
- RAG
- Multi-agent architecture
- User accounts and authentication

---

## Daily Scrum / Progress Check-ins

The team synchronized progress through regular discussions during development sessions.

Frequency:
- Daily during active development
- Additional meetings when integration issues occurred

Topics discussed:
- Database implementation progress
- API integration status
- Model tool-calling behavior
- Testing results
- Documentation completion

---

## Definition of Done

A backlog item is considered Done when:

- The functionality works correctly.
- Acceptance criteria are satisfied.
- Evidence can be demonstrated.
- Code is committed to the repository.
- Documentation has been updated.