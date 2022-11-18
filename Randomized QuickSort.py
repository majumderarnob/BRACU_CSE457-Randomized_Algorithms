                                 #Benchmarking Randomized Quicksort
import random

compare = 0

def quick_sort(array, l, r):
    global compare

    if(l < r):
        p = random.randint(l, r)
        pivot = array[p]
        less_than_pivot = []
        greater_than_pivot = []

        for i in range(l, r + 1):

            if i != p:
                compare = compare + 1

            if(array[i] < array[p]):
                less_than_pivot.append(array[i])

            if array[i] > array[p]:
                greater_than_pivot.append(array[i])

        array = quick_sort(less_than_pivot, 0, len(less_than_pivot) - 1) + \
            [pivot] + quick_sort(greater_than_pivot, 0, len(greater_than_pivot) - 1)
        return array
    return [array[0]] if len(array) else []


if __name__ == '__main__':
    array = [i + 1 for i in range(100)]
    random.shuffle(array) 

    expected_comparison = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            expected_comparison = expected_comparison + 2/(j - i + 1)
    print("Expected Number of Comparison = ", expected_comparison)

    comparisons_list = []
    for total in range(100):
        compare = 0
        quick_sort(array, 0, len(array) - 1)
        comparisons_list.append(compare)
    print(comparisons_list)
    print("Average Comparison = ", sum(comparisons_list) / 100)



# Here we see that, when we take 1 to 100 number in a list and want to get the expected value, accorting to the theory,
# the Expected Number of Comparison, E[X̅] is 647.85. But after doing random suffle and random pivot selection in code
# the average comparison number is 657.89. Almost in every run, it displayed a bit higher value than the exact expected number of comparison.
