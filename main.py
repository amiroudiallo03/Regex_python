   
import re

# orange = ["49","07","09"]

numero = '01890902'
# numero = '05-34-54-89-09'

# reg = re.compile('(07|01|05)(?P<debut> ([-_ ]?\d{2}){4})')
# reg2 = re.compile('(00255|\d{2})(?P<debut> ([-_ ]?\d{2}){3})')
# operator = {'05': 'MTN', '01': 'MOOV', '07': 'ORANGE'}
# validator = reg.match(numero)
# mutator = reg2.match(numero)

# if mutator:
#     print(mutator.groups())


# if validator:
#     print(operator[validator.groups()[0]])
# elif mutator:
#     print('Passez à dix chiffres')
#     # print(reg2.sub('02\g<debut>', numero))
# else:
#     print('le numero invalide')


# MTN = ['54','05','04']
# ORANGE = ['07']
MTN=["04", "05", "06", "44", "45", "46", "54", "55", "56","64","65","66", "74", "75", "76", "84", "85", "86", "94", "95", "96"]
ORANGE=["07", "08", "09", "47", "48", "49", "57", "58", "59","67", "68", "69", "77", "78", "79", "87", "88", "89", "97", "98"]
MOOV=["01", "02", "03", "40", "41", "42", "43", "50", "51", "52", "53", "70", "71", "72", "73"]



reg2 = re.compile('^(00225|\+225)?([-_ ]?\d{2}){4}')

operateur = reg2.match(numero)

if operateur:
    if operateur.groups()[0] == "+225" :
        operateur.string[4:6]
        if operateur.string[4:6] in MTN :
            print('MTN')
            print(operateur.string[4:6])
            print('05'+ operateur.string[4:])
        elif operateur.string[4:6] in ORANGE :
            print('ORANGE')
            print(operateur.string[4:6])
            print('07'+ operateur.string[4:])
        elif operateur.string[4:6] in MOOV:
            print('MOOV')
            print(operateur.string[4:6])
            print('01'+ operateur.string[4:])
    elif operateur.groups()[0] ==  "00225":
        operateur.string[5:7]
        if operateur.string[5:7] in MTN :
            print('MTN')
            print(operateur.string[5:7])
            print('05'+ operateur.string[5:])
        elif operateur.string[5:7] in ORANGE :
            print('ORANGE')
            print(operateur.string[5:7])
            print('07'+ operateur.string[5:])
        elif operateur.string[5:7] in MOOV:
            print('MOOV')
            print(operateur.string[5:7])
            print('01'+ operateur.string[5:])
    else:
        if operateur.string[:2] in MTN :
            print('MTN')
            print(operateur.string[:2])
            print('05'+ operateur.string)
        elif operateur.string[:2] in ORANGE :
            print('ORANGE')
            print(operateur.string[:2])
            print('07'+ operateur.string)
        elif operateur.string[:2] in MOOV:
            print('MOOV')
            print(operateur.string[:2])
            print('01'+ operateur.string)




