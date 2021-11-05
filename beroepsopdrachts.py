
import time
import sys

print("Dit is een text based applicatie dat gaat over een nieuwkomer dat moest vluchten naar een ander land om veilig te zijn.")
print("weet jij de goede keuzes te maken om veilig te blijven?")
time.sleep(1)
print("wie ben jij?")
naam = input ()
print("hallo: " + naam )
print("we gaan nu beginnen met de keuzes,veel succes!")
time.sleep(2)
print("Er is oorlog in je land en je moet gaan vluchten.")
print("Naar welk land wil je vluchten?")
print("kies n voor nederland of d voor duitsland")
antwoord = input()
print("Dat is mooi, maar hoe wil je vluchten?")
print("kies a voor alleen of s voor smokkelaar")
antwoord2 = input()
if antwoord2 == "a":
    print("Oke! het word een lange reis alleen, maar je denkt dat je het wel kan.")
    print("je word snel moe en moet iets anders vinden dan lopen.")
    print("kies a voor auto stelen, kies b voor bus")
    antwoord3 = input()
    if antwoord3 == "b":
        print("je hebt geen geld op zak en je kan niet pinnen dus probeer je zwart te rijden")
        print("de chaffeur geeft je aan en je word opgepakt")
        sys.exit()
    else: 
        print("je probeerd een auto te stelen, maar je hebt het nog nooit gedaan en laat een alarm afgaan")
        print("je krijgt de auto toch aan de praat, maar net toen je weg wilde rijden kwam de politie en werd je aangehouden voor diefstal")
        sys.exit()
else:
    print("je gaat op zoek naar een smokkelaar.")
    print("uiteindelijk kom je iemand tegen die jou wil brengen")
    print("de smokkelaar vraagt of je vooraf kunt betalen")
    print("kies j voor ja, kies n voor nee")
    antwoord4 = input()
    if antwoord4 == "j":
        print("Hij laat je pinnen en neemt je geld aan")
        print("de smokkelaar zegt dat je om half 5 bij de haven moet zijn anders heb je pech")
        time.sleep(1)
        print("je komt aan om half 5 en ziet een klein bootje met 50 andere mensen")
        print("de smokkelaar zegt dat je op moet stappen")
        print("kies d voor het doen, kies w voor loop weg")
        antwoord5 = input()
        if antwoord5 == "d":
            print("de boot begint te zinken en je raakt in paniek!")
            print("gelukkig roept iemand dat hij land ziet maar het is nog een groot stuk zwemmen zonder help")
            print("kies z voor probeer te zwemmen, kies h voor wacht tot iemand je helpt")
            antwoord13 = input()
            if antwoord13 == "z":
                print("je komt aan op land en loopt met de groep mensen mee")
                print("kies z voor zoek politie, kies i voor ga verder illegaal")
                antwoord14 = input()
                if antwoord14 == "i":
                    print("je hebt bijna geen geld meer over") 
                    print("kies w voor werk zoeken, kies s voor stelen")
                    antwoord15 = input()
                    if antwoord15 == "w":
                        print("je gaat op zoek naar werk en vind een baan in een supermarkt")
                        print("kies s voor spaar voor onderdak, kies d voor drank en drug")
                        antwoord16 = input()
                        if antwoord16 == "s":
                            print("je leeft nog lang en gelukkig")
                            print("GEFELICITEERD")
                            sys.exit()
                        else: 
                            print("je raakt verslaaft en gaat dood aan een overdosis")
                            sys.exit()
                    else:
                        print("je begint met zakkenrollen en het gaat goed dus je wilt meer")
                        print("na een lange tijd ga je drugs verkopen en word je de drugs baron van nederland")
                        print("je word gezocht door alle politie en word aangehouden")
                        sys.exit()
                else:
                    print("je vind de politie en zegt dat je asiel aan wilt vragen")
                    print("je word meegenomen en geplaats in een azc waar je een paar vragen krijgt")
                    print("uiteindelijk ben je goed genoeg en krijg je een paspoort voor Nederland")
                    print("GEfELICITEERD")
                    sys.exit()
            else:
                print("niemand komt je helpen en ze gaan allemaal zwemmen, jij blijft achter en verdrinkt op zee")
                sys.exit()
        else:
            print("je besluit weg te lopen en je hebt nu geen kans meer om te vluchten")
            print("je sterft in de oorlog door een bom")
            sys.exit()
    else:
        print("dat is slim je kunt om half 6 naar de stad komen")
        print("je komt aan en je ziet de smokkelaar bij een vrachtwagen")
        print("hij vraagt je om in te stappen en jij doet het")
        print("de smokkelaar gaat achter het stuur zitten en begint te rijden")
        print("Je stopt bij een tankstation en je moet nodig plassen")
        print("kies g voor ga naar de wc, kies h voor hou het op")
        antwoord6 = input()
        if antwoord6 == "g":
            print("De smokkelaar rijd verder en laat jou achter, omdat je te langzaam was")
            print("kies w voor wacht op iemand anders die je mee neemt, kies v voor vraag de medewerker van het tankstation om te helpen")
            antwoord7 = input()
            if antwoord7 == "v":
                print("hij geeft je een flesje water en zegt dat je weg moet gaan")
                print("je loopt snel weg en gaat verder alleen")
                print("je raakt moe en gaat even zitten langs de weg")
                print("een auto stopt naast je en vraagt of je een lift wil")
                print("kies j voor ja, kies n voor nee")
                antwoord8 = input()
                if antwoord8 == "j":
                    print("je gaat mee en je komt veilig aan zonder iets te hoeven betalen")
                    print("je bedankt de bestuurder en je stapt uit")
                    print("kies z voor zoek politie, kies i voor ga verder illegaal")
                    antwoord9 = input()
                    if antwoord9 == "i":
                        print("je hebt bijna geen geld meer over") 
                        print("kies w voor werk zoeken, kies s voor stelen")
                        antwoord18 = input()
                        if antwoord18 == "w":
                            print("je gaat op zoek naar werk en vind een baan in een supermarkt")
                            print("kies s voor spaar voor onderdak, kies d voor drank en drug")
                            antwoord17 = input()
                            if antwoord17 == "s":
                                print("je leeft nog lang en gelukkig")
                                print("GEFELICITEERD")
                                sys.exit()
                            else: 
                                print("je raakt verslaaft en gaat dood aan een overdosis")
                                sys.exit()
                        else:
                            print("je begint met zakkenrollen en het gaat goed dus je wilt meer")
                            print("na een lange tijd ga je drugs verkopen en word je de drugs baron van nederland")
                            print("je word gezocht door alle politie en word aangehouden")
                            sys.exit()
                    else:
                        print("je vind de politie en zegt dat je asiel aan wilt vragen")
                        print("je word meegenomen en geplaats in een azc waar je een paar vragen krijgt")
                        print("uiteindelijk ben je goed genoeg en krijg je een paspoort voor Nederland")
                        print("GEfELICITEERD")
                        sys.exit()
                else:
                    print("je probeerd slaap te krijgen maar je hebt het te koud en uiteindelijk sterf je van onderkoeling en honger")
                    sys.exit()
            else:
                print("je gaat naast de weg staan met je duim in de lucht en wacht dat een auto stopt")
                print("uiteindlijk stopt een auto en je vraagt of je een lift kunt krijgen")
                print("de bestuurder zegt nee")
                print("je blijft nog iets langer wachten en je krijgt toch een lift")
                print("de bestuurder brengt je en je bedankt hem")
                print("kies z voor zoek politie, kies i voor ga verder illegaal")
                antwoord10 = input()
                if antwoord10 == "i":
                    print("je word gevonden en teruggestuurd naar je eigen land") 
                else:
                    print("je vind de politie en zegt dat je asiel aan wilt vragen")
                    print("je word meegenomen en geplaats in een azc waar je een paar vragen krijgt")
                    print("uiteindelijk ben je goed genoeg en krijg je een paspoort voor Nederland")
                    print("GEfELICITEERD")
                    sys.exit()
        else:
            print("je houd het op en de smokkelaar rijd weer verder")
            print("je komt aan en de smokkelaar zet je af")
            print("je wilt net weg lopen, maar je word terug geroepen omdat je nog moet betalen")
            print("kies r voor ren weg, kies b voor betaal")
            antwoord11 = input()
            if antwoord11 == "r":
                print("hij pakt een pistool en schiet je neer")
                sys.exit()
            else:
                print("je betaalt de smokkelaar en loopt snel weg")
                print("kies z voor zoek politie, kies i voor ga verder illegaal")
                antwoord12 = input()
                if antwoord12 == "i":
                    print("je word gevonden en teruggestuurd naar je eigen land") 
                else:
                    print("je vind de politie en zegt dat je asiel aan wilt vragen")
                    print("je word meegenomen en geplaats in een azc waar je een paar vragen krijgt")
                    print("uiteindelijk ben je goed genoeg en krijg je een paspoort voor Nederland")
                    print("GEfELICITEERD")
                    sys.exit()