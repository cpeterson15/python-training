admins = {'Python': 'Pass123@'}
studentDict = {}


# noinspection PyPep8Naming
def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade to enter: ')

    if nameToEnter in studentDict:
        print('Adding grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student does not exist')

    print(studentDict)


# noinspection PyPep8Naming
def removeStudent():
    nameToRemove = input('What student to remove? ')
    if nameToRemove in studentDict:
        print('removing student')
        del studentDict[nameToRemove]


def main():
    print("""

    Welcome to Grade Central
    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """)

    action = input('What would you like to do (enter number 1-4)')

    if action == '1':
        print('1')
    elif action == '2':
        print('2')
    elif action == '3':
        print('3')
    else:
        print('No valid choice selected')

login = input('Username: ')
passwd = input('Password: ')

if login in admins:
    if admins[login] == passwd:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid password')
else:
    print('Invalid username')
