def who_won(game_board: list):
    player1 = 0
    player2 = 0 

    for row in game_board:
        for element in row:
            if element== 1:
                player1+=1
            elif element == 2:
                player2+=1
        
    if player1>=0 and player2>=0:
        if player1 > player2:
            return (1)
        elif player2 > player1 :
            return (2)
        elif player1 == player2:
            return (0)
if __name__=="__main__":
    game = [[2, 2, 2],
            [0, 1, 2],
            [0, 0, 1]]
    
    print(who_won(game))