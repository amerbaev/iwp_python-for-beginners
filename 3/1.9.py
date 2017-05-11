def modify_list(l):
    new_lst = []
    while l != []:
        val = l.pop(0)
        if val % 2 == 0:
            new_lst.append(val // 2)
    l.extend(new_lst)