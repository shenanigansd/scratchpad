from script_2022_07 import (
    File,
    FileSystem,
    Folder,
    build_file_system,
    find_smallest_possible_folder_to_delete,
    size_all_folders,
    size_entire_file_system,
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
                "f": File("f", 29_116),
                "g": File("g", 2_557),
                "h.lst": File("h.lst", 62_596),
            },
        ),
        "b.txt": File("b.txt", 14_848_514),
        "c.dat": File("c.dat", 8_504_156),
        "d": Folder(
            "d",
            {
                "j": File("j", 4_060_174),
                "d.log": File("d.log", 8_033_020),
                "d.ext": File("d.ext", 5_626_152),
                "k": File("k", 7_214_296),
            },
        ),
    }
)


def test_build_file_system() -> None:
    assert build_file_system(EXAMPLE_INPUT) == EXAMPLE_OUTPUT


def test_size_all_folders() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert size_all_folders(file_system) == [584, 94_853, 24_933_642]


def test_sum_folders_under_size() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert sum_folders_under_size(file_system, 100_000) == 95_437


def test_size_entire_file_system() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert size_entire_file_system(file_system) == 48_381_165


def test_find_smallest_possible_folder_to_delete() -> None:
    file_system = build_file_system(EXAMPLE_INPUT)
    assert find_smallest_possible_folder_to_delete(file_system) == 24_933_642
