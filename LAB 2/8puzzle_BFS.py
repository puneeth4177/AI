def printpuzzle(src):
    print(' ' + src[0] + ' | ' + src[1] + ' | ' + src[2])
    print('-----------')
    print(' ' + src[3] + ' | ' + src[4] + ' | ' + src[5])
    print('-----------')
    print(' ' + src[6] + ' | ' + src[7] + ' | ' + src[8])
    print('\n')
def bfs(src,target):
    queue = []
    queue.append(src)
    
    explored = []
    
    while len(queue) > 0:
        source = queue.pop(0)
        explored.append(source)
        
        printpuzzle(source)
        
        if source==target:
            print("Goal State Reached")
            return
        
        poss_moves_to_do = []
        poss_moves_to_do = possible_moves(source,explored)
        
        for move in poss_moves_to_do:
                queue.append(move)
def possible_moves(state,visited_states): 
    b = state.index(' ')
    dir = []
    if b not in [0,1,2]: 
        dir.append('u')
    if b not in [6,7,8]: 
        dir.append('d')
    if b not in [0,3,6]: 
        dir.append('l')
    if b not in [2,5,8]: 
        dir.append('r')
        

    pos_moves= []
    
    
    for i in dir:
        pos_moves.append(convert(state,i,b))
        
    return [move for move in pos_moves if move not in visited_states]
def convert(state, m, b):
    temp = state.copy()                              
    
    if m=='d':
        temp[b+3],temp[b] = temp[b],temp[b+3]
    
    if m=='u':
        temp[b-3],temp[b] = temp[b],temp[b-3]
    
    if m=='l':
        temp[b-1],temp[b] = temp[b],temp[b-1]
    
    if m=='r':
        temp[b+1],temp[b] = temp[b],temp[b+1]
        
        
    return temp
src = ['1','2','3',' ','4','5','6','7','8']
target = ['1','2','3','4','5',' ','6','7','8']         
bfs(src, target)