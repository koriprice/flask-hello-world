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

@app.route("/db_create")
def db_create():
    conn = psycopg2.connect("postgres://lab10_db_dj5p_user:Gzt7PjRQJ45ne27wUD6P52m6bJiTJ5bE@dpg-co51ku779t8c739a5ngg-a/lab10_db_dj5p")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball (
    First varchar(255),
    Last varchar(255),
    City varchar(255),
    Name varchar(255),
    Number int
    );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"
    
    
