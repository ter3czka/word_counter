import argparse
import sys

def main():
    argumenty = muj_argparser.parse_args()
    
    muj_argparser = argparse.ArgumentParser(description="Word Counter je program, který počítá ze vstupního souboru řádky, slova, znaky.")
    muj_argparser.add_argument("soubor", help="vstupni soubory")
    muj_argparser.add_argument("--radky", help="napise radky", action="store_true" )
    muj_argparser.add_argument("--slova", help="napise slova", action="store_true")
    muj_argparser.add_argument("--znaky", help="napise znaky", action="store_true")
    try:
        file = open(argumenty.soubor, "r")
        nazev = file.read()
        
        if argumenty.radky:
            pocet_radku = len(nazev.split('\n'))
            print(f"Počet řádků: {pocet_radku}")
            file.close()
        if argumenty.slova:
            pocet_slov = nazev.count(' ') + len(nazev.split('\n'))
            print(f"Počet slov: {pocet_slov}")   
            file.close()
        if argumenty.znaky:
            pocet_znaku = len(nazev)
            print(f"Počet znaků: {pocet_znaku}")
            file.close()
            
            
    except:
           print("Nefunkční stránka.")
           sys.exit()
    except:
           print("Chyba. Zkuste to znovu.")
           sys.exit()       
        
   if __name__ == '__main__':
       main()