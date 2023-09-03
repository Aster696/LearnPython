class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return f'Planet {self.name} is orbiting around {self.system}'

hoth = Planet('HOTH', 200000, 5.5, 'Hoth System')
print(hoth.name)
print(hoth.radius)
print(hoth.gravity)
print(hoth.system)


naboo = Planet('Naboo', 200000, 5.5, 'Naboo System')
print(naboo.name)
print(naboo.radius)
print(naboo.gravity)
print(naboo.system)
