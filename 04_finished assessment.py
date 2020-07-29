# asks user to only enter the following shapes
print()
print("this program is used to calculate the area and perimeter of certain shapes")
print("choose one of the following shapes: "
      "square, rectangle, "
      "circle, triangle, "
      "parallelogram")
print()
# what user is allowed to input after the questions, the allowed shapes, area / perimeter and units.
valid_shapes = ["square", "rectangle", "circle", "triangle", "parallelogram","s","r","c","t","p"]
valid_ap = ["area", "perimeter"]

# calculation list
calc_list = []
calc = []

# shape checking function, ensures that only valid shapes can be entered


def shape_checker(question):
    error = "this is not a valid shape"
    valid = False
    while not valid:
        response = input(question)

        if response.lower() in valid_shapes:
            print("you chose {}".format(response.lower()))
            return response

        elif response.lower() not in valid_shapes:
            print(error)
            continue

# area and perimeter checking function, ensures only area or perimeter can be chosen


def ap_checker(question):
    error = "please choose either area or perimeter"
    valid = False
    while not valid:
        response = input(question)

        if response.lower() in valid_ap:
            print("you chose {}".format(response.lower()))
            return response

        elif response.lower() not in valid_ap:
            print(error)
            continue

# doesn't let the unit input be blank, however pretty much any unit can be used even if it doesn't make sense


def not_blank(question):
    error = "Please enter a unit"

    valid = False
    while not valid:
        response = input(question)

        if response.lower() == "":
            print (error)
            continue

        elif response.lower() != "":
            print("you chose {}".format(response.lower()))
            return response

# does not let letters in the dimensions input


def no_letters(question):
    error = "you may only input numbers here"
    valid = False
    while not valid:
        response = input(question)

        for letter in response:

            if letter.isdigit():
                return response

            elif not letter.isdigit():
                print(error)
                break

# asks if user wants to end program and prints list at end


def finish(question):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            calc_list.append(calc)
            return response

        elif response != "":
            calc_list.append(calc)
            for item in calc_list:
                if choose_ap == "area":
                    print("{}, area = {}{}^2".format(item[0], item[1], item[2]))
                else:
                    print("{}, perimeter = {}{}".format(item[0], item[1], item[2]))
            break


# main routine
# keeps program running until user decides to stop
keep_going = ""
while keep_going == "":
    calc = []
    # user input for choosing shape, area or perimeter and unit being used

    choose_shape = shape_checker("what shape do you want? ")

    print()

    choose_unit = not_blank("what unit will you be using? ")

    print()

    choose_ap = ap_checker("do you want to calculate area or perimeter? ")

    print()

    # calculations from user input for all valid shapes

    if choose_shape == "rectangle" or choose_shape == "r":
        base = no_letters("what is the base? ")
        height = no_letters("what is the height? ")
        base = float(base)
        height = float(height)
        a = base * height
        p = 2 * (base + height)
        if choose_ap == "area":
            answer = a
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("Area =", a)
            print()

        elif choose_ap == "perimeter":
            answer = p
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("Perimeter =", p)
            print()

    if choose_shape == "square" or choose_shape == "s":
        base = no_letters("what is the side length? ")
        base = float(base)
        a = base * base
        p = 2 * (base + base)
        if choose_ap == "area":
            answer = a
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("Area =", a)
            print()

        elif choose_ap == "perimeter":
            answer = p
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("Perimeter =", p)
            print()

    if choose_shape == "circle" or choose_shape == "c":
        radius = no_letters("what is the radius? ")
        radius = float(radius)
        p = 2*3.1415926535*radius
        a = 3.1415926535*(radius*radius)
        if choose_ap == "area":
            answer = a
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("area = {:.2f}".format(a))
            print()

        if choose_ap == "perimeter":
            answer = p
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter = {:.2f}".format(p))
            print()

    if choose_shape == "triangle" or choose_shape == "t":
        if choose_ap == "area":
            base = no_letters("what is the base? ")
            height = no_letters("what is the height? ")
            base = float(base)
            height = float(height)
            a = (base*height)/2
            answer = a
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("area =", a)
            print()

        if choose_ap == "perimeter":
            side_a = no_letters("what is side a? ")
            side_b = no_letters("what is side b? ")
            side_c = no_letters("what is side c? ")
            p = side_a+side_b+side_c
            answer = p
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter =", p)
            print()

    if choose_shape == "parallelogram" or choose_shape == "p":
        if choose_ap == "area":
            base = no_letters("what is the base? ")
            height = no_letters("what is the height? ")
            base = float(base)
            height = float(height)
            a = base*height
            answer = a
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("area =", a)
            print()

        if choose_ap == "perimeter":
            base = no_letters("what is the base? ")
            side = no_letters("what is the side? ")
            base = float(base)
            side = float(side)
            p = 2*(base+side)
            answer = p
            calc.append(choose_shape)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter =", p)
            print()

    # ends keep going statement, ends program or continues depending on user input
    keep_going = finish("press <enter> to continue or and key to quit")
    print()
