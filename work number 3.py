def function(number):
    num = str(number)
    num_list = list(num)
    extra = 0

    for i in range(len(num_list) - 1, -1, -1):
        digit = num_list[i]
        if digit == 'A':
            result = 8 + extra
        else:
            result = int(digit) - 2 + extra
        if result < 0:
            result += 10
            extra = -1
        else:
            extra = 0

        num_list[i] = str(result)

    result = ''.join(num_list)
    return result

number = "AA1"
result = function(number)
print(f"Результат: {result}")



p = ("wachlabcdllrtibccdddaaaaldsabbsc")
a = p.replace("c", "ab")
print(a)
