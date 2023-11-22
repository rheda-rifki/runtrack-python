def calcule(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:  
            result = num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0: 
            result = num1 % num2
        else:
            return "Erreur : Reste par zéro"
    else:
        return "Opérateur non valide"
    
    return result

print(calcule(5, '+', 3))   
print(calcule(10, '*', 2)) 
print(calcule(8, '/', 4))   
print(calcule(15, '%', 7))  
print(calcule(7, '^', 3))   

    