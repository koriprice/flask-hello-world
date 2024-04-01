import psycopg2
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Kori Price in 3308'

@app.route("/db_test")
def db_test():
    conn = psycopg2.connect("postgres://lab10_db_dj5p_user:Gzt7PjRQJ45ne27wUD6P52m6bJiTJ5bE@dpg-co51ku779t8c739a5ngg-a/lab10_db_dj5p")
    conn.close()
    return "Database Connection Successful"
