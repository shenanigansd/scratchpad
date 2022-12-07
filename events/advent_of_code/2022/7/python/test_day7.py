from script_day7 import (
    File,
    FileSystem,
    Folder,
    build_file_system,
    size_all_folders,
    sum_folders_under_size,
)

EXAMPLE_INPUT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

EXAMPLE_OUTPUT = FileSystem(
    {
        "a": Folder(
            "a",
            {
                "e": Folder("e", {"i": File("i", 584)}),
                "f": File("f", 29116),
                "g": File("g", 2557),
                "h.lst": File("h.lst", 62596),
            },
        ),
        "b.txt": File("b.txt", 14848514),
        "c.dat": File("c.dat", 8504156),
        "d": Folder(
            "d",
            {
                "j": File("j", 4060174),
                "d.log": File("d.log", 8033020),
                "d.ext": File("d.ext", 5626152),
                "k": File("k", 7214296),
            },
        ),
    }
)


def test_build_file_system() -> None:
    assert build_file_system(EXAMPLE_INPUT) == EXAMPLE_OUTPUT


def test_size_all_folders() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert size_all_folders(file_system) == {"a": 94853, "d": 24933642, "e": 584}


def test_sum_folders_under_size() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert sum_folders_under_size(file_system, 100000) == 95437
