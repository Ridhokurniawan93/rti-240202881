-- Schema PostgreSQL untuk DBMS Benchmarking
-- Tabel: app_playstore (19 kolom, terinspirasi dataset Google Playstore)

DROP TABLE IF EXISTS app_playstore CASCADE;

CREATE TABLE app_playstore (
    id              SERIAL PRIMARY KEY,
    app_name        VARCHAR(255) NOT NULL,
    app_id          VARCHAR(100) NOT NULL,
    category        VARCHAR(100) NOT NULL,
    rating          FLOAT DEFAULT 0.0,
    rating_count    INT DEFAULT 0,
    installs        VARCHAR(50),
    free            BOOLEAN DEFAULT TRUE,
    price           FLOAT DEFAULT 0.0,
    currency        VARCHAR(10) DEFAULT 'USD',
    size            VARCHAR(20),
    min_android     VARCHAR(50),
    developer_id    VARCHAR(100),
    released        DATE,
    last_updated    DATE,
    content_rating  VARCHAR(50),
    ad_supported    BOOLEAN DEFAULT FALSE,
    in_app_purchases BOOLEAN DEFAULT FALSE,
    editors_choice  BOOLEAN DEFAULT FALSE,
    scraped_time    TIMESTAMP DEFAULT NOW()
);

-- Index akan ditambahkan secara dinamis oleh script benchmarking
-- sesuai kondisi eksperimen (none, single, composite)
