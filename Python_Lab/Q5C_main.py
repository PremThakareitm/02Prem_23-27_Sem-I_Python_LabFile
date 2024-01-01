# Write a program to create a package with name cars and add different modules
# (such as BMW, AUDI, NISSAN) having classes and functionality and import
# them in main file cars.

import Bmw as bmwpro
import Audi as audipro
import  Nissan as nissanpro

ModBMW = bmwpro.Bmw_m() 
ModBMW.Models() 

ModAudi = audipro.Audi_m() 
ModAudi.Models() 

ModNissan = nissanpro.Nissan_m() 
ModNissan.Models() 
