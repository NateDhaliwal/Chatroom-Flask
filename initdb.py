from main import *

execute(userdb, '''
CREATE TABLE chatdb (
id INTEGER PRIMARY KEY,
chatname varchar(255) UNIQUE,
chatmessages TEXT NOT NULL,
chatdata TEXT NOT NULL
)
''')
