def is_palindrome(s):
    # Chuyển đổi chuỗi thành chữ thường và loại bỏ các ký tự không phải chữ cái
    s = ''.join(c.lower() for c in s if c.isalnum())
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
#VD
print(is_palindrome(" no side edison")) 
print(is_palindrome("live evil")) 