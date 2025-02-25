print("🤗 welcome onboard to my first todo app👍\n"
      "kindly choose from the option below: ")

tasks = []
while True:
    user_choice = int(input("1. Add todo\n"
    "2. view todo\n"
    "3. Edit todo\n"
    "4. Delete todo\n"
    "5. Exit\n"))

    if user_choice == 1:
        user_task = input("add task\n")
        tasks.append(user_task)
        print(f"{user_task} added sucessfully!!")
    elif user_choice == 2:
        if not tasks:
            print("No tasks added, add a task")
        for index, task in enumerate(tasks, 1):
            print("your tasks listed below!!!")
            print(f"{index}.{task}")
