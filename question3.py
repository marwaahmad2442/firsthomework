import json
num=input("enter your name")
s=0
ob={}
with open("question.json","r") as f:
    ob=json.load(f)
    
for i in ob.keys():
     print(i)
     oa=input("enter your answer")
     
     if ob[i]==oa:
         print("excellent")
         s=s+10
     else:
         print("false")
with open("result.json","w") as f:
    f.write(num,s)
