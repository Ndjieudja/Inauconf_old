  CREATE TABLE IF NOT EXISTS inauconf(
        id      SERIAL PRIMARY KEY,
        identifiant       TEXT UNIQUE,
        iaf_pass      VARCHAR(10) UNIQUE
                );

