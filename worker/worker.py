import redis
import psycopg2
import time

r = redis.Redis(host='redis', port=6379, db=0)
conn = psycopg2.connect(
    host='db',
    database='voting_db',
    user='voting_user',
    password='voting_pass'
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    choice TEXT NOT NULL
)''')
conn.commit()

while True:
    vote = r.lpop('votes')
    if vote:
        vote = vote.decode('utf-8')
        cursor.execute('INSERT INTO votes (choice) VALUES (%s)', (vote,))
        conn.commit()
    time.sleep(1)
