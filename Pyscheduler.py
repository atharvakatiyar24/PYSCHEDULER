import calendar

task_planner = {}  

def show_calendar():
    usery = int(input(f"Enter a year [eg,2026]: "))
    userm = int(input("Enter a month [eg,1-12]: "))
    print("=============================")

    print("\n" ,calendar.month(usery, userm))

def manage_tasks():
    usery = int(input(f"Enter a year [eg,2026]: "))
    userm = int(input("Enter a month [eg,1-12]: "))
    userd = int(input("Enter a date [eg,1-31]: "))
    
    userd=f"{usery}-{userm}-{userd}"

    if userd in task_planner:
        print(f" Existing Task found!: {task_planner[userd]}")

    else:
        print(" No task scheduled for this date.")
        usertask=input("Enter your task: ").lower().strip()
        task_planner[userd]=usertask
        print(" Task saved successfully!")

def viewtasks():
    if not task_planner:
        print(" Your planner is empty right now.")
    else:
        print(" Your Saved Plans:")
        for date, task in task_planner.items():
            print(f" {date}: {task}")
        

def main():
    while True:
        print("=============================")
        print("    WELCOME TO PYSCHEDULER  ")
        print("=============================")
        print("[1] View Calendar")
        print("[2] Add / Check Tasks")
        print("[3] View All Tasks")
        print("[4] Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_calendar()
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            viewtasks()
        elif choice == '4':
            print("Exiting the planner. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.") 
        
main()
