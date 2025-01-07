class LinkedListNode:
    def __init__(self,data,next,seq):
        self.data = data
        self.next = next
        self.seq = seq

    def __repr__(self):
        return "Linked node"

def radix_sort(array):
    digits = 3
    for digit_number in range(digits):
        buckets = [None] * 10
        for num in array:
            put_num_in_corresponding_bucket(num,buckets,digit_number)

        array = get_sorted_array_from_buckets(buckets)
        print(len(array))

    return array

def put_num_in_corresponding_bucket(num, buckets,digit_number):
    digit = num.data // 10 ** digit_number % 10
    add_to_bucket(buckets,digit,num)

def add_to_bucket(buckets, digit, num):
    node = LinkedListNode(data=num.data, next=None, seq=num.seq)
    bucket_index = digit

    if buckets[bucket_index] is None:
        buckets[bucket_index] = node
        return

    current = buckets[bucket_index]
    prev = None

    while current and current.data < node.data:
        prev = current
        current = current.next

    if prev:
        prev.next = node
        node.next = current
    else:
        buckets[bucket_index] = node
        node.next = current


def get_sorted_array_from_buckets(buckets):
    sorted_array = []
    for node in buckets:
        while node:
            sorted_array.append(DataObj(data=node.data, seq=node.seq))
            node = node.next

    return sorted_array

class DataObj:
    def __init__(self,data,seq):
        self.data = data
        self.seq = seq

    def __repr__(self):
        return f"data = {self.data}, seq = {self.seq}"

arr = [123,322,233,436,514,197]


data_arr = [DataObj(data=num, seq=seq) for seq, num in enumerate(arr, start=1)]

data_arr = radix_sort(data_arr)
print(data_arr)
