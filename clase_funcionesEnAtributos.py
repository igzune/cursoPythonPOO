class Persona(object):
    edad = 27
    nombre = 'Victor'
    pais = 'Brazil'


doctor = Persona()


print('la edad es: ', doctor.edad)
print('la edad es: ', getattr(doctor, 'edad'))
# getattr() nos devuelve el varlos del atributo solicitado del objeto.

print('el doctor tiene una edad?', hasattr(doctor, 'ap'))
# hasattr() nos dice si el atributo existe o no en el objeto, devolviendo un
# booleano.


print(doctor.nombre)
setattr(doctor, 'nombre', 'Carlos')
# setattr() nos permite cambiar el valor del atributo de un objeto.
print(doctor.nombre)

print(doctor.pais)
delattr(doctor, 'pais')
# delattr() borra el atributo de un objeto.
print(doctor.pais)
