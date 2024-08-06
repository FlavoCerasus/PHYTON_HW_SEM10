# HOMEWORK - SEM 10 - Danil Eliseev
"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
Сможете ли вы это сделать без get_dummies?
"""
# Условия задания:
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()

print(f"Список: {lst}")
print()
# # 1 - С использованием функции "get_dummies":
one_hot_enc_var1 = pd.get_dummies(data, columns=['whoAmI'])
print(one_hot_enc_var1.head(n=20))

# # 2 - Без использования функции:
one_hot_enc_var2 = pd.DataFrame({'whoAmI': lst})
one_hot_enc_var2.loc[one_hot_enc_var2['whoAmI'] == 'robot', 'r_group'] = '1'
one_hot_enc_var2.loc[one_hot_enc_var2['whoAmI'] != 'robot', 'r_group'] = '0'
one_hot_enc_var2.loc[one_hot_enc_var2['whoAmI'] == 'human', 'h_group'] = '1'
one_hot_enc_var2.loc[one_hot_enc_var2['whoAmI'] != 'human', 'h_group'] = '0'
print(one_hot_enc_var2.head(n=20))
