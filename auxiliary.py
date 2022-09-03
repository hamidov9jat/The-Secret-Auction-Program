import os


def clear_console():
    print(os.name)
    os.system('cls')


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


if __name__ == '__main__':
    print('hello')
    clear_console()
