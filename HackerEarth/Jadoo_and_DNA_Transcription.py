import sys
x=input()
y={'G':'C','C':'G','T':'A','A':'U'}
res=""
for i in range(len(x)):
    if x[i] in y.keys():
        res+=y[x[i]]
    else:
        print("Invalid Input")
        sys.exit()
print(res)  
