sati=int(input('Radni sati: '))
satnica=float(input('eura/h: '))

def total_euro(sati, satnica):
    return sati*satnica

print(total_euro(sati, satnica))