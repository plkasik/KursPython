liczba_elementow = int(input("podaj mi liczbę elementów do wysłania:"))
suma_wszystkich_kilogramow = 0
waga_paczki = 0
ilosc_paczek = 1
suma_pustych_kilogramow = 0
paczka_z_najwieksza_iloscia_pustych_kilogramow = 1
najwiecej_pustych_kilogramow = 0
nieprawidlowa_waga_elementu = 0
waga_elementu = [1,2,3,4,5,6,7,8,9,10]
for element in range (liczba_elementow):
        waga_elementu = float(input("podaj mi wage elementu:"))
        if waga_elementu > 0 and waga_elementu < 10:
            print(f"prawidłowa waga elementu, dodaje element do paczki")

        else:
            print(f"nieprawidłowa waga elementu, rozpocznij od nowa")
            break
        suma_wszystkich_kilogramow += waga_elementu

if waga_elementu + waga_paczki < 20:
        waga_paczki += waga_elementu
else:
        suma_pustych_kilogramow += (20 - waga_paczki)
        puste_kilogramy_w_tej_paczce = 20 - waga_paczki
        if puste_kilogramy_w_tej_paczce > najwiecej_pustych_kilogramow:
            paczka_z_najwieksza_iloscia_pustych_kilogramow = ilosc_paczek
            najwiecej_pustych_kilogramow = puste_kilogramy_w_tej_paczce
            ilosc_paczek += 1
            waga_paczki = waga_elementu
            puste_kilogramy_w_ostatniej_paczce = 20 - waga_paczki
            suma_pustych_kilogramow += (20 - waga_paczki)
        if puste_kilogramy_w_ostatniej_paczce > najwiecej_pustych_kilogramow:
            paczka_z_najwieksza_iloscia_pustych_kilogramow = ilosc_paczek
            najwiecej_pustych_kilogramow = puste_kilogramy_w_ostatniej_paczce

print(f"Suma wszystkich kilogramow wyslanych to: {suma_wszystkich_kilogramow}" )
print(f"liczba wszystkich paczek to: {ilosc_paczek}")
print(f"liczba pustych kilogramow w paczkach to: {suma_pustych_kilogramow}")
print(f"najmniej kilogramow było wysłanych w paczce {paczka_z_najwieksza_iloscia_pustych_kilogramow},było to: {najwiecej_pustych_kilogramow}")





