'''number = [2,2,2,2,6]
for x in number:
    output= ''
    for counr in range (x):
        output += 'x'
    print(output)

number =[2,2,2,2,6]
for x in number:
    print('x' *  x)'''

numbers= [2,2,4,6,3,5,6,3,1,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


    
      
  
    

