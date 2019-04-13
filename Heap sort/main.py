from random import randint
from time import time


def generate_array(n, min_val=0, max_val=1000):
    return [randint(min_val, max_val) for _ in range(n)]


def heapify(array, idx, last_idx):
    left_node_idx = 2 * idx + 1
    right_node_idx = 2 * idx + 2
    max_idx = idx
    # check if the left node exists and is greater than the top node
    if left_node_idx < last_idx and array[left_node_idx] > array[max_idx]:
        max_idx = left_node_idx
    # the same for the right node
    if right_node_idx < last_idx and array[right_node_idx] > array[max_idx]:
        max_idx = right_node_idx
    if max_idx != idx:
        array[idx], array[max_idx] = array[max_idx], array[idx]
        heapify(array, max_idx, last_idx)


def heap_sort(array):
    length = len(array)
    last_idx_has_child = length // 2 - 1
    # build max-heap tree
    for i in range(last_idx_has_child, -1, -1):
        heapify(array, i, length)
    # now sort
    for i in range(length - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)
    return array


def benchmark(n_numbers=[10, 100, 1000, 10000, 100000], n_measure=10):
    for n in n_numbers:
        times = []
        array = generate_array(n)
        for _ in range(n_measure):
            start_time = time()
            heap_sort(array)
            final_time = time()
            times.append(final_time - start_time)
        avr_time = sum(times) / n_measure
        print('Average time for sorting {} numbers is {:.5f} seconds.'.format(n, avr_time))


benchmark()
