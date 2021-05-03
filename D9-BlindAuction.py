import D9ArtBlindAuction
import os #to clear the terminal



print('\n\t\t Blind Action program')

bids = {} #Dictionary

bidding_finised = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record :
        bid_amount = bidding_record[bidder] #corrently bid in the loop
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f'The winner is {winner} with a bid of $ {highest_bid} ')


while not bidding_finised:
    print(f'{D9ArtBlindAuction.logo}\n')
    name = input('whats is yout name 👀 ?  ')
    price = int(input('What is yout bid 💸 ?  $'))

    bids[name] = price

    answerBidding = input('Any other bidders?  [yes]/ [no] \t').lower()
    if answerBidding == 'no':
        bidding_finised = True # break the while statement
        find_highest_bidder(bids) #pass the dictionary as a parameter
    elif answerBidding == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')  

