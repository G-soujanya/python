#lex_auth_012742471863279616506

def update_mark_list(mark_list, new_element, pos):
    mark_list=mark_list.insert(pos,new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    l=[] 
    l.append(mark_list[pos1])
    l.append(mark_list[pos2])
    return l

#Provide different values for the variables and test your program
mark_list=[89,78,99,76,77,72,88,99]
new_element=69
pos=2
pos1=5
pos2=8
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))