#!/usr/bin/env python

import shutil
import sys
import os
import subprocess

with open(sys.argv[1]) as f:
    bvals = f.read().split(' ')
    bvals = [x for x in bvals if x != '']
    bvals = [x for x in bvals if x != '\n']
    bvals = [x for x in bvals if x != ' ']

b0_present = False
with open('dwi.bvals','w') as f:
    for bval in bvals:
        bval = bval.replace('\n','')
	bval = round(float(bval),-2)
        if bval == 0:
            b0_present = True
        f.write("%s " %bval)

#exit if there are no b0 images
if b0_present == False:
    sys.exit("At least one b0 image must be present in the DWI")

shutil.move(os.path.join(os.getcwd(),'dwi.bvals'), sys.argv[1])
