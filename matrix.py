x=[[2,3,4],
[1,4,6],
[6,5,2]]

y=[[2,3,4],
[1,5,7],
[6,2,3]]

result=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        x[i]+[j]+y[i][j]
for r in result:
    print(r)