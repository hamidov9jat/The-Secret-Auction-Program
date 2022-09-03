import os


def clear_console():
    os.system('cls')


def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def make_a_bid():
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    return name, bid


def get_winner(bidders: dict):
    max_bid = max(bidders.values())
    name = get_key_from_value(bidders, max_bid)
    return name, max_bid


if __name__ == '__main__':
    print('hello')
    clear_console()
