def maximalSubarray(array):
    outArray = []
    for x in array:
        if x>0:
            outArray.append(x)
    return outArray

A = [1,2,-4,-4,5,-6,2,3,4]
print(maximalSubarray(A))
