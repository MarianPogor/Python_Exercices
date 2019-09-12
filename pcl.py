hetero_list = [0, 'en', 2, 3, 'four', 5, 6, 7, 8, 9] 

#print (hetero_list[1]) 
#print (hetero_list[-1])

#print (hetero_list[:4])

#print (hetero_list[3:-2]) 

#tup1 = (23, 'April' , 13.00)

#print(tup1[-1:3]) 

# tuple example 

#d1 = {'code': 'PCL', 'title' : 'Programming', 'ECTS': 5}

#print(d1['code'] ,d1['title'] , d1['ECTS']) 

#print( "The object consists" ,d1)

#d1.clear()

#print (d1)  

#myName = { 'name': 'Marian Pogor', 'studentNumber': 239783}

#print ("This program prints a string 10 times")

#for count in range(10):
	#print( myName)
	
	
#print("Can you please add two numbers? : ")

#g1= input()

#for count in range(int(g1)):
	#print(g1)
	


#numLst = [2, 3, 3, 4]
 
#def sumList(intList):
    #if (len(intList) == 0):
        #return 0;
   # else:
        #return intList[0] + sumList(intList[1:])
		

#print(sumList(numLst))

def printEvenNumbers():
	naturalNumbers = [0,1,2,3,4,5,6,7,8,9]
	
	for nr in naturalNumbers:
		if(nr%2 == 1):
			print(nr)

printEvenNumbers()


trait_point = [('Caring', 9) , ('Kind',6) ,('Social' ,5), ('Innovative',7) , ('Programming',8)] 

#print(max(trait_point, key=lambda sprice: sprice[1]))

courseList = [("SDJ1", 5, 1), ("DNP1", 5, 1), ("SEP1", 10, 1),
              ("SDJ2", 5, 2), ("SDJ3", 5, 3), ("PME1", 5, 6),
              ("BPR1", 5, 6), ("PCL1", 5, 6), ("BPR2", 15, 7)]
 

def get6SemCourses(lst):
    resultLst = []
    for item in lst:
        _, _, semester = item
        if (semester == 6):
            resultLst.append(item)
    return resultLst
 
 
print(get6SemCourses(courseList))

