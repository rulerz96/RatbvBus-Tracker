import ratbv_data
import time
import argparse

def credit():
    rulerzCredit =  """ 
                _                ___   __   
     _ __ _   _| | ___ _ __ ____/ _ \ / /_  
    | '__| | | | |/ _ \ '__|_  / (_) | '_ \ 
    | |  | |_| | |  __/ |   / / \__, | (_) |
    |_|   \__,_|_|\___|_|  /___|  /_/ \___/ 
        """
    return rulerzCredit

def clear():
    print('\n' * 30)
    return None

def decebalToLivada():
    try:
        while True:
            clear()
            data = ratbv_data.getDataDecebal()
            print('\n[*] Statia Decebal - Livada Postei\n')
            for bus in data:
                print('   {}\t{}\t{}'.format(bus[0], bus[1], bus[2]))
            print()
            time.sleep(30)
    except:
        KeyboardInterrupt

def judeteanToLivada():
    try:
        while True:
            clear()
            data = ratbv_data.getDataJudetean()
            print('\n[*] Statia Judetean - Livada Postei')
            for bus in data:
                print('{}\t{}\t{}'.format(bus[0], bus[1], bus[2]))
            print()
            time.sleep(30)
    except:
        KeyboardInterrupt


def menuLogic():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=credit())
    parser.add_argument('--decebal', help='monitor all buses from decebal-livada', action='store_true')
    parser.add_argument('--judetean', help='monitor all buses from judetean-livada', action='store_true')
    args = parser.parse_args()

    if args.decebal:
        decebalToLivada()
    if args.judetean:
        judeteanToLivada()


def main():
    menuLogic()
    return None


if __name__ == '__main__':
    main()
