import pandas as pd
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95]}
df = pd.DataFrame(exam_data)

print(df)


data = '열\t이\t름\na\tb\tc\na\tb\tc'
data = data.split('\n')
print(data)
list = []
for i in data :
    row = i.split('\t')
    list.append(row)
df = pd.DataFrame(list, columns=list[0])
df = df.loc[1:]
print(df)





