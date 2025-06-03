# While loop 通常較適合運用在不知道執行次數的case 上
products = []
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

for product in products:
	print(product[0], '的價格是', product[1])
