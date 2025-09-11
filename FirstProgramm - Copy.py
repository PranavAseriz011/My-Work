#check the prim no, or not prim no,

num=int(input("enter the number:"))

if num <= 1:
    print("not a prim number")
else:
    for i in range(2,num):
        if num % i == 0: 
            print("not a prim number")
            break
        else:
            print("prim number")