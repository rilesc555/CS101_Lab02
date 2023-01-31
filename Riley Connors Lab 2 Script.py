print('Welcome to the LAB grade calculator!\n')

#get name of student
name = input('Who are we calculating grades for?\n')

#get lab grade, limit to [0,100]

labs = int(input('Enter the Labs grade:\n'))
if labs < 0:
    print('The lab value should have been zero or greater. It has been changed to zero.')
    labs = 0
if labs > 100:
    print('The lab value should have been 100 or less. It has been changed to 100.')
    labs = 100
print()

#get exams grade, limit to [0,100]
exams = int(input('Enter the EXAMS grade:\n'))
if exams < 0:
    print('The exam value should have been zero or greater. It has been changed to zero.')
    exams = 0
if exams > 100:
    print('The exam value should have been 100 or less. It has been changed to 100.')
    exams = 100
print() 

#get attendance grade, limit to [0,100]
atten = int(input('Enter the attendance grade:\n'))
if atten < 0:
    print('The attendance value should have been zero or greater. It has been changed to zero.')
    atten = 0
if atten > 100:
    print('The attendance value should have been 100 or less. It has been changed to 100.')
    atten = 100
print()

#calculate and print weighted grade
weighted = (labs * 0.7) + (exams * 0.2) + (atten * 0.1)
print(f'The weighted grade for {name} is {weighted}')

#calculate and print letter grade
if weighted >= 90:
    print(f'{name} has a letter grade of A')
elif weighted >= 80:
    print(f'{name} has a letter grade of B')
elif weighted >= 70:
    print(f'{name} has a letter grade of C')
elif weighted >= 60:
    print(f'{name} has a letter grade of D')
else:
    print(f'{name} has a letter grade of F')
