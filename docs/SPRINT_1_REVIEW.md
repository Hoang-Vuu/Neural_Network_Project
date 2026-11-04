# Sprint 1 Review and Retrospective

## Sprint Goal

Deliver a working weather-aware trip planner assistant that combines database and weather information through LLM tool calling.

---

## Completed Work

### Database Integration

Completed:
- SQLite database created.
- Attraction search functionality implemented.
- Outdoor and category filtering supported.

Evidence:
- Successful retrieval of attractions in Stockholm, Berlin, and Munich.

---

### Weather API Integration

Completed:
- Open-Meteo forecast retrieval implemented.
- Daily precipitation probability extracted.
- Daily wind speed extracted.

Evidence:
- Forecast results returned successfully during evaluation scenarios.

---

### Tool Calling

Completed:
- LangChain tools registered.
- Groq-hosted Qwen successfully generated tool calls.
- Tool results returned to the model.

Evidence:
- Trace logs show calls to:
  - find_attractions_tool
  - get_forecast_tool

---

### User Interaction

Completed:
- Command-line interface implemented.
- Users can submit travel requests and receive recommendations.

Evidence:
- Demonstrated during evaluation scenarios.

---

## Partially Completed Work

### User Interface Improvements

Status:
- Not implemented.

Reason:
- Streamlit GUI is planned for Sprint 2.

---

## Not Completed

### Streamlit Web Interface

Reason:
- Outside Sprint 1 scope.

### Automated Unit Tests

Reason:
- Deferred to Sprint 2.

---

## Sprint Review Feedback

Positive Feedback:
- The assistant successfully combines information from both tools.
- Recommendations are grounded in real database rows and forecast results.
- Tool traces make behavior transparent.

Areas for Improvement:
- Improve handling of missing cities.
- Expand attraction coverage.
- Improve recommendation explanations.

---

## Product Backlog Changes

Added:
- Streamlit GUI
- Larger attraction database
- Persistent user preferences
- Automated testing

Increased Priority:
- Better error handling
- Improved tool validation

---

# Sprint Retrospective (4Ls)

## Liked

- Tool calling worked reliably.
- SQLite and Open-Meteo integration was straightforward.
- Execution traces simplified debugging.

## Learned

- The model requests tools, but Python validates and executes them.
- Grounded responses require verifying database and API outputs.

## Lacked

- More diverse attraction data.
- Better user interface.

## Longed For

- Streamlit web interface.
- More advanced recommendation features.
- Larger geographical coverage.

---

## Action for Sprint 2

Implement a Streamlit-based graphical user interface and expand the attractions database while maintaining grounded recommendations.