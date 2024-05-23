f = open('marks.txt','r')
m1_lst = []
m2_lst = []
m3_lst =[]
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m1_lst.append(m1)
    m2 = line.split(",")[1]
    m2_lst.append(m2)
    m3 = line.split(",")[2]
    m3_lst.append(m3)
    print(f"Marks of student {i} in Maths are: {m1}")
    print(f"Marks of student {i} in English are: {m2}")
    print(f"Marks of student {i} in SST are: {m3}")
    print(f"line:{line}")
    print(f"m1_lst:{m1_lst}")
    print(f"m2_lst:{m2_lst}")
    print(f"m3_lst:{m3_lst}")
