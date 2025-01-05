class LinkNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Data:
    def __init__(self,data, seq):
        self.data = data
        self.seq = seq

    def __repr__(self):
        return f"({self.data}, {self.seq})"


#bucket sort
def bucket_sort(arr_to_be_sorted, max_number, min_number, total_numbers):

    bucket_size = max_number//total_numbers + 1
    total_number_of_buckets = total_numbers

    buckets = [None] * total_number_of_buckets

    for number in arr_to_be_sorted:
        bucket_index = number.data//bucket_size
        add_to_bucket(buckets,bucket_index,number)

    sorted_numbers = []
    for bucket in buckets:
        sorted_numbers.extend(get_all_numbers_list_from_bucket(bucket))

    print(sorted_numbers)

def add_to_bucket(buckets,bucket_index,number):
    node = LinkNode(data = number)

    if not buckets[bucket_index]:
        buckets[bucket_index] = node
        return

    current = buckets[bucket_index]
    prev = None

    while current and current.data.data <= node.data.data:
            prev = current
            current = current.next

    if prev:
        prev.next = node
    else:
        buckets[bucket_index] = node

    node.next = current


def get_all_numbers_list_from_bucket(bucket):
    sorted_numbers = []
    while bucket:
        sorted_numbers.append(bucket.data)
        bucket = bucket.next

    return sorted_numbers



arr = [1,3,23,12,432,123,654,23,76,9999,123,435,123,2432,654,123,4356,234,346,213,45]
data = []
i = 0
for no in arr:
    i +=1
    data.append(Data(data = no,seq=i))
bucket_sort(data, 9999,1,21)
# bucket_sort([5,234,3,4,5,6,9999], 9999,1,7)






