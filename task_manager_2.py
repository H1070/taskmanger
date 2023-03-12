#import libraies

import shutil
import datetime

#define functions for the menu options
# this used geeks for geks article on how to serarch for a string in text files
def reg_user():
    with open('user.txt','r+') as h:
        content = h.read()
        username = input("Please input your username")
        if username in content:
            print("This username already exists please choose another ")#if username is already in the txt file then an error meassage appears
        else:
            password_1=input("Enter new password for new user: ")
            confirm_pwd=input("Please confirm your password: ")
            if password_1==confirm_pwd:
                h.write(f"\n{username},{password_1}")
            else:
                print ("Your password entries don't match, please start the process again:  ")
#function for adding new task to the txt file, question are asked then written to the txt file
def add_task():
    with open('tasks.txt','a') as task:
           user_2=input("Enter user name of person task is assigned to: ")
           title=input("Enter title of task assigned: ")
           des=input("Enter description of task: ")
           due_date=input("Enter due date for task in the format DD/MM/YY: ")
           date = datetime.datetime.now()
           comp=input("Is task completed? Yes or No: ")
           task.write(f"\n{user_2},{title},{des},{date},{due_date},{comp}")

#function for viewing all tasks on the terminal screen from the txt tasks
def view_all():
    tasks=[]

    with open('tasks.txt','r+') as task:
        line = task.read()
        line=line.split('\n')
        
        for word in line:
            word=word.split(",")
            print  ("Person assigned too           " + word[0])
            print ("Task                           " + word[1])
            print ("Description of task            " + word[2])
            print("Current date                    " + word[3])
            print("Due date                        " + word[4])
            print("Task completed? Yes or No       " + word[5] + "\n")
                
#create a function to write to the file so we can call it later in the code.                
def write_file(file_name,list_tasks):
    file=open(file_name,'w')
    for line in list_tasks:
        file.write(','.join(line)+'\n')
    file.close()
      
#function for viewing all task assigned to user that is logged in

def view_mine():
    tasks=[]

    with open('tasks.txt','r+') as task:
        line = task.read()
        line=line.split('\n')
        
        line_list = []
        for x in line:
            x=x.split(",")
            
            line_list.append(x)
        while True:
        #the below code adds a number to each task and lets the person signed in edit their tasks. If they want to go back to the main menu then they select -1      
            for count, i in enumerate(line_list):
                if signed_in.lower()==i[0].lower() and i[5].lower() =="no":
                    print(count, i[1])

            number = int(input("Please enter the number of the task you would like to edit. If you would like to go back to the main menu please enter -1: "))#asks for task number they would like to edit
            word = line_list[number] #uses the input number to refrer the task required from the list of tasks
            if number == -1:
                break
                
            print("Person assigned too            " + word[0])
            print("Task                            " + word[1])
            print("Description of task             " + word[2])
            print("Current date                     " + word[3])
            print("Due date                         " + word[4])
            print("Task completed? Yes or No        " + word[5] + "\n")

            while True:
                edit=input("Would you like to edit this task or mark it as complete? Please type in no or yes:  ")
        
                if edit.lower()=="yes" and 'no' in word[5].lower(): #if the answer to the above input is yes and the task is not complete they can edit it
                    option=input("Select the option you would like to change user/date/complete/exit ")
                    while option != "exit":
                        if option == "user":
                            user=input("Enter the new user for this task")
                            line_list[number][0] = user
                            option=input("Select the option you would like to change user/date/complete/exit ")
                        elif option=='date':
                            due_date=input("Enter new due date for task in the format DD/MM/YY ")
                            line_list[number][4]=due_date
                            option=input("Select the option you would like to change user/date/complete/exit ")
                        elif option=='complete':
                            line_list[number][5]="yes"
                            break

                        else:
                            option=input("Please only select the option you would like to change user/date/complete/exit ")

                    #ask for inputs and assign thme to the correct location in the list and overwrite what is already in the txt file
                    write_file('tasks.txt',line_list)
                    break
                else:
                    print ("This task has alerady been completed") 
                    break

def generate_report():
    #if the signed in equals admin then total tasks can be displayed and the files are opened and read
    #split lines by new line \n
         if signed_in=="admin":
            task_over=open('task_overview.txt','w')
            user_over=open('user_overview.txt','w')
            f=open('user.txt','r')
            h=open('tasks.txt.','r')
            contents = f.read()
            info=h.read()

            line=contents.split("\n")
            sentence=info.split("\n")
   
            count=0
            num=0
            completed=0
            uncompleted=0
            over_due=0
            per_incomplete=0
            per_overdue=0

#use for loop to add up number of users from the user txt file and add one to the count
#do the same for number of task but change varaible names

            for i in line:
                count+=1

            for x in sentence:
                num+=1
                x=x.split(",")
                if x[5]=="yes": #if the task has been completed add count to the above if not then add to the uncompleted
                    completed+=1
                else:
                    uncompleted+=1
                    #get the current date from datetime and then get the expected date for the task by locating it in the list
                    #compare using a if statement and add one to the count if true
                    CurrentDate = datetime.datetime.now()
                    expected_date=datetime.datetime.strptime(x[4], "%d/%m/%y")
                    
                    if CurrentDate > expected_date:
                            over_due+=1

            #get the percentages by diving the value by the total value and multiplying by 100

            percentage_incomplete=round((uncompleted/num)*100)
            percentage_overdue=round((over_due/num)*100)
         
#write results to text for task overview

            task_over.write(f"Total number of users: {count}\n")
            task_over.write(f"Total number of tasks: {num}\n")
            task_over.write(f"Total number of completed tasks:{completed}\n")
            task_over.write (f"Total number of uncompleted tasks: {uncompleted}\n")
            task_over.write (f"Total tasks overdue:{over_due}\n")
            task_over.write (f"Percentage of tasks that are incomplete is {percentage_incomplete} %\n")
            task_over.write(f"Percentage of tasks that are overdue is {percentage_overdue} %\n")


            #use for loop to go through and check how many times the user from the user txt files matches the name at the start of the list in the task txt
            for p in line:
                p=p.split(',')
                num_tasks=0
                usercompleted=0
                undone=0
                over_due_date=0
                for x in sentence:
                    x=x.split(",")

                    if p[0]==x[0]:
                        num_tasks += 1
                        if x[5]=='yes':
                            usercompleted +=1
                        else:
                            undone+=1
                            CurrentDate = datetime.datetime.now()
                            expected_date=datetime.datetime.strptime(x[4], "%d/%m/%y")

                            if CurrentDate > expected_date:
                                    over_due_date+=1
                    else:
                        pass



                if num_tasks==0 or num ==0:
                    per_user=0
                else:
                    per_user=round((num_tasks/num)*100)

                if num_tasks==0 or usercompleted ==0:
                    per_done=0
                else:     
                    per_done=round((usercompleted/num_tasks)*100)

                if num_tasks == 0 or undone ==0:
                    per_notdone=0
                else:                   
                    per_notdone=round((undone/num_tasks)*100)

                if num_tasks == 0 or over_due_date ==0:
                    per_overdue_incomplete=0
                else:                   
                    per_overdue_incomplete=round(((over_due_date)/num_tasks)*100)

#write results to text file for user overview
                user_over.write (f" Number of tasks for {p[0]} is {num_tasks}\n")
                user_over.write(f"Percentage of tasks assgined to {p[0]} is {per_user}%\n")
                user_over.write (f"Percentage of tasks {per_done}% that have been completed assigned to {p[0]}\n")
                user_over.write (f"Percentage of task {per_notdone}% that need to be completed by {p[0]}\n")
                user_over.write (f"Percentage of tasks {per_overdue_incomplete}% that are overdue and incomplete for {p[0]}\n\n")
            user_over.write(f"Total number of users: {count}\n")
            user_over.write(f"Total number of tasks: {num}\n")
                 
            f.close()
            h.close()
            task_over.close()
            user_over.close()
       
         else:
            print("Only admin has access")


#====Login Section====

#create empty list to put the entries from the txt file into
#empty string singed in is created to store the user input
#read the txt using a for loop and split by comma and by new line
#add the data into a list

data=[]

signed_in=""

with open('user.txt','r+') as h:
    for line in h.readlines():
        username, passID=line.split(",")
        line=h.read()
        line=line.split('\n')
        data.append((username.strip(),passID.strip()))

#ask the user for login details
#if their details are not in the data list then display error message this is completed with an if/else statement         

while True:
    user=input("Enter your username: ")
    password=input("Enter your password: ")
    if (user,password) in data:
        print ("Welcome")
        signed_in = user
        break
    
    else:
        print ("Incorrect username or password, try again ")
   
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if signed_in=="admin":

        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate reports
    ds - display statistics
    e - Exit
    : ''').lower()

        if menu == 'r':
            
            if signed_in=="admin":
                reg_user()
            else:
                print("You don't have access to add a new user ")
    
        elif menu == 'a':
            
            add_task()

    #open file and read lines. Split by new line with \n
    # print data from list using index wanted
        
        elif menu == 'va':
            
            view_all()
        
    #open file and read lines. Split by new line \n
            
        elif menu == 'vm':
            
            view_mine()

        elif menu == 'gr':
            generate_report()


        elif menu=='ds':
            #open files for the user to see displayed on the termial
            if signed_in=="admin":
                generate_report()
                statis_user=open("user_overview.txt",'r')
                statis_tasks=open("task_overview.txt",'r')
                f=statis_user.read()
                h=statis_tasks.read()
                inside=f.split('\n')
                lines=h.split('\n')

                print (f)
                print (h)    

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

    else:
        menu = input('''Select one of the following Options below:
    va - View all tasks
    a - Adding a task
    vm - view my task
    e - Exit
    : ''').lower()

        if menu == 'a':
            
            add_task()

    #open file and read lines. Split by new line with \n
    # print data from list using index wanted
        
        elif menu == 'va':
            
            view_all()
        
    #open file and read lines. Split by new line \n
            
        elif menu == 'vm':
            
            view_mine()

        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
