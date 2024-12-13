import Timer

def main():

    tasks = []

    is_running = True
    while is_running:
        question = """1- Add task \n2- Mark the complete task \n3- View tasks \n4- Timer for Task \n5- Quite"""
        print(question)

        choice = int(input("Enter your choice (should be a number between 1 and 4) : "))
        while not(1<=choice<=4):
            choice = int(input("!!Enter your choice (should be a number between 1 and 4) : "))

        if choice == 1:
            Add_Task(tasks)
        elif choice == 2:
            Comp_Task(tasks)
        elif choice == 3:
            View_Task(tasks)
        elif choice == 4:
            Start_Task(tasks)
        else:
            print("="*30+"\nHave nice day")
            is_running = False


def Add_Task(tasks):
      choice = input("\nEnte your task please : ")
      task = [{"task" : choice},{"complete" : False}]
      tasks.append(task)
    

def Comp_Task(tasks):
    not_comp_tasks = []
    i = 0
    j = 1
    for task in tasks:
        if task[1]["complete"] == False:
            print(f"{j}- {task[0]["task"]}")
            not_comp_tasks.append(i)
            j+= 1
        i+= 1

    indice = 0
    choice = int(input("Enter your number : "))
    for ncp in range(len(not_comp_tasks)):
        if ncp+1 == choice:
            indice = not_comp_tasks[ncp]
    
    tasks[indice][1]["complete"] = True
    

def View_Task(tasks):

    for task in tasks:
        if task[1]["complete"] == True:
            print(f"{task[0]["task"]} {"✅"}\n")
        else:
            print(f"{task[0]["task"]} {"❌"}\n")

def Start_Task(tasks):
    Timer.timer()
    

main()
