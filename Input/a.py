import os

for i in os.listdir('Input'):
    if i.endswith('py'): 
        continue
    for j in os.listdir(f'Input\\{i}'):
        with open(f'Input\\{i}\\{j}','r+') as file:
            lst=file.readlines()
            # print(lst)
            file.seek(0)
            file.truncate()
            n=1
            for k in lst[1:]:
                if k=='\n':
                    n+=1
                else:
                    break
            file.writelines(lst[n:])
