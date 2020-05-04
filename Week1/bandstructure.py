from pymatgen.ext.matproj import MPRester

from pymatgen.electronic_structure.plotter import BSPlotter

MPR = MPRester("Z16g6jms0jQ2DAsPTeQ")

bs = MPR.get_bandstructure_by_material_id("mp-406")

plotter = BSPlotter(bs)
plotter.get_plot().show()