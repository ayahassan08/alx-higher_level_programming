#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    result = 0
    for number in range(len(sys.argv) - 1):
        result += int(sys.argv[number + 1])
    print(result)
