# a loop is used for iterating over a sequencs(that is either a list, a tuple,a dictionary,a set, or a string).

people = ['john','paul','sara','susan']

#simple for loop
#for person in people:
    #print(f'current person: {person}')

#break
#for person in people:
  # if person == 'sara':
 #    break
   #print(f'current person: {person}')
#while loops excecute a  set of statements as long as a condition is true.

#continue
#for person in people:
 # if person == 'sara':
  ##print(f'current person: {person}')

  #range
  #for i in range(len(people)):
   # print(people[i])

for i in range(0, 11):
  print(f'number:{i}')

  #while loops execute a set of statements as long as a condition is true.

  count = 0
  while count <= 10:
    print(f'Count:{count}')
    count += 1