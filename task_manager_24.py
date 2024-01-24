import random

user_file = open("user.txt", "r+")
login = False
loop = 1
task_counter = 0
user_counter = 0 

# Beginning the loop by asking the user to enter their login details.
# If username and password are recognized, then it will log in.
# If the admin details are used, it will then output the admin's menu.
while login == False:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    for line in user_file:
        valid_username, valid_password = line.strip().split(",")

        if username == valid_username and password == valid_password:
            login = True
        elif username == "admin" and password == "adm1n":
            while loop == 1:
                choice = input("""
                Please select one of the following options:
                r - Register a user
                a - Add a task
                va - View all tasks
                vm - View my tasks
                s - View statistics
                e - Exit
                """).lower()

# If the admin selects "r" it will ask details to register another user.
# It will also pick up if the user already exists.
                if choice == "r":
                    user_file.close()
                    user_file = open("user.txt", "r")
                    new_username = input("Please enter the username of the new user:")
                    new_password = input("Please enter the password of the new user:")
                    for user in user_file:
                        usrname, pswrd = user.strip().split(",")
                        if new_username == usrname:
                            print("The Username already exists, please try again.")
                            new_username = input("Please enter the username of the new user:")
                            new_password = input("Please enter the password of the new user:")
                            print("Registration successful!")
                    user_file = open("user.txt","a+")
                    user_file.write(f"\n{new_username},{new_password}")
                    print("Registration successful!")
                    user_file.close()

# If the admin selects "a" it will allow the admin to assign a task to a user by entering the task details via inputs.
                if choice == "a":
                    task_file = open("tasks.txt", "a+")
                    user_task = input("Please enter the username of the person to whom the task is assigned to: ")
                    task_title = input("Please enter the task title: ")
                    task_description = input("Please enter the task description: ")
                    assign_date = input("Please enter the date you are assigning the task to the user: ")
                    due_date = input("Please enter the due date of the task: ")
                    task_id = random.randint(0, 100)
                    task_completed = input("Is the task completed: ")

                    # Below it will write the info to the .txt file.
                    task_file.write(f"{user_task}, {task_title}, {task_description}, {assign_date}, {due_date}, {task_id}, {task_completed}")
                    task_file.close()

# If the admin selects "va" it will output all the tasks.
                elif choice == "va":
                    task_file = open("tasks.txt", "r")

                    for line in task_file:
                        user_task, task_title, task_description, assign_date, due_date, task_id, task_completed = line.split(", ")

                        print(f"""
                        Name:           {user_task}
                        Task:           {task_title}
                        Description:    {task_description}
                        Date assigned:  {assign_date}  
                        Due date:       {due_date}
                        Task ID:        {task_id}
                        Completed:      {task_completed}
                        """)

                    task_file.close()

# If the admin selects "vm" it will view his own tasks.
                elif choice == "vm":
                    task_file = open("tasks.txt", "r")

                    for line in task_file:
                        user_task, task_title, task_description, assign_date, due_date, task_id, task_completed = line.split(", ")
                        if username == user_task:

                            print(f"""
                            Name:           {user_task}
                            Task:           {task_title}
                            Description:    {task_description}
                            Date assigned:  {assign_date}  
                            Due date:       {due_date}
                            Task ID:        {task_id}
                            Completed:      {task_completed}
                            """)

                    task_file.close()

# If the admin selects "s" it will output the amount of users and tasks.
                if choice == "s":
                    task_file = open("tasks.txt", "r")
                    user_file = open("user.txt", "r")

                    task_content = task_file.read()
                    con_list = task_content.split("\n")
                    for i in con_list:
                        if i:
                            task_counter += 1
                    print("There are", task_counter, "tasks.")

                    user_content = user_file.read()
                    con_list = user_content.split("\n")
                    for i in con_list:
                        if i:
                            user_counter += 1
                    print("There are", user_counter, "users.")

                    task_file.close()
                    user_file.close()

# If the admin selects "e" it will close the loop and stop the program.
                elif choice == "e":
                    print("Thank you for using our service.")
                    exit()
            loop = 0
            

# If invalid login details were entered, it will inform the user and loop back to the login details.
    if login == False:
        print("Please make sure that you have entered the correct username and password.")
    user_file.seek(0)

# If a user logged in other than the admin.
while loop == 1:
    choice = input("""
    Please select one of the following options:
    a - Add a task
    va - View all tasks
    vm - View my tasks
    e - Exit
    """).lower()

# If "a" is selected then user inputs are asked to add a task.
    if choice == "a":
        task_file = open("tasks.txt", "a+")
        user_task = input("Please enter the username of the person to whom the task is assigned to: ")
        task_title = input("Please enter the task title: ")
        task_description = input("Please enter the task description: ")
        assign_date = input("Please enter the date you are assigning the task to the user: ")
        due_date = input("Please enter the due date of the task: ")
        task_id = random.randint(0, 100)
        task_completed = input("Is the task completed: ")

        task_file.write(f"\n{user_task}, {task_title}, {task_description}, {assign_date}, {due_date}, {task_id}, {task_completed}")

        task_file.close()

# If "va" is selected then all tasks will be outputted.
    elif choice == "va":
        task_file = open("tasks.txt", "r")

        for line in task_file:
            user_task, task_title, task_description, assign_date, due_date, task_id, task_completed = line.split(", ")

            print(f"""
            Name:           {user_task}
            Task:           {task_title}
            Description:    {task_description}
            Date assigned:  {assign_date}  
            Due date:       {due_date}
            Task ID:        {task_id}
            Completed:      {task_completed}
            """)

        task_file.close()

# If "vm" is selected, the users tasks will be displayed depending on who signed in.
    elif choice == "vm":
        task_file = open("tasks.txt", "r")

        for line in task_file:
            user_task, task_title, task_description, assign_date, due_date, task_id, task_completed = line.split(", ")
            if username == user_task:

                print(f"""
                Name:           {user_task}
                Task:           {task_title}
                Description:    {task_description}
                Date assigned:  {assign_date}  
                Due date:       {due_date}
                Task ID:        {task_id}
                Completed:      {task_completed}
                """)

        task_file.close()

# If "e" is selected then the loop will end.
    elif choice == "e":
        print("Thank you for using our product.")
        loop = 0
        