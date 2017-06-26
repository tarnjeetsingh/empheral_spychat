#Importing steganography from libarary
from steganography.steganography import Steganography

# Importing spy details from other file
from spydetails import spy,Spy

# Importing datetime
from datetime import datetime

# Create a class for the chat messages
class ChatMessage:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time  = datetime.now()
        self.sent_by_me = sent_by_me

#making some friends of our spy
friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)

friends = [friend_one, friend_two, friend_three]



# starting application and printing a hello message
print'Hello'
print'Let\'s get started'
# ask user to continue as existing spy or to create a new profile
question = raw_input("Continue as " + spy.salutation + " " + spy.name + "(Y/N)?")
# if user says yes then continue with existing profile
if question.upper() == 'Y':
    print 'Welcome %s %s with age %d and rating %.1f' % (spy.salutation, spy.name, spy.age, spy.rating)
# if user says no the ask user to enter a new profile
elif question.upper() == 'N':
    # ask user for name of name of spy
    spy_name = raw_input("what is your name?")
    # validation on name
    # strip function used for trimming the spaces
    if len(spy_name.strip()) == 0:
        print('Sorry you must have a name')
    else:
        # ask spy for the salutation and include that salutation in the name of the spy
        spy_salu = raw_input('what should I call you?(Mr. or Miss):')
        spy_name = spy_salu + ' ' + spy_name
        print'welcome ' + ' ' + spy_name + ' glad to have you back with us.'
        # new variables for age,rating and status of the spy
        spy_age = 0
        spy_rating = 0.0
        spy_status = False
        spy_age = int(raw_input('enter your age'))
        # input age by spy
        # validation so that the age of spy is in between the 12 and 50 years
        if 12 < spy_age < 50:
            spy_rating = float(raw_input('enter your rating'))
        else:
            print('sorry u cant be a spy')
            # enter rating of spy
            # different messages are printed according to the rating of the spy
        if spy_rating > 4.5:
            print ('you are an ace')
        elif 4.5 >= spy_rating >= 3.5:
            print ('you are one of good one')
        elif 3.5 >= spy_rating >= 2.5:
            print ('you can always do better')
        elif spy_rating <= 2.5 and spy_rating > 0:
            print('We always need someone help in office')
        # update status of spy
        spy_status = True
        # message after complete of authentication
        print 'authentication complete %s with age %d and rating %.1f' % (spy_name, spy_age, spy_rating)
else:
    print 'Please enter a valid choice'



# creating a function to start our applicaiton to start our chat application
def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    status_message = None
    # loop to show the choice menu again and again
    while show_menu:
        menu_choices = "What do you want to do? \n1. Add a status update \n2. Add a friend \n3. Send message \n4. Read message \n5. Read chat history \n6. Close application "
        menu_choice = raw_input(menu_choices)
        menu_choice = int(menu_choice)
        # piece of code to update status using add_status function
        if menu_choice == 1:
            print 'You chose to update the status'
            spy.current_status_message = add_status(spy.current_status_message)
        # piece of code to add a friend by the use of add_friend function
        elif menu_choice == 2:
            add_friend()
        # Option to send a message
        elif menu_choice == 3:
            send_message()
        # Option to read a message from a friend
        elif menu_choice == 4:
            read_message()
        # Option to read chat history of a friend
        elif menu_choice == 5:
            read_chat_history()
        # piece of code to close the menu
        elif menu_choice == 6:
            show_menu = False
        # piece of code to be executed if niether of the above conditions are met
        elif menu_choice > 6 or menu_choice < 1:
            print 'Please enter a valid choice from the options listed above'


# list to store old status messages
STATUS_MESSAGES = ['I am james bond', 'Welcome to the world of a spy']


# Function to update the status of spy
def add_status(current_status_message):
    updated_status_message = None
    # Display current status message
    if current_status_message != None:
        print 'your status message is ' + current_status_message
    else:
        print 'Sorry! you don\'t have any status message'
    # ask  user whether to update from older status or update a new one
    ques1 = raw_input('Do you want to update older status(Y/N)?')
    # piece of code if user want to add a new status including validations
    if ques1.upper() == 'N':
        new_status = raw_input('Please enter the new status')
        if len(new_status.strip()) == 0:
            print 'Please enter a valid choice'
        else:
            updated_status_message = new_status
            STATUS_MESSAGES.append(updated_status_message)
    # piece of code if user want to update from older status including validations
    elif ques1.upper() == 'Y':
        for i in STATUS_MESSAGES:
            print str(STATUS_MESSAGES.index(i) + 1) + ".  " + i
        select_status = int(raw_input('choose the status no. from above status '))
        if len(STATUS_MESSAGES) >= select_status != 0 and select_status > 0:
            status_message = STATUS_MESSAGES[select_status - 1]
            updated_status_message = STATUS_MESSAGES[select_status - 1]
            print'your updated message is' + status_message
        else:
            print 'enter a valid choice'
    # print message if user enters a invalid choice
    else:
        print'Please enter a valid choice for status update'
    return updated_status_message

# function to add a friend
def add_friend():
    # input name,age,rating of the spy by the user
    name = raw_input('What is your friend\'s name?')
    salutation = raw_input('Are they Mr. or Miss')
    name = salutation + name
    age = raw_input('What is your friend\'s age?')
    rating = raw_input('What is your friend\'s rating?')
    # convert age into int and rating to float
    age = int(age)
    rating = float(rating)
    # validation to check that name has a value
    # validation to check age of spy is between 12 and 50
    # validation to check that the spy's friend rating is greater than or equal to that of spy
    # IF THE VALIDATIONS ARE TRUE THAN THE DATA OF FRIEND IS ADDED TO THE LISTS
    if len(name.strip()) != 0 and 12 < age < 50 and rating >= spy.rating:
        new_friend = Spy(name,age,salutation,rating)
        friends.append(new_friend)
        print 'Friend added'
    else:
        # ELSE IF VALIDATIONS ARE NOT SATISFIED THEN A SORRY MESSAGE IS PRINTED
        print 'Sorry! We can\'t enter the spy with the details you provided.' \
              'There may be on eof the following errors' \
              '1. Name is not valid' \
              '2. Age is not in integer format' \
              '3. Rating is not in number format'
    print 'you have' + str(len(friends)) + 'friends in total'
    return len(friends)


# function to select a friend to chat with
def select_a_friend():
    for friend in friends:
        print str(friends.index(friend) + 1) + ' %s is online' % (friend.name)
    try:
        friend_choice = int(raw_input('select the friend you want to chat with'))
        if len(friends) >= friend_choice and friend_choice!= 0 and friend_choice > 0:
            friend_choice_position = int(friend_choice)-1
            print 'You Choose To Chat With '+ friends[friend_choice_position].name
            return friend_choice_position
        else:
            print'Please enter a valid choice'
    except ValueError:
        print 'Please enter a choice in integer'

# Function to send a secret message
def send_message():
        friend_chat = None
        # Call select a friend fuction to select a friend with whom the spy wants to chat
        friend_chat = select_a_friend()
        while friend_chat == None:
            friend_chat = select_a_friend()
        original_image= raw_input('what is the name of your image?')
        output_path= 'output.jpg'
        text= raw_input('Enter the text you want to encode?')
        try:
            Steganography.encode(original_image,output_path,text)
            message =  text
            sent_by_me = True
            new_chat = ChatMessage(message,sent_by_me)
            friends[friend_chat].chats.append(new_chat)
            print'your secret message is ready'
        except IOError:
            print 'Sorry no file of such name can be found'

# Function to receive a secret message
def read_message():
    sender = None
    sender = select_a_friend()
    while sender == None:
        sender = select_a_friend()
    try:
        output_name= raw_input('what is the  name of the file you want to read?')
        ouput_text= Steganography.decode(output_name)
        message = ouput_text
        sent_by_me = False
        new_chat = ChatMessage(message,sent_by_me)
        friends[sender].chats.append(new_chat)
        print 'your secret message has been saved'
        print friends[sender].chats[-1].message
        if friends[sender].chats[-1].message.upper() == 'SOS':
            print 'Hurry the spy %s is in an emergency' % (friends[sender].name)
        elif friends[sender].chats[-1].message.upper() == 'SAVE ME':
            print 'Time to get in action \nThe life of %s is in danger' % (friends[sender].name)
    except IOError:
        print 'Sorry the fie you named cannot be found'

# Function to read the chat history
def read_chat_history():
    read_for = None
    # Calling select a friend function to select a friend whose chat history has to be read
    read_for = select_a_friend()
    while read_for == None:
        read_for = select_a_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said %s' % (chat.time.strftime('%d %B %Y'), friends[read_for].name, chat.message)
            # Adding special conditons if spy sends special messages such as SOS, Save Me
            if chat.message == 'SOS':
                print 'Hurry the spy %s is in an emergency' % (friends[read_for].name)
            elif chat.message.upper() == 'SAVE ME':
                print 'Time to get in action \nThe life of %s is in danger' % (friends[read_for].name)

# calling the function to start the chat application
start_chat(spy.name, spy.age, spy.rating)
