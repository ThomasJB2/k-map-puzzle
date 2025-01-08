import random
o = " or "
yesOrNo = ["", "not "]

grid = [
        [(False, False, False, False), (False, True, False, False), (True, True, False, False), (True, False, False, False)], 
        [(False, False, False, True), (False, True, False, True), (True, True, False, True), (True, False, False, True)],
        [(False, False, True, True), (False, True, True, True), (True, True, True, True), (True, False, True, True)],
        [(False, False, True, False), (False, True, True, False), (True, True, True, False), (True, False, True, False)]
            ]

def create_equation():
    return random.choice(yesOrNo) + "A " + "and " + random.choice(yesOrNo) + "B " + "and " + random.choice(yesOrNo) + "C " + "and " + random.choice(yesOrNo) + "D"
            
# Function to replace letters based on boolean values in the grid
def replace_letters(grid, template):
    def convert(value):
        return 1 if value else None
    # Iterate through the grid
    result = []
    for row in grid:
        new_row = []
        for cell in row:
            A, B, C, D = cell
            # Use eval to compute the result of the template
            evaluated = eval(template)  # Evaluate the expression
            converted = convert(evaluated)
            new_row.append(converted)
        result.append(new_row)
    return result

repe = random.randint(2, 7)

Equation = o.join([create_equation() for _ in range(repe)])

# for i in range(repe):
#     solved = replace_letters(grid, Equation)
#     i =+ 1

parts = [part.strip() for part in Equation.split("or")]
equations = {f"{i+1}": part for i, part in enumerate(parts)}

# print(equations["1"])
# print(equations["2"])
# print(equations["3"]) if "3" in equations else print("No Value")
# print(equations["4"]) if "4" in equations else print("No Value")
# print(equations["5"]) if "5" in equations else print("No Value")
# print(equations["6"]) if "6" in equations else print("No Value")
# print(equations["7"]) if "7" in equations else print("No Value")

def replace_letters(grid, template):
    def convert(value):
        return 1 if value else None
    # Iterate through the grid
    result = []
    for row in grid:
        new_row = []
        for cell in row:
            A, B, C, D = cell
            # Use eval to compute the result of the template
            evaluated = eval(template)  # Evaluate the expression
            converted = convert(evaluated)
            new_row.append(converted)
        result.append(new_row)
    return result

equGrid1 = replace_letters(grid, equations["1"])
equGrid2 = replace_letters(grid, equations["2"])
equGrid3 = replace_letters(grid, equations["3"]) if "3" in equations else None
equGrid4 = replace_letters(grid, equations["4"]) if "4" in equations else None
equGrid5 = replace_letters(grid, equations["5"]) if "5" in equations else None
equGrid6 = replace_letters(grid, equations["6"]) if "6" in equations else None
equGrid7 = replace_letters(grid, equations["7"]) if "7" in equations else None

finalGrid = []
for i in range(len(equGrid1)):
    row = []
    for j in range(len(equGrid1[0])):
        # Get all values at this position from each grid
        values = [
            equGrid1[i][j],
            equGrid2[i][j],
            equGrid3[i][j] if equGrid3 != None else None,
            equGrid4[i][j] if equGrid4 != None else None,
            equGrid5[i][j] if equGrid5 != None else None,
            equGrid6[i][j] if equGrid6 != None else None,
            equGrid7[i][j] if equGrid7 != None else None
        ]
        # Take the first non-None value
        value = next((x for x in values if x is not None), None)
        row.append(value)
    finalGrid.append(row)
    
print(Equation)
print(finalGrid)