class pokemon():
    pass

    def __init__(self, nombre, tag, tipo):
        self.nombre = nombre
        self.tag = tag
        self.tipo = tipo

    def descripcion(self):
        return '{1} es un pokemon de tipo {2}'.format(self.nombre, self.tag, self.tipo)


class pikachu(pokemon):

    def ataque(self, tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoAtaque)


class charmander(pokemon):

    def ataque(self, tipoAtaque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoAtaque)


nuevoPokemon = pikachu('pikachu', 'bob', 'electrico')
print(nuevoPokemon.descripcion())
print(nuevoPokemon.ataque('Hierba lazo'))
