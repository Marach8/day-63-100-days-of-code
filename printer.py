import time, os
list1 = []
head = ['Description', 'Due Date', 'Priority']
p = 0
m = 0
def printer(w):
  global p
  os.system('clear')
  if p == 0:
    w.insert(0, head)
    p += 1
  else:
    pass
  m = 0
  for i in w:
    if m == 0:
      for j in i:
        print(f'\033[1;33m{j:^20}', end='|')
        m += 1
      print()
      print('    ___________________________________________________________')
    else:
      for j in i:
        print(f'\033[34m{j:^20}', end='|')
    print()
  print()
