import math
import os

def clear_screen():
    # Voor Windows
    if os.name == 'nt':
        os.system('cls')
    # Voor Mac en Linux
    else:
        os.system('clear')

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Voer alstublieft een numerieke waarde in.")

def get_formula(prompt):
    while True:
        formula = input(prompt)
        if formula in ['1', '2', '3', '4']:
            return formula
        print("Ongeldige invoer. Voer alstublieft een formule in zoals 1, 2, 3, of 4")

def optellen(num1, num2): return num1 + num2
def aftrekken(num1, num2): return num1 - num2
def vermenigvuldigen(num1, num2): return num1 * num2
def delen(num1, num2): return num1 / num2

while True:
    print("\nWelke rekenmachine wil je gebruiken?")
    print("1. Basis rekenmachine")
    print("2. Elektriciteit")
    print("3. Computer")
    wat_rekenen = input("Kies een optie (1, 2 of 3): ")

    if wat_rekenen == '1':
        clear_screen()
        numer1 = get_number("Voer een eerste nummer in: ")
        formula = input("Welke formule wil je gebruiken? Kies uit +, -, /, *: ")
        numer2 = get_number("Voer een tweede nummer in: ")

        if formula == "+":
            uitkomst = optellen(numer1, numer2)
        elif formula == "-":
            uitkomst = aftrekken(numer1, numer2)
        elif formula == "/":
            uitkomst = delen(numer1, numer2)
        elif formula == "*":
            uitkomst = vermenigvuldigen(numer1, numer2)
        else:
            uitkomst = "Het berekenen is niet gelukt."
        print("Uitkomst:", uitkomst)

    elif wat_rekenen == '2':
        clear_screen()
        print("\nElektriciteitsformules:")
        print("1. Wet van Ohm")
        print("2. Vermogenswet")
        print("3. Arbeidsfactor (Vermogendriehoek)")
        print("4. Periodeduur (T)")
        print("5. Hoekfrequentie (Hz) (Rad/s)")
        print("6. Maximale waarde van sinus (Um) of (Im) en effectieve waarde van sinus (U) of (I)")
        print("7. Piek tot piek waarde sinus (Upp) of (Ipp) ")
        print("8. Ogenblikkelijk waarde of momentele waarde ")
        print("9. Sinus graden, radialen, tijd berken ")
        print("10. Transformater verhouding")
        print("11. Redement")
        print("12. Cosinus phi")
        print("13. Draaddoorsnede berekenen bij zeer lage veiligheidsspanning")
        suboptie = input("Kies een optie (1-12): ")

        if suboptie == '1': # De wet van OHM
            clear_screen()
            print("Wat wil je berekenen:")
            print("1. Spanning")
            print("2. Stroom")
            print("3. Weerstand")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == "1":
                stroom = get_number("Wat is de stroom (A)? ")
                weerstand = get_number("Wat is de weerstand (R)? ")
                print("De spanning is gelijk aan", stroom * weerstand, "V")

            elif berekening == "2":
                spanning = get_number("Wat is de spanning (U)? ")
                weerstand = get_number("Wat is de weerstand (R)? ")
                print("De stroom is gelijk aan", spanning / weerstand, "A")

            elif berekening == "3":
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                print("De weerstand is gelijk aan", spanning / stroom, "Ω")

        elif suboptie == '2': # Vermogens wet
            clear_screen()
            print("Wat wil je berekenen:")
            print("1. Vermogen")
            print("2. Stroom")
            print("3. Spanning")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == "1":
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                cosinus_phi = get_number("Wat is de cosinus phi (cos φ)? ")
                print("Het vermogen is gelijk aan", spanning * stroom * cosinus_phi, "W")

            elif berekening == "2":
                vermogen = get_number("Wat is het vermogen (W)? ")
                spanning = get_number("Wat is de spanning (U)? ")
                cosinus_phi = get_number("Wat is de cosinus phi (cos φ)? ")
                print("De stroom is gelijk aan", vermogen / spanning * cosinus_phi, "A")

            elif berekening == "3":
                vermogen = get_number("Wat is het vermogen (W)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                cosinus_phi = get_number("Wat is de cosinus phi (cos φ)? ")
                print("De spanning is gelijk aan", vermogen / stroom * cosinus_phi, "V")

        elif suboptie == '3': # Arbeidsfactor
            clear_screen()
            print("Wat wil je berekenen:")
            print("1. Vermogen (W)")
            print("2. Schijnbaar vermogen (VA)")
            print("3. Reactief vermogen (VAR)")
            print("4. Cosinus phi (cos φ)")
            berekening = get_formula("Kies een optie (1, 2, 3 of 4): ")

            if berekening == "1":
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                cosinus_phi = get_number("Wat is de cosinus phi (cos φ)? ")
                vermogen = spanning * stroom * cosinus_phi
                print("Het vermogen is gelijk aan", vermogen, "W")

            elif berekening == "2":
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                schijnbaar_vermogen = spanning * stroom
                print("Het schijnbaar vermogen is gelijk aan", schijnbaar_vermogen, "VA")

            elif berekening == "3":
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                cosinus_phi = get_number("Wat is de cosinus phi (cos φ)? ")
                schijnbaar_vermogen = spanning * stroom
                vermogen = spanning * stroom * cosinus_phi
                reactief_vermogen = (schijnbaar_vermogen ** 2 - vermogen ** 2) ** 0.5
                print("Het reactief vermogen is gelijk aan", reactief_vermogen, "VAR")

            elif berekening == '4':
                vermogen = get_number("Wat is het vermogen (W)? ")
                spanning = get_number("Wat is de spanning (U)? ")
                stroom = get_number("Wat is de stroom (A)? ")
                schijnbaar_vermogen = spanning * stroom
                cosinus_phi = vermogen / schijnbaar_vermogen
                print("De cosinus phi (cos φ) is gelijk aan", cosinus_phi)

        elif suboptie == '4': # Periodeduur
            clear_screen()
            print("Wat wil je berekenen:")
            print("1. Periode duur (T)")
            print("2. Frequentie (f)")
            berekening = get_formula("Kies een optie (1 of 2): ")

            if berekening == '1':
                frequentie = get_number("Wat is de frequentie (f)? ")
                periodeduur = 1 / frequentie
                print("De periodeduur is gelijk aan", periodeduur, "per seconde")
            elif berekening == '2':
                periodeduur = get_number("Wat is de periode duur (T)? ")
                frequentie = 1 / periodeduur
                print("De frequentie is gelijk aan", frequentie, "Hz")

        elif suboptie == '5': #Hoekfrequentie
            clear_screen()
            print("Wat wil je berekenen:")
            print("1. Radialen (w)")
            print("2. Frequentie (f)")
            berekening = get_formula("Kies een optie (1 of 2): ")

            if berekening == "1":
                frequentie = get_number("Wat is de frequentie (f)? ")
                pi = 3.141592653589793
                radialen = (2 * pi) * frequentie
                print("De radialen zijn", radialen, "rad/s")

            elif berekening == "2":
                radialen = get_number("Wat is de hoekfrequentie (rad/s)? ")
                pi = 3.141592653589793
                frequentie = radialen / (2 * pi)
                print("De frequentie is gelijk aan", frequentie, "Hz")

        elif suboptie == '6': #Maximale waarde
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Maximale waarde van sinus (Um) of (Im)")
            print("2. De effectieve waarde (U) of (I)")
            berekening = get_formula("Kies een optie (1 of 2): ")

            if berekening == "1":
                effectieve_waarde = get_number("Wat is de spanning (U) of Stroom (A)? ")
                maximale_waarde = effectieve_waarde * 1.414213562
                print("De maximale waarde is gelijk aan", maximale_waarde, "(V) of (A)")
            elif berekening == "2":
                maximale_waarde = get_number("Wat is de maximale waarde (U) of (I)? ")
                effectieve_waarde = maximale_waarde / 1.414213562
                print("De effectieve waarde is gelijk aan", effectieve_waarde, "(V) of (A)")

        elif suboptie == '7': #Piek tot piek waarde
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Piek-tot-piek waarde van de sinus (Upp) of (Ipp)")
            print("2. De maximale waarde (Um)")
            berekening = get_formula("Kies een optie (1 of 2): ")

            if berekening == "1":
                maximale_waarde = get_number("Wat is de maximale waarde (Um) of (Im)? ")
                piek_tot_piek_waarde = 2 * maximale_waarde
                print("De piek-tot-piek waarde is gelijk aan", piek_tot_piek_waarde, "(V) of (A)")
            elif berekening == "2":
                piek_tot_piek_waarde = get_number("Wat is de piek-tot-piek waarde (Upp) of (Ipp)? ")
                maximale_waarde = piek_tot_piek_waarde / 2
                print("De maximale waarde is gelijk aan", maximale_waarde, "(V) of (A)")

        elif suboptie == '8': #Ogenblikkelijk waarde
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. De ogenblikkelijke waarde (Ueff) of (Ieff)")
            print("2. Maximale waarde (Um) of (Im)")
            print("3. Sinus alpha (Sina)")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == "1":
                maximale_waarde = get_number("Geef de maximale waarde (Um) of (Im): ")
                graden_hoek = get_number("Geef de gradenhoek van de sinus: ")
                sinus_alpha = math.sin(math.radians(graden_hoek))
                effectieve_waarde = maximale_waarde * sinus_alpha
                print("De effectieve waarde is gelijk aan", effectieve_waarde, "(V) of (A)")

            if berekening == "2":
                effectieve_waarde = get_number("Geef de ogenblikkelijke (Ueff) of (Ieff) waarde in: ")
                graden_hoek = get_number("Geef de gradenhoek van de sinus: ")
                sinus_alpha = math.sin(math.radians(graden_hoek))
                maximale_waarde = effectieve_waarde / sinus_alpha
                print("De maximale waarde is", maximale_waarde, "(V) of (A)")

            if berekening == "3":
                effectieve_waarde = get_number("Geef de ogenblikkelijke waarde in (Ueff) of (Ieff): ")
                maximale_waarde = get_number("Geef de maximale waarde in (Um) of (Im): ")
                verhouding = effectieve_waarde / maximale_waarde
                hoek_in_radialen = math.asin(verhouding)
                hoek_in_graden = math.degrees(hoek_in_radialen)
                print("De gradenhoek van de sinus alpha is gelijk aan", hoek_in_graden, "graden")

        elif suboptie == '9': # Sinus aplha
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Sinushoek in graden")
            print("2. Radialen berekenen van sinus")
            print("3. De tijd in seconden")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == '1':
                radialen = get_number("Geef het aantal radialen in (rad/s): ")
                tijd = get_number("Geef de tijd in seconden in (t): ")
                hoek_in_radialen = radialen * tijd
                hoek_in_graden = math.degrees(hoek_in_radialen)
                print("De hoek is gelijk aan", hoek_in_graden, "graden")

            if berekening == "2":
                graden_hoek = get_number("Geef de gradenhoek van de sinus: ")
                tijd = get_number("Geef de tijd in seconden in (t): ")
                hoek_in_radialen = math.radians(graden_hoek)
                radialen = hoek_in_radialen / tijd
                print("Het aantal radialen is gelijk aan", radialen, "radialen")

            if berekening == "3":
                radialen = get_number("Geef het aantal radialen in (rad/s): ")
                hoek_in_graden = get_number("Geef de hoek in graden: ")
                hoek_in_radialen = math.radians(hoek_in_graden)
                tijd = hoek_in_radialen / radialen
                print("De tijd is gelijk aan", tijd, "seconden")

        elif suboptie == '10': # Verhouding transfo
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. De verhouding van de transformator")
            print("2. De spanning van de spoel")
            print("3. De windingen van de transformator")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == '1':
                spoel_effectieve_waarde = get_number("Geef de spanning of de stroom van de transformator: ")
                wikkelingen = get_number("Geef het aantal wikkelingen van de spoel: ")
                verhouding = spoel_effectieve_waarde / wikkelingen
                print("De verhouding is gelijk aan", verhouding)

            if berekening == '2':
                verhouding = get_number("Geef de verhouding van de transformator: ")
                wikkelingen = get_number("Geef het aantal wikkelingen van de spoel: ")
                spoel = verhouding * wikkelingen
                print("De spanning of stroom van de spoel is gelijk aan", spoel, "(V) of (A)")

            if berekening == '3':
                spoel = get_number("Geef de spanning of stroom van de spoel: ")
                verhouding = get_number("Geef de verhouding van de transformator: ")
                wikkelingen = spoel / verhouding
                print("Het aantal wikkelingen van de spoel is gelijk aan", wikkelingen)

        elif suboptie == '11':  # Rendement
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Het rendement")
            print("2. Het nuttige vermogen")
            print("3. Het totale vermogen")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == '1':
                vermogen = get_number("Geef het nuttige vermogen in: ")
                schijnbaar_vermogen = get_number("Geef het totale vermogen in: ")
                rendement = vermogen / schijnbaar_vermogen
                rendement_procent = rendement * 100
                print("Het rendement is gelijk aan", rendement, "of", rendement_procent, "%")

            if berekening == '2':
                rendement = get_number("Geef het rendement in, bv (0.70): ")
                schijnbaar_vermogen = get_number("Geef het totale vermogen in: ")
                vermogen = rendement * schijnbaar_vermogen
                print("Het nuttige vermogen is", vermogen, "W")

            if berekening == '3':
                vermogen = get_number("Geef het nuttige vermogen in: ")
                rendement = get_number("Geef het rendement van het toestel in, bv (0.70): ")
                schijnbaar_vermogen = vermogen / rendement
                print("Het totale vermogen is", schijnbaar_vermogen, "W")

        elif suboptie == '12':  # Cosinus phi
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Cosinus phi")
            print("2. Het vermogen")
            print("3. Het totale vermogen")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == '1':
                vermogen = get_number("Geef het nuttige vermogen in (W): ")
                schijnbaar_vermogen = get_number("Geef het schijnbare vermogen in (VA): ")
                cosinus_phi = vermogen / schijnbaar_vermogen
                print("De cosinus phi is gelijk aan", cosinus_phi)

            elif berekening == '2':
                cosinus_phi = get_number("Geef de cosinus phi (bijv. 0.8): ")
                schijnbaar_vermogen = get_number("Geef het schijnbare vermogen in (VA): ")
                vermogen = cosinus_phi * schijnbaar_vermogen
                print("Het nuttige vermogen is gelijk aan", vermogen, "W")

            elif berekening == '3':
                cosinus_phi = get_number("Geef de cosinus phi (bijv. 0.8): ")
                vermogen = get_number("Geef het nuttige vermogen in (W): ")
                schijnbaar_vermogen = vermogen / cosinus_phi
                print("Het schijnbare vermogen is gelijk aan", schijnbaar_vermogen, "VA")

        elif suboptie == '13': # Draad door snede op zeer lage veiligheid spanning
            clear_screen()
            print("Wat wil je berekenen?")
            print("1. Doorsnede bij zeer lage veiligheidsspanning")
            print("2. De lengte van de kabel (draad)")
            print("3. Het vermogen van de verbruiker")
            berekening = get_formula("Kies een optie (1, 2 of 3): ")

            if berekening == '1':
                vermogen = get_number("Wat is het totale vermogen van de verbruiker of verbruikers (W): ")
                lengte = get_number("Hoe lang is de kabel van de verbruiker (meter): ")
                draaddoorsnede = (vermogen * lengte) / 200
                print("De draaddoorsnede van de verbruiker is gelijk aan", draaddoorsnede, "mm²")

            elif berekening == '2':
                draaddoorsnede = get_number("Wat is de draaddoorsnede (mm²): ")
                vermogen = get_number("Wat is het totale vermogen van de verbruiker of verbruikers (W): ")
                lengte = (200 * draaddoorsnede) / vermogen
                print("De lengte van de kabel is gelijk aan", lengte, "meter")

            elif berekening == '3':
                draaddoorsnede = get_number("Wat is de draaddoorsnede (mm²): ")
                lengte = get_number("Hoe lang is de kabel (meter): ")
                vermogen = (200 * draaddoorsnede) / lengte
                print("Het vermogen van de verbruiker is gelijk aan", vermogen, "W")

        else:
            print("Heef aub een numer in van 1 tot 13.")
    elif wat_rekenen == '3':
        clear_screen()
        print("\nComputer:")
        print("1. Decimaal en Hexadecimaal")
        print("2. Subnet rekenmachine ")
        suboptie = input("Kies een optie (1): ")

        if suboptie == '1':
            clear_screen()
            keuze = input("Kies een conversie:\n1. Decimaal naar Hexadecimaal\n2. Hexadecimaal naar Decimaal\n")

            if keuze == '1':
                decimaal_getal = get_number("Voer een decimaal getal in: ")
                hex_getal = hex(int(decimaal_getal))[2:]  # Verwijder de "0x" prefix
                print("Het hexadecimale getal is:", hex_getal)
            elif keuze == '2':
                while True:
                    try:
                        hexadecimaal_getal = int(input("Voer een hexadecimaal getal in: "), 16)
                        print("Het decimale getal is:", hexadecimaal_getal)
                        break
                    except ValueError:
                        print("Ongeldige invoer. Voer alstublieft een geldig hexadecimaal getal in.")
            else:
                print("Ongeldige keuze. Kies alstublieft 1 of 2.")

        elif suboptie == '2':
            clear_screen()
            import ipaddress

            def subnet_calculator(ip_address, subnet_mask, required_hosts):
                # Functie om het IP-adres in binaire vorm te converteren
                def ip_to_bin(ip):
                    return ''.join(f'{int(octet):08b}' for octet in ip.split('.'))

                # Functie om het binaire IP-adres om te zetten naar decimaal
                def bin_to_ip(binary_ip):
                    return '.'.join(str(int(binary_ip[i:i + 8], 2)) for i in range(0, 32, 8))

                # Functie om het netwerkadres te berekenen
                def calculate_network_address(ip_bin, mask_bin):
                    return ''.join('1' if ip_bin[i] == '1' and mask_bin[i] == '1' else '0' for i in range(32))

                # Functie om het broadcastadres te berekenen
                def calculate_broadcast_address(network_bin, mask_bin):
                    return ''.join(network_bin[i] if mask_bin[i] == '1' else '1' for i in range(32))

                # Functie om het aantal bruikbare hosts te berekenen
                def calculate_number_of_hosts(mask_bin):
                    return 2 ** mask_bin.count('0') - 2

                # Functie om het eerste bruikbare IP-adres te berekenen
                def calculate_first_usable_ip(network_bin):
                    first_usable_bin = network_bin[:-1] + '1'
                    return bin_to_ip(first_usable_bin)

                # Functie om het laatste bruikbare IP-adres te berekenen
                def calculate_last_usable_ip(broadcast_bin):
                    last_usable_bin = broadcast_bin[:-1] + '0'
                    return bin_to_ip(last_usable_bin)

                # Functie om de DHCP-bereik te berekenen
                def calculate_dhcp_range(last_usable_ip, required_hosts):
                    last_ip = int(ipaddress.IPv4Address(last_usable_ip))
                    first_ip = last_ip - required_hosts + 1
                    return ipaddress.IPv4Address(last_ip), ipaddress.IPv4Address(first_ip)

                try:
                    ip_bin = ip_to_bin(ip_address)
                    mask_bin = ip_to_bin(subnet_mask)
                    network_bin = calculate_network_address(ip_bin, mask_bin)
                    broadcast_bin = calculate_broadcast_address(network_bin, mask_bin)

                    network_address = bin_to_ip(network_bin)
                    broadcast_address = bin_to_ip(broadcast_bin)
                    number_of_hosts = calculate_number_of_hosts(mask_bin)

                    # Controleer of het gewenste aantal hosts niet groter is dan het maximale aantal hosts
                    if required_hosts > number_of_hosts - 1:  # -1 om rekening te houden met de gereserveerde router IP
                        print(
                            f"Het aantal gewenste hosts overschrijdt het maximale aantal hosts ({number_of_hosts - 1}).")
                        return None, None, None, None, None, None, None

                    first_usable_ip = calculate_first_usable_ip(network_bin)
                    last_usable_ip = calculate_last_usable_ip(broadcast_bin)

                    # Zorg ervoor dat het DHCP-bereik rekening houdt met de gereserveerde IP-adressen
                    dhcp_first, dhcp_last = calculate_dhcp_range(last_usable_ip, required_hosts)

                    return network_address, broadcast_address, number_of_hosts, first_usable_ip, last_usable_ip, dhcp_first, dhcp_last

                except ValueError:
                    print("Onjuist IP-adres of subnetmasker ingevoerd.")
                    return None, None, None, None, None, None, None

            try:
                ip = input("Geef een IP-adres in, bijvoorbeeld (192.168.0.1): ")
                subnet = input("Geef een subnetmasker in, bijvoorbeeld (255.255.255.0): ")
                required_hosts = int(input("Geef het aantal gewenste hosts: "))
                network, broadcast, hosts, first_usable, last_usable, dhcp_first, dhcp_last = subnet_calculator(ip,subnet,required_hosts)

                if network is not None:
                    print(f'Netwerkadres: {network}')
                    print(f'Broadcastadres: {broadcast}')
                    print(f'Aantal bruikbare hosts: {hosts}')
                    print(f'Eerste bruikbare IP-adres: {first_usable}')
                    print(f'Laatste bruikbare IP-adres: {last_usable}')
                    print(f'DHCP-bereik: {dhcp_last} - {dhcp_first}')
            except KeyboardInterrupt:
                print("\nDe invoer is afgebroken door de gebruiker.")
            except Exception as e:
                print(f"Er is een fout opgetreden: {e}")

    opnieuw = input("Wil je nog een berekening maken? (ja/nee): ").strip().lower()
    if opnieuw not in ['ja', 'j']:
        print("Bedankt voor het gebruiken van de rekenmachine. Tot ziens!")
        break
