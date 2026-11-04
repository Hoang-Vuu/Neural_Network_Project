"""LangChain wrappers around the approved database and API functions."""

from langchain_core.tools import tool
from db import find_attractions
from api import get_forecast


@tool
def find_attractions_tool(
    city: str,
    category: str | None = None,
    outdoor_only: bool = True,
    limit: int = 5,
) -> list[dict]:
    """Search seeded attractions in Stockholm, Gothenburg, Berlin, or Munich.

    Use for choosing real candidate places. Returns names, approximate
    coordinates, categories, indoor/outdoor flags, and descriptions.
    Does not provide opening hours or real-time availability.
    """
    return find_attractions(city, category, outdoor_only, limit)


@tool
def get_forecast_tool(
    latitude: float,
    longitude: float,
    days: int = 7
) -> dict:
    """Get a future daily forecast for coordinates from Open-Meteo.

    Returns local dates, daily maximum precipitation probability (%),
    and daily maximum 10-m wind speed (km/h). Call after obtaining
    coordinates from a returned attractions database row.
    """
    return get_forecast(latitude, longitude, days)


APPROVED_TOOLS = [
    find_attractions_tool,
    get_forecast_tool
]

TOOL_REGISTRY = {
    item.name: item for item in APPROVED_TOOLS
}


def groq_schema(item):
    """Convert a LangChain tool into a Groq-compatible function schema."""
    return {
        "type": "function",
        "function": {
            "name": item.name,
            "description": item.description,
            "parameters": item.args_schema.model_json_schema()
        }
    }


TOOL_SCHEMAS = [
    groq_schema(item) for item in APPROVED_TOOLS
]
