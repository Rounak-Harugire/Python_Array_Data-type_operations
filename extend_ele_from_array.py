import array as arr 
a = arr.array('i', [10, 20, 30,40,50])
print("The before array extend  : ", end =" ")
for i in range (0, 5): 
  
    print (a[i], end =" ") 
    
print()
a.extend([60,70,80,90,100])
print("\nThe array after extend :",end=" ")

for i in range(0,10):  
  
    print(a[i],end=" ") 
    
print()
