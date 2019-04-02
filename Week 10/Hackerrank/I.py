if __name__ == '__main__':
    list = []
    st = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        st.add(score)
    for i in sorted([i[0] for i in list if i[1] == sorted(st)[1]]):
        print(i)
    
