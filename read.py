# 留言分析程式 ('reviews.txt'檔不上傳)
# 計算留言清單總筆數
# 讀取檔案過程中，印出len(data)才知道讀取進度
# 計算留言平均長度
data = []  # 設置data空清單
count = 0  # 計數器設置為0
with open('reviews.txt', 'r') as f: # 讀取reviews.txt 存入f
    for line in f:                  # 將f 用迴圈 每行一列出來
        data.append(line)           # 將line每行存入data清單
        count += 1                  # 等於 count = count + 1
        if count % 10000 == 0:
            print(len(data))
print('讀取完了，總共有', len(data), '筆資料')

numdata = 0
for line2 in data:
	numdata = numdata + len(line2)
# 計算平均長度，取整數int
print('留言平均長度為', int(numdata/len(data)), '個字')
