import time

def find_rows(board):
        rows = board.split("\n")
        for i, row in enumerate(rows):
            rows[i] = row.strip()
        return rows

def valid(rows, size, pieces):
        for row in rows:
            if (len(row) != size):
                return False
            for column in row:
                 if column != 'K' and column != '.' and not column in pieces:
                      return False
        return True
    
def find_king_pos(rows):
        for i, row in enumerate(rows):
            for j, column in enumerate(row):
                if column == 'K':
                    return (i, j)
        return False

def not_exceed_boundary(pos, size):
     if not pos[0] < size or not pos[1] < size or not pos[0] > -1 or not pos[1] > -1:
          return False
     return True

def check_attack_king(pos, size, pieces, piece, king_pos):
     if piece == 'P':
        for tuple in pieces[piece]:
            check_pos = (pos[0]+tuple[0], pos[1]+tuple[1])
            if not_exceed_boundary(check_pos, size):
                if check_pos == king_pos:
                    return True
     else:
        for tuple in pieces[piece]:
            check_pos = (pos[0]+tuple[0], pos[1]+tuple[1])
            while not_exceed_boundary(check_pos, size):
                 if check_pos == king_pos:
                      return True
                 check_pos = (check_pos[0]+tuple[0], check_pos[1]+tuple[1])
     return False

        
def checkmate(board):
    pieces = {
        'P': [(-1, -1), (-1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(0, -1), (0, 1), (-1, 0), (1, 0)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    }
    
    rows = find_rows(board)
    size = len(rows)
    king_pos = find_king_pos(rows)
    
    if not valid(rows, size, pieces) or king_pos == False:
        print("Error")
        return
    
    for i, row in enumerate(rows):
         for j, column in enumerate(row):
              if column in pieces:
                   if check_attack_king((i, j), size, pieces, column, king_pos):
                        print("Success")
                        return
    print("Fail")

    