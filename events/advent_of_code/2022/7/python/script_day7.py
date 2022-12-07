from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    name: str
    contents: dict[str, 'Folder' | File]


@dataclass
class FileSystem:
    contents: dict[str, Folder | File]

    def create_item_at_path(self, keypath: list[str], item: File | Folder) -> None:
        folder = self
        for path in keypath:
            next_folder = folder.contents.get(path)
            if next_folder is None:
                new_folder = Folder(path, {})
                folder.contents[new_folder.name] = new_folder
                next_folder = new_folder
            folder = next_folder
        folder.contents[item.name] = item

    # https://github.com/python/cpython/blob/3.11/Lib/os.py#L345
    def walk(self, top=None):
        if top is None:
            top = self
        folders = [item for item in top.contents.values() if isinstance(item, Folder)]
        files = [item for item in top.contents.values() if isinstance(item, File)]
        yield folders, files
        for folder in folders:
            yield from self.walk(folder)


def build_file_system(text: str) -> FileSystem:
    file_system = FileSystem({})

    current_folder = []
    for line in text.splitlines():
        match line.split():
            case ["$", "ls"]:
                pass
            case ["$", "cd", folder_name]:
                if folder_name == "/":
                    current_folder.clear()
                elif folder_name == "..":
                    current_folder.pop()
                else:
                    current_folder.append(folder_name)
            case ["dir", folder_name]:
                file_system.create_item_at_path(current_folder, Folder(folder_name, {}))
            case [file_size, file_name]:
                file_system.create_item_at_path(current_folder, File(file_name, int(file_size)))

    return file_system


def sum_folder_size(folder: Folder) -> int:
    total_size = 0
    total_size += sum(item.size for item in folder.contents.values() if isinstance(item, File))
    nested_folders = [item for item in folder.contents.values() if isinstance(item, Folder)]
    for folder in nested_folders:
        total_size += sum_folder_size(folder)
    return total_size


def size_all_folders(file_system: FileSystem) -> dict[str, int]:
    folder_sizes = {}
    for folders, files in file_system.walk():
        for folder in folders:
            folder_sizes[folder.name] = sum_folder_size(folder)
    return folder_sizes


def sum_folders_under_size(file_system: FileSystem, size: int) -> int:
    folder_sizes = list(size_all_folders(file_system).values())
    folder_sizes.append(sum(folder_sizes))
    return sum(folder_size for folder_size in folder_sizes if folder_size <= size)


def part_one(text: str) -> int:
    file_system = build_file_system(text)
    return sum_folders_under_size(file_system, 100000)


def part_two(text: str) -> int:
    return 0


if __name__ == "__main__":
    data = Path("../input.txt").read_text().strip()
    print(part_one(data))
    print(part_two(data))
