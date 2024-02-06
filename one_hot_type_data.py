# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
# из 1 столбца. Ваша задача перевести его в one hot вид.

import pandas as pd
import random
import matplotlib.pyplot as plt

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

robot_lst = [0]*20
human_lst = [0]*20
for i in range(len(lst)):
    if lst[i] == 'robot':
        robot_lst[i] = 1
        human_lst[i] = 0
    else:
        robot_lst[i] = 0
        human_lst[i] = 1        

data = pd.DataFrame({'whoAmI':lst})
data_one_hot = pd.DataFrame({'robot':robot_lst, 'human': human_lst})
print(data.head(n=20))
print(data_one_hot.head(n=20))

