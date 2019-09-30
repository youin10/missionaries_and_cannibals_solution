from .operation import move

class State :
    def __init__(self):
        pass

    def isActionValid(self, state, action) : #주어진 state에 대해 주어진 action이 수행 가능한지 판단하여 boolean값을 리턴함
        afterState = move(state, action) #action을 수행한 결과

        isValid = (self.numberCheck(afterState) #결과 state의 사람 수가 범위 이내인지 확인
            and self.isLeftSafe(afterState) #결과 state에서 강 왼편의 수도사가 안전한지 확인
            and self.isRightSafe(afterState) #결과 state에서 강 오른편의 수도사가 안전한지 확인
            and self.shipPosition(state, action)) #현재 state와 action의 배 위치가 일치하는지 확인

        return isValid
        
    def numberCheck(self, state) :
        if (0 <= state[0] <= 3) and (0 <= state[1] <=3) :
            return True
        else :
            return False

    def isLeftSafe(self, state) :
        if (state[0] == 0) :
            return True
        elif (state[0] >= state[1]) :
            return True
        else :
            return False

    def isRightSafe(self, state) :
        right0 = 3 - state[0]
        right1 = 3 - state[1]
        if (right0 == 0) :
            return True
        elif (right0 >= right1) :
            return True
        else : 
            return False

    def shipPosition(self, state, action) :
        if (state[2] == action[2]) :
            return True
        else :
            return False
