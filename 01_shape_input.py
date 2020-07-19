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

# user input for choosing shape


user_input = shape_checker("what shape will you choose? ")
