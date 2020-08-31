#UnBlocks-Gen: 3D rock mass generator and analyser
#Copyright (C) 2020  Leandro Lima Rasmussen
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#any later version.
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.

from unblocks import *

dfn = DFN()
dfn.set_RegionMaxCorner([100,100,100])
dfn.add_FractureSet()
dfn.add_FractureSet()

dfn.fractureSets[0].add_TriangularFracture([10,10,10],[80,90,70],[35,60,15])
dfn.fractureSets[0].add_CircularFracture([50,50,50],90,45,40)
dfn.fractureSets[1].add_TriangularFracture([60,35,75],[15,45,20],[85,70,40])
dfn.fractureSets[1].add_CircularFracture([30,30,60],180,90,30)

dfn.export_DFNVtk("dfnCreated")
dfn.export_RegionVtk("modelRegion")

generator = Generator()
generator.generate_RockMass(dfn)
generator.export_BlocksVtk("rockBlocks")

for i in range(len(generator.blocks)):
	generator.blocks[i].export_BlockVtk("Block"+str(i))
