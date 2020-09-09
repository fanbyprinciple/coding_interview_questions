
# 8 threeSum    
# My answer 
# passes 216/324 cases
# Time limit exceeded error
# any pointers for optimisation

def threeSum(nums):
    #unique_nums = list(set(nums))
    #unique_nums = nums
    #print(unique_nums)
    
    answer = []
    for i in range(0, len(nums)):
        #unique_i = unique_nums[:]
        #unique_i.pop(i)
        #print("i",unique_i, unique_nums)
        
            for j in range(0, len(nums)):
                if(i !=j):
                #unique_j = unique_i[:]
                #print("j:", unique_i,unique_j)
                #unique_j.pop(j)
                    for k in range(0, len(nums)):
                        if(i !=k and j !=k):        
                            sum = (nums[i] + nums[j] + nums[k])
                            #sum = (unique_nums[i] + unique_i[j] + unique_j[k])
                            #print((unique_nums[i],unique_i[j],unique_j[k]), sum)
                            if(sum == 0):
                                current = sorted(list([nums[i], nums[j], nums[k]]))
                                if(current not in answer): 
                                    answer.append(current)
                
            

    return answer

# passes this
print(threeSum([3,-9,3,9,-6,-1,-2,8,6,-7,-14,-15,-7,5,2,-7,-4,2,-12,-7,-1,-2,1,-15,-13,-4,0,-9,-11,7,4,7,13,14,-7,-8,-1,-2,7,-10,-2,1,-10,6,-9,-1,14,2,-13,9,10,-7,-8,-4,-14,-5,-1,1,1,4,-15,13,-12,13,12,-11,12,-12,2,-3,-7,-14,13,-9,7,-11,5,-1,-2,-1,-7,-7,0,-7,-4,1,3,3,9,11,14,10,1,-13,8,-9,13,-2,-6,1,10,-5,-6,0,1,8,4,13,14,9,-2,-15,-13]))
# fails this
print(threeSum([0,8,2,-9,-14,5,2,-5,-5,-9,-1,3,1,-8,0,-3,-12,2,11,9,13,-14,2,-15,4,10,9,7,14,-8,-2,-1,-15,-15,-2,8,-3,7,-12,8,6,2,-12,-8,1,-4,-3,5,13,-7,-1,11,-13,8,4,6,3,-2,-2,3,-2,3,9,-10,-4,-8,14,8,7,9,1,-2,-3,5,5,5,8,9,-5,6,-12,1,-5,12,-6,14,3,5,-11,8,-7,2,-12,9,8,-1,9,-1,-7,1,-7,1,14,-3,13,-4,-12,6,-9,-10,-10,-14,7,0,13,8,-9,1,-2,-5,-14]))


### Accepted solution

# class Solution(object):
#     def threeSum(self, nums):
#         res = []
#         nums.sort()
        
#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue
            
#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
#         return res
        