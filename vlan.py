vlan = int(input("Cual es el id de VLAN: "))
if vlan >= 1 and vlan <= 1005:
    print("Esta es una VLAN de rango normal.")
elif vlan >= 1006 and vlan <= 4095:
    print("Esta es una VLAN de rango extendida.")
else:
    print("El número de vlan es desconocido.")