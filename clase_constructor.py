class Persona():
    pass

    def __init__(self, nombre, ano):
        self.nombre = nombre
        self.ano = ano
        pass

    def descripcion(self):
        return '{} tiene {} anios'.format(self.nombre, self.ano)

    def comentario(self, frase):
        return '{} dijo {}'.format(self.nombre, frase)


doctor = Persona('Jose', 26)
print(doctor.descripcion())
print(doctor.comentario('Hola mundo!!'))


class email():
    pass

    def __init__(self):
        self.enviado = False

    def enviarCorreo(self):
        self.enviado = True


miCorreo = email()
print(miCorreo.enviado)
miCorreo.enviarCorreo()
print(miCorreo.enviado)
