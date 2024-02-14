import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import math
def binarysearch(a,low,high,key):
    if low<=high:
        mid=(high+low)//2
        if a[mid]==key:
            print("search successfull, Key found at location:",mid+1)
            return
        elif key<a[mid]:
            binarysearch(a,low,mid-1,k)
        else:
            binarysearch(a,mid+1,high,k)
    else:
        print("Search unsuccesfull")
a=[13,24,35,46,57,68,79]
print("the array elements are:",a)
k=int(input("enter the key element"))
binarysearch(a,0,len(a)-1,k)
x=list(range(1,10000))
plt.plot(x,[math.log(y,2)for y in x])
plt.title("Binary search - Time complexity is o(logn)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()
      
             
