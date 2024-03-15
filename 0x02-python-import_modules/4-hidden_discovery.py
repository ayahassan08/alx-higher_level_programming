#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    for number in dir(hidden_4):
        if number[:2] != "__":
            print(number)
