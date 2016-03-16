gradeDict = {'Kelly':89, 'David':65, 'Jack':95, 'Samantha': 78}
print(gradeDict)

print(gradeDict['David'])

gradeDict['David'] = 56
print(gradeDict)

gradeDict['Jessey'] = 95
print(gradeDict)

del gradeDict['David']
print(gradeDict)

gradeDict = {'Kelly':[89, 90], 'David':[65, 70], 'Jack':[95, 97], 'Samantha': [78, 85]}
print(gradeDict)

print(gradeDict['Kelly'][0])