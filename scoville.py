# 스코빌 지수를 K 이상으로 만들고 싶다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 스코빌 지수가 가장 낮은 두 개의
# 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만든다.
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

scoville = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    queue = [s for s in scoville]

    answer = 0

    while True:
        if min(queue) <= K:
            if len(queue) == 1 and K >= queue[0]:
                return -1
            low = min(queue)
            queue.remove(low)
            queue.append(low + (min(queue) * min(queue)))
            answer += 1
            queue.remove(min(queue))
        else:
            return answer

print(solution(scoville, K))