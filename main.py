from art import logo
from auxiliary import make_a_bid, clear_console, get_key_from_value
from auxiliary import get_winner

print(logo)
print('Welcome to the secret auction program')

end_of_game = False
bidders = {}

while not end_of_game:
    # Bidder has name and bid
    name, bid = make_a_bid()

    # Add the bidder's name and his bid to the dictionary
    bidders[name] = bid

    ans = input('Are there any other bidders? Type "yes" or "no".\n').lower()
    if ans == 'no':
        end_of_game = True
    else:
        clear_console()

winner_name, winner_bid = get_winner(bidders)
print(f'The winner is {winner_name} with '
      f'a bid of ${winner_bid}.')
