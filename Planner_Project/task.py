""" TASK OBJECT WHERE WE CAN HAVE THE INFORMATION OF EACH TASK FROM DATE, STARTING AND FINISHING TIME TO THE TASK JOB """

import datetime

class clsTask:
    def __init__(self, describtion, date, start_time, end_time):
        """
            Description:
            -----------
            Create a task object which contain the task, date, starting time and finishing time

            var:
            ---
            describtion --> str
            date        --> date object
            start_time        --> time object
            end_time        --> time object

            return:
            ------
            None
        """
        self.set_description(describtion)
        self.set_date(date)
        self.set_start_time(start_time)
        self.set_end_time(end_time)

    # Setters
    def set_description(self, describtion):
        """Create an attribute named describtion and assign to it describtion argument"""
        self.describtion = describtion

    def set_date(self, date):
        """set a date attribute by converting the parameter from a string to a date object"""
        date_list = date.split("-") # split string to sub string which are represent year, month, day
        self.date = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2])) # Create a date object
        del date_list

    def set_start_time(self, start_time):
        """set a start_time attribute by converting the parameter from a string to a time object"""
        start_time_list = start_time.split(":") # split string to sub string which are represent hour, minute, second
        self.start_time = datetime.time(int(start_time_list[0]), int(start_time_list[1]), 0) # Create a time object
        del start_time_list

    def set_end_time(self, end_time):
        """set an end_time attribute by converting the parameter from a string to a time object"""
        end_time_list = end_time.split(":") # split string to sub string which are represent hour, minute, second
        self.end_time = datetime.time(int(end_time_list[0]), int(end_time_list[1]), 0) # Create a time object
        del end_time_list  

    # Getters
    def get_description(self):
        """return the string attribute 'describtion'"""
        return self.describtion
    
    def get_date(self):
        """return the date object attribute 'date'"""
        return self.date
    
    def get_start_time(self):
        """return the time object attribute 'start_time'"""
        return self.start_time
    
    def get_end_time(self):
        """return the time object attribute 'end_time'"""
        return self.end_time
    
    def __str__(self):
        """
            describtion:
            -----------
            returning a string  from the object which contains date, task, starting time and finishing time

            par:
            ---
            None

            var:
            ---
            sentence  --> str

            return:
            ------
            str
        """
        sentence = f"{self.describtion}  --> from {str(self.start_time)[:-3]} to {str(self.end_time)[:-3]}"
        return f"{str(self.date)}\n{sentence}"

    def general_time(self):
        """
            describtion:
            -----------
            this function return the date and time for both starting and finishin as a unique object
            which will help us to compare easily

            var:
            ---
            start_general_time  --> datetime object
            end_general_time    --> datetime object

            return:
            ------
            2 datetime objects
        """
        start_general_time = datetime.datetime(self.date.year, self.date.month, self.date.day, self.start_time.hour, self.start_time.minute, self.start_time.second)
        end_general_time = datetime.datetime(self.date.year, self.date.month, self.date.day, self.end_time.hour, self.end_time.minute, self.end_time.second)
 
        return start_general_time, end_general_time

    def __eq__(self, other):
        """
            describtion:
            -----------
            Compare if the date of two objects are equal we are using this to check for the intersection time and dates

            var:
            ---
            None

            return:
            ------
            bool
        """
        return self.date == other.date # check if two dates are equal to be sure if we are gonna check the intersection for time or not

    def __gt__(self, other):
        """
            describtion:
            -----------
            After checking if the dates are equal then we should check if times are intersected

            var:
            ---
            None

            return:
            ------
            bool
        """
        return (self.start_time > other.end_time) or (other.start_time > self.end_time) 
        # Check if the time between two objects are not intersected
        # first task should be finish before starting the second task  
       
    def __lt__(self, other):
        """
            describtion:
            -----------
            Check if an object is less then the other

            var:
            ---
            self_start  --> datetime object
            self_end  --> datetime object
            other_start  --> datetime object
            self_end  --> datetime object

            return:
            ------
            bool
        """
        self_start, self_end = self.general_time()
        other_start, other_end = other.general_time()

        return (self_end < other_start) # Check if the time of this object is smaller than the other object time