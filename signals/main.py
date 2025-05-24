import ast 

with open('./input.txt', 'r') as f:
  input = f.read()
  input = ast.literal_eval(input.strip())

eventlist = [item[1] for item in input]
signallist = [item[0] for item in input]
allevents = {}

for item in eventlist:
  for event in item:
    if event not in allevents.keys():
      one_event = []
      for i in range(len(eventlist)):
        if event in eventlist[i]:
          one_event.append(i)
      allevents[event] = one_event 


common = []
def_good = {}
not_so_good = {}
for event in allevents.keys():
  common = []
  for i in allevents[event]:
    if not common:
      common = signallist[i]
      continue
    common = list(set(common) & set(signallist[i]))
  if len(common) == 1:
    def_good[event] = common
  else:
    not_so_good[event] = common

for good in def_good.keys():
  for lists in not_so_good.keys():
    if good in lists:
      not_so_good[lists] = lists.pop(lists.index(def_good))
print("asd")
