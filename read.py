
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

print(data[0])

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


good = [d for d in data if 'good' in d]


#文字計數

wc ={}#word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 #新增key進入字典

for word in wc:
    if wc[word] > 1000000:
        print(word,wc[word])

print(len(wc))
print(wc['Allen'])

while True:
    word = input('請問你想查什麼字')
    if word == 'q':
        break
    if word in wc:
        print(word,'出現的次數為:',wc[word])
    else:
        print('這個字沒出現過喔')
print('感謝使用查詢功能喲')






