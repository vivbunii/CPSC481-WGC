# Programming Project 1 CPSC481
# Edited by Vivian Cao, Randell Lapid, Angarag Gansukh
# Date: 09/28/2023
# Description: This program solves the Wolf, Goat, and Cabbage problem using the uninformed search algorithm, Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms.

from search import depth_first_graph_search, breadth_first_graph_search
from search import Problem

class WolfGoatCabbage(Problem):
    def __init__(self):
        initial = frozenset({'F', 'W', 'G', 'C'}) # Initializes the problem with the initial and goal states
        goal = frozenset({})
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        left_bank = state # Items currently on the left bank
        right_bank = self.initial - state # Items currently on the right bank
        
        # Determine which bank the farmer is on, and generate actions accordingly
        if 'F' in left_bank:
            for item in left_bank - {'F'}:
                actions.append(frozenset({'F', item}))  # Farmer takes item from left to right
            actions.append(frozenset({'F'}))  # Farmer goes alone from left to right
        else:
            for item in right_bank - {'F'}:
                actions.append(frozenset({'F', item}))  # Farmer takes item from right to left
            actions.append(frozenset({'F'}))  # Farmer goes alone from right to left

        # Filter actions to retain only those leading to valid states
        valid_actions = [action for action in actions if self.is_valid_state(self.result(state, action))]
        return valid_actions


    def result(self, state, action): # Returns the new state after applying the given action to the given state
        if 'F' in state:
            return state - action # If farmer is in the state, remove farmer and possibly an item
        else:
            return state | action

    def is_valid_state(self, state): # Checks if a given state is valid based on problem constraints.
        items_without_farmer = state - frozenset({'F'})
        if ('W' in items_without_farmer and 'G' in items_without_farmer) or ('G' in items_without_farmer and 'C' in items_without_farmer):
            return False
        return True

    def goal_test(self, state):
        return state == self.goal

    def is_valid_state(self, state):
        left_bank = state
        right_bank = self.initial - state

        # Check for invalid combinations on both banks
        # The check is performed for both combinations: Wolf with Goat and Goat with Cabbage

        if ('W' in left_bank and 'G' in left_bank and 'F' not in left_bank) or \
        ('G' in left_bank and 'C' in left_bank and 'F' not in left_bank):
            return False
        if ('W' in right_bank and 'G' in right_bank and 'F' not in right_bank) or \
        ('G' in right_bank and 'C' in right_bank and 'F' not in right_bank):
            return False
    
        return True
def print_solution(solution, method):
    # Initialize the solution string with method
    solution_str = f"{method}: ["

    # Iterate through the steps in the solution and add them to the solution string
    for step in solution:
        step_list = list(step)
        step_list.remove('F')  # Remove 'F' from the set to print only the item
        action_str = f"{{'F'}}" if not step_list else f"{{'{step_list[0]}', 'F'}}"
        solution_str += action_str + ", "  # Append action string to the solution string

    # Remove trailing comma and space, and close the list in the solution string
    solution_str = solution_str.rstrip(', ') + "]"

    # Print the final solution string
    print(solution_str)

if __name__ == '__main__':
    # Create an instance of the WolfGoatCabbage problem
    wgc = WolfGoatCabbage()
    
    # Depth-first search
    dfs_solution = depth_first_graph_search(wgc)
    if dfs_solution is not None:
        print_solution(dfs_solution.solution(), "dfs")
    else:
        print("DFS did not find a solution.")

    # Breadth-first search
    bfs_solution = breadth_first_graph_search(wgc)
    if bfs_solution is not None:
        print_solution(bfs_solution.solution(), "bfs")
    else:
        print("BFS did not find a solution.")
