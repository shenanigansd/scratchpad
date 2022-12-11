from collections import defaultdict
from dataclasses import asdict, dataclass
from os import chdir
from pathlib import Path
from subprocess import CompletedProcess, run
from time import perf_counter_ns

import pandas
import toml


@dataclass(frozen=True, slots=True)
class Result:
    language: str
    run_time: float
    part1: int | str
    part2: int | str


def run_subprocess(path: str | None, command_list: list[str]) -> tuple[float, CompletedProcess]:
    time_started = perf_counter_ns()
    if path is not None:
        chdir(path)
    result = run(command_list, capture_output=True)
    time_completed = perf_counter_ns()
    time_delta = time_completed - time_started
    if path is not None:
        dirs = path.count("/") + 1
        chdir("../" * dirs)
    return time_delta, result


def run_python(path: str) -> tuple[float, CompletedProcess]:
    path, file = path.rsplit("/", maxsplit=1)
    return run_subprocess(path, ["python", file])


def run_rust(year: int, day: int) -> tuple[float, CompletedProcess]:
    return run_subprocess(None, ["cargo", "run", "--quiet", "--bin", f"aoc-{year}-{day}"])


def get_rust_projects() -> list[str]:
    data = toml.loads(Path("Cargo.toml").read_text())
    return [project for project in data["workspace"]["members"] if "advent_of_code" in project]


def runner() -> None:
    chdir("../../")

    results: dict[tuple[int, int], list[Result]] = defaultdict(list)

    for python_script in Path(".").glob("**/script_*_*.py"):
        print(f"running {python_script=}")
        run_time, process_result = run_python(str(python_script))
        output: list[str] = process_result.stdout.decode().split("\n")
        output.remove("")
        _, year, day = python_script.stem.split("_")
        results[(year, day)].append(
            Result(
                language="Python",
                run_time=run_time,
                part1=output[0],
                part2=output[1],
            )
        )

    for rust_project in get_rust_projects():
        print(f"running {rust_project=}")
        _, _, year, day, _ = rust_project.split("/")
        run_time, process_result = run_rust(year, day)
        output: list[str] = process_result.stdout.decode().split("\n")
        output.remove("")
        results[(year, day)].append(
            Result(
                language="Rust",
                run_time=run_time,
                part1=output[0],
                part2=output[1],
            )
        )

    for key, values in results.items():
        print(key)
        data_frame = pandas.DataFrame([asdict(value) for value in values])
        print(data_frame)


if __name__ == "__main__":
    runner()
