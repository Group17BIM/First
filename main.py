
import ifcopenshell
from blenderbim.bim.ifc import IfcStore




file = IfcStore.get_file()
projecy = file.by_type('IfcProject')



    
beams = file.by_type("IfcBeam")

N  = len(beams)

print('There are '+ str(N) + ' beams in the building.\nEach one of which has the following dimention and position:')

for beam in beams:
    print(beam.ObjectType)
    print(beam.ObjectPlacement)

    
