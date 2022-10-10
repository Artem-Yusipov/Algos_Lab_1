def largest_number(numbers):
    answer = ''
    arr_0 = len(str(max(map(int, numbers))))
    while numbers:
        max_numbers = numbers[0]
        for x in numbers:
            if preparation(x, arr_0) > preparation(max_numbers, arr_0):
                max_numbers = x
        answer += max_numbers
        numbers.remove(max_numbers)
    return answer


def preparation(num, arr_0):
    num += '9' * (arr_0 - len(num))
    return int(num)


n = input()
arr = list(input().split())
print(largest_number(arr))

