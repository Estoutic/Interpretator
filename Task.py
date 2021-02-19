def multi(a,b):
    x = a * b
    return x
def div_numbers(a,b):
    x = a / b
    return x
def cyrcle(r):
    P = 3.14
    S = P * (r ** 2)
    return  S
def equation(z,x,c):
    D = z ** 2 - 4 * x * c
    if D > 0:
        x1 = ( -x  * (pow(D,.5)))/2 * z
        x2 = ( -x  * -(pow(D,.5)))/2 * z
        return x1, x2
    elif D == 0:
        x = - (x / ( 2 * c))
        return x
def hypotenuse(a,c):
        y = a**2 + c**2
        pow(y,.5)
        return y
def sfera(r):
        P = 3.14
        V = 4/3 * P * r**3 
        return V
def binary(x:str,base:int):
    res = 0
    Number_strochka = x[::-1]
    fer = 0
    for i in Number_strochka:
        num = int(i)
        next_num = num * base ** fer
        res += next_num
        fer += 1 
    return(res)



m = open("test.txt", "r")
for line in m:
    parametrs = line.split()
    command = parametrs[0]
    if command == "multi":
    
        try:
            multiplication = multi(int(parametrs[1]), int(parametrs[2]))
            print(f'multiplication_of_numbers =  {multiplication}')
        except Exception as e:
            print("wrong")
    elif command == "div":
            try:
                res = div_numbers(int(parametrs[1]), int(parametrs[2]))
                print(f'div_of_numbers = {res}')
            except ZeroDivisionError as e:
                print("zero is wrong")
    elif command == "cyrcle_square":
        try:
            cyrcle_square = cyrcle(int(parametrs[1]))
            print (f'cyrcle_of_square = {cyrcle_square}')
        except Exception as e:
            print("zero is wrong argument")
    elif command == "equation":
        try:
            equation_of_numbers = equation(int(parametrs[1]), int(parametrs[2]), int(parametrs[3]))
            print(f'equation = {equation_of_numbers}')
        except Exception as e:
            print("wrong argument")
    elif command == "hypotenuse":
        try:
            hypotenuse_of_katets = hypotenuse(int(parametrs[1]), int(parametrs[2]))
            print(f'hypotenuse is {hypotenuse_of_katets}')        
        except Exception as e:
                print("enter anorher number")
    elif command == "cyrcle_volume":
        try:
            shar = sfera(int(parametrs[1]))
            print(f'sfera_volume = {shar}')
        except Exception as e:
            print('cant be a negative number')
    elif command == "binary":
        try:
            binary_of_numbers=binary(parametrs[1])
            print(f'binary of nubmers = {binary_of_numbers}')
        except Exception as e:
            print("not rihgt")           




