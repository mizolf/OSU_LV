try:
    ocjena=float(input('Unesite ocjenu: '))
    if ocjena<0 or ocjena>1:
        raise ValueError()
    
    if ocjena>=0.9 and ocjena<1:
        print('A')
    elif ocjena>=0.8 and ocjena<0.9:
        print('B')
    elif ocjena>=0.7 and ocjena<0.8:
        print('C')
    elif ocjena>=0.6 and ocjena<0.7:
        print('D')
    else:
        print('F')
           
except ValueError:
    print('Pogreška')