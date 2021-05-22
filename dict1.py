#dictionary 1
samolot = {'name': 'boenig',
            'przebieg': 10000,
            'type': 'pasazerski'}

#in python3 samolot.itmes()
for key, value in samolot.items():
    print("{0}:{1}".format(key, value))

#
for key in samolot:
    print("{0}:{1}".format(key, [key]))
