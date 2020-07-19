# asks user to only enter the following shapes
print("choose one of the following shapes: "
      "square, rectangle, "
      "circle, triangle, "
      "parallelogram")
# what user is allowed to input after the questions
valid_shapes = ["square", "rectangle", "circle", "triangle", "parallelogram"]
valid_ap = ["area", "perimeter"]

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

# no letters allowed in number input function


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


# user input for choosing shape, area or perimeter and dimensions of the shape
# shows user back the dimensions they chose

choose_shape = shape_checker("what shape do you want? ")

choose_ap = ap_checker("do you want to calculate area or perimeter? ")

if choose_shape == "rectangle":
    base = no_letters("what is the base? ")
    height = no_letters("what is the height? ")
    print("the base is", base)
    print("the height is", height)

if choose_shape == "square":
    base = no_letters("what is the base? ")
    height = no_letters("what is the height? ")
    print("the base is", base)
    print("the height is", height)

if choose_shape == "circle":
    radius = no_letters("what is the radius? ")
    print("the base is", radius)

if choose_shape == "rectangle":
    base = no_letters("what is the base? ")
    height = no_letters("what is the height? ")
    print("the base is", base)
    print("the height is", height)

if choose_shape == "triangle":
    if choose_ap == "area":
        base = no_letters("what is the base? ")
        height = no_letters("what is the height? ")
        print("the base is", base)
        print("the height is", height)
    if choose_ap == "perimeter":
        side_a = no_letters("what is the side a? ")
        side_b = no_letters("what is the side b? ")
        side_c = no_letters("what is the side c? ")
        print("the side a is", side_a)
        print("the side b is", side_b)
        print("the side c is", side_c)

if choose_shape == "parallelogram":
    if choose_ap == "area":
        base = no_letters("what is the base? ")
        height = no_letters("what is the height? ")
        print("the base is", base)
        print("the height is", height)
    if choose_ap == "perimeter":
        base = no_letters("what is the base? ")
        side = no_letters("what is the side? ")
        print("the base is", base)
        print("the side is", side)
