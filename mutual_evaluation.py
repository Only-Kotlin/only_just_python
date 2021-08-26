# 대학 교수인 당신은, 상호평가를 통하여 학생들이 제출한 과제물에 학점을 부여하려고 합니다. 아래는 0번부터 4번까지 번호가
# 매겨진 5명의 학생들이 자신과 다른 학생의 과제를 평가한 점수표입니다.
# No.  0    1    2    3    4
# 0  100   90   98   88   65
# 1   50   45   99   85   77
# 2   47   88   95   80   67
# 3   61   57  100   80   65
# 4   24   90   94   75   65
# 당신은 각 학생들이 받은 점수의 평균을 구하여, 기준에 따라 학점을 부여하려고 합니다.
# 만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.


def solution(scores):
    answer = ''
    sco_len = len(scores)
    for l in range(sco_len):
        count = sco_len
        sum = 0
        if all(scores[l][l] + 1 > scores[q][l] for q in range(sco_len)) or all(scores[l][l] - 1 < scores[q][l] for q in range(sco_len)):
            bol = 0
            for i in range(sco_len):
                if scores[l][l] == scores[i][l]:
                    bol += 1
            if bol == 1:
                count -= 1
                sum -= scores[l][l]

        for a in range(sco_len):
            sum += scores[a][l]
        if (sum/count) >= 90:
            answer += 'A'
        elif (sum/count) >= 80:
            answer += 'B'
        elif (sum/count) >= 70:
            answer += 'C'
        elif (sum/count) >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer



scores1 = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
scores2 = [[50,90],[50,87]]
scores3 = [[70,49,90],[68,50,38],[73,31,100]]

print(solution(scores2))