def get_starting_number():
    while True:
        _input = input("How many bottles of beer on the wall? ")
        if _input.isdigit():
            bottles = int(_input)
            if bottles >= 1:
                return bottles


def sing(startings):
    bottles = startings
    is_singing = True
    while is_singing:
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
            is_singing = False
        elif bottles == 2:
            print("2 bottles of beer on the wall, 2 bottles of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.")
            print()
            bottles = bottles - 1
        else:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.")
            print()
            bottles = bottles - 1