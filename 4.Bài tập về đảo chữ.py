def are_anagrams(word1, word2):
    # Loại bỏ khoảng trắng và chuyển tất cả thành chữ thường
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    # Kiểm tra độ dài của hai từ
    if len(word1) != len(word2):
        return False
    # Sắp xếp các ký tự của từ và so sánh
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    return sorted_word1 == sorted_word2

# VD một số cặp từ đảo chữ

print(are_anagrams("restful ", "fluster"))
print(are_anagrams("yone", "enjoy")) 