##  Python Code

##  This program will take a list of students and accept input for each student's discussion,
##  quiz, and assignment grades. It will then calculate the weighted average of each student's
##  grades and output the name and grade of the student with the highest overall score.

##  I chose the four names Alvin, Simon, Theodore, and Dave.

##  Developer: Shane Bottomley   Class: CMSC105   Date: 02/09/2024

##----Functions----------------------

#Welcome message, explain program
def welcome_message():
    print('Welcome to the Highest Student Grade calculator!')
    print('This program will take three grades for each student, output the weighted'
          ' average for that student, and\nthen output the student with '
          'the highest overall score.\nLets get started!\n')

#Get students discussion, quiz, and assignement grade from user. Return weighted grade
def students_weighted_grade(studentname):
    discgrade = float(input(f"Enter {studentname}'s discussion grade: "))
    quizgrade = float(input(f"Enter {studentname}'s quiz grade: "))
    assigrade = float(input(f"Enter {studentname}'s assignment grade: "))
    weightedgrade = (discgrade * 0.15) + (quizgrade * 0.35) + (assigrade * 0.5)
    #return weighted grade rounded to two decimal points
    return round(weightedgrade, 2)

##---------Main-----------------------------------------------------

#Take a list of students and call function to input discussion, quiz, and assignment
#grades then return weighted grade
#Compare weighted grade of each student and output student with highest grade
def main():
    #print welcome message
    welcome_message()

    #initialize variables for highest grade, highest student, and list of students
    highestgrade = 0
    higheststudent = None
    studentlist = ['Alvin', 'Simon', 'Theodore', 'Dave']

    #call function for each name in studentlist, print name and grade
    for student in studentlist:
        wtAvgGrade = students_weighted_grade(student)
        print(f"{student}'s weighted average grade is {wtAvgGrade}\n")

        #assign highest grade and student name while looping
        if wtAvgGrade > highestgrade:
            highestgrade = wtAvgGrade
            higheststudent = student

    #Output student with highest grade
    print(f'{higheststudent} has the highest overall grade with a {highestgrade}')

##--------Execute-----------------------------------
main()