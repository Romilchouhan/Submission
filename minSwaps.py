# Python code for minimum number of adjacent swaps 
# required to group all 1's together

def minSwaps(arr, n):
    oneIndices = []  # list containing indices of all 1's in the input
    for i in range(0, n):
        if arr[i] == 1:
            oneIndices.append(i)
    
    middleOfoneIndices = int((len(oneIndices) - 1) / 2)
    minimumSwaps = 0
    for i in range(len(oneIndices)):
        minimumSwaps += abs(oneIndices[middleOfoneIndices] - oneIndices[i]) - abs(middleOfoneIndices - i)
    
    return minimumSwaps
        
n = int(input("n = "))
arr = [int(item) for item in input("Arr (separated by spaces) = ").split()]

print(minSwaps(arr, n))
