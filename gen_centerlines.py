from vmtk import pypes


input_file_name = "Aorta_voi.mha"
vti_fname = "level_sets.vti"
vtp_fname = "surface.vtp"
vtp_centerline_fname = "centerline.vtp"

# 1. image segmentation

# myArguments = f"vmtklevelsetsegmentation -ifile {input_file_name} -ofile {vti_fname}"
# myPype = pypes.PypeRun(myArguments)

# 2. generate a vtp file from a vti file

# myArguments = f"vmtkmarchingcubes -ifile {vti_fname} --pipe vmtksurfaceviewer -ofile {vtp_fname}"
# myPype = pypes.PypeRun(myArguments)

# (optional) 2-1. generate centerlines

# myArguments = f"vmtkcenterlines -ifile {vtp_fname} -ofile {vtp_centerline_fname}"
# myPype = pypes.PypeRun(myArguments)

# 3. Centerlines visualization

# myArguments = f"""\
# vmtksurfacereader -ifile {vtp_fname} \
# --pipe vmtkcenterlines --pipe vmtkrenderer --pipe vmtksurfaceviewer \
# -opacity 0.25 --pipe vmtksurfaceviewer -i @vmtkcenterlines.o \
# -array MaximumInscribedSphereRadius"""
# myPype = pypes.PypeRun(myArguments)

# Voronoi diagram

# myArguments = f"""vmtksurfacereader -ifile {vtp_fname} \
# --pipe vmtkcenterlines --pipe vmtkrenderer --pipe vmtksurfaceviewer \
# -opacity 0.25 --pipe vmtksurfaceviewer -i @vmtkcenterlines.voronoidiagram \
# -array MaximumInscribedSphereRadius --pipe vmtksurfaceviewer -i @vmtkcenterlines.o"""
# myPype = pypes.PypeRun(myArguments)
