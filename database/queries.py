class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS surveys_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL,
        visit_date DATE NOT NULL,
        food_rating INTEGER NOT NULL,
        cleanliness_rating INTEGER NOT NULL,
        extra_comments TEXT NOT NULL        
    )
    """