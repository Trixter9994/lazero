import sqlite3

conn=sqlite3.connect("tits.db")

# it is not good.
# the command is not avaliable.
conn.execute("PRAGMA foreign_keys=off;")

conn.execute("BEGIN TRANSACTION;")

conn.execute("ALTER TABLE subdir  RENAME TO old_subdir;")

conn.execute("""CREATE TABLE subdir
( id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,name   TEXT    NOT NULL,
type         TINYINT     NOT NULL,  
depth TINYINT NOT NULL,
parent TEXT, 
miscellaneous TEXT NOT NULL,
  CONSTRAINT rule  UNIQUE (name, miscellaneous)
);""")

conn.execute("INSERT INTO subdir SELECT * FROM old_subdir;")

conn.execute("DROP TABLE old_subdir;")

#COMMIT;

conn.execute("PRAGMA foreign_keys=on;")

#conn.execute("ALTER TABLE subdir ADD CONSTRAINT chain UNIQUE (name, miscellaneous);")
#conn.execute("ALTER TABLE subdir ADD CONSTRAINT chain0 UNIQUE (id);")
conn.commit()
conn.close()
