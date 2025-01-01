board = [['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'N', 'B', 'k', 'q', 'b', 'n', 'r']]    
for row in board:
    print(" ".join(row))
color=1
while True:    
    if color==1: #white
        print("White's turn")
        while True: #coordinate of piece
            inst_pos=input('Enter the coordinates of piece(ex e4): ')
            row_ins=int(inst_pos[-1])-1
            column_ins=ord(inst_pos[0])-97
            piece=board[row_ins][column_ins]
            if piece!=' ' and piece.isupper()==True:
                break
            print('Bro,there is nothing to pick,check your coordinates')
        print('You have picked',piece)
        if piece=='P': #Pawn white
            while True: 
                end_pos=input('Enter the end position of Pawn(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end] 
                if (end_coord==' ' and column_end==column_ins and ((row_end-row_ins==1) or (row_ins==1 and (row_end-row_ins)<=2))) or (end_coord.islower()==True and (row_end-row_ins)==1 and abs(column_end-column_ins)==1): #Pawn properties
                    break
                print('You can move pawn only forward by 1 tile(2 if first move)')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            if row_end==7:
                board[row_end][column_end]=input('Promote your pawn(R,N,B,Q)').upper()
            for row in board:
                print(" ".join(row))
        elif piece=='R': #Rook white
            while True:
                end_pos=input('Enter the end position of Rook(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                tile_vert_1=[]
                tile_horiz_1=[]
                tile_vert_2=[]
                tile_horiz_2=[]
                for col in range(row_ins+1,row_end): #not allow to jump over other pieces in vertical
                    tile_vert_1.append(board[col][column_end])
                space=tile_vert_1.count(' ')
                for row in range(column_ins+1,column_end): #not allow to jump over other pieces in horizontal
                    tile_horiz_1.append(board[row_end][row])
                space_2=tile_horiz_1.count(' ')
                for col_2 in range(row_ins+1,row_end,-1):
                    tile_vert_2.append(board[col_2][column_end])
                space_3=tile_vert_2.count(' ')
                for row_2 in range(column_ins,column_end,-1):
                    tile_horiz_2.append(board[row_end][row_2])
                space_4=tile_horiz_2.count(' ')
                if (end_coord==' ' or end_coord.islower()==True) and (column_end==column_ins or row_ins==row_end) and space==len(tile_vert_1) and space_2==len(tile_horiz_1) and space_3==len(tile_vert_2) and space_4==len(tile_horiz_2): #Rook properties
                    break
                print('Rook moves and eats only in vertical and horizontal and cannot jump over')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='N': #Knight white
            while True:    
                end_pos=input('Enter the end position of Knight(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                if (end_coord==' ' or end_coord.islower()==True) and ((abs(row_end-row_ins)==2 and abs(column_end-column_ins)==1) or (abs(row_end-row_ins)==1 and abs(column_end-column_ins)==2)): #knight properties
                    break
                print("Knight moves in 'Г' path and can jump")
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='B': #Bishop white
            while True:    
                end_pos=input('Enter the end position of Bishop(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                bishop_vert_1,space=[],0
                bishop_vert_2,space_2=[],0
                bishop_horz_1,space_3=[],0
                bishop_horz_2,space_4=[],0
                if column_ins<column_end and row_ins<row_end:   
                    for dio_1 in range(row_ins+1,row_end): #not allow to jump over other pieces in diagonal
                        bishop_vert_1.append(board[dio_1][dio_1])
                    space=bishop_vert_1.count(' ')
                elif column_ins>column_end and row_ins>row_end:    
                    for dio_2 in range(column_ins-1,column_end,-1): 
                        bishop_horz_1.append(board[dio_2][dio_2])
                    space_2=bishop_horz_1.count(' ')
                elif column_ins>column_end and row_ins<row_end:    
                    for dio_3 in range(row_end-1,row_ins,-1):
                        bishop_vert_2.append(board[dio_3][7-dio_3])
                    space_3=bishop_vert_2.count(' ')
                elif column_ins<column_end and row_ins>row_end:    
                    for dio_4 in range(column_end-1,column_ins,-1):
                        bishop_horz_2.append(board[7-dio_4][dio_4])
                    space_4=bishop_horz_2.count(' ')
                if (end_coord==' ' or end_coord.islower()==True) and abs(column_end-column_ins)==abs(row_end-row_ins) and space==len(bishop_vert_1) and space_2==len(bishop_horz_1) and space_3==len(bishop_vert_2) and space_4==len(bishop_horz_2): #Bishop properties
                    break
                print('Bishop moves in diagonal and cannot jump over other pieces')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='Q': #Queen white
            while True:    
                end_pos=input('Enter the end position of Queen(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                tile_vert_1=[]
                tile_horiz_1=[]
                tile_vert_2=[]
                tile_horiz_2=[]
                bishop_vert_1=[]
                bishop_vert_2=[]
                bishop_horz_1=[]
                bishop_horz_2=[]
                for col in range(row_ins+1,row_end): #not allow to jump over other pieces in vertical
                    tile_vert_1.append(board[col][column_end])
                space=tile_vert_1.count(' ')
                for row in range(column_ins+1,column_end): #not allow to jump over other pieces in horizontal
                    tile_horiz_1.append(board[row_end][row])
                space_2=tile_horiz_1.count(' ')
                for col_2 in range(row_ins+1,row_end,-1):
                    tile_vert_2.append(board[col_2][column_end])
                space_3=tile_vert_2.count(' ')
                for row_2 in range(column_ins,column_end,-1):
                    tile_horiz_2.append(board[row_end][row_2])
                space_4=tile_horiz_2.count(' ')
                for dio_1 in range(row_ins+1,row_end): #not allow to jump over other pieces in diagonal
                    bishop_vert_1.append(board[dio_1][dio_1])
                space=bishop_vert_1.count(' ')
                for dio_2 in range(column_ins+1,column_end): 
                    bishop_horz_1.append(board[dio_2][dio_2])
                space_2=bishop_horz_1.count(' ')
                for dio_3 in range(row_ins+1,row_end,-1):
                    bishop_vert_2.append(board[7-dio_3][dio_3])
                space_3=bishop_vert_2.count(' ')
                for dio_4 in range(column_ins,column_end,-1):
                    bishop_horz_2.append(board[dio_4][7-dio_4])
                space_4=bishop_horz_2.count(' ')
                if (end_coord==' ' or end_coord.islower()==True) or (column_end==column_ins or row_ins==row_end) or abs(column_end-column_ins)==abs(row_end-row_ins) : #Queen properties
                    break
                print('Queen goes like rook+bishop :3')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='K':
            while True:    
                end_pos=input('Enter the end position of KING(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]     
                if (end_coord==' ' or end_coord.islower()==True) or (abs(column_end-column_ins)==1 and abs(row_ins-row_end)==1) or (board[0][3]=='K' and ((board[0][4]==' ' and board[0][5]==' ' and board[0][6]==' ' and board[0][7]=='R') or (board[0][0]=='R' and board[0][1]=='' and board[0][2]==' '))): #KING properties
                    break
                print('It is KING,wish you know how it moves')
            if end_coord==board[0][5]:
                board[0][7]=' '
                board[0][5]='K'
                board[0][4]='R'
                board[0][3]=' '
            elif end_coord==board[0][1]:
                board[0][0]=' '
                board[0][1]='K'
                board[0][2]='R'
                board[0][3]=' '
            for row in board:
                print(" ".join(row)) 
        color=color*(-1)
    for row in board:
        king=''.join(row)
    Check_mate=king.find('k')
    if Check_mate==-1:
        break
    elif color==(-1): #Black
        print("Black's turn") 
        while True:
            inst_pos=input('Enter the coordinates of piece(ex e4): ')
            row_ins=int(inst_pos[-1])-1
            column_ins=ord(inst_pos[0])-97
            piece=board[row_ins][column_ins]
            if piece!=' ' and piece.islower()==True:
                break
            print('Bro,there is nothing to pick,check your coordinates')
        print('You have picked',piece)
        if piece=='p': #Pawn black
            while True: 
                end_pos=input('Enter the end position of Pawn(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end] 
                if (end_coord==' ' and column_end==column_ins and ((row_end-row_ins==-1) or (row_ins==6 and (row_ins-row_end)<=2))) or (end_coord.isupper()==True and (row_end-row_ins)==-1 and abs(column_end-column_ins)==1): #Pawn properties
                    break
                print('You can move pawn only forward by 1 tile(2 if first move)')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            if row_end==0:
                board[row_end][column_end]=input('Promote your pawn(R,N,B,Q)').lower()
            for row in board:
                print(" ".join(row))
        elif piece=='r': #Rook black
            while True:
                end_pos=input('Enter the end position of Rook(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                tile=[]
                tile_2=[]
                for col in range(row_ins+1,row_end): #not allow to jump over other pieces in vertical
                    tile.append(board[col][column_end])
                space=tile.count(' ')
                for row_2 in range(column_ins+1,column_end): #not allow to jump over other pieces in horizontal
                    tile_2.append(board[row_end][row_2])
                space_2=tile_2.count(' ')
                if (end_coord==' ' or end_coord.islower()==True) and (column_end==column_ins or row_ins==row_end) and space==len(tile) and space_2==len(tile_2): #Rook properties
                    break
                print('Rook moves and eats only in vertical and horizontal')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='n': #Knight black
            while True:    
                end_pos=input('Enter the end position of Knight(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                if end_coord==' ' and end_coord.isupper()==True and ((abs(row_end-row_ins)==2 and abs(column_end-column_ins)==1) or (abs(row_end-row_ins)==1 and abs(column_end-column_ins)==2)): #Knight properties
                    break
                print("Knight moves in 'Г' path and can jump")
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='b': #bishop black
            while True:    
                end_pos=input('Enter the end position of Bishop(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                if (end_coord==' ' or end_coord.isupper()==True) and abs(column_end-column_ins)==abs(row_end-row_ins): #Bishop properties
                    break
                print('Bishop moves in diagonal and cannot jump over other pieces')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='q': #Queen black
            while True:    
                end_pos=input('Enter the end position of Bishop(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]
                tile_vert_1=[]
                tile_horiz_1=[]
                tile_vert_2=[]
                tile_horiz_2=[]
                bishop_vert_1=[]
                bishop_vert_2=[]
                bishop_horz_1=[]
                bishop_horz_2=[]
                for col in range(row_ins+1,row_end): #not allow to jump over other pieces in vertical
                    tile_vert_1.append(board[col][column_end])
                space=tile_vert_1.count(' ')
                for row in range(column_ins+1,column_end): #not allow to jump over other pieces in horizontal
                    tile_horiz_1.append(board[row_end][row])
                space_2=tile_horiz_1.count(' ')
                for col_2 in range(row_ins+1,row_end,-1):
                    tile_vert_2.append(board[col_2][column_end])
                space_3=tile_vert_2.count(' ')
                for row_2 in range(column_ins,column_end,-1):
                    tile_horiz_2.append(board[row_end][row_2])
                space_4=tile_horiz_2.count(' ')
                for dio_1 in range(row_ins+1,row_end): #not allow to jump over other pieces in diagonal
                    bishop_vert_1.append(board[dio_1][dio_1])
                space=bishop_vert_1.count(' ')
                for dio_2 in range(column_ins+1,column_end): 
                    bishop_horz_1.append(board[dio_2][dio_2])
                space_2=bishop_horz_1.count(' ')
                for dio_3 in range(row_ins+1,row_end,-1):
                    bishop_vert_2.append(board[7-dio_3][dio_3])
                space_3=bishop_vert_2.count(' ')
                for dio_4 in range(column_ins,column_end,-1):
                    bishop_horz_2.append(board[dio_4][7-dio_4])
                space_4=bishop_horz_2.count(' ')
                if (end_coord==' ' or end_coord.isupper()==True) and (column_end==column_ins or row_ins==row_end) and abs(column_end-column_ins)==abs(row_end-row_ins) and space==len(tile_vert_1) and space_2==len(tile_horiz_1) and space_3==len(tile_vert_2) and space_4==len(tile_horiz_2) and space==len(bishop_vert_1) and space_2==len(bishop_horz_1) and space_3==len(bishop_vert_2) and space_4==len(bishop_horz_2): #f Queen properties
                    break
                print('Queen goes like rook+bishop :3')
            board[row_ins][column_ins]=' '
            board[row_end][column_end]=piece
            for row in board:
                print(" ".join(row))
        elif piece=='k':
            while True:    
                end_pos=input('Enter the end position of KING(ex e5): ')
                row_end=int(end_pos[-1])-1
                column_end=ord(end_pos[0])-97
                end_coord=board[row_end][column_end]     
                if (end_coord==' ' or end_coord.isupper()==True) or (abs(column_end-column_ins)==1 and abs(row_ins-row_end)==1) or (board[7][3]=='k' and ((board[7][4]==' ' and board[7][5]==' ' and board[7][6]==' ' and board[7][7]=='r') or (board[7][0]=='r' and board[7][1]==' ' and board[7][2]==' '))): #KING properties
                    break
                print('It is KING,wish you know how it moves')
            if end_coord==board[7][5]:
                board[7][7]=' '
                board[7][5]='k'
                board[7][4]='r'
                board[7][3]=' '
            elif end_coord==board[7][1]:
                board[7][0]=' '
                board[7][1]='k'
                board[7][2]='r'
                board[7][3]=' '
            for row in board:
                print(" ".join(row)) 
        color=color*(-1)
    for row in board:
        king=''.join(row)
    Check_mate_black=king.find('k')
    if Check_mate_black==-1:
        break
if Check_mate==-1:
    print('Congrats, Whites won')
elif Check_mate_black==-1:
    print('Congrats, Blacks won')

