import sqlite3
conn = sqlite3.connect('prac.db')
c = conn.cursor()
def table():
    c.execute("CREATE TABLE IF NOT EXISTS username(username VARCHAR, password VARCHAR)")
table()
def add_money():
    c.execute("CREATE TABLE IF NOT EXISTS money(amount INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS number(passwored,bankAccountNumber,Accountballancex)")
add_money