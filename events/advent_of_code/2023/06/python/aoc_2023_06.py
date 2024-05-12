from dataclasses import dataclass
from itertools import starmap
from math import prod
from pathlib import Path


@dataclass(frozen=True)
class Race:
    time_allowed: int
    record_distance: int

    def count_possible_wins(self) -> int:
        return sum(
            1 for time in range(1, self.time_allowed) if (self.time_allowed - time) * time > self.record_distance
        )


@dataclass(frozen=True)
class Paper:
    races: list[Race]

    @classmethod
    def from_text(cls, text: str) -> "Paper":
        time_line, distance_line = text.strip().split("\n")
        times = [int(time) for time in time_line.split()[1:]]
        distances = [int(distance) for distance in distance_line.split()[1:]]
        return cls(races=list(starmap(Race, zip(times, distances, strict=False))))

    def count_possible_wins(self) -> int:
        return Race(
            time_allowed=int("".join(str(race.time_allowed) for race in self.races)),
            record_distance=int(
                "".join(str(race.record_distance) for race in self.races),
            ),
        ).count_possible_wins()


def part1(paper: Paper) -> int:
    return prod(race.count_possible_wins() for race in paper.races)


def part2(paper: Paper) -> int:
    return paper.count_possible_wins()


if __name__ == "__main__":
    raw_text = Path("../input.txt").read_text(encoding="locale")
    paper_ = Paper.from_text(raw_text)
    print(part1(paper_))
    print(part2(paper_))
