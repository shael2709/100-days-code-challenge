l=[int(x) for x in input("Enter numbers seperated by space").split()]
sum,d,flag=0,{},0
oldIndex=None
for x in range(len(l)):
     oldIndex=d.get(sum,None)
     if oldIndex==None and x==len(l):
          flag=1
          break;
     if oldIndex==None:
          d[sum]=x
          sum+=l[x]
     else:
          l2=l[oldIndex:x]
if flag==1:
     print("No Sub Array")
else:
     print("Sub array with sum zero is= ",l2)
