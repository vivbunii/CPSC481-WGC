from search import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial=[['F', 'W', 'C', 'G'], []], goal=[[], 'F']):
        super().__init__(initial, goal)

    # return True if is the given state is a goal state
    def goal_test(state):
        pass

    # returns the new state reached from the given state and the given action 
    def result(state, action):
        pass
    
    # returns a list of valid actions in the given state
    def actions(state):
        pass

if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    print(wgc.initial)
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
