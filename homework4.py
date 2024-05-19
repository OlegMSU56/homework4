immutable_var=(1,2.3,"kek",False)
print(immutable_var)
#кортеж не поддерживает обращение к элементам, его нелья редактировать
mutable_list=[4.5,8,'fjgbkzkjb']
print(mutable_list)
mutable_list[1]='R'
mutable_list.append(800)
mutable_list.extend(['qwer'])
print(mutable_list)
print(mutable_list[1:3])