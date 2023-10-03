a = int(input('Introduzca el primer valor: ' ))
b = int(input('introduzca el segundo valor: ' ))
c = int(input('introduzca el tercer valor: '))
if a > b :
    print('El mayor de los tres es: ',a)
elif a > c:
    print('El mayor de los tres es: ',a)
elif c > a:
    print('El mayor de los tres es: ',c)
elif c > b:
    print('El mayor de los tres es: ',c)

else :
    print('el numero mayor de los dos es: ',b )