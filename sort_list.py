def sort(lst: list[int | float] = []) -> list[int | float]:
    if len(lst) < 2:
        return lst
    
    base = lst.pop(len(lst) // 2)
    less_base = list(filter(lambda x: x <= base, lst))
    greater_base = list(filter(lambda x: x > base, lst))

    return sort(less_base) + [base] + sort(greater_base)


def to_num(str_num: str) -> int | float:
    try:
        return int(str_num)
    except ValueError:
        return float(str_num)


if __name__ == '__main__':
    nums = list(map(to_num, input().split()))

    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    sorted_nums = sort(nums)

    print(f'Четные числа: {even_nums}')
    print(f'Максимальное число: {max(nums)}')
    print(f'Минимальное число: {min(nums)}')
    print(f'Отсортированный список: {sorted_nums}')
