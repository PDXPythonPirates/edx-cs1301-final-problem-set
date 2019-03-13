# -----------------------------------------------------------
# In this problem, we're going to explore a little of how
# game AI works. We'll do this with a simple problem: building
# an agent to play the popular card game Blackjack.
#
# Blackjack is a card game played with a standard 52-card
# deck. Suits do not matter in Blackjack, and so we'll just
# use letters to indicate the different cards: A, 2, 3, 4, 5,
# 6, 7, 8, 9, 10, J, Q, K.
#
# The goal of Blackjack is to get as close to 21 points as
# possible without going higher. Each of the thirteen cards
# above has a point total attached: the numerals are worth
# their given value (2 points for 2, 7 points for 7, etc.).
# J, Q, and K are worth 10 points. A is worth either 1 or 11
# points, whichever is better for the player.
#
# At any time, the player has some number of cards in their
# hand. They must then make a decision of whether to Hit or
# Stay. Hit means they request an additional card, Stay means
# they stop with their current total. Players generally try
# to Hit until it is likely that another card will push them
# over 21. For example, if a player has a 5 and a 7, there is
# a relatively low chance that another card would push them
# over 21 (only J, Q, and K would do so, since 12 + 10 = 22).
# On the other hand, if they have a 5, a 6, and a 7, they will
# likely stay because any card above 3 will push them over 21
# points.
#
# The specific goal in Blackjack is to get closer to 21 than
# the dealer. Dealers must follow a set of prescribed rules
# for when to Hit and Stay. These are the rules we'll use for
# our Blackjack-playing AI.
#
# The rules are:
#
# - The dealer must Hit if their total is below 17.
# - The dealer must Stay as soon as their total is 17 or
#   higher.
# - An Ace (A) should be counted as 11 if it puts the
#   dealer between 17 and 21 points. If it puts them over
#   21, though, it should be counted as 1.
#
# For example, imagine the dealer's first cards are A and 3.
# Their point total is either 4 or 14, both below 17, so they
# Hit. The next card is a 9. If we count the A as 11, then
# their total is now 23 (11 + 3 + 9), and so we count the
# A as 1. Their total is 13, and so they Hit again. The next
# card is a 7, so their total is 20, so they Stay.
#
# Write a function called next_move. next_move should have
# one parameter, a string. Each character of the string will
# be a card in the dealer's current hand, such as "AK" or
# "175". The function should return one of three strings:
#
# - "Hit" if the dealer should take another card.
# - "Stay" if the dealer should not take another card.
# - "Bust" if the sum is already over 21.
#
# Remember, your function is only responsible for playing
# one move at a time. Take in a string representing the
# current hand, return "Hit", "Stay", or "Bust".


# Add your code here!


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Hit, Hit, Stay, and Bust.
print(next_move("A3"))
print(next_move("A39"))
print(next_move("A397"))
print(next_move("A397K"))
