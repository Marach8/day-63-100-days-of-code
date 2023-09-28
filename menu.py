def menu():
  w = '\033[4mWELCOME TO OUR TO-DO LIST MANAGER\033[0m'
  print(f'\033[0m{w:^65}')
  print()
  print('\033[1;33m1: Add\n2: View\n3: Edit\n4: Remove')
  ask = input('\033[0m>> ')
  return ask