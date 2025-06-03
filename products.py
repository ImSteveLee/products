# While loop 通常較適合運用在不知道執行次數的case 上
#

products = []

#讀取檔案
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			Continue #繼續, 跳到下一回; 相較於break, break 會跳出 loop 迴圈, Continue 不會 (所以Continue 通常只用在 For or IF 中很高的位置; 少見)
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')

	p = []  #創建"二維"list (小清單)
	p.append(name)
	p.append(price)
	products.append(p) #小清單(小火車) 寫入大清單 (大火車)

#Line 9 ~ 12 簡寫~
#   products.append([name, price])

print(products)

#products[0][0]  #拿出 第0個商品 的第0個欄位 "名稱"
#products[1][1]  #拿出 第1個商品 的"價格"


#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])


#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
