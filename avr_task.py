if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    sum=0
    for k,v in student_marks.items():
        if k==query_name:
            for marks in student_marks.get(query_name):
                sum+=marks
    print("{0:.2f}".format(sum/3) )
            