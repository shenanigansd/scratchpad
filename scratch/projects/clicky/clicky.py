import readline  # noqa: F401


def main() -> None:
    try:
        while True:
            s = input(">> ")
            print(s)
    except (EOFError, KeyboardInterrupt):
        print("\nShutting down...")


if __name__ == "__main__":
    main()
