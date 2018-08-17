def checklessthan(num, checknum):
    if num < checknum:
        return True


outputlist = []
checknum = int(input('Enter the Number to Check'))
checklist = [2, 4, 5, 6, 79, 56]

for ele in checklist:
    if checklessthan(ele, checknum):
        outputlist.append(ele)

print(outputlist)
