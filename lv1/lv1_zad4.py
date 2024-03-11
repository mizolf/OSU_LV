rijeciPjesme={}

datoteka=open('song.txt')
for line in datoteka:
    line.rsplit()
    rijeci=line.split(' ')
    for rijec in rijeci:
        if rijec not in rijeciPjesme:
            rijeciPjesme[rijec]=1
            continue
        rijeciPjesme[rijec]+=1

jedinstveneRijeci=0
for rijec in rijeciPjesme:
    if rijeciPjesme[rijec]==1:
        jedinstveneRijeci+=1
        print(f"{rijec}:{rijeciPjesme[rijec]}")

print(jedinstveneRijeci)