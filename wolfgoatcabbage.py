from search import *


class WolfGoatCabbage(Problem):
    def __init__(self, initial=[['F', 'W', 'C', 'G'], []], goal=[[], 'F']):

        super().__init__(self, initial, goal)


if __name__ == "__main__":
    wgc = WolfGoatCabbage()
    print(wgc.initial)
    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
