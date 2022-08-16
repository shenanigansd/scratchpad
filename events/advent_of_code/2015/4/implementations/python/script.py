import hashlib
import time
from pathlib import Path


def timer(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('Time elapsed:', time.time() - start)
        return result

    return inner


@timer
def find_hash_with_prefix(text: str, prefix: str) -> int:
    number = -1
    while True:
        number += 1
        hash_ = hashlib.md5(f"{text}{number}".encode('utf-8')).hexdigest()
        if hash_.startswith(prefix):
            break
    return number


def part_one(text: str) -> int:
    return find_hash_with_prefix(text, "0" * 5)


def part_two(text: str) -> int:
    return find_hash_with_prefix(text, "0" * 6)


if __name__ == '__main__':
    data: str = Path("../../input.txt").read_text().strip()
    print(f"{data=}")

    print(part_one(text=data))
    print(part_two(text=data))
