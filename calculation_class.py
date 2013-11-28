import os
import datetime

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

class calc:
    """ This is the main class for qm calculations. Its properties are the minimal set that should be known for all calculations, no matter which program. """

    URI = ""     # unique resource identifier
    abspath = "" # absolute path to folder
    relpath = "" # relative path to folder (decide for one, relative will make data
                 # more transferable
    #date = ""    # date+time of last change in folder
    files = []   # list of all files in the folder
    folders = [] # list of additional folders, if applicable
    #qmprogram = ""

    def __init__(self, foldertuple):
        self.abspath, self.folders, self.files = foldertuple
        self.date = self.modification_date(self.abspath)
        self.URI = self.abspath.split("/")[-1] + self.date

    def modification_date(filename):
        t = os.path.getmtime(filename)
        return t, datetime.datetime.fromtimestamp(t)

class aims(calc):
    """ This class will handle all fhi-aims specific tasks and data for calculations. Its main class is calculation()"""

    calc_converged = ""     # is the calc in folder converged and done?
    aims_version = ""       # aims version grepped from output
    geometry = [] #ase.atoms.atom(...) # ASE atoms object
    dft_method = ""         # ASE 
    tot_energy = ""         # ASE

