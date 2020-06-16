# clase

class Nombre(object):
    edad = ''
    sexo = ''
    pais = ''
    pass


victor = Nombre()
maria = Nombre()

# objeto.atributo = valor
victor.edad = 18
victor.sexo = 'masculino'
victor.pais = 'bolivia'

maria.edad = 30
maria.sexo = 'femenino'
maria.pais = 'colombia'

print(victor.edad)
print(maria.edad)
