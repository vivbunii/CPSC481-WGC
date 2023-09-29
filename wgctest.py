from search import depth_first_graph_search, breadth_first_graph_search
from search import Problem

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=frozenset()):
        super().__init__(initial, goal)

    def actions(self, state):
        actions = []
        items_on_left = state - frozenset({'F'})

        for item in items_on_left:
            # Action is a set of items and 'F' representing moving the item and the farmer
            action = frozenset([item, 'F'])
            new_state = state - action  # Move the item and the farmer
            if self.is_valid_state(new_state):
                actions.append(action)
        return sorted(actions)  # Sort the actions for consistency

    def result(self, state, action):
        new_state = state - action  # Move the items and the farmer
        return new_state

    def goal_test(self, state):
        return state == self.goal

    def is_valid_state(self, state):
        # Check if the state is valid (wolf and goat or goat and cabbage are not left alone)
        if ('W' in state and 'G' in state and 'C' not in state) or ('G' in state and 'C' in state and 'W' not in state):
            return False
        return True

def print_solution(solution, method):
    # Initialize the solution string with method and start of the list
    solution_str = f"{method}: [{{'G', 'F'}}"

    # Iterate through the steps in the solution and add them to the solution string
    for step in solution:
        step_list = list(step)
        step_list.remove('F')  # Remove 'F' from the set to print only the item
        solution_str += f", {{'F'}}" if not step_list else f", {{'{step_list[0]}', 'F'}}"

    # Close the list in the solution string
    solution_str += "]"

    # Print the final solution string
    print(solution_str)

if __name__ == '__main__':
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