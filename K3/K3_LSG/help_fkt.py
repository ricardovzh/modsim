# -*- coding: utf-8 -*-
import os, glob

def delete_OM_files(modelname):
    pattern=[modelname+'*.o', modelname+'*.h', modelname+'*.c']
    filelist=[]; [filelist.extend(glob.glob(e)) for e in pattern]
    filelist.extend([modelname+'.libs',modelname+'.makefile',modelname+'_info.json', modelname+'_init.xml',modelname+'.log', modelname+'_res.mat'])
    if (os.name=='posix'): # Linux
        filelist.extend([modelname])
    if (os.name=='nt'): # Windows
        filelist.extend([modelname+'.exe'])
    for singlefile in filelist:
        try:
            os.remove(singlefile)
        except:
            print("Error while deleting file : ", singlefile)
