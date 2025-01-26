from random import shuffle, randint

class Gun:
    """
    Representa el arma que se usará en la ronda.
    """
    def __init__(self, barrel_size: int = 6 , bullets: int = 1):
        """
        Inicializa el arma con el tamaño del barril y el número de balas en él.
        Posteriormente, revuelve las balas en el barril.

        Parámetros:
            barrel_size (int): tamaño del barril
            bullets (int): número de balas en el barril
        """
        self.barrel_size = int(barrel_size)
        self.bullets = int(bullets)
        self.barrel = [1] * self.bullets + [0] * (self.barrel_size - self.bullets)
        shuffle(self.barrel)
        print('\nArma cargada.')

    def shoot(self) -> bool:
        """
        Dispara el arma una vez y mueve el barril.

        Returns:
            bool: Bala en cartucho disparado o no
        """
        self.barrel.pop(0)
        self.barrel += [0]
        if self.barrel[0] == 1:
            print('\nBAM\nHas muerto.\n')
            return False
        else:
            print('\nCLICK\nSigues con vida.')
            return True

    def roll(self) -> None:
        """
        Gira el barril de la pistola aleatoriamente
        """
        slide = randint(0, self.barrel_size)
        self.barrel = self.barrel[slide:] + self.barrel[0:slide]
        print('\nArma revuelta.')

def setup_round() -> tuple[int, int]:
    """
    Consulta al usuario los futuros argumentos para crear el arma.

    Return:
         tuple[int, int]: tamaño del barril y número de balas en él
    """
    print('\nSetup partida')
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
            elif round_bullets < 1:
                print('\nNo hay balas en el barril.\n')
            else:
                break
        except(Exception,):
            print('\nRespuesta no válida.\n')

    return round_barrel_size, round_bullets

def star_round(barrel: int, bullets: int) -> None:
    """
    Crea el arma e inicia la partida accionándola según los métodos de la clase Gun para gatillar o revolver el barril.
    Finaliza destruyendo el objeto creado con la clase Gun.

    Parámetros:
        barrel (int): tamaño del barril
        bullets (int): número de balas en el barril
    """
    game_gun = Gun(barrel, bullets)
    alive = True
    while alive:
        choice = input('\nDesea:\n1. Dispararse\n2. Revolver\n(Ingrese número)\n')
        match choice:
            case '1':
                alive = game_gun.shoot()
            case '2':
                game_gun.roll()
            case _:
                print('\nRespuesta no valida.\n')
    del game_gun

def main() -> None:
    """
    Función principal donde se elige el inicio de una nueva partida.
    """
    print('\nBIENVENIDO A BULLET ROULETTE\n')

    while True:
        keep_playing = input('¿Desea iniciar una nueva ronda? [S/N]\n')
        if keep_playing == 'N':
            print('\n¡Adiós! Vuelva pronto.')
            break
        elif keep_playing == 'S':
            star_round(*setup_round())
        else:
            print('Respuesta no válida.\n')

if __name__ == '__main__':
    main()
