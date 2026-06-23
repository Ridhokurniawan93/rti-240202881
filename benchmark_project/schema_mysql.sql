-- Schema MySQL untuk DBMS Benchmarking
-- Tabel: app_playstore (19 kolom, terinspirasi dataset Google Playstore)

DROP TABLE IF EXISTS app_playstore;

CREATE TABLE app_playstore (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    app_name        VARCHAR(255) NOT NULL,
    app_id          VARCHAR(100) NOT NULL,
    category        VARCHAR(100) NOT NULL,
    rating          FLOAT DEFAULT 0.0,
    rating_count    INT DEFAULT 0,
    installs        VARCHAR(50),
    free            TINYINT(1) DEFAULT 1,
    price           FLOAT DEFAULT 0.0,
    currency        VARCHAR(10) DEFAULT 'USD',
    size            VARCHAR(20),
    min_android     VARCHAR(50),
    developer_id    VARCHAR(100),
    released        DATE,
    last_updated    DATE,
    content_rating  VARCHAR(50),
    ad_supported    TINYINT(1) DEFAULT 0,
    in_app_purchases TINYINT(1) DEFAULT 0,
    editors_choice  TINYINT(1) DEFAULT 0,
    scraped_time    DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Index akan ditambahkan secara dinamis oleh script benchmarking
-- sesuai kondisi eksperimen (none, single, composite)
