def reverse_integer(number):
    # Xử lý trường hợp số âm
    sign = -1 if number < 0 else 1
    number *= sign
    # Chuyển số nguyên thành chuỗi để dễ xử lý
    str_number = str(number)
    # Đảo ngược chuỗi
    reversed_str = str_number[::-1]
    # Chuyển lại thành số nguyên và nhân với dấu đúng
    reversed_number = int(reversed_str) * sign
    return reversed_number
#ví dụ
print(reverse_integer(1234))  