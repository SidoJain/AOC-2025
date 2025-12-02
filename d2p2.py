import re

def is_invalid_id(id_num: int) -> bool:
    s = str(id_num)
    return bool(re.fullmatch(r'(.+)\1+', s))

def parse_ranges(ranges_str: str) -> list[tuple[int, int]]:
    ranges = []
    for range in ranges_str.split(','):
        start, end = range.split('-')
        ranges.append((int(start), int(end)))
    return ranges

def sum_invalid_ids(ranges: list[tuple[int, int]]) -> int:
    invalid_ids = [id_num for start, end in ranges for id_num in range(start, end + 1) if is_invalid_id(id_num)]
    return sum(invalid_ids)

with open("../inputs/input2.txt", "r") as file:
    input_ranges = file.read()

ranges = parse_ranges(input_ranges)
result = sum_invalid_ids(ranges)
print(result)