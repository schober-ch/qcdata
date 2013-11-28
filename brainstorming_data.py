#!/usr/bin/python 
# 
# Outline of a calc class used for storage and manipulation

class calculation:
    """ Main storage and processing instance for calculations. """

    # Basic properties, identifiying calculations. Directly accessible from files/folders
    uri
    abspath
    folders
    files
    ctime
    mtime

    # Additional properties, processed
    chemical_formula
    project
    qmprogram

    # Additional informations like input params, geometries, etc.
    geometry
    xc


class project:
    """ Manage projects, consisting of n calculations. """


Types of folders:


    
