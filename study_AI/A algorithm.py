import queue

class State:
    def __init__(self, board, goal, depth=0):
        self.board = board
        self.depth = depth
        self.goal = goal

    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)
    
    def expand(self, moves):
        result=[]
        i = self.board.index(0)
        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i-1, moves))
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i-3, moves))
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i+1, moves))
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i+3, moves))
        return result
    
    def f(self):
        return self.h()+self.g()
    
    def h(self):
        score = 0
        for i in range(9):
            if self.board[i] != 0 and self.board[i] != self.goal[i]:
                score += 1
        return score
    
    def g(self):
        return self.depth
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __ne__(self, other):
        return self.board != other.board
    
    def __lt__(self, other):
        return self.f() < other.f()
    
    def __gt__(self, other):
        return self.f() > other.f()
    
    def __str__(self):
        return f"f(n)={self.f()} h(n)={self.h()} g(n)={self.g()}\n"+\
        str(self.board[:3])+"\n"+\
        str(self.board[3:6])+"\n"+\
        str(self.board[6:])+"\n"
    
puzzle = [2, 8, 3,
          1, 6, 4,
          7, 0, 5]
    
goal = [1, 2, 3,
        8, 0, 4,
        7, 6, 5]
    
open_queue = queue.PriorityQueue()
open_queue.put(State(puzzle, goal))

closed_queue = [ ]
depth = 0
count = 0

while not open_queue.empty():
    current = open_queue.get()
    count += 1
    print(count)
    print(current)
    if current.board == goal:
        print("탐색 성공")
        break
    depth = current.depth+1
    for state in current.expand(depth):
        if state not in closed_queue and state not in open_queue.queue:
            open_queue.put(state)
    closed_queue.append(current)
else:
    print("탐색 실패")