from pymatgen import Composition, Element
from pymatgen.ext.matproj import MPRester
from pymatgen.ext.matproj import MPRester
from pymatgen.core.composition import Composition
from pymatgen.core.periodic_table import Element
from pymatgen.core.structure import Structure
import numpy as np
from numpy import zeros, mean
import pandas as pd
from matplotlib import pyplot as plt
import os
import json
MPR = MPRester("Z16g6jms0jQ2DAsPTeQ")
current_dir = os.path.join(os.path.dirname('data'))

def get_bs_entries():
    #inquiry data
    cache = os.path.join(current_dir, 'data1')
    if os.path.exists(cache):
        print("Loading from cache.")
        with open(cache, 'r') as f:
            return json.load(f)
    else:
        print("Reading from db.")
        from pymatgen.ext.matproj import MPRester
        MPR = MPRester("2d5wyVmhDCpPMAkq")
        
        criteria = {'elements':{"$in":["Li", "Be","C", "N", "O", "Na","Mg", "Al", "Si", "P", "S", "K", "Ca", "Sc", "Ti","V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As",
            "Se", "Br", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "Cs", "Ba"]}, 
			'nelements':2,
            'icsd_ids': {'$gte': 0},
            'e_above_hull': {'$lte': 0.05},
            'band_gap': {"$gte":0.1},
            }
        props = ['structure', "material_id",'pretty_formula','e_above_hull',"band_gap","band_structure","spacegroup","band_gap.search_gap.is_direct"]
        entries = MPR.query(criteria=criteria, properties=props)
        
        new_entries=[]
        for e in entries:
            X=e
            X['structure']=X['structure'].as_dict()
            new_entries.append(X)
            
        with open(cache, 'w') as f:
            json.dump(new_entries, f)
        return entries

entries=get_bs_entries()

print(len(entries))

D = {'formula': [],'atomic_volume': [], 'band_gap': [], 'outer_electron': [], 'diff_electroneg': [], 'spacegroup':[], 'band_gap.is_direct':[]}

for e in entries:
    comp=Composition(e['pretty_formula'])
    s=Structure.from_dict(e['structure'])
    atomic_volume=s.volume/len(s)
    D['atomic_volume'].append(atomic_volume)
    D['band_gap'].append(e['band_gap'])
    D['formula'].append(e['pretty_formula'])
    D['spacegroup'].append(e['spacegroup']['point_group'])
    A=sorted(comp.elements, key=lambda el: el.X)[0] # This sorts the elements by electronegativity and takes the first element
    B=sorted(comp.elements, key=lambda el: el.X)[1] 
    D['diff_electroneg'].append(B.X-A.X)
    
    x1,y1 = map(lambda x: x.group, comp) #calculate the outer electron
    x2,y2 = map(lambda x: x.Z, comp)
    if x2 < 18 and x1 > 13:
        x1 = x1-8
    if y2 < 18 and y1 > 13:
        y1 = y1-8
    if x1 > 2:
        x1 = x1-2
    if y1 > 2:
        y1 = y1-2
    x0 = x1+y1
    D['outer_electron'].append(x0)
    
    if e['band_gap.search_gap.is_direct'] == True:
        D['band_gap.is_direct'].append(1)
    else:
        D['band_gap.is_direct'].append(0)

df = pd.DataFrame(D)
df.to_csv('data1.csv')