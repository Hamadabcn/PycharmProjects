import sqlite3
from pathlib import Path

# 'a' to append, 'd' to delete, 's' to show, 'u' to update, 'q' to quit
message = """
'a' => Add New Task
'd' => Delete A Task
's' => Show All Tasks
'u' => Update A Task
'q' => Quit the App
Please choose an option: 
"""

# even if the input is in capital letters it will lowercase it and strip the whitespaces
user_input = input(message).strip().lower()

# command list
command_list = ['a', 'd', 's', 'u', 'q']

user_id = 2  # this is the user_id (you can add as many users as you want)

try:
    # connect to DB
    sqliteConnection = sqlite3.connect(Path.home() / Path("OneDrive", "Escritorio", "todoApp.db"))
    crsr = sqliteConnection.cursor()

except:
    print("connection error")

finally:
    if(sqliteConnection):
        # create table
        sql_command = """CREATE TABLE IF NOT EXISTS tasks(
        user_id INTEGER,
        task_name VARCHAR(20),
        description TEXT)"""
        crsr.execute(sql_command)

        # 's' => Show All Tasks
        def show_tasks():
            # {user_id} will get the tasks of the number of the user used
            crsr.execute(f"SELECT * FROM tasks WHERE user_id='{user_id}'")  # * means everything

            results = crsr.fetchall()

            print(f"You have {len(results)} tasks")

            if len(results) > 0:
                for task in results:
                    # index 1 to get the second column which contains task_name
                    print(f"Task Name: {task[1]} AND", end=" ")
                    print(f"Description: {task[2]}")

            sqliteConnection.commit()

        # 'a' => Add New Task
        def add_task():
            task_name = input("Write Task Name: ").strip()
            des = input("Write Task Description: ").strip()

            crsr.execute(f"INSERT INTO tasks (user_id, task_name, description) VALUES ('{user_id}', '{task_name}', '{des}')")

            sqliteConnection.commit()

        # 'd' => Delete A Task
        def delete_task():
            task_name = input("Write Task Name You Want To Delete: ").strip()

            crsr.execute(f"DELETE FROM tasks where task_name = '{task_name}' AND user_id = '{user_id}'")
            sqliteConnection.commit()

        # 'u' => Update A Task
        def update_task():
            task_name = input("Write The Name Of The Task You Want To Modify: ").strip()
            crsr.execute(f"SELECT * FROM tasks WHERE task_name = '{task_name}' AND user_id = '{user_id}'")
            results = crsr.fetchall()

            if not results:
                print("No Task with that Name Found.")

            else:
                des = input("Write The New Task Description: ").strip()
                crsr.execute(f"UPDATE tasks SET description='{des}' WHERE task_name = '{task_name}' AND user_id = '{user_id}'")

                sqliteConnection.commit()

                print("The Task Updated Successfully!")

        # 'q' => Quit the App
        def end_app():
            print("Thank You For Using todoApp.")
            exit()

        if user_input in command_list:
            if user_input == 's':
                show_tasks()

            elif user_input == 'a':
                add_task()

            elif user_input == 'd':
                delete_task()

            elif user_input == 'u':
                update_task()

            else:
                end_app()

        else:
            print('Sorry, this command in not found')

    sqliteConnection.close()
