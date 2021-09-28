f = open('woodpecker.txt', 'w')
start = int(input('Start puzzle number? '))
num = int(input('Number of puzzles? '))
for n in range(start, start + num):
    f.write(f'{n}) 1{"…" if int(input(f"{n}: Who to play? (0 = W, 1 = B) ")) else "."}\n')
f.close()