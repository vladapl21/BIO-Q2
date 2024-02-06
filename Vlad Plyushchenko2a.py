#question 2a
E = [i for i in range(2, 400, 2)]
O = [i for i in range(1, 400, 2)]
T = []
for x in range(400):
  for t in range(x):
    T.append(x)

def lists(description, i):
  print(description, i)
  list_description = []
  #for x in description:
   # list_description.append(x)
  for letter in range(12):
    try:
      if description[letter] == "E" or "O" or "T":
        list_description.append(description[letter])
    except IndexError:
      break

  list1 = []
  list2 = []
  current = []
  if list_description[0] == "E":
    list1 = E
  elif list_description[0] == "O":
    list1 = O
  elif list_description[0] == "T":
    list1 = T
  if list_description[1] == "E":
    list2 = E
  elif list_description[1] == "O":
    list2 = O
  elif list_description[1] == "T":
    list2 = T

  for j in range(20):
    current.append(list2[list1[list2[j]-1]-1])


  final = []
  if len(list_description) > 2:
    list_description.pop(0)
    list_description.pop(0)

    if list_description[0] == "E":
      list1 = E
    elif list_description[0] == "O":
      list1 = O
    elif list_description[0] == "T":
      list1 = T
    for j in range(6):
      final.append(list1[current[list1[j]-1]-1])
    print(final)
    print(final[i-1])
  else:
    print(current[i-1])

description = str(input())
i = int(input())
lists(description, i)