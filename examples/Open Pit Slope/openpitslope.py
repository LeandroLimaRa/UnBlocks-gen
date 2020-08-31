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
dfn.set_RegionMaxCorner([100,100,20])
dfn.set_RandomSeed(10)
dfn.add_FractureSet()
dfn.add_FractureSet()
dfn.add_QuadrilateralMapping([0,0,20],[100,0,20],[100,100,20],[0,100,20])
dfn.add_VolumeMapping()

while (dfn.surfacesMapping[0].get_P21(0) < 0.2):
	dfn.fractureSets[0].add_BaecherFracture(90, 45, 20, "exp", 40, 0);
while (dfn.volumesMapping[0].get_P30(1) < 0.0001):
	dfn.fractureSets[1].add_BaecherFracture(180, 45, 100, "exp", 55, 0);

dfn.surfacesMapping[0].export_SurfaceMappingVtk("surfaceMapping")
dfn.export_DFNVtk("dfn")
dfn.export_RegionVtk("region")

generator = Generator()
generator.set_MinInscribedSphereRadius(0.5) 
generator.set_MaxAspectRatio(30)
generator.generate_RockMass(dfn)

plotTools.blockVolumeDistribution(generator.get_Volumes(False))
plotTools.blockShapeDiagram(generator.get_AlphaValues(False), generator.get_BetaValues(False), generator.get_Volumes(False), 1)
plotTools.BlockShapeDistribution(generator.get_AlphaValues(False), generator.get_BetaValues(False), generator.get_Volumes(False))

generator.import_ExcavationElementsObj("openpit") 
generator.export_ExcavationElementsVtk("openpitVtk")
generator.excavate_RockMass()
generator.export_BlocksVtk("blocksGenerated")

plotTools.showPlots()
