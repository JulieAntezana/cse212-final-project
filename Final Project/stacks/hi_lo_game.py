# Example Program Using Stacks

# Write a program using stacks to reverse a string.

"""
This program will reverse a string using stacks. For example “Racecar” should be reversed to “racecaR”.

For this program, we will do the following: 

1) Create an empty stack.
2) Push each character from the string to the stack, one at a time.
3) Pop each character from the stack and put it back to string, one at a time.

"""
 
# Function to create an empty stack.
# It initializes size of stack as 0
def createStack():
    stack=[]
    return stack
 
# Function to determine the size of the stack
def size(stack):
    return len(stack)
 
# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return True
 
# Function to add an item to stack .
# It increases size by 1
def push(stack,item):
    stack.append(item)

# Function to return the value of the item at the back of the stack.
def peek_stack(stack):
    if stack:
        return stack[-1]    # this will get the last element of stack
    else:
        return None
 
# Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): 
      return
    return stack.pop()
 
# A stack based function to reverse a string
def reverse(string):
    n = len(string)
     
    # Create a empty stack
    stack = createStack()
 
    # Push all characters of string to stack
    for i in range(0,n,1):
        push(stack,string[i])
 
    # Making the string empty since all
    #characters are saved in stack
    string=""
 
    # Pop all characters of string and
    # put them back to string
    for i in range(0,n,1):
        string+=pop(stack)
         
    return string
     
################################
#TEST 1
################################
string = "1 2 3 4 5 6 7"
string = reverse(string)
print("\nTest 1: Reversed string is " + string)
# Expected result: "Test 1: Reversed string is 7 6 5 4 3 2 1"

################################
#TEST 2
################################
string="wow mom civic racecar minim level radar rotator rotavator reverse"
string = reverse(string)
print("\nTest 2: Reversed string is " + string)
# Expected result:"Test 2: Reversed string is esrever rotavator rotator radar level minim racecar civic mom wow"

################################
#TEST 3
################################
string = "1 @ tenet & 3 + 4 = 7"
string = reverse(string)
print("\nTest 3: Reversed string is " + string)
# Expected result: "Test 3: Reversed string is 7 = 4 + 3 & tenet @ 1"

"""
Practice Exercise: The Hi Lo Game. 

In this exercise we will practice the use stacks to predict the winner of a simple card game with two players. The players use a deck of 36 cards. Each card has a number between 1 and 9. There are 4 sets of each number in the deck. In the game Player1 and Player2 are each presented with identical stacks of seven cards. 

For each round of the game, each player selects a card and shows it to the other player. The value of the two cards are compared. If the value is the same for both players, then both players remove their cards from their stacks and discard them. Otherwise, the player with the lower value card removes the card from their stack and discards it. The player with the higher value card keeps the card on their stack, and the round ends. The higer card will be selected again in the next round, and will continue to be selected until the other player runs out of cards or selects a card with an equal or higher value. The game ends when a player runs out of cards, and the other player is declared the winner.

Our program will take into account the differing strategies of the two players: Player1 selects cards from the top of their stack of cards. Player2 selects cards from the bottom of their stack of cards. Write the program to simulate these two strategies. Keep in mind that we are practising use of the stacks data structure functions only (no slice, dequeue or linked list functions). We will have to use our stack functions to assure that the correct card will be located at the back of the stack when the player shows their card. 

The program should do the following:

1) Create an empty stack for Player1.
2) One by one push all characters of string to Player1's stack.
3) Reverse the string for Player2.
4) Create an empty stack for Player2.
5) One by one push all characters of the reversed string to Player2's stack.
6) Create a while loop to start the game.
7) Assign a variable for each player and use the function to show their selected card. 
8) Create conditions that direct how to end the game.
9) Create conditions that compare the selected cards shown and direct what should happen as a result of the comparison.

"""
def hi_lo_game(string):
   n = len(string)

   # Create an empty stack for player1
   p1 = createStack()

   # Push all characters of string to stack for player1
   for i in range(0,n,1):
      push(p1,string[i])

   # Reverse the string for player2
   string2 = reverse(string)

   # Create an empty stack for player2
   p2 = createStack()

   # Push all characters of string to stack for player2
   for i in range(0,n,1):
      push(p2,string2[i])

   # Start the game loop
   while True:
      # Assign a variable to the function to select a card for Player1.
      p1_card = peek_stack(p1)

      # Assign a variable to the function to select a card for Player2.
      p2_card = peek_stack(p2)

      # Check length of stacks and provide conditions for ending the game.
      # Both players ran out of cards on the previous turn.
      if p1_card == None and p2_card == None:
         print("\nGame Over! Tie game.")
         return
      # Player1 runs out of cards, Player2 still has cards
      elif len(p1) == 0:
         if len(p2) > 0:
            print("\nGame Over! Player 2 wins.")
            return
      # Player2 runs out of cards, Player1 still has cards
      elif len(p2) == 0:
         if len(p1) > 0:
            print("\nGame Over! Player 1 wins.")
            return
      # Both players select the same card
      elif p1_card == p2_card:
         print(p1_card, p2_card)
         print("Round is a tie.")
         pop(p1)
         pop(p2)
      # Player1 selects card with higher value   
      elif p1_card > p2_card:
         print(p1_card, p2_card)
         print("Round goes to Player 1.")
         pop(p2)
      # Player2 selects card with higher value  
      elif p2_card > p1_card: 
         print(p1_card, p2_card)
         print("Round goes to Player 2.")
         pop(p1)
      
   

################################
#TEST 1
################################
print("\nTest 1 Game Results:")
string = "1234567"
test1 = hi_lo_game(string)
# Expected result: "Game Over! Player 1 wins."

################################
#TEST 2
################################
print("\nTest 2 Game Results:")
string = "9876543"
test2 = hi_lo_game(string)
# Expected result: "Game Over! Player 2 wins."

################################
#TEST 3
################################
print("\nTest 3 Game Results:")
string = "3275137"
test3 = hi_lo_game(string)
# Expected result: "Game Over! Player 1 wins."

################################
#TEST 4
################################
print("\nTest 4 Game Results:")
string = "1234321"
test4 = hi_lo_game(string)
# Expected result: Game Over! Tie game.

################################
#TEST 5
################################
print("\nTest 5 Game Results:")
string = "9886549"
test5 = hi_lo_game(string)
# Expected result: Game Over! Tie game.









