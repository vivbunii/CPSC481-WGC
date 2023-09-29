# Programming Project 1 CPSC481
# Edited by Vivian Cao, Randell Lapid, Angarag Gansukh
# Date: 09/28/2023
# Description: This program solves the Wolf, Goat, and Cabbage problem using the uninformed search algorithm, Breadth-First Search (BFS) and Depth-First Search (DFS).

from search import depth_first_graph_search, breadth_first_graph_search
from search import Problem, Node

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=frozenset()):
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        items_on_left = state - frozenset({'F'})

        for item in items_on_left:
            new_state = state - frozenset([item, 'F'])  # Move the item and the farmer
            if self.is_valid_state(new_state):
                actions.append((item, 'F'))  # Action is represented as a tuple with the moved item and the farmer
        return actions

    def result(self, state, action):
        item = action[0]  # Item to move
        new_state = state - frozenset([item, 'F'])  # Move the item and the farmer
        return new_state

    def goal_test(self, state):
        return state == self.goal

    def is_valid_state(self, state):
        # Check if the state is valid (wolf and goat or goat and cabbage are not left alone)
        if ('W' in state and 'G' in state and 'C' not in state) or ('G' in state and 'C' in state and 'W' not in state):
            return False
        return True

def print_solution(solution, method):
    print(f"{method} Solution: {solution}")

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    
    # Depth-first search
    dfs_solution = depth_first_graph_search(wgc).solution()
    print_solution(dfs_solution, "DFS")
    
    # Breadth-first search
    bfs_solution = breadth_first_graph_search(wgc).solution()
    print_solution(bfs_solution, "BFS")
