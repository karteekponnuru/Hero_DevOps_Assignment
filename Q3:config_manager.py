import configparser, json, sqlite3
from flask import Flask

app = Flask(__name__)

f = input("config file name: ")
c = configparser.ConfigParser()
c.read(f)
d = {}
for s in c.sections():
    d[s] = dict(c.items(s))

con = sqlite3.connect("config.db")
cur = con.cursor()
cur.execute("create table if not exists t (id integer primary key, data text)")
cur.execute("insert into t (data) values (?)", (json.dumps(d),))
con.commit()
con.close()

@app.route("/config")
def show():
    con = sqlite3.connect("config.db")
    cur = con.cursor()
    cur.execute("select data from t order by id desc limit 1")
    r = cur.fetchone()
    con.close()
    return json.loads(r[0]) if r else {}

app.run()
