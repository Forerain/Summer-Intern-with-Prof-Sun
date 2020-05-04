from pymatgen.ext.matproj import MPRester
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
from pymatgen.core.composition import Composition
from pymatgen.core.periodic_table import Element
from pymatgen.core.structure import Structure
import plotly.express as px
import plotly

MPR = MPRester("Z16g6jms0jQ2DAsPTeQ")

criteria = {'elements': {"$in": ["O", "S", "Se", "Te"], "$all": ["Si"]},
            'icsd_ids': {'$gte': 0},
            'e_above_hull': {'$lte': 0.01},
            'band_gap': {"$gt": 0.1},
            }

props = ['structure', "material_id", 'pretty_formula', 'e_above_hull', "band_gap", "band_structure"]

entries = MPR.query(criteria=criteria, properties=props)

new_entries = []
for e in entries:
    X = e
    X['structure'] = X['structure'].as_dict()
    new_entries.append(X)

D = {'atomic_volume': [], 'band_gap': [], 'mpid': [], 'formula': [], 'name': [], 'diff_electroneg': []}

for e in new_entries:
    comp = Composition(e['pretty_formula'])
    s = Structure.from_dict(e['structure'])
    atomic_volume = s.volume / len(s)

    D['atomic_volume'].append(atomic_volume)
    D['band_gap'].append(e['band_gap'])
    D['mpid'].append(e['material_id'])
    D['formula'].append(e['pretty_formula'])

    A = sorted(comp.elements, key=lambda el: el.X)[0]
    B = sorted(comp.elements, key=lambda el: el.X)[1]
    D['diff_electroneg'].append(B.X - A.X)

    name = e['material_id'] + ': ' + e['pretty_formula']
    D['name'].append(name)

df = pd.DataFrame(D)

fig = px.scatter(df, x="atomic_volume", y="band_gap", color='diff_electroneg', hover_name='name')
plotly.offline.plot(fig, filename='BandGapvsDensitySi.html')