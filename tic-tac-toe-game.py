print('\n\nWelcome to Tic Toe game\n'+'\n')

print('Available positions for marking\n\n')
board_place=['0','1','2','3','4','5','6','7','8']


board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
 
def display_board(board):
    print(board[0]+' | '+board[1]+' | '+board[2] +'\n----------' )
    print(board[3]+' | '+board[4]+' | '+board[5] + '\n----------' )
    print(board[6]+' | '+board[7]+' | '+board[8] + '\n----------' )
    
display_board(board_place)



def win_check(num):
    if board[0:3]==[num,num,num]:
        
        return True
        
    elif board[3:6]==[num,num,num]:
        
        return True
        
    elif board[6:9]==[num,num,num]:
        
        return True
        
    elif board[0]==num and board[3]==num and board [6]==num:
        
        return True
        
    elif board[2]==num and board[5]==num and board [8]==num:
        
        return True
        
    elif board[2]==num and board[4]==num and board [6]==num:
        
        return True
        
    elif board[0]==num and board[4]==num and board [8]==num:
       
        return True
    
    elif board[1]==num and board[4]==num and board [7]==num:
        
        return True
               
#def result():
    #print('GAME IS OVER PLEASE RETRY')
       

def player_input():
    
    index=0
    p1mark=input('Enter marker (X or O) of player 1 : ')
    
    p1mark=p1mark.upper()
    player1 = True
    while index<=8:      
        while player1==True:
            if p1mark=='X' or p1mark=='O':                
                player_1_turn=int(input('Enter position for player 1 \n'))
                if player_1_turn in range(0,9):
                    if board[player_1_turn]==' ':
                     board[player_1_turn]=p1mark
                     index+=1
                     if win_check(p1mark)==True:
                         print('Player 1 is Winner')
                         index=9
                         #result()
                         
                         
                     player1=False
                     display_board(board)                     
                    else:
                         print('position already placed')
                else:
                     print('position exceeds')
                     player1=True
                    
                
            else:
                 print('Marker invalid')
                 player_input()
                
            
             
          
             
             
        while player1==False and index<=8:
            if p1mark=='X':
                p2mark='O'
            else:
                p2mark='X'
            if p2mark=='X' or p2mark=='O':
                player_2_turn=int(input('Enter position for player 2\n '))
                if player_1_turn in range(0,9):
                    if board[player_2_turn]==' ':
                      board[player_2_turn]=p2mark
                      index+=1
                      if win_check(p2mark)==True:
                         print('Player 2 is Winner')
                         index=9
                         #result()
                         
                      player1=True
                      display_board(board) 
                    else:
                         print('position already placed')
                else:
                     print('position exceeds')
                     player1=False
                
    else:
       print('Game is Over Please Retry')
       
                 
                 
player_input()
