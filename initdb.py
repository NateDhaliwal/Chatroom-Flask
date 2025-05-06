from config import chatdb, execute, userdb

# Create databases, see format

# chatmessages and chatdata are both TEXT types to store JSON data

execute(chatdb, '''
CREATE TABLE IF NOT EXISTS chatdb (
id INTEGER PRIMARY KEY,
chatname varchar(255) UNIQUE,
chatmessages TEXT NOT NULL,
chatdata TEXT NOT NULL
)
''')

execute(userdb, '''
CREATE TABLE IF NOT EXISTS userdb (
userid int PRIMARY KEY,
username varchar(15) UNIQUE,
name varchar(30),
password varchar(30) NOT NULL
)
''')
