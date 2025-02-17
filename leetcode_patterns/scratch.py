arr = [2,3,1,4,2]
arr = sorted(arr,reverse=True)
arr_sum = 0

for item in arr:
    arr_sum += item

curr_count = 0

while arr_sum > curr_count:
    i = 0
    temp_count = 0

    while temp_count < curr_count +1:
        if arr[i] > 0:
            arr[i] -= 1
            temp_count += 1
        i += 1
    arr_sum = 0

    for item in arr:
        arr_sum += item

    curr_count += 1

print(curr_count)
