TEMPERATURE_TABLE_CREATE = (
    "CREATE TABLE IF NOT EXISTS temperature ("
    " 'id' INTEGER PRIMARY KEY AUTOINCREMENT,"
    " 'created_on' DATETIME NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%f','now'))," # UTC time.
    " 'temp_c' REAL NOT NULL,"
    " 'temp_f' REAL NOT NULL"
    ");"
)
