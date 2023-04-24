line_dict = []

line_stopper = True

while line_stopper:

    try:
        line_input = input("Enter a line (ctrl-D to stop): ")
        line_dict.append(line_input)

    except EOFError:
        line_dict.reverse()
        for x in line_dict:
            print(x)
        break
