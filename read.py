
data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))
print(len(data))
print('檔案讀取完了總共有',len(data),'筆資料')


sum_len = 0
for d in data:
    sum_len = sum_len + len(d)

print('平均長度是',sum_len/len(data),'個字')


new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有',len(new),'比留言長度小於100')
print(new[0])  


good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good),'筆留言有包含good')
print(good[0])