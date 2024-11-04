num_entered = input('Enter a number: ')

number = float(num_entered)
if  number >= 7:
    print("Hello")


#2
name_input = input('Enter a name: ')

if name_input == 'John':
    print('Hello, John')
else:
    print('There is no such name')


#3
array = input('Enter numbers separated by spaces: ')

numbers = list(map(int, array.split()))
result = []

for num in numbers:
    if num%3==0:
        result.append(num)

print(result)


#4 
# [((())()(())]]
# [] - first
# (()) () (()) - sequence of brackets inside
# ( - one extra after first
# ] - one extra in the end 

# corrected 
# [((())()(()))] or [[(())()(())]] or [(())()(())]
