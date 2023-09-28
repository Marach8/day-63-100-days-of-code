import os, time, menu, printer

list1 = []
head = ['Description', 'Due Date', 'Priority']


def add():
  os.system('clear')
  time.sleep(1.5)
  print('\033[4mFill the following information for your TODO\033[0m')
  print()
  time.sleep(1)
  ask1 = input('Enter the To-do: ')
  ask2 = input('Enter the due date or time of the To-do: ')
  list2 = [ask1, ask2]

  while True:
    print()
    print('\033[1;36mBased on how important the event is to you, you can select a priority of High, Medium or Low.')
    time.sleep(1)
    print()
    ask3 = input('\033[0mEnter the priority\n1: High\n2: Medium\n3: Low\n>> ')
    if ask3 == '1':
      list2.append('High')
      break
    elif ask3 == '2':
      list2.append('Medium')
      break
    elif ask3 == '3':
      list2.append('Low')
      break
    else:
      print()
      print('\033[31mPlease select 1, 2 or 3 to proceed')
      time.sleep(2)
      continue 
  time.sleep(1)
  list1.append(list2)
  print('\033[32mYour Todo has been added Succesfully😎')
  time.sleep(2)
  querry = input('\033[0mWant to add again? y/n: ')
  if querry == 'y':
    time.sleep(1.5)
    os.system('clear')
    add()
  else:
    os.system('clear')
    time.sleep(2)
    body()
    

def view():
  if len(list1) != 0:
    time.sleep(2)
    print()
    q = '\033[4mEnter any of the numbers to perform the following operations\033[0m'
    print(f'\033[0m{q}')
    print()
    ask = input('\033[0;37m1: View all todo\n2: View by priority\n>> ')
    if ask == '1':
      printer.printer(list1)
      print()
      todo_load()
    elif ask == '2':
      while True:
        print()
        list2 = []
        list2.insert(0, head)
        ask2 = input('1: view High priority\n2: view Medium priority\n3: view Low priority\n>> ')
        if ask2 == '1':
          for i, j in enumerate(list1):
            if 'High' in j:
              list2.append(j)
          printer.printer(list2)
          break
        elif ask2 == '2':
          for i, j in enumerate(list1):
            if 'Medium' in j:
              list2.append(j)
          printer.printer(list2)
          break
        elif ask2 == '3':
          for i, j in enumerate(list1):
            if 'Low' in j:
              list2.append(j)
          printer.printer(list2)
          break
        else:
          print ()
          print('\033[31mplease input 1, 2 or 3 to proceed!')
          print()
          continue
    else:
      print()
      print('\033[31mPlease input 1, or 2 to proceed!')
      print()
      view()
    todo_load()
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can view!')
    time.sleep(2)
    os.system('clear')
    body()
    
def edit():
  if len(list1) != 0:
    print ()
    printer.printer(list1)
    print ()
    
    a = input('Type in any of the information above that you wish to change?: ').strip()
    b = input('Enter the replacement: ').strip()
    m = 0
    for i, j in enumerate(list1):
      if a in j:
        d = j.index(a)
        list1[i][d] = b
        print()
        print('\033[32mItem edited Successfully😊')
        time.sleep(2)
        break
      else:
        m += 1
        if m == len(list1):
          print()
          time.sleep(1.5)
          print('\033[31mThe item you chose is not in there')
          time.sleep(2.5)
        else:
          continue
              
    print()
    time.sleep(3)
    os.system('clear')
    body()

                    
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can edit!')
    time.sleep(8)
    os.system('clear')
    body()


def remove():
  if len(list1) != 0:
    print ()
    printer.printer(list1)
    print ()
    
    m = 0
    while True:
      print()
      a = input('''\033[0mType in any of the information above that you wish to remove?: ''')
      for i, j in enumerate(list1):
        if a in j:
          list1.remove(j)
          print()
          time.sleep(1.5)
          print('\033[32mItem removed succesfully')
          time.sleep(2)
          break
        else:
          m += 1
          if m == len(list1):
            print()
            time.sleep(1.5)
            print('\033[31mThe item you chose is not in there')
            time.sleep(2.5)
          else:
            continue
            
      print()                     
      printer.printer(list1)
      response = input('\033[0mWant to remove again? y/n: ')
      if response == 'y':
        os.system('clear')
        printer.printer(list1)
        continue
      else:
        break
    time.sleep(1.5)
    os.system('clear')
    body()
                    
  else:
    print ('\033[31mYou currently have no entries in your To-do list. Add entries first before you can remove!')
    time.sleep(8)
    os.system('clear')
    body()

def todo_load():
  time.sleep(2)
  ask4 = input('''
\033[0mWhen you are done viewing, press 'Enter' to go back to main menu: 
''')
  if len(ask4) == 0:
    time.sleep(1.5)
    print()
    print('\033[35mTODO menu Loading... Please wait...')
    time.sleep(1.5)
    os.system('clear')
    body()


def body():
  b = menu.menu()
  while True:
    if b == '1':
      add()
    elif b == '2':
      view()
    elif b == '3':
      edit()
    elif b == '4':
      remove()
    else:
      print()
      print('\033[31mInvalid selection! Please select either 1, 2, 3 or 4')
      time.sleep(3)
      os.system('clear')
      continue 

body()