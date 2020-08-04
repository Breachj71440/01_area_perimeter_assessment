# asks user to only enter the following shapes
print()
print("this program is used to calculate the area and perimeter of certain shapes")
print("choose one of the following shapes: "
      "square, rectangle, "
      "circle, triangle, "
      "parallelogram")
print()

# what user is allowed to input after the questions, the allowed shapes, area / perimeter and units.
valid_shapes = ["square", "rectangle", "circle", "triangle", "parallelogram", "s", "r", "c", "t", "p"]
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
            print("your chosen shape is acceptable")
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
            print("your chosen calculation type is acceptable")
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
            print(error)
            continue

        elif response.lower() != "":
            print("your chosen unit is acceptable")
            return response

# does not let letters in the dimensions input


def no_letters(question):
    error = "please enter a valid number input"
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


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
                    print("{}, {} = {}{}^2  |  ".format(item[0], item[1], item[2], item[3]))
                elif choose_ap == "perimeter":
                    print("{}, {} = {}{}  |  ".format(item[0], item[1], item[2], item[3]))
            return response


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
        shape = "rectangle"
        base = no_letters("what is the base? ")
        height = no_letters("what is the height? ")
        base = float(base)
        height = float(height)
        a = base * height
        p = 2 * (base + height)
        if choose_ap == "area":
            answer = a
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("Area =", a,)
            print()

        elif choose_ap == "perimeter":
            answer = p
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("Perimeter =", p)
            print()

    if choose_shape == "square" or choose_shape == "s":
        shape = "square"
        base = no_letters("what is the side length? ")
        base = float(base)
        a = base * base
        p = 2 * (base + base)
        if choose_ap == "area":
            answer = a
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("Area =", a)
            print()

        elif choose_ap == "perimeter":
            answer = p
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("Perimeter =", p)
            print()

    if choose_shape == "circle" or choose_shape == "c":
        shape = "circle"
        radius = no_letters("what is the radius? ")
        radius = float(radius)
        p = 2*3.1415926535*radius
        a = 3.1415926535*(radius*radius)
        if choose_ap == "area":
            answer = a
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("area = {:.2f}".format(a))
            print()

        if choose_ap == "perimeter":
            answer = p
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter = {:.2f}".format(p))
            print()

    if choose_shape == "triangle" or choose_shape == "t":
        shape = "triangle"
        if choose_ap == "area":
            base = no_letters("what is the base? ")
            height = no_letters("what is the height? ")
            base = float(base)
            height = float(height)
            a = (base*height)/2
            answer = a
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("area =", a)
            print()

        if choose_ap == "perimeter":
            side_a = no_letters("what is side a? ")
            side_b = no_letters("what is side b? ")
            side_c = no_letters("what is side c? ")
            side_a = float(side_a)
            side_b = float(side_b)
            side_c = float(side_c)
            p = side_a+side_b+side_c
            answer = p
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter =", p)
            print()

    if choose_shape == "parallelogram" or choose_shape == "p":
        shape = "parallelogram"
        if choose_ap == "area":
            base = no_letters("what is the base? ")
            height = no_letters("what is the height? ")
            base = float(base)
            height = float(height)
            a = base*height
            answer = a
            calc.append(shape)
            calc.append(choose_ap)
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
            calc.append(shape)
            calc.append(choose_ap)
            calc.append(answer)
            calc.append(choose_unit)
            print("perimeter =", p)
            print()

    # ends keep going statement, ends program or continues depending on user input
    keep_going = finish("press <enter> to continue or any key to quit")
    print()
