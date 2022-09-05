meioTrans = input("o transporte é terrestre? (s- sim | n- não)")
if meioTrans == "s":
    qtdPessoas = input("cabe apenas uma pessoas? (s- sim | n- não)")
    if qtdPessoas == "s":
        peso = input ("o transporte é pesado? (s- sim | n- não)")
        if peso == "s":
            print ("você escolheu trator!")
        else:
            print ("vocÊ escolheu bicicleta!")
    else:
        Capacete = input("o transporte usa capacete? (s- sim | n- não")
        if Capacete == "s":
             print ("você escolheu moto!")
        else:
            Tempassageiro = input ("o transporte tem passageiro? (s- sim | n- não")
            if Tempassageiro == "s":
                Usatrilho = input ("o transporte usa trilho? (s- sim| n- não")
                if Usatrilho == "s":
                    print ("você escolheu trem!")
                else:
                    Andanapista = input ("o transporte anda na pista? (s- sim | n- não")
                    if Andanapista == "s":
                        Ealto = input ("o transporte é alto? (s- sim | n- não")
                        if Ealto == "s":
                            Usacarroceria = input ("o transporte usa carroceria? (s- sim | n- não")
                            if Usacarroceria == "s":
                                print ("você escolheu caminhão!")
                            else:
                                Temcobrador = input ("o transporte tem cobrador? (s- sim | n- não")
                                if Temcobrador == "s":
                                    print ("você escolheu ônibus!")
                        else:
                            Eleve = input ("o transporte é leve? (s- sim | n- não")
                            if Eleve == "s":
                                print ("você escolheu carro!")
else:
    Eaerio = input ("o transporte é aério? s- sim | n- não")
    if Eaerio == "s":
        Precisapular = input ("o transporte precisa que pule? (s- sim | n- não!")
        if Precisapular == "s":
            print ("o transporte é asa delta")
        else: 
            Viajadentro = input ("viaja dentro? s- sim | n- não!")
            if Viajadentro == "s":
                Edevagar = input ("o transporte é devagar ? s- sim | n- não")
                if Edevagar == "s":
                    print ("o transporte é um balão!")
                else:
                    Tempiloto = input ("o transporte tem piloto? s- sim | n- não")
                    if Tempiloto == "s":
                        Temasasf = input ("o transporte possui asas fixas? s- sim | n-não")
                        if Temasasf == "s":
                            print ("o transporte é um avião")
                        else:
                            Fazvoovert = input ("o transporte faz voo vertical? s- sim | n- não")
                            if Fazvoovert == "s":
                                print ("o transporte é um helicóptero")
    else: 
        Eaquatico = input ("o transporte é aquático? s- sim | n- não")
        if Eaquatico == "s":
            Ecobertodagua = input ("o transporte é coberto de água? s- sim | n- não")
            if Ecobertodagua == "s":
                print ("o transporte é um submarino")
            else:
                Naveganaagua = input ("o transporte navega na água? s- sim | n- não")
                if Naveganaagua == "s":
                    Possuivela = input ("o transporte possui vela? s- sim | n- não")
                    if Possuivela == "s":
                        print ("você escolheu barco!")
                    else: 
                        Temmotor = input ("o transporte tem motor? s- sim | n- não")
                        if Temmotor == "s":
                            Ealto = input ("o transporte é alto? s- sim | n-não")
                            if Ealto == "s":
                                print ("o transporte é um navio!")
                            else:
                                Podeserdescoberto = input ("o transporte pode ser coberto? s- sim | n- não")
                                if Podeserdescoberto== "s":
                                    print ("o transporte é uma lancha")