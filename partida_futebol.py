equipa1 = int(input("digite os golos do sporting"))
equipa2 = int(input ("digite os golos do benfica"))

diferenca_golos = abs(equipa1 - equipa2)
print("dieferença : {} " .format(diferenca_golos))
if diferenca_golos == 0 : 
    print("empate")
elif diferenca_golos in [1,2,3,4]:
    print("partida normal")
else:
    print("goleada")

print("fim")
