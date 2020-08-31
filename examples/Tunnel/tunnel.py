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
import plotTools

dfn = DFN()
dfn.set_RegionMaxCorner([10,30,30])
dfn.set_RandomSeed(100)
dfn.add_FractureSet()
dfn.add_FractureSet()
dfn.add_FractureSet()
dfn.add_LineMapping([10,30,0], [0.766582,4.631392,24.30794])
dfn.add_VolumeMapping()

while (dfn.linesMapping[0].get_P10(0) < 1.2):
	dfn.fractureSets[0].add_BaecherFracture(110,48,50000,"det",200,0)

while (dfn.volumesMapping[0].get_P32(1) < 1.24):
	dfn.fractureSets[1].add_BaecherFracture(180,71,23,"log",0.725, 0.52)

while (dfn.volumesMapping[0].get_P32(2) < 2.12):
	dfn.fractureSets[2].add_BaecherFracture(258,65,30,"log",1.02, 0.445)

dfn.export_DFNVtk("dfn")
dfn.fractureSets[0].export_FractureSetVtk("set0")
dfn.fractureSets[1].export_FractureSetVtk("set1")
dfn.fractureSets[2].export_FractureSetVtk("set2")
dfn.export_RegionVtk("region")

generator = Generator()
generator.set_MinInscribedSphereRadius(0.05) 
generator.set_MaxAspectRatio(30)

generator.generate_RockMass(dfn)
generator.export_BlocksVtk("blocksBeforeExcavation")

plotTools.blockVolumeDistribution(generator.get_Volumes(False))
plotTools.blockShapeDiagram(generator.get_AlphaValues(False), generator.get_BetaValues(False), generator.get_Volumes(False), 0.05)
plotTools.BlockShapeDistribution(generator.get_AlphaValues(False), generator.get_BetaValues(False), generator.get_Volumes(False))

generator.import_ExcavationElementsObj("tunnel")  
generator.export_ExcavationElementsVtk("tunnelvtk")

generator.excavate_RockMass()
generator.export_BlocksVtk("blocksAfterExcavation")

plotTools.showPlots()



