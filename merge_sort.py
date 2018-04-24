import random

def merge(l1, l2):
    '''Merges two sorted arrays'''
    l = []
    while len(l1) != 0 and len(l2) != 0:
        if l1[0] <= l2[0]:
            l.append(l1.pop(0))
        else:
            l.append(l2.pop(0))

    # This will add any remaining elements from either of the arrays (in the case of two uneven halves).
    while len(l1) != 0:
        l.append(l1.pop(0))

    while len(l2) != 0:
        l.append(l2.pop(0))
    return l

def merge_sort(A):
    '''Recursive merge sort'''
    A1 = []
    A2 = []
    # Eventually we get down to one element in each half
    if len(A) > 1:
        for j in range(int(len(A)/2)):
            A1.append(A[j])
        for j in range(int(len(A)/2), len(A)):
            A2.append(A[j])

        # Sort each half of the array
        A1 = merge_sort(A1)
        A2 = merge_sort(A2)
        # Merge both halves
        A = merge(A1,A2)
    return A

def merge_sort_alt(A):
    '''A more 'Pythonic' way of doing things' '''
    # Eventually we get down to one element in each half
    if len(A) > 1:
        # Split array to two halves
        A1 = A[:int(len(A)/2)]
        A2 = A[int(len(A)/2):]

        # Sort each half of the array
        A1 = merge_sort_alt(A1)
        A2 = merge_sort_alt(A2)
        # Merge both halves
        A = merge(A1,A2)
    return A


# Quick check to see if our values are sorted!
values = [random.randint(0, 1000) for i in range(30)]
print('Unsorted values', values)
print('Sorted', merge_sort(values))
print('Sorted (version 2)', merge_sort(values))



