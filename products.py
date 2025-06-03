#重點：
#理想的function應該"只做一件事"，所以refactor(重構程式)的核心概念，就是把程式碼不斷的改寫，寫成越來越小的function，讓function "盡量"只做一件事。
#程式最好有main() function 為程式的進入點

import os  #operating system

def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line or not line.strip():
                continue #繼續
            
            parts = line.strip().split(',')
            if len(parts) == 2:
                # 只有當剛好分割成兩份時，才進行賦值和添加
                name, price = parts
                products.append([name, price])
            else:
                # 如果格式不對，就印出警告並跳過此行
                print(f"警告：讀取到格式不符的資料，已略過此行 -> {line.strip()}")

    return products
    
#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

#印出所有購買紀錄
def print_product(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yeah! ˋ找到檔案了!')
        products = read_file(filename)
    else:
        print('找不到檔案...')

    products = user_input(products)
    print_product(products)
    write_file('products.csv',products)

main()