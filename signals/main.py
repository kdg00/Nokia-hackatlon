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
for item in allevents.keys():
  if not common:
    common = item
    continue



print("asd")
