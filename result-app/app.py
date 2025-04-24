from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_results():
    conn = psycopg2.connect(
        host='db',
        database='voting_db',
        user='voting_user',
        password='voting_pass'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT choice, COUNT(*) FROM votes GROUP BY choice")
    results = cursor.fetchall()
    conn.close()
    return dict(results)

@app.route('/')
def show_results():
    results = get_results()
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
