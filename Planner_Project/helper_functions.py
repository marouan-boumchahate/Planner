""" ALL NEEDING FUNCTIONS THAT HELP US TO MANAGE THE USER WANTS AND PROJECT INTERACTING """

import datetime

def read_choice(msg, spaces_size, start = 1, end = 1):
    """
        describtion:
        -----------
        This method will read a number between two bounds with checking the whole excpected errors for you

        par:
        ---
        msg          --> str (represent the message that should be print  on the screen to type)
        spaces_size  --> int (represent after how many spaces the msg will be printed)
        start        --> int (represent the least bound the user must not exceed - default 1)
        end          --> int (represent the highest bound the user must not exceed - default 1)

        var:
        ---
        num   --> int (represent the number that will be return after testing it)

        return:
        ------
        int
    """
    while True:
        try:
            num = int(input(msg))
        except:
            print(" "*spaces_size + "ERROR!! Number is expected")
            print(" "*spaces_size + "Try Again\n")
            continue
        else:
            if not (1 <= num <= end):
                print(" "*spaces_size + f"ERROR!! Number between {start} and {end} is expected")
                print(" "*spaces_size + "Try Again\n")
                continue

        return num
    
def isyes(msg):
    """
        describtion:
        -----------
        This Method will ask the user for yes or no in short case (Y/N)
        True --> if the user print Y - y
        False --> if the user print N - n
        NOT UNDERSTANDABLE --> if the user print something else

        par:
        ---
        msg  --> str (represent a message the user will be asked to enter yes or no)

        var:
        ---
        answer  --> str (represent the answer (Y - y / N - n))

        return:
        ------
        bool
    """
    print()
    
    while True:
        answer = input("\n" + msg)

        if answer in ['y', 'Y']:
            return True
        
        if answer in ['N', 'n']:
            return False
        
        print("Error!! input NOT acceptable\nTry Again")
    
def Draw_Line(character, space_size, char_frequency):
    """
        describtion:
        -----------
        Draw a line of characters with specific length

        par:
        ---
        character      --> str (represent a letter that will be printed)
        char_frequency --> int (represent how many time that letter will be repeated)
        space_size     --> int (represent how many spaces far from the main position that letter will start printing)

        var:
        ---
        None

        return:
        ------
        None
    """
    print(" "*space_size, end = '')

    for i in range(char_frequency):
        print(character, end = '')

    print()

def Draw_Header_Screen(msg, spaces = 25):
    """
        describtion:
        -----------
        Printing a message in a frame of *

        par:
        ---
        msg    --> str (represent the title)
        spaces --> int (How many spaces far from the main position the program will start print and draw the title - default 25)

        var:
        ---
        None

        return:
        ------
        None
    """
    Draw_Line('*', spaces, len(msg) + 12)
    print(" "*spaces + "*" + msg.center(len(msg) + 10) + '*')
    Draw_Line('*', spaces, len(msg) + 12)

    print()

def readtime(word):
    """
        describtion:
        -----------
        read a time and check if it has no error

        par:
        ---
        word  --> str (represent a specific word of which time starting or ending)

        var:
        ---
        time  --> str (represent the time string in form hh:mn:sc)

        return:
        ------
        str
    """
    time = ""
    while True:
        time = input(" "*40 + f"{word} Task Time (hh:mn): ")
        time_list = time.strip().split(':')

        try:
            datetime.time(int(time_list[0]), int(time_list[1]), 0)
        except:
            print(" "*40 + "Follow The Form (hours:minutes)")
            print(" "*40 + "Try Again\n")
        else:
            break

    return time

def readdate(return_object = False, word = ""):
    """
        describtion:
        -----------
        read a date and check if it has no error

        par:
        ---
        word  --> str (represent a specific word of which time starting, ending - default of empty string)
        return_object   --> bool (represent in which for the method will return its data as a date object or string - default False)

        var:
        ---
        date         --> str (represent the date string in form yy:mm:dd)
        date_list    --> list (represent yy, mm and dd as a seperate info)
        date_object  --> date object (represent the date as an object)

        return:
        ------
        str or a date object
    """
    date = ""
    while True:
        date = input(" "*40 + f"{word}Task Date (yy-mm-dd): ")
        date_list = date.strip().split('-')

        try:
            date_object = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        except:
            print(" "*40 + "Follow The Form (year-month-day)")
            print(" "*40 + "Try Again\n")
        else:
            break
    
    if return_object:
        return date_object
    
    return date

def checkendtime(start_time, end_time):
    """
        describtion:
        -----------
        Check if the starting time is before ending time

        par:
        ---
        start_time  --> str (represent starting time)
        end_time    --> str (represent ending time)

        var:
        ---
        start   --> time object (represent starting time)
        end   --> time object (represent finishing time)

        return:
        ------
        bool
    """
    end = datetime.time(int(end_time.split(":")[0]), int(end_time.split(":")[1]), 0)
    start = datetime.time(int(start_time.split(":")[0]), int(start_time.split(":")[1]), 0)

    return start < end
