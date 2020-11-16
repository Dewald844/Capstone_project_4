# Rewriting taskmanager capstone to add function for more efficient code 

import os
# i tried using datetime but am stil struggling to comapre date to see if date is overdue 
import datetime 

userLog = open('user.txt' , 'r+' , encoding= 'utf-8')
userTasksFile = open('tasks.txt' , 'r+' , encoding= 'utf-8')
tasksOverviewFile = open("task_overview.txt" , "r+" , encoding= "utf-8")
userOverviewFile = open("user_overview.txt" , "r+" , encoding= "utf-8")


#adding an function to use during the program to clear the sceeen 
def clearScreen():
    
    print('\n' * 20)

def AdminMenu() :

    print("Welcome Admin" + ('\n' * 2) +
          "Please pick your option as indexed below" + ('\n' *2) +
          ('_' * 80) + ('\n' ) +
          "r  : Register an new user" + ('\t' * 2) + '|' +
          "a  : Add an new task" + '\n' +
          "va : View all tasks " + ('\t' * 3) + '|' +
          "vm : View specific user tasks " + ('\n') +
          "gr : Generate reports " + ('\t' * 3) + '|'+
          "ds : Display statistics" + ('\n') +
          "e : Exit" +
          ("_" * 80))

def userMenu(): 
    
    print("Welcome Admin" + ('\n' * 2) +
          "Please pick your option by number as stated below" + 
          ('\n' *2) + ('_' * 80) + '\n' +
          "vm : View all my tasks" + '\n' + 
          "ct : Complete an task" + '\n' + 
          'ds : Display statistics' + '\n' + 
          'gr : Generate reports' + '\n'
          ("_" * 80))

def reg_user(x):
    
    newUserName = input("Please enter new user name --> :")
    newUserPassword = input("Please enter user password ---> :")
    userInfo = []
    count = 0
    for line in x :
        
        userInfo = line.split(' ')
        print(userInfo)
        if  userInfo[0] == newUserName :
            
            clearScreen()
            print("User name already exists. Please try an different user Name ")
            count += 1 
            reg_user(x)
            

                
    if count == 0 : 
        clearScreen()
        print("You have succesfully added an new user")
        x.write(newUserName + ' ' + newUserPassword + '\n')

def add_task(x):
    
    taskAssignee = input("Enter who this task wil be assigned to --> :")
    task_count = 1
    
    for line in x :

        task_count += 1
        
    taskName = input("Enter new task name --> :")
    taskDueDate = input("Enter task dead line --> :")
    taskDescriptionInput = input("Enter an brief description of task --> :")
    taskDescriptionOutput = taskDescriptionInput.replace(' ','_')
    taskAssignDate = input("Enter today's date --> :")
    
    x.write(str(task_count) + " " + 
            taskAssignee + " " +
            taskName + " " + 
            taskDescriptionOutput + " " +
            taskAssignDate + " " + 
            taskDueDate + " " + 
            "no" +
            " " + '\n')
        
def view_all(x):
    
    with open('tasks.txt' , 'r+' , encoding= 'utf-8') as x :
        
        for line in x  :
            
            task = line.split(" ")
            
            if task[6] == 'no' :
                
                task3Clean = task[3].replace('_' , " ")
                
                print(('_' * 80) +'\n'+
                        "Assignee " + ('\t'*3) +'|'+ str(task[1]) + '\n' +
                        "Task ID" + ('\t' *4) + '|' + str(task[0]) + '\n' +
                        "Task Title " + ('\t'*3)+'|' + str(task[2]) + '\n' + 
                        "Task Discription" + ('\t'*2)+'|' + str(task3Clean) + '\n' +
                        "Assigned Date " + ('\t'*3)+'|' + str(task[4]) + '\n' +
                        "Due Date " + ('\t'*3)+'|' + str(task[5]) + '\n' + 
                        "Completed " + ('\t'*3)+ '|' + str(task[6]) + '\n'+
                        ("_" * 80))
                 
def view_mine(x):
    
    userNameView = input("Please your user name --->>> :")
     
    with open('tasks.txt' , 'r+' , encoding= 'utf-8') as x :
        
        for line in x :
            
            task = line.split(" ")
            
            if task[1] == userNameView and task[6] == 'no' :
            
                    task3Clean = task[3].replace('_' , " ")
                    print(('_' * 80) +'\n'+
                        "Assignee " + ('\t'*3) +'|'+ str(task[1]) + '\n' +
                        "Task ID" + ('\t'*4) + '|' + str(task[0]) + '\n' +
                        "Task Title " + ('\t'*3)+'|' + str(task[2]) + '\n' + 
                        "Task Discription" + ('\t'*2)+'|' + str(task3Clean) + '\n' +
                        "Assigned Date " + ('\t'*3)+'|' + str(task[4]) + '\n' +
                        "Due Date " + ('\t'*3)+'|' + str(task[5]) + '\n' + 
                        "Completed " + ('\t'*3)+ '|' + str(task[6]) + '\n'+
                        ("_" * 80))  
            
            else :
                pass

def view_specific(x):

    IDnum = int(input('Please enter you task ID number --->>>:'))
    for line in x :

        task = line.split(' ')

        if int(task[0]) == IDnum :

            task3Clean = task[3].replace('_' , " ")
            print(('_' * 80) +'\n'+
                        "Assignee " + ('\t'*3) +'|'+ str(task[1]) + '\n' +
                        "Task ID" + ('\t'*4) + '|' + str(task[0]) + '\n' +
                        "Task Title " + ('\t'*3)+'|' + str(task[2]) + '\n' + 
                        "Task Discription" + ('\t'*2)+'|' + str(task3Clean) + '\n' +
                        "Assigned Date " + ('\t'*3)+'|' + str(task[4]) + '\n' +
                        "Due Date " + ('\t'*3)+'|' + str(task[5]) + '\n' + 
                        "Completed " + ('\t'*3)+ '|' + str(task[6]) + ' \n'+
                        ("_" * 80)) 
            
def complete_task(x):

    
    all_lines = ''
    IDnum = int(input("Please enter the task ID that you want to complete --->>> :"))

    for line in x :

        task = line.split(' ') 
        

        if int(task[0]) == IDnum :

            if "no" in line :

                task[6] = "Yes"
                
                all_lines += " ".join(task)
        else :

            all_lines += " ".join(task)
            
    x.seek(0)
    x.truncate()
    x.write(all_lines)
    x.flush()
    os.fsync(x)
    clearScreen()

    print('Task Completed')

def reassign(x):

    IDnum = int(input("Please enter the task ID that you want to change --->>> :"))
    newAssignee = input("Please enter who this task wil be assigned to --->>> :")
    all_lines = ''

    for line in x :

        task = line.split(' ')

        if int(task[0]) == IDnum and task[6] == 'no' :

            task[1] = newAssignee

            all_lines += " ".join(task)

        else :

            all_lines += " ".join(task)


    x.seek(0)
    x.truncate()
    x.write(all_lines)
    x.flush()
    os.fsync(x)


    print('Task Reassigned')

def due_date_change(x):

    IDnum = int(input("Please enter the task ID that you want to change --->>> :"))
    newDueDate = input("Please enter the new task due date --->>>:")
    all_lines = ''

    for line in x :

        task = line.split(" ")

        if int(task[0]) == IDnum and task[6] == 'no' :

            task[5] = newDueDate 

            all_lines += " ".join(task)

        else :

            all_lines += " ".join(task)

    x.seek(0)
    x.truncate()
    x.write(all_lines)
    x.flush()
    os.fsync(x)

def tasks_overview(x , y):

    totalTasks = 0
    incompleteTasks = 0 
    completedTasks = 0
    date = input("Please enter todays date(yyyy-mm-dd) --->>>: ")
    overdueTasks = 0 


    for line in x :

        task = line.split(' ')
        totalTasks += 1 
        

        if task[6] == 'no':

            incompleteTasks += 1

        elif task[6] == "Yes":

            completedTasks += 1 

    for line in x :

        task = line.split('')

        taskdate = task[5]

        if taskdate	< date:

            overdueTasks +=1 

    incompletePercentage = incompleteTasks / totalTasks	* 100 
    oveduePercentage = overdueTasks / totalTasks * 100 

    y.write(str(totalTasks) + " "+ str(incompleteTasks)+ " " + str(completedTasks) + " " + str(overdueTasks) + str(incompletePercentage) + " " + str(overdueTasks) + '\n')

def userOverview(x , y , z):

    users = 0
    tasks = 0
    userTotalTask = 0
    userView = input("please enter username --->>> :")
    incompleteTask = 0
    Taskcompleted = 0

    for line in x : 

        users += 1
    
    for line in y :

        tasks += 1
        task = line.split(" ")

        if task[1] == userView:

            userTotalTask += 1

    for line in y :

        tasks += 1
        task = line.split(" ")

        if task[1] == userView and task[6] == 'no':

            incompleteTask += 1

        elif task[1] == userView and task[6] == 'Yes':

            Taskcompleted += 1 

    z.write(str(userView) + " " + str(tasks) + " " + str(incompleteTask)+ " " + str(Taskcompleted))

def displayTaskOverview(x):

    for line in x:

        overview = line.split(" ")

    print(("_" * 80) + '\n' +
            "Total Tasks" + ("\t" * 2) + overview[0] + '\n' +
            "Incomplete Tasks" + ("\t" * 2) + overview[1] + '\n' +
            "CompletedTasks" + ('\t'* 2) + overview[3] + '\n' +
            ('_' * 80))

def displayUserOverview(x):
    userView = input("PLease enter overview username --->>> :")
    
    for line in x :

        overview = line.split(' ')

        if overview[0] == userView :

            print(('_' * 80) + '\n' + 
                "User" + ('\t'*3) + overview[0] + '\n' + 
                "Total Tasks" + ('\t'*2) + overview[1] + '\n' + 
                "Incomplete Tasks" + ("\t")+ overview[2] +'\n'+ 
                ('_' *80))

        else :

            print("Username not found")


userLogView = userLog.read()
userNameInput = input("Please enter your User name :  ")
userPasswordInput = input('Please enter your password :  ')
userNameFound = userLogView.find(userNameInput)
userPasswordFound = userLogView.find(userPasswordInput)

if userNameInput == 'admin' and userPasswordInput == 'adm1n' :
    
    userAdminAccess = True
    print(" Welcome .Your Admin credentials are correct")
    clearScreen()

elif (userNameFound != -1) and (userPasswordFound != -1) :
    
    print("Your credentials are correct")
    userAccess = True 

elif (userNameFound != -1) and (userNameFound == -1) :

    print("You have not enterd an valid password ")
    
elif (userNameFound == -1) and (userPasswordFound != -1) :
    
    print("You have not entered an valid user name ")  

# all admin statements work now for the user to have only the ability to view his own task
    # userNameFound has to be defined by searching for user name and pasword in user file 
                
elif (userNameFound != -1) and (userPasswordFound != -1) :
    
    print("Your credentials are correct")
    userAccess = True 

elif (userNameFound != -1) and (userNameFound == -1) :

    print("You have not enterd an valid password ")
    
elif (userNameFound == -1) and (userPasswordFound != -1) :
    
    print("You have not entered an valid user name ")  
            
if userAdminAccess == True : 
    
    AdminMenu()
    adminChoice = int(input('--->  :'))
    if adminChoice == 'r' :
        
        reg_user(userLog)
          
    elif adminChoice == 'a' : 
        
        add_task(userTasksFile)
                         
    elif adminChoice == 'va':
        
        view_all(userTasksFile)
        
    elif adminChoice == 'vm' :
        
        view_mine(userTasksFile)

    elif adminChoice == 'gr':

        tasks_overview(userTasksFile,tasksOverviewFile)

    elif adminChoice == 'ds':

        displayTaskOverview(tasksOverviewFile)

elif userAccess == True :
    
    userMenu()
    
    userChoice = int(input('--->  :'))
    
    if userChoice == 'vm' :
        
        view_mine(userTasksFile)
      
    elif userChoice == 'ct' :
        
        complete_task(userTasksFile)

    elif userChoice == 'gr' :

        userOverview(userLog , userTasksFile , userOverviewFile)

    elif userChoice == 'ds' : 

        displayUserOverview(userOverviewFile)











# testing all function in program

#displayUserOverview(userOverviewFile)
#displayTaskOverview(tasksOverviewFile)
#userOverview(userLog , userTasksFile, userOverviewFile)
#tasks_overview(userTasksFile , tasksOverviewFile)
#due_date_change(userTasksFile)
#reassign(userTasksFile)
#view_specific(userTasksFile)
#AdminMenu()
#add_task(userTasksFile) 
#view_all(userTasksFile)
#complete_task(userTasksFile)
#reg_user(userLog)
#view_mine(userTasksFile)
userTasksFile.close()
userLog.close()
tasksOverviewFile.close()   
userOverviewFile.close()
