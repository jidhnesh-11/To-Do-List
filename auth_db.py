import sqlite3

db_filename= "todo.db"

def get_conn():  # so we dont have to open the connection every time we can just call this func thats returns the conn!!!!!!
  conn= sqlite3.connect(db_filename)
  conn.execute("PRAGMA foreign_keys = ON") # so we can use foreign key rules in sqlite3!!
  return conn

def init_db(): # initializes the db!!
  
  with get_conn() as conn:
    conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL
            )
        """)
    
    conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                title TEXT NOT NULL,
                due_date TEXT,
                priority TEXT DEFAULT 'low',
                done INTEGER DEFAULT 0,
                FOREIGN KEY (username) REFERENCES users (username) ON DELETE CASCADE
            )
        """)
    
def signup(username,password):
  
  try:
    
    with get_conn() as conn:
      conn.execute("INSERT INTO users (username, password) VALUES (?, ?)",(username, password))
    return True , "Signup successful!!"
  
  except sqlite3.IntegrityError:
    return False, "Username already exists :( "
  
def login (username, password):
  
  conn= get_conn()
  cursor = conn.execute("SELECT * FROM users WHERE username = ? AND password = ?",(username, password))
  
  row = cursor.fetchone()
  conn.close()
  
  return row is not None # literal meaning 🥀, becomoes true if row is NOT NONE, lese false , this is a bool eqn!

def add_task(username, title, due_date, priority):
    """Insert a new task for the given user. Returns the new task ID."""
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO tasks (username, title, due_date, priority, done) VALUES (?, ?, ?, ?, 0)",
            (username, title, due_date, priority)
        )
        return cur.lastrowid
      
      
def get_tasks(username):  # to see the tasks of that USER !! 
  #FK username ^-^ 
  conn = get_conn()
  try:
    
    cursor = conn.execute("SELECT id, title, due_date, priority, done FROM tasks WHERE username = ?",(username,))
    
    rows = cursor.fetchall()  # fetch all
  finally:
    conn.close()
    
  tasks = []
    
  for row in rows:
      tasks.append({
            "id": row[0],
            "title": row[1],
            "due_date": row[2],
            "priority": row[3],
            "done": bool(row[4])   # convert if 0 False , 1 True- convert that shi-
        
      })
      
  return tasks
    
    
def delete_task(task_id, username): # do we really need an explanation 🥀
  
  with get_conn() as conn:
    conn.execute("DELETE FROM tasks WHERE id = ? AND username = ?",
            (task_id, username))
    

def toggle_task(task_id , username):  # the check and uncheck shi-
  
  with get_conn( ) as conn:
    
    conn.execute("UPDATE tasks SET done = NOT done WHERE id = ? AND username = ?",(task_id, username))
    
    cursor = conn.execute("SELECT done FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    if row:
        return bool(row[0])
    return None
    
    
    
