#this is a python example for mutations in string.
#str= input();list= list(str);n=int(input());n1=input();list[n]= n1;str1=''.join(list);print(str1)----not working only in hackerrank.
s =input()
i, c =input().split()

print (s[:int(i)] + c + s[int(i)+1:])
      
 
