#python code for find a string and count it's occurances.
string=input()
substring=input()
count=0
for i in range(0,len(string)):
      if(string[i]==substring[0]):
            if(string[i:i+len(substring)]==substring):
                  count+=1
      else:
           continue
           
print(count)
