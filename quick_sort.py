import random

def quick_sort(A):
    '''
        Simple implementation of quick sort
    '''
    S =[]
    E = []
    G = []
    if len(A) > 1:
        pivot = A[0]
        for i in A:
            if i < pivot:
                S.append(i)
            elif i == pivot:
                E.append(i)
            else:
                G.append(i)
        S = quick_sort(S)
        G = quick_sort(G)
        # Merge arrays together in order. 
        return S+E+G
    else:
        return A

# Quick check to see if our values are sorted!
values = [random.randint(0, 1000) for i in range(30)]
print('Unsorted values', values)
print('Sorted', quick_sort(values))

