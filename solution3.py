#Ques3

p=input()
st=eval(input())
n=set()
for k in st:
  if p==k[0:len(p)]:
    n.add(k)
print(n)