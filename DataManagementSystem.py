import random
import sys
from tabulate import tabulate

user_list = []
course_list = []

def isValid(id):
    for user in user_list:
        if user.U_Id == id:
            return False
    return True

def generateId(type):
        numbers = "1234567890"
        id = type
        while True:  
                id = type      
                for i in range(6): 
                        id += random.choice(numbers)
                if isValid(id) :
                        break
        return id

class User:
        def __init__(self,User_type,Name,Email,Phone,Address,Courses,Batches):
                self.U_Id = generateId(User_type)
                self.User_type = User_type
                self.Name= Name
                self.Email=Email
                self.Phone=Phone
                self.Address=Address
                self.Courses =Courses
                self.Batches = Batches

class Course:
       def __init__(self,Course_name,Course_descr,Associated_faculty,Students_enrolled):
               self.CourseId=generateId("Course")
               self.Course_name=Course_name
               self.Course_descr=Course_descr
               self.Associated_faculty=Associated_faculty
               self.Students_enrolled=Students_enrolled

class System:
       def listing(self,listFor):
            list = []
            while True:
                list.append(str(input(f"Enter {listFor}: ")))
                if list[-1]=="none":   
                       list.pop()
                       break             
            return list
       
       def addUser(self,User_type):
            print("\n")
            Name=str(input(f"{User_type} name:"))
            Email=str(input(f"{User_type} email: "))
            Phone=int(input(f"{User_type} number: "))
            Address=str(input(f"{User_type} address: "))
            
            Batch =self.listing("a batch") if User_type == "Faculty" else []
            Course=self.listing("a course") if User_type == "Faculty" else []

            user = User(User_type,Name,Email,Phone,Address,Course,Batch)
            user_list.append(user)
            print(f"{User_type} created successfully with Id: ",user.U_Id)

       def addCourse(self):
             print("\n")
             Name=str(input("Enter course name: "))
             Description=str(input("Enter course description: "))
             Faculties=self.listing(f"Facultie of {Name}")
             Students=self.listing(f"Student of {Name}") 

             course = Course(Name,Description,Faculties,Students)
             course_list.append(course)
             print("Course created successfully with id: ",course.CourseId)

       def printDetails(self,datatype):
            print("\n\n")
            if datatype == 1 or datatype == 2:
                user_type = "Student" if datatype == 1 else "Faculty"
                taken_Id = input(f"Enter 'all' to display all {user_type.lower()}s or a user ID: ")
                
                if user_type == "Student": 
                    data = [
                            [user.U_Id, user.Name, user.Email, user.Phone, user.Address]
                            for user in user_list if user.User_type == user_type and (taken_Id == "all" or user.U_Id == taken_Id)
                            ]
                    headers = ["ID", "Name", "Email", "Phone", "Address"]
                else:
                    data = [
                            [user.U_Id, user.Name, user.Email, user.Phone, user.Address, ', '.join(user.Courses),', '.join(user.Batches)]
                            for user in user_list if user.User_type == user_type and (taken_Id == "all" or user.U_Id == taken_Id)
                            ]
                    headers = ["ID", "Name", "Email", "Phone", "Address","Courses", "Batches"]    
            elif datatype == 3:
                taken_Id = input("Enter 'all' to display all courses or a specific course ID: ")
                data = [
                        [course.CourseId, course.Course_name, course.Course_descr, ', '.join(course.Associated_faculty), ', '.join(course.Students_enrolled)]
                        for course in course_list if taken_Id == "all" or course.CourseId == taken_Id
                       ]
                headers = ["Course ID", "Name", "Description", "Faculties", "Students"]
            else:
                print("Invalid option.")
                return

            print(tabulate(data, headers=headers, tablefmt="pretty"))   
        
       def getPrompt(self):
            print("\n\n")
            prompt = int(input("What data access do you need?\n1>Student\n2>Faculty\n3>Course\n4>Exit program"))
            print("\n\n")

            if prompt == 4 :  
                print("Thanks for running my code! Respecting bugs since day one.\n"
                      "                                                             —by K@llii.") 
                sys.exit()

            if prompt in [1,2]:
                usertype="Student" if prompt == 1 else "Faculty"
                if int(input("What do you want:\n1>Edit database.\n2>Print details.")) == 2:
                         self.printDetails(prompt)
                else:
                         self.addUser(usertype)
            elif prompt == 3:  
                if int(input("What do you want:\n1>Edit database.\n2>Print details.")) == 2:
                         self.printDetails(prompt)
                else:
                         self.addCourse()  
            else:
                print("Enter a valid choice.") 

start = System()
while True: start.getPrompt()            
