if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    
    cur = 0.0
    scores_q = student_marks[query_name]

    for x in scores_q:
        cur += x
    ans = cur / 3.0
    ans = "{0:0.2f}".format(ans)
    print(ans)
