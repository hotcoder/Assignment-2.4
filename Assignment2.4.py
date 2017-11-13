'''

Python Program to print the given string in the format specified in the sample
output.
'''

givenStirng = '''
WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
its citizens
'''

resultStatement=""

firstLine = givenStirng[0:25]
secondLine_0 = givenStirng[26:78]
secondLine_1 = givenStirng[78:88]+"!"
secondLine = secondLine_0.strip('\n')+" "+secondLine_1.strip("\n")
thirdLine = givenStirng[89:128]
fourthLine_0 = givenStirng[129:149].strip("\n")
fourthLine_1=givenStirng[149:].strip("\n")
fourthLine=fourthLine_0+fourthLine_1

resultStatement = firstLine+"\n"+6*" "+secondLine+"\n"+13*" "+thirdLine+"\n"+14*" "+fourthLine+":"

print(resultStatement)