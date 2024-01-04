""" MANAGING THE PROJECT WITH LETTING THE USER INTERACT WITH IT AS HE WANTS """

import os
import helper_functions as hf
from sys import exit
from tasks_manager import Task_Manager
from Error_Exceptions import TimeException

class Project_Manager:
    # Here The program will be start by defining an object from the task manager
    # and lauch the main menu screen
    def __init__(self):
        """
            describtion:
            -----------
            The project interface where the user can interact with the program easily

            par:
            ---
            None

            var:
            ---
            TSKS  --> Task_Manager object

            return:
            ------
            None
        """
        self.TASKS = Task_Manager()
        self.main_menu_manager()

    # Main menu manager has two tasks
    # first display Main Menu
    # Second get interact from the user
    def main_menu_manager(self):
        """
            describtion:
            -----------
            Managing the main menu after display the available menu and get interact from the user

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        self.main_menu()
        self.perform_main_menu()

    # type menu manager has two tasks
    # first display type Menu form
    # Second get interact from the user
    def display_type_menu_manager(self):
        """
            describtion:
            -----------
            Managing the sub-menu for the display or list the tasks (daily, weekly or let the user decide)

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        self.display_type_menu()
        self.perform_display_type_menu()

    # Printing a design of how the menu should be look like and display
    # The available choices
    def main_menu(self):
        """
            describtion:
            -----------
            Display the whole available choices that you can do with the program

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        os.system("cls")
        hf.Draw_Header_Screen("Main Menu", 30)

        print(" "*31 + "[1]  Display Tasks")
        print(" "*31 + "[2]  Add a Task")
        print(" "*31 + "[3]  Delete a Task")
        print(" "*31 + "[4]  Exit")

    # Read a choice from the user of the main menu
    # Then apply what it is pointing to
    def perform_main_menu(self):
        """
            describtion:
            -----------
            Let the user take his responsibily of chosing what will do

            par:
            ---
            None

            var:
            ---
            choice  --> int (represent the choice of what he/she is gonna do - Adding, deleting, listing or exit)

            return:
            ------
            None
        """
        choice = hf.read_choice("\n" + " "*20 + "Please enter a number choice from above (1-4): ", 20, end = 4)

        match(choice):
            case 1:
                self.display_type_menu_manager()
            
            case 2:
                while True:
                    os.system("cls") # Clear The screen
                    hf.Draw_Header_Screen("Add Tasks Screen", 40) # Draw the TITLE

                    if self.addTask():
                        break
                    
                input("\npress enter to return...") # Thi will give the user sometime to rest and knows what is happening
                self.main_menu_manager() # return to the main menu again
            
            case 3:
                os.system("cls")
                hf.Draw_Header_Screen("Delete Tasks Screen", 40)

                self.deleteTask()

                input("\npress enter to return...")
                self.main_menu_manager()
            
            case 4:
                exit(1)

    # Printing a design of how the type menu should be look like and display
    # The available choices
    def display_type_menu(self):
        """
            describtion:
            -----------
            Display the whole available choices that you can do with display tasks part

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        os.system("cls")
        hf.Draw_Header_Screen("Printing Types", 30)

        print(" "*30 + "[1]  All Tasks")
        print(" "*30 + "[2]  Daily")
        print(" "*30 + "[3]  Weekly")
        print(" "*30 + "[4]  List Tasks with your interval")
        print(" "*30 + "[5]  Main Menu")

    # Read a choice from the user of the display type menu
    # Then apply what it is pointing to
    def perform_display_type_menu(self):
        """
            describtion:
            -----------
            Let the user take his responsibily of chosing what will do in the listing part

            par:
            ---
            None

            var:
            ---
            choice  --> int (represent the choice of what he/she is gonna do - daily tasks, weekly tasks, intervaling or return to the main menu)

            return:
            ------
            None
        """
        choice = hf.read_choice("\n" + " "*22 + "Please enter a number choice from above (1-4): ", 22, end = 5)

        match(choice):
            case 1:
                self.printTasks()

                input("\npress enter to return...")
                self.display_type_menu_manager()

            case 2:
                self.printTodayTasks()

                input("\npress enter to return...")
                self.display_type_menu_manager()

            case 3:
                self.printWeekTasks()

                input("\npress enter to return...")
                self.display_type_menu_manager()

            case 4:
                self.printIntervalTasks()

                input("\npress enter to return...")
                self.display_type_menu_manager()

            case 5:
                self.main_menu_manager()

    # Reading the needing attributes
    def read_info(self):
        """
            describtion:
            -----------
            Read the whole attribute that are needed to create an object with checking the errors

            par:
            ---
            None

            var:
            ---
            describtion  --> str (represent the task instruction)
            date         --> str (represent the date in the form yy-mm-dd)
            start_time         --> str (represent the starting time in the form hh-mn-sc)
            end_time         --> str (represent the finishing time in the form hh-mn-sc)

            return:
            ------
            List
        """
        describtion = input(" "*40 + "Task Description: ")
        date = hf.readdate()
        start_time = hf.readtime("Start")
        while True:
            end_time = hf.readtime("End")

            if hf.checkendtime(start_time, end_time):
                break
            else:
                print(" "*40 + "The finishing time must be after the starting time")
                print(" "*40 + "Try Again\n")

        return [describtion, date, start_time, end_time]

    # Add Task
    def addTask(self):
        """
            describtion:
            -----------
            Add a new task to the tasks

            par:
            ---
            None

            var:
            ---
            info --> list

            return:
            ------
            bool
        """
        info = self.read_info() # Read attributes
        try:
            if self.TASKS.add_task(info[0], info[1], info[2], info[3]):  # Add a Task object
                print("\n" + " " * 50 + "Successfully Added")
                return True
            else:
                # The time of the current task and one of already exist tasks are intersected
                raise TimeException("\n" + " " * 50 + "Time NOT AVAILABLE")
        except TimeException as e:
            print(e)
            if not hf.isyes(" " * 40 + "Do you wanna Try Again?? (Y/N): "):  # Asking if they want to try a new time
                return True
            else:
                return False

    # Delete a Task
    def deleteTask(self):
        """
            describtion:
            -----------
            Delete a task from tasks

            par:
            ---
            None

            var:
            ---
            number_of_tasks --> int

            return:
            ------
            None
        """
        print(" "*50 + "Tasks List")
        hf.Draw_Line('-', 50, 10)

        number_of_tasks = len(self.TASKS.tasks) # How many tasks are available for us

        self.TASKS.print_tasks()
        if number_of_tasks != 0: # Means there is tasks
            self.TASKS.delete_task(hf.read_choice(" "*30 + f"Enter the number of the task you wanna delete (1-{number_of_tasks}): ", 30, 1, number_of_tasks) - 1) # we substract it from 1 to represent the list index (starting from 0)
            print("\n" + " "*30 + "Successfuly Deleted!!")

    # Print all tasks
    def printTasks(self):
        """
            describtion:
            -----------
            Display the whole list of tasks to the screen

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        os.system("cls")
        hf.Draw_Header_Screen("All Tasks", 40)

        self.TASKS.print_tasks()

    # Print Today's tasks
    def printTodayTasks(self):
        """
            describtion:
            -----------
            Display all tasks that are available for today

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        os.system("cls")
        hf.Draw_Header_Screen("Today's Tasks", 40)

        self.TASKS.print_daily_tasks()

    # Print Week's tasks
    def printWeekTasks(self):
        """
            describtion:
            -----------
            Display the whole tasks that are available in this week

            par:
            ---
            None

            var:
            ---
            None

            return:
            ------
            None
        """
        os.system("cls")
        hf.Draw_Header_Screen("This Week's Tasks", 40)

        self.TASKS.print_bounded_tasks()

    # Print interval tasks
    def printIntervalTasks(self):
        """
            describtion:
            -----------
            Display the whole tasks that are available between the dates that the user will enter

            par:
            ---
            None

            var:
            ---
            date_1 --> date object
            date_2 --> date object

            return:
            ------
            None
        """
        while True:
            os.system("cls")
            hf.Draw_Header_Screen("List Tasks In interval", 40)

            date_1 = hf.readdate(return_object = True, word = "Starting ")
            date_2 = hf.readdate(return_object = True, word = "Last ")

            if date_1 < date_2:
                break

            input("\n" + " "*30 + "ERROR!! STARTING DATE MUST BE BEFORE THE ENDING DATE (Try Again)...")

        os.system("cls")
        hf.Draw_Header_Screen("List Tasks In interval", 40)
        self.TASKS.print_bounded_tasks(date_1, date_2, "INTERVAL")


Project = Project_Manager()