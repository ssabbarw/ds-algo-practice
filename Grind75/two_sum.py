def two_sum_greedy(array, target):
    for i in range(len(array)):
        for j in range(i,len(array)):
            if array[i] + array[j] == target:
                return [i, j]
    return []

def two_sum(array, target):
    number_vs_index = {}

    for i in range(len(array)):
        number_vs_index[array[i]] = i

    for i in range(len(array)):
        new_target = target - array[i]
        if new_target in number_vs_index and number_vs_index[new_target] != i:
            return [i, number_vs_index[new_target]]

    return []



print(two_sum([3,2,4],6))
