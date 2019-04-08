import pymysql

def showTask():
    sql= "SELECT id, task FROM tasks.task_list"
    conn= pymysql.connect(user='root', password='user', host='localhost', database='tasks')
    cur= conn.cursor()
    cur.execute(sql)
    res= cur.fetchall()
    cur.close()
    conn.close()
    return res

def newTask(args, urgent):
    sql = "INSERT INTO tasks.task_list(task, urgent) VALUES (%s, %s)"
    conn = pymysql.connect(user='root', password='user', host='localhost', database='tasks')
    cur = conn.cursor()
    cur.execute(sql, (args, urgent,))
    conn.commit()
    cur.close()
    conn.close()
    return


def removeTask(args):
    sql = "DELETE FROM tasks.task_list WHERE id= (%s)"
    conn = pymysql.connect(user='root', password='user', host='localhost', database='tasks')
    cur = conn.cursor()
    cur.execute(sql, (args,))
    conn.commit()
    cur.close()
    conn.close()
    return