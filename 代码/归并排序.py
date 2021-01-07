def mergesort(seq):
    if len(seq)<=1:
        return seq
    mid = len(seq) // 2
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [56,89,11,2,899,0,3,9]
result = mergesort(seq)
print("排序之前",seq)
print("排序之后",result)

'''
输出
排序之前 [56, 89, 11, 2, 899, 0, 3, 9]
排序之后 [0, 2, 3, 9, 11, 56, 89, 899]
'''

# TODO:
#      逐行注释
