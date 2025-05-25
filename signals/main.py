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

for good in def_good.values():
  for i in range(len(not_so_good)):
    val = list(not_so_good.values())[i]
    if good[0] in list(not_so_good.values())[i]:
      val.pop(val.index(good[0]))
      key = list(not_so_good.keys())[i] 
      not_so_good[key] = val
for i in range(len(not_so_good)):
  val = list(not_so_good.values())[i]
  key = list(not_so_good.keys())[i]
  n = [] 
  for event in val:
    for item in not_so_good.values():
      if event in item and item != val:
        n.append(key)
      

    #if all(event in item for item in not_so_good.values() if item != val):
for key, value in def_good.items():
    print(f"{value[0]}: {key}")

#Átmegyünk a not_so_good.values-on és keressük, hogy melyik elemben van bent az összes item a jelenleg
# vizsgált not_so_good.values elemben
