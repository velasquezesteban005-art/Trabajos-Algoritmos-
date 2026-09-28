import time
import random

def bubble_sort(arr):
    A = arr.copy()
    comp, inter = 0, 0
    n = len(A)
    for i in range(n):
        cambio = False
        for j in range(0, n - i - 1):
            comp += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                inter += 1
                cambio = True
        if not cambio:
            break
    return A, comp, inter

def selection_sort(arr):
    A = arr.copy()
    comp, inter = 0, 0
    n = len(A)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            A[i], A[min_idx] = A[min_idx], A[i]
            inter += 1
    return A, comp, inter

def insertion_sort(arr):
    A = arr.copy()
    comp, inter = 0, 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0:
            comp += 1
            if A[j] > key:
                A[j + 1] = A[j]
                inter += 1
                j -= 1
            else:
                break
        A[j + 1] = key
    return A, comp, inter