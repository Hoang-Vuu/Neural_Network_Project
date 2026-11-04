"""Read-only attractions catalog for the weather and trip-planner marathon."""

import sqlite3
from pathlib import Path

DB_PATH = Path("data/attractions_sweden_germany.sqlite")
DB_PATH.parent.mkdir(exist_ok=True)

# sample records; coordinates are approximate.
ATTRACTIONS = [
    (1, "Djurgården", "Stockholm", "Sweden", "park", 1, 59.325, 18.103,
     "Large area for outdoor walks and sightseeing."),
      (2, "Skansen Open-Air Museum", "Stockholm", "Sweden", "museum", 1,
     59.324, 18.101, "Open-air cultural attractions and historical buildings."),
    (3, "Vasa Museum", "Stockholm", "Sweden", "museum", 0,
     59.328, 18.091, "Indoor museum with a historic ship."),
    (4, "Slottsskogen", "Gothenburg", "Sweden", "park", 1,
     57.683, 11.947, "Large city park with walking paths."),
    (5, "Gothenburg Botanical Garden", "Gothenburg", "Sweden", "garden", 1,
     57.681, 11.953, "Outdoor botanical garden and walking areas."),
    (6, "Universeum", "Gothenburg", "Sweden", "museum", 0,
     57.695, 11.989, "Indoor science and nature exhibits."),
    (7, "Tiergarten", "Berlin", "Germany", "park", 1,
     52.515, 13.351, "Large green space in central Berlin."),
    (8, "Tempelhofer Feld", "Berlin", "Germany", "park", 1,
     52.473, 13.405, "Open recreational space on a former airfield."),
    (9, "German Museum of Technology", "Berlin", "Germany", "museum", 0,
     52.498, 13.377, "Indoor technology collections."),
    (10, "English Garden", "Munich", "Germany", "park", 1,
     48.152, 11.593, "Outdoor green space and walking routes."),
    (11, "Olympiapark", "Munich", "Germany", "park", 1,
     48.174, 11.549, "Outdoor recreation area and landscaped grounds."),
    (12, "Deutsches Museum", "Munich", "Germany", "museum", 0,
     48.130, 11.583, "Indoor science and technology museum."),
]


def initialize_db():
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS attractions (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                city TEXT NOT NULL,
                country TEXT NOT NULL,
                category TEXT NOT NULL,
                is_outdoor INTEGER NOT NULL CHECK(is_outdoor IN (0, 1)),
                latitude REAL NOT NULL,
                longitude REAL NOT NULL,
                description TEXT NOT NULL
            )
        """)

        connection.executemany("""
            INSERT OR IGNORE INTO attractions
            (id, name, city, country, category, is_outdoor,
             latitude, longitude, description)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ATTRACTIONS)

    return len(ATTRACTIONS)


def find_attractions(city, category=None, outdoor_only=True, limit=5):
    """Search the local catalog with parameterized SQL."""

    if not city or not city.strip():
        raise ValueError("city is required")

    if not 1 <= limit <= 12:
        raise ValueError("limit must be from 1 to 12")

    sql = "SELECT * FROM attractions WHERE lower(city) = lower(?)"
    arguments = [city.strip()]

    if outdoor_only:
        sql += " AND is_outdoor = ?"
        arguments.append(1)

    if category:
        sql += " AND lower(category) = lower(?)"
        arguments.append(category.strip())

    sql += " ORDER BY name LIMIT ?"
    arguments.append(limit)

    with sqlite3.connect(DB_PATH) as connection:
        connection.row_factory = sqlite3.Row
        rows = connection.execute(sql, arguments).fetchall()

    return [dict(row) for row in rows]

if __name__ == "__main__":
    initialize_db()
    print("Database:", DB_PATH)
    print("Berlin:", find_attractions("Berlin"))