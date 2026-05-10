# Warmup projects exerscises
sos = [[ ' ' for i in range(3)] for i in range (3)]
dict1 = {'top left': 0, 'top middle': 1, 'top right': 2,
         'middle left': 3, 'middle middle': 4, 'middle right': 5,
         'bottom left': 6, 'bottom middle': 7, 'bottom right': 8}


def available_positions(dict1):
  for key, value in dict1.items():
    print(f'Enter {value} for {key} position')


def display_board(sos):
  for i in sos:
    print(i)


def find_key(dict1, value):
  for key, val in dict1.items():
    if val == value:
      return key
  return "Key not found"


def update_list(lst, position, value):
  lst[position//3][position%3] = value
  return lst

def winner_check(lst):
  for i in lst:
    if i[0] == i[1] == i[2] != ' ':
      return True
  for i in range(3):
    if lst[0][i] == lst[1][i] == lst[2][i] != ' ':
      return True
  if lst[0][0] == lst[1][1] == lst[2][2] != ' ':
    return True
  if lst[0][2] == lst[1][1] == lst[2][0] != ' ':
    return True
  return False



# algorithm
'''
get input from user
only available positions should be allowed
check if the input is valid
if valid, update the board
update the list of available positions
check if the game is won or tied

'''
# [0 1 2 3 4 5 6 7 8]
# [00 01 01 10 11 12 20 21 22]
# position_mapping = {0: (0, 0), 1: (0, 1), 2: (0, 2),
#                     3: (1, 0), 4: (1, 1), 5: (1, 2),
#                     6: (2, 0), 7: (2, 1), 8: (2, 2)}
for i in range(9):
  display_board(sos)
  available_positions(dict1)
  position = (input("Enter your position: "))
  while (position.isdigit() == False) :
    print("Incorrect type. Please enter a valid number.")
    position = (input("Enter your position: "))
  while (int(position) not in dict1.values()) :
    print("Invalid position. Please choose an available position.")
    position = (input("Enter your position: "))
  position = int(position)
  if i%2 == 0:
    update_list(sos, int(position), 'X')
  else:
    update_list(sos, position, 'O')
  del dict1[find_key(dict1, position)]
  if winner_check(sos):
    display_board(sos)
    print(f'Player {"X" if i%2 == 0 else "O"} wins!')
    break


