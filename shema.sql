self.cursor.executescripts('''
                CREATE TABLE IF IS NOT EXISTS inauconf(
                        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        user_name       TEXT UNIQUE
                        password        INTEGER NOT NULL UNIQUE
                );
                
                ''')