""" PERFORM ALL THE NEEDING OPERATIONS FROM DISPLAYING TASKS, ADDING TASKS AND DELETING TASKS """

import pickle
from datetime import date, timedelta
from task import clsTask

class Task_Manager:
    def __init__(self):
        """
            describtion:
            -----------
            initialize an empty list then try to load the whole Task objects and append them to the list

            var:
            ---
            self.tasks  --> list of Task objects

            return:
            ------
            None
        """
        self.tasks = []
        self.load_tasks()

    def add_task(self, describtion, date, start_time, end_time):
        """
            describtion:
            -----------
            adding a new task to the file, if there is no intersection between dates

            par:
            ---
            decribtion --> str
            date       --> date object
            start_time --> time object
            end_time   --> time object

            var:
            ---
            task  --> Task Object
            tasks --> List of Task Objects

            return:
            ------
            bool
        """
        task = clsTask(describtion, date, start_time, end_time) # Create an object from Task

        for tsk in self.tasks:
            if (tsk == task) and not(tsk > task): # Checking if there is any intersection between two days
                del task
                return False
        
        self.tasks.append(task)
        self.store_tasks()
        return True
        
    def delete_task(self, position):
        """
            describtion:
            -----------
            deleting a task from the file

            par:
            ---
            position  --> int (represent the index that we should remove from the list)

            var:
            ---
            tasks  --> list of Task objects

            return:
            ------
            None
        """
        self.tasks.pop(position) # Delete the index has been sent

        self.store_tasks() # write the new data to the file

    def print_daily_tasks(self):
        """
            describtion:
            -----------
            Print tasks that are available for this day

            var:
            ---
            added_counter  --> int
            tasks          --> List Of Task Objects

            return:
            ------
            None
        """
        added_counter = 0 # This will count how many task we print only to be sure is there any task printed or not

        for task in self.tasks:
            if task.date == date.today(): # Print only tasks that have the same date as today
                print(" "*35 + str(task).split('\n')[1])
                added_counter += 1

        if added_counter == 0: # When no task has printed we will tell the user you have no tasks on this day
            print(" "*42 + "NO TASKS ON THIS DAY")

    def print_bounded_tasks(self, fbound_date = date.today(), lbound_date = date.today() + timedelta(days=7), word = "WEEK"):
        """
            describtion:
            -----------
            Print the whole tasks which are available for this week

            par:
            ---
            fbound_date   --> date object (represent the starting date and has defaul of today's date)
            lbound_date   --> date object (represent the ending date and has defaul of a week from today)
            word          --> str (represents the word that will be printed if there is no tasks default of 'WEEK')

            var:
            ---
            current_date  --> date object
            checking_date --> date object
            week_tasks    --> List of Task Objects
            
            return:
            ------
            None
        """
        # Where the sub-list of tasks will be stored
        week_tasks = []

        # Create a sub-list of tasks between two dates
        for task in self.tasks:
            if fbound_date <= task.date < lbound_date:
                week_tasks.append(task)

        # Checking if there is no tasks
        if week_tasks == []:
            print(' '*37 + f"NO TASKS ARE AVAILABLE ON THIS {word}")
            return
        
        # Sort the sub-list of tasks then print them
        for task in sorted(week_tasks):
            sentences = str(task).split('\n')
            print(' '*35 + sentences[0].center(len(sentences[1])))
            print(' '*35 + sentences[1] + "\n")

    def print_tasks(self):
        """
            describtion:
            -----------
            Print The whole Tasks and assign them to a specific number in an order way
            
            var:
            ---
            tasks  --> List Of Task Objects

            return:
            ------
            None
        """
        if self.tasks == []: # if tasks list is empty print no tasks
            print(' '*45 + "NO TASKS ARE AVAILABLE\n")
            return
        
        counter = 1

        for task in self.tasks:
            print(" "*30 + f'[{counter}]: ' + str(task).replace('\n', ' | ')) # print the object string with changing the \n by |
            counter += 1

        print()

    def load_tasks(self):
        """
            describtion:
            -----------
            Read data (Task Object) from the binary file 'tasks.bin', if the EOFError raised assign
            an empty list to our data list otherwise assign objects that got from the file

            var:
            ---
            tasks  --> List Of Task Objects
            file   --> File Object

            return:
            ------
            None
        """
        file = open("tasks.bin", 'rb') # open file

        try:
            lst = pickle.load(file) # read file list if there is an error (EOF). in other words, the file is empty
        except:
            self.tasks = [] # Assign the tasks to an empty list
        else:
            self.tasks = lst # Otherwise assign it to the list you have read from the file

    def store_tasks(self):
        """
            describtion:
            -----------
            Write the List of Task objects into the binary file

            var:
            ---
            file  --> File Object

            return:
            ------
            None
        """
        file = open("tasks.bin", 'wb') # Open the file

        pickle.dump(self.tasks, file) # Write into the file