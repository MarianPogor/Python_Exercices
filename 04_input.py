# input() will make the program stop and wait for the user to input
# some text and press [enter]

# input() will return text inputed by the user, we can store it in a
# variable (see below)

# we can concatenate text inputed and display it

# usually before a input() we use a print() to let the user know
# that we expect him to type something
#print("Please describe today's weather and press [enter]")
#weather_desc = input()
#weather_desc_with_wow = "WOW! Is is really " + weather_desc + "? I love this kind of weather!"
#print(weather_desc_with_wow)

#print("What country are you from?")
#ctry = input()
#print("What city are you from?")
#city = input()
#msg = ctry + city
#print("so you're from " + msg)

# Since the user can type anything in the console, we never know if
# the user actually typed a number or some text. This is why input()
# always returns a str and we have to convert it to a int.
#print("What year were you born in?")
#y_as_text = input()
#y = int(y_as_text)
#age = 2019 - y
#print("You are: " + str(age) + " (if it's still 2019)")

# exercise 1: write a program which will ask the user for his/hers
# name and reply with a:
# "Hello [name here]! I'm flattered to meet you."
#print("Can you write your name please?")
#name = input()
#print("Hello  " +  str(name)+ "! I'm flattered to meet you.")

# tip: you can "comment out" the code above so you're not asked for
# the weater every time. To "comment out" means to preceed a line of
# code with a # sign so that python will treat it as a comment and
# ignore it.


# exercise 2: write a program which will ask the user for two
# numbers, add them and display the sum. Make sure you're actually
# adding the numbers, not concatenating them.

print("Can you please add two numbers? : ")

g1= input()

g1_num = int(g1)
g2 = input()
g2_num =int(g2)

g3 = g1_num + g2_num

print ("The sum of the numbers is :  " + str(g3))


# exercise 3: write a program which will ask the user for his/hers
# weight (in kilograms) and weight (in meters) and compute BMI*.
# *BMI - Body Mass Index, a convinient rule of thumb allowing to
# categorize a persons weight. BMI = weight / (height * height)
print("Can you please add your kg and height?")

kg= input()
kg_num =int(kg)

height = input()
height_num = float(height)

BMI = kg_num/(height_num * height_num)

print("Your BMI is :" + str(float(BMI)))
if BMI <= 15: 
      print("Very severely underweight ")
elif BMI >= 15 and BMI <=16:
      print("Severely underweight")
elif BMI >= 16 and BMI <=18.5:
    print("Obese")
elif BMI >= 18.5 and BMI <= 25:
    print("Normal (healthy weight")
elif BMI >= 25 and BMI <=30:
    print("Overweight")
elif BMI > 30 and BMI <=35:
    print("Obese Class I (Moderately obese) ")
elif BMI > 35 and BMI <=40:
    print("Obese Class II (Severely obese) ")
elif BMI > 40 and BMI <=45:
    print("Obese Class III (Very severely obese) ")
elif BMI > 45 and BMI <=50:
    print("bese Class IV (Morbidly Obese)   ")
elif BMI > 50 and BMI <=60:
    print("Obese Class V (Super Obese) ")
elif BMI > 60:
    print("Obese Class VI (Hyper Obese)")
else:
    print(" Too Obese")
      
