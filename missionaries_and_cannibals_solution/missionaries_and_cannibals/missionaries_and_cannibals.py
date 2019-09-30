from search import Problem
from .state import State
from .operation import move

class MissionariesAndCannibals(Problem) :
    def __init__(self, initial, goal):
        self.initial = initial
        print('initial state is...')
        print(initial)
        self.goal = goal
    
    def getActions(self) : #현재 문제에서 정의된 모든 action의 set을 리턴함
        return {
            (1, 0, 0),
            (2, 0, 0),
            (0, 1, 0),
            (0, 2, 0),
            (1, 1, 0),
            (1, 0, 1),
            (2, 0, 1),
            (0, 1, 1),
            (0, 2, 1),
            (1, 1, 1)     
        }

    def actions(self, state) :
        return self.getValidAction(state, self.getActions()) #현재 state에 대해 수행 가능한 action set을 리턴함


    def result(self, state, action) :
        return move(state, action)

    def getValidAction(self, state, allActions) : #현재 state와 전체 action set을 받아서 현재 state에 대해 수행 가능한 action set을 리턴함
        validActionSet = set() # return할 set 생성
        objectState = State() # State 클래스의 객체 생성

        for action in allActions : #allActions 집합에서 action을 하나씩 꺼내서 for문 반복
            if objectState.isActionValid(state, action) : #objectState를 통해 action이 수행 가능한지 확인
                validActionSet.add(action) #수행 가능한 경우 set에 추가
            else : #아닌경우 그냥 넘어감
                pass
        
        return validActionSet #action set 리턴

    
    def goal_test(self, state) :
        return state == self.goal
