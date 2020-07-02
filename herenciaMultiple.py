class Telefono():
    def __init__(self):
        pass

    def llamar(self):
        print('Llamando...')

    def ocupado(self):
        print('Ocupado...')


class Camara():
    def __init__(self):
        pass

    def fotografia(self):
        print('Tomando foto...')


class Reproduccion():
    def __init__(self):
        pass

    def reproduccionDeMusica():
        print('Reproduciendo musica...')

    def reproduccionDeVideo():
        print('Reproduciendo video...')


class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print('Telefono apagado')


movil = smartphone()
print(movil.llamar())
print(dir(movil))
