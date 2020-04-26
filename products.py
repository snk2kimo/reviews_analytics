# 讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue # 跳到下一個迴圈
		name, price = line.strip().split(',') # 將line去調換行符號(strip).去掉逗號(split)後存入name, price兩個清單內
		products.append([name, price])		
print(products)

# 記帳程式專案 - 讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	products.append([name, price])
print(products)

# 印出所有商品跟價格
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
