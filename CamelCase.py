def conversion(s):
    operation, element = operation_finder(s)
    output = output_finder(operation, element)

def operation_finder(operator):
    c = 0
    array = []
    element = None

    for i in operator:
        if i == ";":
            c += 1
            continue
        elif c == 2:
            element = operator[4:]
        else:
            array.append(i)
    return array, element

def output_finder(operation, element):

    new_element = ""
    match operation[0]:
        case "S":
            for i in element:
                if i.isupper():
                    if element.index(i) == 0:
                        new_element += i.lower()
                    else:
                        new_element += " " + i.lower()
                else:
                    new_element += i
        case "C":
            for i in element:
                if i == " ":
                    element_index = element.index(i)
                    
                    new_element += element[element_index].upper()
                else:
                    new_element += i
    print(new_element)
    element_operation(operation[1],new_element)

def element_operation(operation_value,element):
    new_element = None

    match operation_value:
        case "M":
            for i in element:
                if i == "(" or i == ")":
                    continue
                else:
                    new_element += i
        case "V":
            pass
        case "C":
            pass
#     command_operator = operator_finder(s)
#     real_variable = variable_finder(s)
#     print(command_operator, real_variable)
    
#     solution = kind_finder(command_operator[0], command_operator[1], real_variable)
#     print(solution)
# # def solution(command,operation):
# #     if command == "S":
# #         kind_finder
# #     elif command == "C":
# #         pass
# #     else:
# #         return "You did something wrong"

# def kind_finder(command, operator, real_variable):
    
#     match operator:
#         case "M":
#             new_variable = ""
#             for i in real_variable:
#                 if (i.isupper()):
#                     c = 0
#                     if c == 0:
#                         pass
#                     else:
#                         new_variable += " "
#                         new_variable += str(i.lower())
#                         c += 1
#                 elif (i == "(" or i == ")"):
#                     continue
#                 else:
#                     new_variable += i
#             return new_variable
#         # case "V":
            
#         # case "C":
#         #     pass

# def operator_finder(variable):
#     c = 0
#     command_operator = []

#     for i in variable:
#         if i == ";":
#             c = c + 1
#             continue
#         elif c == 2:
#             return command_operator
#         else:
#             command_operator.append(i)
    

# def variable_finder(variable):
#     c = 0
#     real_variable = ""
#     for i in variable:
#         if i == ";":
#             c += 1
#         elif c == 2:
#             real_variable += i
            
#     else:
#         return real_variable


conversion("S;M;LargeSoftwareBook")
