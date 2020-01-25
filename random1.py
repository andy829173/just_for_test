import random
start = 1
end = 100
r = random.randint(start, end)
i = 0
while True:
    guess = int(input('請猜一組數字: '))
    i += 1
    if guess == r:
        print('答對了!')
        print('共猜了', i, '次')
        break
    elif guess > end:
        print('猜太大了!')
        print(start, '~', end)
    elif guess < start:
        print('猜太小了!')
        print(start, '~', end)
    elif guess > r:
        end = guess
        print(start, '~', end)
    elif guess < r:
        start = guess
        print(start, '~', end)