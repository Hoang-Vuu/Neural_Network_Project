# Product Backlog

The Product Backlog contains the ordered list of candidate work for the Weather-Aware Trip Planner Assistant. Items may be refined and reprioritized as the team gains more knowledge through development and evaluation.

| ID | User story / task | Priority | Acceptance criteria | Notes |
|----|-------------------|----------|---------------------|-------|
| PBI-01 | As a traveler, I want to search for attractions in a selected city so that I can find places to visit. | High | The assistant returns attractions stored in the SQLite database for the requested city. | Core database functionality. |
| PBI-02 | As a traveler, I want to filter attractions by category (park, museum, garden) so that I can find attractions matching my interests. | High | Only attractions matching the selected category are returned. | Uses SQL filtering. |
| PBI-03 | As a traveler, I want to view outdoor attractions only so that I can plan outdoor activities. | High | Returned attractions have `is_outdoor = 1`. | Supports weather-based recommendations. |
| PBI-04 | As a traveler, I want the assistant to retrieve weather forecasts for attraction locations so that I can choose a suitable day to visit. | High | The assistant successfully retrieves forecast data from the Open-Meteo API. | Requires external API integration. |
| PBI-05 | As a traveler, I want the assistant to recommend the best attraction and day based on weather conditions so that I can make informed travel decisions. | High | The recommendation uses actual database records and forecast values. | Main end-to-end workflow. |
| PBI-06 | As a traveler, I want a clear message when no attractions are available so that I understand the search result. | High | The assistant reports that no matching attractions were found and does not invent data. | Tested with unsupported cities such as Madrid. |
| PBI-07 | As a team, we want evaluation scenarios and trace logs so that we can verify tool use and answer groundedness. | Medium | Evaluation records and execution traces are stored and reviewed. | Required for Sprint 1. |
| PBI-08 | As a traveler, I want a graphical user interface so that I can interact with the assistant more easily. | Low | Users can access the assistant through a Streamlit interface. | Planned for Sprint 2. |

---

# Backlog Prioritization

## High Priority
- PBI-01 Attraction search
- PBI-02 Category filtering
- PBI-03 Outdoor filtering
- PBI-04 Weather API integration
- PBI-05 Weather-aware recommendation
- PBI-06 No-result handling

## Medium Priority
- PBI-07 Evaluation and trace logging

## Low Priority
- PBI-08 Streamlit user interface

---

# Backlog Refinement Notes

The backlog is expected to evolve based on Sprint Reviews, testing results, and user feedback.

Potential future backlog items include:

- User preferences and personalization
- Additional cities and attractions
- Multiple weather criteria
- Saved trips and history
- Streamlit dashboard
- Automated unit testing
- Improved ranking and recommendation logic