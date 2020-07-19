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

# user input for choosing shape and area or perimeter


choose_shape = shape_checker("what shape do you want? ")

choose_ap = ap_checker("do you want to calculate area or perimeter? ")
