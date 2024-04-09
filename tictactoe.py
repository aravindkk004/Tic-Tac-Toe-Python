#displaying a board
def display_board(board):
    print("-------------")
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' | ')
    print("|-----------|")
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' | ')
    print("|-----------|")
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' | ')
    print("-------------")

#player deciding
def player_deciding():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input("Enter player1 choice (X or O): ")
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2,marker)

#choice filling
def position_for(player1,player2,test_board,marker):
    count=0
    while count<4:
        position1='a'
        position2='a'
        while position1 not in range(1,10):
            position1=int(input("Enter your choice1(1-9): "))
        test_board[position1]=player1
        display_board(test_board)
            
        if (test_board[1]==test_board[2]==test_board[3]==marker):
            return marker
            
        elif (test_board[4]==test_board[5]==test_board[6]==marker):
            return marker
                
        elif (test_board[7]==test_board[8]==test_board[9]==marker):
            return marker
        
        elif (test_board[1]==test_board[4]==test_board[7]==marker):
            return marker
            
        elif (test_board[2]==test_board[5]==test_board[8]==marker):
            return marker
                
        elif (test_board[3]==test_board[6]==test_board[9]==marker):
            return marker
            
        elif (test_board[3]==test_board[5]==test_board[7]==marker):
            return marker
            
        elif (test_board[1]==test_board[5]==test_board[9]==marker):
            return marker

        while position2 not in range(1,10):
                position2=int(input("Enter your choice2(1-9): "))
        test_board[position2]=player2
        display_board(test_board)
        if (test_board[1]==test_board[2]==test_board[3]==marker):
            return marker
            
        elif (test_board[4]==test_board[5]==test_board[6]==marker):
            return marker
                
        elif (test_board[7]==test_board[8]==test_board[9]==marker):
            return marker
        
        elif (test_board[1]==test_board[4]==test_board[7]==marker):
            return marker
            
        elif (test_board[2]==test_board[5]==test_board[8]==marker):
            return marker
                
        elif (test_board[3]==test_board[6]==test_board[9]==marker):
            return marker
        
        elif (test_board[3]==test_board[5]==test_board[7]==marker):
            return marker
            
        elif (test_board[1]==test_board[5]==test_board[9]==marker):
            return marker
        count+=1


              
def another_play(player1,player2,test_board,marker):
    choice=''
    while choice != 'Y' and choice!='N':
        choice = input("Do you want to play another time (Y or N):")
    if choice=='Y':
        position_for(player1,player2,test_board,marker)
    if choice=='N':
        print("Thank you for playing this game")
    
    
test_board=[' ']*10
print("\nWelcome to Tic Tac Toe game!, play and enjoy your game")

display_board(test_board)

player1,player2,marker = player_deciding()

print('Player 1 :',player1)
print('Player 2 :',player2)

result = position_for(player1,player2,test_board,marker)
print(result,'wins')
another_play(player1,player2,test_board,marker)



