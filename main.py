from art import logo
from auxiliary import make_a_bid, clear_console, get_key_from_value

print(logo)
print('Welcome to the secret auction program')

end_of_game = False
bidders = {}

while not end_of_game:
    # Bidder has name and bid
    bidder = make_a_bid()

    bidders.update(bidder)

    ans = input('Are there any other bidders? Type "yes" or "no".\n').lower()
    if ans == 'no':
        end_of_game = True
    else:
        clear_console()



