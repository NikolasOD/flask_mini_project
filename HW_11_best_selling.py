import sqlite3
from flask import Flask
from flask import render_template

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('example.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/best_selling/<int:limit>')
def get_best_selling(limit):
    conn = get_connection()
    tracks = conn.execute('SELECT t.Name AS Name, SUM(ii.UnitPrice) AS Total \
                           FROM invoice_items AS ii \
                           JOIN tracks AS t ON ii.TrackId = t.TrackId \
                           GROUP BY ii.TrackId \
                           ORDER BY Total \
                           DESC LIMIT (?);', (limit,)).fetchall()
    conn.close()
    return render_template('tracks.html', tracks=tracks)


app.run(debug=True, port=5050)
