def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    report_set = set(report)
    report = list(report_set)
    array = [[] for i in range(len(id_list))]
    for name in report:
        name = name.split()
        array[id_list.index(name[1])].append(id_list.index(name[0]))
    for ary in array:
        if len(ary) >= k:
            for i in ary:
                answer[i] += 1
    return answer