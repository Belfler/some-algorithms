from random import randint
from time import time


def generate_array(n, min_val=0, max_val=1000):
    return [randint(min_val, max_val) for _ in range(n)]


def merge(left, right):
    array = []
    i = j = 0  # i is index for the left part, j is for the right one
    while i != len(left) and j != len(right):
        if left[i] <= right[j]:
            array.append(left[i])
            i += 1
        else:
            array.append(right[j])
            j += 1
    else:
        array += (left[i:] + right[j:])
    return array


def merge_sort(array):
    if len(array) == 1:
        return array
    half_length = len(array) // 2
    left = merge_sort(array[:half_length])
    right = merge_sort(array[half_length:])
    array = merge(left, right)
    return array


def benchmark(n_numbers=[10, 100, 1000, 10000, 100000], n_measure=10):
    for n in n_numbers:
        times = []
        array = generate_array(n)
        for _ in range(n_measure):
            start_time = time()
            merge_sort(array)
            final_time = time()
            times.append(final_time - start_time)
        avr_time = sum(times) / n_measure
        print('Average time for sorting {} numbers is {:.5f} seconds.'.format(n, avr_time))


benchmark()
