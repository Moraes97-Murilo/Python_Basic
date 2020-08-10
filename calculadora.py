#programa teste para vincular PC-Cloud usando git push e git pull   
op = input("Você gostaria de somar, subtrair, multiplicar ou dividir? ")
a = float (input ("Digite o primeiro valor: ")) 
b = float (input ("Digite o segundo valor: ")) 

if op == "somar":
    print (a+b)
    
elif op == "subtrair":
    print (a-b)
    
elif op == "multiplicar":
    print (a*b)
    
elif op == "dividir":
    print (a/b)
    
else:
    print("Operação desconhecida.")
