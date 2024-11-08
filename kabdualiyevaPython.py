def check_number():
    num_entered = input('Enter a number: ')

    try:
        number = float(num_entered)
        if  number >= 7:
            print("Hello")
    except ValueError:
        print("Invalid input.")


def check_name():
    name_input = input('Enter a name: ')

    try:
        if name_input == 'John':
            print('Hello, John')
        else:
            print('There is no such name')

    except ValueError:
        print("Invalid input.")


def find_multiples_of_3():
    array = input('Enter numbers separated by spaces: ')

    try:
        numbers = list(map(int, array.split()))
        result = []

        for num in numbers:
            if num%3==0:
                result.append(num)

        print(result)

    except ValueError:
        print("Invalid input.")



#4 
# [((())()(())]]
# [] - first
# (()) () (()) - sequence of brackets inside
# ( - one extra after first
# ] - one extra in the end 

# corrected 
# [((())()(()))] or [[(())()(())]] or [(())()(())]



def main():
    check_number()
    check_name()
    find_multiples_of_3()

if __name__ == "__main__":
    main()