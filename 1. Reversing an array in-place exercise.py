def reverse_array_in_place(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
#INPUT
my_array = [1, 2, 3, 4, 5]
reverse_array_in_place(my_array)
#OUTPUT
print("Mảng sau khi đảo ngược:", my_array)