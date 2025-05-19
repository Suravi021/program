
def print_state(state):
    for row in state:
        row_str = ""
        for num in row:
            row_str += str(num) + " "
        print(row_str)
    print()

# Function to find the blank tile in the puzzle

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state,direction):
  i,j=find_blank(state)
  new_state = []
  for row in state:
    new_row = row[:]
    new_state.append(new_row)

  if direction=="up":
    if i > 0:
      new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
      return new_state
    else:
      return None

  if direction=="down":
    if i < 2:
      new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
      return new_state
    else:
      return None

  if direction=="left":
    if j > 0:
      new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
      return new_state
    else:
      return None

  if direction=="right":
    if j < 2:
      new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
      return new_state
    else:
      return None

   
def calculate_heuristic(state, goal_state):
    # Simple heuristic: count the number of misplaced tiles
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h




def a_star(initial_state, goal_state):
    OPEN = [(calculate_heuristic(initial_state, goal_state), 0, initial_state)]
    CLOSED = set()
    found=False
    while OPEN:
        f, g, current_state = min(OPEN)
        OPEN.remove((f, g, current_state))
        CLOSED.add(tuple(map(tuple, current_state)))


        print_state(current_state)


        if current_state == goal_state:
            print("Solution found!")
            found=True
            break

        steps=["up","down","left","right"]
        successors = [move(current_state,direction) for direction in steps]

        suc = []
        for s in successors:
            if s:
                if (tuple(map(tuple, s)) not in CLOSED):
                    suc.append(s)


        for successor in suc:
            h = calculate_heuristic(successor, goal_state)
            g_successor = g + 1
            f_successor = g_successor + h


            if (f_successor, g_successor, successor) not in OPEN:
                OPEN.append((f_successor, g_successor, successor))
    if found==False:
        print("Solution not found")

# Updated example usage with the provided input
initial_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

goal_state = [
    [1, 2, 0],
    [8, 6, 3],
    [7, 5, 4]
]

a_star(initial_state, goal_state)

