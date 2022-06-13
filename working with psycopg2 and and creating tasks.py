import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import datetime
class Todo:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.create_or_get_table()
    
    def connect_to_db(self):
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="myordersystemdb",
                user="postgres",
                password="Promise678.",
                cursor_factory=RealDictCursor
            )
            self.cur = self.conn.cursor()
            print("Connection successful!")
            return True
        except Exception as error:
            print("Unable to connect to database")
            print("Error: ", error)
            return False
         

    def create_or_get_table(self):
        connection =  self.connect_to_db()
        if connection:
            try:
                self.cur.execute("""
                CREATE TABLE public.todo
                (
                    title character varying,
                    active boolean,
                    created_at timestamp with time zone NOT NULL DEFAULT now()
                );
                ALTER TABLE IF EXISTS public.todo
                    OWNER to postgres;
                """)
                self.conn.commit()
                return print("Table has been successfully created!")
            except Exception as error:
                print("Error: ", error)
                print("Reconnecting...")
                return self.connect_to_db()
        return print("Failed to create table.")
    
    def get_tasks(self):
        self.cur.execute("""SELECT * FROM todo""")
        tasks = list(map(dict, self.cur.fetchall()))
        data = {'Title':[], 'Active':[], 'Created_at': []}
        for task in tasks:
            data["Title"].append(task["title"])
            data["Active"].append(str(task["active"]))
            data["Created_at"].append(str(task["created_at"].date()))
        
        df = pd.DataFrame(data)
        df.index.name = 's/n'
        df.index += 1
        print(df)
    
    def create_task(self, title, active:bool):
        self.cur.execute("""SELECT * FROM todo WHERE title = '{}' """.format(title))
        task = self.cur.fetchone()
        if task:
            print("Task Already Exists")
            return
        self.cur.execute("""INSERT INTO todo(title, active) VALUES(%s,%s) RETURNING *""", (title, active))
        time.sleep(2)
        new_task = dict(self.cur.fetchone())
        self.conn.commit()
        data = {'Title':[new_task["title"]], 'Active':[str(new_task["active"])], 'Created_at': [str(new_task["created_at"].date())]}
        df = pd.DataFrame(data)
        df.index.name = 's/n'
        df.index += 1
        print(df)
        print('\n')
    
    def get_task(self, title):
        self.cur.execute("""SELECT * FROM todo WHERE title = '{}' """.format(title))
        try:
            task = dict(self.cur.fetchone())
            data = {'Title':[task["title"]], 'Active':[str(task["active"])], 'Created_at': [str(task["created_at"].date())]}
            df = pd.DataFrame(data)
            df.index.name = 's/n'
            df.index += 1
            print(df)
            return True
        except TypeError:
            print("\nTask Doesn't exist")
            return False
    
    def update_task(self, title, new_title, active:bool):
        self.cur.execute("""UPDATE todo SET title=%s, active=%s, created_at=%s WHERE title=%s RETURNING *""", (new_title, active, datetime.datetime.now(), title))
        try:
            updated_task = dict(self.cur.fetchone())
            self.conn.commit()
            data = {'Title':[updated_task["title"]], 'Active':[str(updated_task["active"])], 'Created_at': [str(updated_task["created_at"].date())]}
            df = pd.DataFrame(data)
            df.index.name = 's/n'
            df.index += 1
            print(df)
        except TypeError:
            print("\nTask Doesn't exist")
    def delete_task(self, title):
        if not self.get_task(title):
            return 
        self.cur.execute("""DELETE FROM todo WHERE title = '{}' """.format(title))
        self.conn.commit()
        print("Task Successfully Deleted!")
 

todo = Todo()
print("\nCreate Task\n==========")
todo.create_task("new task", False)
todo.create_task("go swimming", False)
todo.create_task("go shopping", False)
todo.create_task("buy clothes", False)
print("\nRetrieve Task\n=====")
todo.get_task("go swimming")
print("\nUpdate Task\n=====")
todo.update_task("go swimming", "prepare dishes", True)
print("\nDelete Task\n=============")
todo.delete_task("go shopping")
print("\nToDo List\n=======")
todo.get_tasks()
