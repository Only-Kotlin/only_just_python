def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1] += 1
    #print(q[1] for q in Q)
    return [q[1] for q in Q]



progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))