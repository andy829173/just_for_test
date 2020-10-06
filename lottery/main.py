import os
import random

def read_file(filename):
    r = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            r.append(line.strip().split(', '))
    return r


def random_num(nums=6, start=1, end=49):
    tmp_num = random.randint(start, end)
    s = []
    while len(s) < nums:
        while tmp_num in s:
            tmp_num = random.randint(start, end)
        s.append(tmp_num)
    return sorted(s)


def write_file(filename, r):
    with open(filename, 'w', encoding='utf-8') as f:
        for n in r:
            f.write(', '.join(map(str, n)) + '\n')


def main():
    filename = 'lottery.csv'
    if os.path.isfile(filename):
        print('讀取檔案')
        r = read_file(filename)
    else:
        print('找不到檔案')
        r = []
    s = []
    while True:
        choice = input('請輸入數字 1.產生數列 2.儲存至清單 q.離開/存檔: ')
        if choice == 'q':
            write_file(filename, r)
            break
        elif choice == '2':
            if len(s) < 6:
                print('請先產生數列')
                continue
            else:
                r.append(s)
                s = []
        else:
            s = random_num()
            print(s)
    
    
main()