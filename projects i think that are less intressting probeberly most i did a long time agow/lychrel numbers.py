number = 0
listofnumbers = []
for i in range(100000):
    for trys in range(50):
        ilist = []
        palindromic1 = ""
        palindromic2 = ""
        for j in str(i):
            ilist.append(j)
        for k in range(len(ilist)):
            palindromic2 += str(ilist[len(ilist)-1-k])
        if int(palindromic2) == int(i):
            listofnumbers.append(i)
            number += 1
            break
        else:
            i = i + int(palindromic2)
print(number)