#write code for both for and while loop
#Get marks from 5  students and calculate avg
#
student=int(input('Enter the no of student:'))
#for loop
total = 0
for num in range(student):
    #get user input
  m1=int(input("Enter mark1:"))   
  m2=int(input("Enter mark2:"))   
  m3=int(input("Enter mark3:")) 
  m4=int(input("Enter mark4:"))   
  m5=int(input("Enter mark5:"))   
total =m1+m2+m3+m4+m5
average=total/5
print ("Avg is ",average)

#using while loop
total = 0
noOfStudents = 5
i = 0
while (i <6)
   #get user input
 vmark1=int(input("Enter mark1:"))   
  mark2=int(input("Enter mark2:"))   
  mark3=int(input("Enter mark3:")) 
  mark4=int(input("Enter mark4:"))   
  mark5=int(input("Enter mark5:"))  
     total= mark1+mark2+mark3+mark4+mark5
     avg=total/5
print ("Avg is ",avg)
i=i+1
