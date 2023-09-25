n=int(input("Enter a number:"))
a=0
b=2
sum=0
count=1
print("Fibonaccib Series:", end= "")
while(count<=n):
    print(sum, end="")
    count+=1
    a=b=sum
    sum=a+b
