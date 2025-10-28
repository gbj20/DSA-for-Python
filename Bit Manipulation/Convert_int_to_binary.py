def convert2Binary(num: int) -> str:
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    return result[::-1]
print(convert2Binary(10))  # Output: "1010"
print(convert2Binary(0))   # Output: "0"
print(convert2Binary(5))   # Output: "101"
