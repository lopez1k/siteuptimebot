from sqlite3 import connect 


class DataBase():
    def connection():
        conn = connect('data/main.db')
        cur = conn.cursor()
        return conn, cur
    
    def create_db():
        conn, cur = DataBase.connection()
        cur.execute("CREATE TABLE IF NOT EXISTS sites(id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, website TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, uid INTEGER, silent INTEGER DEFAULT '0', pause INTEGER DEFAULT '0')")
        conn.commit()
        conn.close()

    def add_site(uid, site):
        conn, cur = DataBase.connection()
        cur.execute("INSERT INTO sites(uid, website) VALUES(?,?)", (uid, site))
        conn.commit()
        conn.close()

    def del_site(uid, site):
        conn, cur = DataBase.connection()
        cur.execute("DELETE FROM sites WHERE uid = ? AND website = ?", (uid, site))
        conn.commit()
        conn.close()

    def create_user(uid):
        conn, cur = DataBase.connection()
        cur.execute("SELECT * FROM users WHERE uid=?", (uid,))
        res = cur.fetchone()
        if res:
            pass
        else:
            cur.execute("INSERT INTO users(uid) VALUES(?)", (uid,))
            conn.commit()
        conn.close()

    def get_user_links(uid):
        conn, cur = DataBase.connection()
        cur.execute("SELECT website FROM sites WHERE uid = ?", (uid,))
        result = cur.fetchall()
        conn.close()
        return result
    
    def check_site():
        conn, cur = DataBase.connection()
        cur.execute("SELECT DISTINCT uid FROM sites")
        users = cur.fetchall()
        return users
    
    def get_setting_user(uid):
        conn, cur = DataBase.connection()
        cur.execute("SELECT silent, pause FROM users WHERE uid = ?", (uid,))
        res = cur.fetchone()
        silent, pause = res[0], res[1]
        conn.close()
        return silent, pause
    
    def switch_silent(uid):
        conn, cur = DataBase.connection()
        cur.execute("SELECT silent FROM users WHERE uid = ?", (uid,))
        res = cur.fetchone()
        silent = res[0]
        if silent == 0:
            cur.execute("UPDATE users SET silent = ? WHERE uid = ?", (1, uid))
        elif silent == 1:
            cur.execute("UPDATE users SET silent = ? WHERE uid = ?", (0, uid))
        conn.commit()
        conn.close()

    def switch_pause(uid):
        conn, cur = DataBase.connection()
        cur.execute("SELECT pause FROM users WHERE uid = ?", (uid,))
        res = cur.fetchone()
        silent = res[0]
        if silent == 0:
            cur.execute("UPDATE users SET pause = ? WHERE uid = ?", (1, uid))
        elif silent == 1:
            cur.execute("UPDATE users SET pause = ? WHERE uid = ?", (0, uid))
        conn.commit()
        conn.close()
        