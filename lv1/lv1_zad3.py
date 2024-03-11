brojevi=[]

while(True):
    try:
        x=(input())
        if x=='Done':
            break
        x=float(x)
        brojevi.append(x)
    except:
        print('greška')

print('Uneseno brojeva: ',len(brojevi))
print('Min vrijednost: ' ,min(brojevi))
print('Max vrijednost: ',max(brojevi))

zbroj=0
for i in range(0, len(brojevi)):
    zbroj+=brojevi[i]

print('Srednja vrijednost: ',zbroj/len(brojevi))

brojevi.sort()
print('Sortirana lista: ',brojevi)
