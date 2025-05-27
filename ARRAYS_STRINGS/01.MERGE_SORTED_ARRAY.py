#trail
def Merge_Array(nums1,m,nums2,n):
    res=[0]*(m+n)
    a=[i for i in nums1 if i!=0]
    #print(a)
    b=[i for i in nums2 if i!=0]
    #print(b)
    if len(a)+len(b)!=len(res):
        return -1 
    else:
        res=a+b
        return sorted(res)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Merge_Array(nums1,m,nums2,n))


#OPTIMAL 

def Merge_Array(nums1,m,nums2,n):
    #STEP1 adding len(nums2) to len(nums1)
    for _ in range(len(nums2)):
        nums1.append(0)
    #return nums1    
    
    #STEP2  POINTERS FROM END 
    i=m-1 
    j=n-1 
    k=m+n-1 
    
    #STEP3 MERGE IN reverse so that nums1 can be modified without extra space 
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1 
        else:
            nums1[k]=nums2[j]
            j-=1 
        k-=1 #Because to dec len nums1 with arrangement    
        
    #STEP4 now we need to do remain elements in nums 
    while j>=0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    nums1=[i for i in nums1 if i!=0]    
    return nums1    
    
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(Merge_Array(nums1,m,nums2,n))