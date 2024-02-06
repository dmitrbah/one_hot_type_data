# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего 
# из 1 столбца. Ваша задача перевести его в one hot вид.

import pandas as pd
import random
import matplotlib.pyplot as plt

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(n=20))
