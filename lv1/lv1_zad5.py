def prosjek_rijeci(sms_list):
    ukupno_rijeci = 0
    for sms in sms_list:
        ukupno_rijeci += len(sms.split(" "))
    return ukupno_rijeci / len(sms_list)

def zavrsava_usklicnikom(sms):
    brojac = 0
    for sms in spam:
        if sms.endswith('!'):
            brojac += 1
    return brojac

spam = []
ham = []

datoteka = open("SMSSpamCollection.txt")
for redak in datoteka:
    redak = redak.rstrip()
    dio = redak.split("\t")
    if (dio[0] == "spam"):
        spam.append(dio[1])
    elif (dio[0] == "ham"):
        ham.append(dio[1])


print("Prosjek riječi koji su tipa spam", prosjek_rijeci(spam))
print("Prosjek riječi koji su tipa ham", prosjek_rijeci(ham))
print("Broj riječi u spamu koji završavaju s uskličnikom: ", zavrsava_usklicnikom(spam))

datoteka.close()