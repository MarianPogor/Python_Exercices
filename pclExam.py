def factorialItr(n):
    if (n < 0):
        raise Exception("n cannot be less than zero.")
    elif (n == 0):
        return 1
    factResult = 1
    for idx in range(1, n + 1):
        factResult *= idx
    return factResult

print("The result is of factorialItr is   :   " + str(factorialItr(4)))

#The result is of factorialItr is   :   24

#Question 6b


def recFactorial(n):
    if (n < 0):
        raise Exception("n cannot be less than zero.")
    elif (n == 0):
        return 1
    return n * recFactorial(n - 1)

print("The result of recFactorial is :   "   + str(recFactorial(4)))


#The result of recFactorial is :   24

numLst = [2, 3, 3, 4]
 
def sumList(intList):
    if (len(intList) == 0):
        return 0;
    else:
        return intList[0] + sumList(intList[1:])
 
print("The sum of the list is " + str(sumList(numLst)))

#The sum of the list is 12


# Question 7
 
# Question 7a:
 
courseList = [("SDJ1", 5, 1), ("DNP1", 5, 1), ("SEP1", 10, 1),("SDJ2", 5, 2), 
              ("SDJ3", 5, 3), ("PME1", 5, 6), ("SEP 6",5,6),
              ("BPR1", 5, 6), ("PCL1", 5, 6), ("BPR2", 15, 7)]
			  
			  
def getSixSemester(lst):
    resultLst = []
    for item in lst:
        _, _, semester = item
        if (semester == 6):
            resultLst.append(item)
    return resultLst			 
	
print("The semester from 6th semester from the list are: "  + str(getSixSemester(courseList)))

#The semester from 6th semester from the list are: [('PME1', 5, 6), ('SEP 6', 5, 6), ('BPR1', 5, 6), ('PCL1', 5, 6)]



