from missionaries_and_cannibals import MissionariesAndCannibals
from search import breadth_first_tree_search, depth_first_tree_search, Node
import time

def main() :
    problem = MissionariesAndCannibals([3,3,0], [0,0,1])
    startTime = time.time()
    result = breadth_first_tree_search(problem)
    #result = depth_first_tree_search(problem)
    endTime = time.time()
    print('걸린 시간 : ', endTime-startTime)
    printPathAndSolution(result)

def printPathAndSolution(result) :
    print('path is ...')
    print(Node.path(result))
    print('solution is ...')
    print(Node.solution(result))

if __name__ == "__main__" :
    main()
