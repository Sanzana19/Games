import random


class Barrel:
    def __init__(self, barrel_size: int, bullets: int):
        self.barrel_size = int(barrel_size)
        self.bullets = int(bullets)
        self.barrel = [1] * self.bullets + [0] * (self.barrel_size - self.bullets)
        random.shuffle(self.barrel)
        print('\nArma cargada.')

    def shoot(self):
        if self.barrel[0] == 1:
            print('\nBAM\nHas muerto.\n')
            return 0
        else:
            self.barrel.pop(0)
            self.barrel += [0]
            print('\nCLICK\nSigues con vida.')
            return 1

    def roll(self):
        slide = random.randint(0, self.barrel_size)
        self.barrel = self.barrel[slide:] + self.barrel[0:slide]
        print('\nArma revuelta.')


print('\nBIENVENIDO A BULLET ROULETTE\n')

while True:
    keep_playing = input('¿Desea iniciar una nueva ronda? [S/N]\n')
    if keep_playing == 'S' or keep_playing == 'N':
        break

while keep_playing == 'S':

    # Set up the game
    while True:
        try:
            round_barrel_size = int(input('\nIngrese tamaño del barril: '))
            if round_barrel_size > 0:
                break
            else:
                print('\nA ese barril no le entran balas.\n')
        except(Exception,):
            print('\nRespuesta no válida.\n')

    while True:
        try:
            round_bullets = int(input('Ingrese el número de balas: '))
            if round_bullets > round_barrel_size:
                print('\nDemasiadas balas para el barril.\n')
            if round_bullets < 1:
                print('\nNo hay balas en el barril.\n')
            else:
                break
        except(Exception,):
            print('\nRespuesta no válida.\n')

    game = Barrel(round_barrel_size, round_bullets)

    # Play the game
    alive = 1

    while alive:
        choose = input('\nDesea:\n1. Dispararse\n2. Revolver\n(Ingrese número)\n')
        while True:
            if choose == '1':
                alive = game.shoot()
                break
            if choose == '2':
                game.roll()
                break
            else:
                print(choose)
                print('\nRespuesta no valida.\n')
                break

    while True:
        keep_playing = input('\n¿Desea jugar otra ronda? [S/N]\n')
        if keep_playing == 'S' or keep_playing == 'N':
            break

print('\n¡Adiós! Vuelva pronto.')
bye_bye = input()
