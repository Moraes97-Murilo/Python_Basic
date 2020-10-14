'''
Exercicio-Programa, objetivo era calcular a trajetoria do arremesso de uma pokebola e o resultado da captura.
A localizacao do pokemon e fixa, mas a cada tentativa o treinador pode se mover.
'''

n = int(input(" Digite o numero N de pokebolas: \n"))
g = int(input("Digite o valor da gravidade: \n"))
x_pok = int(input("Digite a coordenada x (inteiro >= 0) do pokemon:\n"))
y_pok = int(input("Digite a coordenada y (inteiro >= 0) do pokemon:\n"))

t_ini = 0
cont = 1
while cont <= n:
    print("\nTentativa {}:\n".format(cont))
    x_trein = int(input("Digite a coordenada x (inteiro >= 0) do treinador:\n"))
    y_trein = int(input("Digite a coordenada y (inteiro >= 0) do treinador:\n"))
    vel_yini = int(input("Digite a componente y da velocidade de lancamento:\n"))
    x_bol = x_trein 
    y_bol = y_trein
    t = t_ini
    if x_bol == 0 and y_bol == 0:
        print("t=    %4d    vy=    %4d    x=    %4d    y=    %4d"%(t,vel_yini,x_bol,y_bol))
        t += 1
        x_bolini = x_trein 
        y_bolini = y_trein
        x_bol = int(x_bolini + t)
        y_bol = int((y_bolini) + (vel_yini * t) - ((g / 2) * (t**2)))
        vel_y = int(vel_yini - g * t)
        while y_bol > 0 and x_bol < x_pok:
            x_bolini = x_trein 
            y_bolini = y_trein
            x_bol = int(x_bolini + t)
            y_bol = int((y_bolini) + (vel_yini * t) - ((g / 2) * (t**2)))
            vel_y = int(vel_yini - g * t)
            print("t=    %4d    vy=    %4d    x=    %4d    y=    %4d"%(t,vel_y,x_bol,y_bol))
            t += 1

    elif x_bol == x_pok and y_bol == y_pok:
        print("t=    %4d    vy=    %4d    x=    %4d    y=    %4d"%(t,vel_yini,x_bol,y_bol))
   
    else:
        while y_bol > 0 and x_bol < x_pok:
            x_bolini = x_trein 
            y_bolini = y_trein
            x_bol = int(x_bolini + t)
            y_bol = int((y_bolini) + (vel_yini * t) - ((g / 2) * (t**2)))
            vel_y = int(vel_yini - g * t)
            print("t=    %4d    vy=    %4d    x=    %4d    y=    %4d"%(t,vel_y,x_bol,y_bol))
            t += 1
                
    if x_bol != x_pok or y_bol != y_pok:
        print("\nA pokebola nao atingiu o pokemon.")
    else:
        print("\nA pokebola atingiu o pokemon.")
    cont += 1
