CREATE_ARTICLES_TABLE = (
    """
    CREATE TABLE IF NOT EXISTS articles(
        id SERIAL PRIMARY KEY,
        api_id VARCHAR (100) UNIQUE NOT NULL,
        title TEXT,
        url TEXT,
        description TEXT,
        body TEXT,
        snippet TEXT,
        img_url TEXT,
        language VARCHAR (100),
        published_at TIMESTAMP
    );
    """
)
