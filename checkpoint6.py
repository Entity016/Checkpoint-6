class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

# Crear un objeto usando la clase Usuario
usuario1 = Usuario("entity016", "contraseña_segura")

# Imprimir los atributos del objeto para verificar
print(f'Nombre de usuario: {usuario1.username}')
print(f'Contraseña: {usuario1.password}')