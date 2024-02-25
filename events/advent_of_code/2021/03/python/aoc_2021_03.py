def get_rates(values: list[str]) -> tuple[str, str]:
    gamma_rate = ""
    epsilon_rate = ""

    item_length = len(values[0])
    for i in range(item_length):
        bits = [value[i] for value in values]
        zeros = bits.count("0")
        ones = bits.count("1")

        if ones > zeros:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    return gamma_rate, epsilon_rate


def part_one(values: list[str]) -> int:
    gamma_rate, epsilon_rate = get_rates(values)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_two(values: list[str]) -> int:
    length_index = 0
    results = values.copy()
    while len(results) > 1:
        bits = [result[length_index] for result in results]
        zeros = bits.count("0")
        ones = bits.count("1")

        new_results = []
        [
            new_results.append(result)
            for result in results
            if result[length_index] == ("1" if ones >= zeros else "0")
        ]
        results = new_results

        length_index += 1
    oxygen_generator_rating = results[0]

    length_index = 0
    results = values.copy()
    while len(results) > 1:
        bits = [result[length_index] for result in results]
        zeros = bits.count("0")
        ones = bits.count("1")

        new_results = []
        [
            new_results.append(result)
            for result in results
            if result[length_index] == ("0" if zeros <= ones else "1")
        ]
        results = new_results

        length_index += 1
    co2_scrubber_rating = results[0]

    return int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)


if __name__ == "__main__":
    values_: list[str] = [
        row.strip() for row in open("../input.txt", encoding="locale")
    ]
    print(part_one(values=values_))
    print(part_two(values=values_))
