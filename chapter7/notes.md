 ### Notes about lists and loops

-   _for i in range (1,3):_  **only loop two times** from 1 to 3 excluded
-   a.append() **add to list other nested elements** in the following way

---
a = [1, 2, 3]  
b= [4, 5, 6]  
a.append(b)  
print(a)  
[1,2,3,[4,5,6]]  

---
a = [1, 2, 3]  
b= [4, 5, 6]  
a.extend(b)  
print(a)  
[1,2,3,4,5,6]

---
Another way to create a list could be  
l = [i for i in range(1:7)]  
print(l)
[0,1]
