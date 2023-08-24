import bcrypt
import sqlite3

conn = sqlite3.connect('project.db')
cur = conn.cursor()
def verify_user(user, password=None):
    cur.execute("SELECT password FROM users WHERE name=?", (user,))
    result = cur.fetchone()
    conn.close()
    
    if not result: return False
    if password is None: return True
    
    return bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8'))
