IDEA
====

Whats the goal?
---------------
I want to have a program I can use to extract data from my calculations and to group and sort the data indpendent of the folder structure on my harddisc. 

Essentials features are:

    * Automatically read folders and find folders with calculations
    * Extract basic information from the calculations
        * Time of calculation
        * Calculation title (folder name, or more if given in input?)
        * Chemical formula
        * Type of calculation (SP, geom opt, ...)
        * geometry
        * Association to project
        

Nice features would be:

    * ...

How to do it?
-------------
Basic idea of many QM programs: One calculation per folder. Since the program should work **in addition** to how I and many others do their calculations, changes to the folders or changes only saved in a database are not possible. Still, meta-data need to be saved somewhere. 

**XML-file per folder for meta-data:** 
    * Lets define a syntax for qm-meta data (perhaps object-based, e.g. each calculation is an "object" with properties
    * Save this information on a per folder basis to a file (*qm_meta.xml*)

On the first run, create these xml-files based on scraped information from the folders. Make this modular and extendable.

    * Create a database with **all** the information and metadata from the xml files.
    * On Startup, rescan the xml-files?
    * Track the folders for changes with inotify? 
    

Open questions
--------------

    * How are changes tracked and handled?
    * Shall there be actual qc data in the database? Such as geometries or input files. Will make it faster and independent of the file system, but again, how to track and apply changes?



Available tools
---------------

    * Extracting informations: ASE
        * chemical formula
        * geometry-file in xyz or other
        
    



