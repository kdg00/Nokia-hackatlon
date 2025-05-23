with open('./input.txt', 'r') as f:
  input = f.read()

print(input)

for item in input:
  if type(item) != int:
    print("N/A")
    continue