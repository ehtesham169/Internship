#A school has 100 lockers and 100 students. All lockers are closed on the first day of school. As
#the students enter, the first student, denoted S1, opens every locker. Then the second student, S2,
#begins with the second locker, denoted L2, and closes every other locker. Student S3 begins with
#the third locker and changes every third locker (closes it if it was open, and opens it if it was
#closed). Student S4 begins with locker L4 and changes every fourth locker. Student S5 starts with
#L5 and changes every fifth locker, and so on, until student S100 changes L100.
#After all the students have passed through the building and changed the lockers, which lockers are
#open? Write a program to find your answer. The program should display the answer like this:
#Locker x is open
#Locker y is open
#Locker z is open
students = []
lockers=[]
lockercondition=[]
print("All lockers are closed on the first day of school.")
for j in range(100):
    studentnumber = j+1
    studentnumber = str(studentnumber)
    students.append(("S" + studentnumber))
    lockernumber=j+1
    lockernumber=str(lockernumber)
    lockers.append(("L"+lockernumber))
    lockercondition.append("close")

#print(students,lockers,lockercondition)
for k in range(100):
    if(students[k]=='S1'):
        for l in range(100):
            lockercondition[l]='open'
    elif(students[k]=='S2'):
        for m in range(2,100,2):
            lockercondition[m]='close'
    else:
        for n in range(k,100,k):
            if (lockercondition[n]=='close'):
                lockercondition[n]='open'
            else:
                lockercondition[n]='close'
for o in range(100):
    if(lockercondition[o]=='open'):
        print(lockers[o],lockercondition[o])
    #print(students[k],lockers[k],lockercondition[k])
        #print("Student:",students[i],'is now opening lockers.')
        #for k in range(i,100,i):
            #if(lockercondition[k]=='close'):
                #lockercondition[k]='open'
            #else:
                #lockercondition[k]='close'
        #if(i==99):
            #for l in range(100):
                #print("Locker:", lockers[l], "is", lockercondition[l])


