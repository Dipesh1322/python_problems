f = open('user_tip.txt','r')
user_id_lst = []
tip_lst = []
while True:
    line = f.readline()
    if not line:
        break
    id = line.split(",")[0]
    tip = line.split(",")[1].rstrip()
    user_id_lst.append(id)
    tip_lst.append(tip)

user_id_lst.remove(user_id_lst[0])
print(f"user_id_lst:{user_id_lst}")
tip_lst.remove(tip_lst[0])
print(f"tip_lst:{tip_lst}")