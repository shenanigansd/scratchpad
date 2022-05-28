import readline


def main():
    try:
        while True:
            s = input('>> ')
            print(s)
    except (EOFError, KeyboardInterrupt):
        print('\nShutting down...')


if __name__ == '__main__':
    main()
