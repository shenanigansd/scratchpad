import hashlib
from pathlib import Path


def part_one(text: str) -> int:
    number = -1
    while True:
        number += 1
        hash_ = hashlib.md5(f"{text}{number}".encode("utf-8")).hexdigest()
        print(hash_)
        if hash_.startswith("00000"):
            break
    return number


def part_two(text: str) -> int:
    number = -1
    while True:
        number += 1
        hash_ = hashlib.md5(f"{text}{number}".encode("utf-8")).hexdigest()
        print(hash_)
        if hash_.startswith("000000"):
            break
    return number


if __name__ == "__main__":
    data: str = Path("../input.txt").read_text().strip()
    print(f"{data=}")

    print(part_one(text=data))
    print(part_two(text=data))
