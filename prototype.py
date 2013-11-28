#!/usr/bin/python
# Prototype for OO testing...
import os

#class initialize_calcs():
#
#    def scan_dir(self, target):
#        for root, dirs, files in os.walk(target):
#            dirlist.append([root, dirs, files])
#        return dirlist
    
class start_folders:
    """ All the data and methods related to folders. Check if calculation or project folder, prepare paths etc."""
    
    def has_sub(self, foldertuple):
        """ Check if there are any subfolders."""
        if foldertuple[1] == []:
            subfolders = False
        else:
            subfolders = True
        return subfolders

    def has_files(self, foldertuple):
        """ Check if there are any files."""
        if foldertuple[2] == []:
            files = False
        else:
            files = True
        return files
        
    
    def scan_dir(self, target):
        """ Scan all directories for given root/top level. Returns tuple of [root, dirs, files]."""
        for root, dirs, files in os.walk(target):
            dirlist.append([root, dirs, files])

class folders:
    """ This is the main class for qm calculations. Its properties are the minimal set that should be known for all calculations, no matter which program. """
     
    URI = ""     # unique resource identifier
    abspath = "" # absolute path to folder
    relpath = "" # relative path to folder (decide for one, relative will make data
                 # more transferable
    date = ""    # date+time of last change in folder
    files = []   # list of all files in the folder
    folders = [] # list of additional folders, if applicable
    #qmprogram = ""

    def __init__(self, foldertuple):
        self.abspath, self.folders, self.files = foldertuple
        
        self.URI = self.abspath.split("/")[-1] + self.date
        self.is_calc()

    def is_calc(self):
        if "control.in" and "geometry.in" in self.files:
            self.qmprogram = "fhiaims"
            
class aims(folders):
    """ This class will handle all fhi-aims specific tasks and data for calculations. Its main class is calculation()"""

    calc_converged = ""     # is the calc in folder converged and done?
    aims_version = ""       # aims version grepped from output
    geometry = [] #ase.atoms.atom(...) # ASE atoms object
    dft_method = ""         # ASE 
    tot_energy = ""         # ASE


