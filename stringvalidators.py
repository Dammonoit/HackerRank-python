string=input()
print (any(str.isalnum() for str in string))
print (any(str.isalpha() for str in string))
print (any(str.isdigit() for str in string)) 
print (any(str.islower() for str in string))
print (any(str.isupper() for str in string)) 

