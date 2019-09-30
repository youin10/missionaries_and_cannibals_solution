def move(state, action) : #현재 state와 수행할 action을 받아서, action을 수행한 결과 state를 반환함
    afterState = []

    if action[2] == 0 :
        afterState.append(state[0] - action[0])
        afterState.append(state[1] - action[1])
        afterState.append(1)
    elif action[2] == 1 :
        afterState.append(state[0] + action[0])
        afterState.append(state[1] + action[1])
        afterState.append(0)

    return afterState