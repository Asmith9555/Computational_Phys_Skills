#Part a) of Excercise 2.10:
def Binding_Energy(Z,A):
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    if A%2 != 0:
        a5 = 0
    elif (A%2 == 0) and (Z%2 == 0):
        a5 = 12
    elif (A%2 == 0) and (Z%2 != 0):
        a5 = -12
    print(a5)
    volume_term = a1*A
    surface_term = a2*(A**(2/3))
    coulomb_term = a3*((Z**2)/(A**(1/3)))
    asymmetry_term = a4*(((A-(2*Z))**2)/A)
    pairing_term = a5/(A**(1/2))
    binding_energy = (volume_term - surface_term - coulomb_term - asymmetry_term
                     + pairing_term)
    return binding_energy
print(Binding_Energy(28,58))
#Part b) modification:
def be_per_nucleon(Z,A):
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    if A%2 != 0:
        a5 = 0
    elif (A%2 == 0) and (Z%2 == 0):
        a5 = 12
    elif (A%2 == 0) and (Z%2 != 0):
        a5 = -12
    print(a5)
    volume_term = a1*A
    surface_term = a2*(A**(2/3))
    coulomb_term = a3*((Z**2)/(A**(1/3)))
    asymmetry_term = a4*(((A-(2*Z))**2)/A)
    pairing_term = a5/(A**(1/2))
    binding_energy = (volume_term - surface_term - coulomb_term - asymmetry_term
                     + pairing_term)
    be_per_nucleon = binding_energy/A
    return be_per_nucleon
print(be_per_nucleon(28,58))
#Part c) modification:
def stable_a_value(Z):
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    A = range(Z,3*Z+1,1)
    binding_energys_per_a = []
    for value in A:
        if value%2 != 0:
            a5 = 0
        elif (value%2 == 0) and (Z%2 == 0):
            a5 = 12
        elif (value%2 == 0) and (Z%2 != 0):
            a5 = -12
        pairing_term = a5/(value**(1/2))
        volume_term = a1*value
        surface_term = a2*(value**(2/3))
        coulomb_term = a3*((Z**2)/(value**(1/3)))
        asymmetry_term = a4*(((value-(2*Z))**2)/value)
        binding_energys_per_a.append((volume_term - surface_term - coulomb_term - asymmetry_term
                     + pairing_term))
    stable_binding_energy = max(binding_energys_per_a)
    stable_a_value = ((binding_energys_per_a.index(stable_binding_energy))+Z)
    return stable_binding_energy, stable_a_value
print(stable_a_value(5))
#Part d) modification
def stable_a_value_per_z():
    a1 = 15.8
    a2 = 18.3
    a3 = 0.714
    a4 = 23.2
    Z = range(1,101,1)
    binding_energys_per_a = []
    stable_binding_energys_per_z = []
    stable_a_values_per_z = []
    be_per_nucleon_per_z = []
    for z in Z:
        A = range(z,3*z+1,1)
        for value in A:
            if value%2 != 0:
                a5 = 0
            elif (value%2 == 0) and (z%2 == 0):
                a5 = 12
            elif (value%2 == 0) and (z%2 != 0):
                a5 = -12
            pairing_term = a5/(value**(1/2))
            volume_term = a1*value
            surface_term = a2*(value**(2/3))
            coulomb_term = a3*((z**2)/(value**(1/3)))
            asymmetry_term = a4*(((value-(2*z))**2)/value)
            binding_energys_per_a.append((volume_term - surface_term - coulomb_term - asymmetry_term
                      + pairing_term))
        max_binding_energy = max(binding_energys_per_a)
        stable_binding_energys_per_z.append(max_binding_energy)
        stable_a_values_per_z.append((binding_energys_per_a.index
                                 (max_binding_energy))+z)
        be_per_nucleon_per_z.append((max_binding_energy/z))
    return stable_binding_energys_per_z, stable_a_values_per_z, be_per_nucleon_per_z
print(stable_a_value_per_z())
sbe_per_z, sav_per_z, be_per_nucleon_per_z = stable_a_value_per_z()
print(be_per_nucleon_per_z.index(max(be_per_nucleon_per_z))+1)
