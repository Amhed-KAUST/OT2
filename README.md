# OT2
## This repository contains the code required to perform simple routines adapted to our lab needs

Please be aware of the correct deck positioning. E.g.:

https://drive.google.com/open?id=1Og2vHm8AUVc24NeOYHRboBxKIULkhylm

## Routines
### Resuspend 384 library and transfer into 96 well plates
### **Yet to be tested

Test-Fill_384_to_4_96.py

Strategy:
Dispense 20ul from tube rack (A1, A2, A3, and A4) into 384 well plate (per set of 6 columns respectively).
Mix each well and transfer 10 ul to 4 different 96 well plates.

Diagram:
https://drive.google.com/file/d/1yetmTQG9DVCJ7jzeO-JHSRjcQXP64lDb/view?usp=sharing

### Perform a PCR in a 96 well plate combining 11 Fwd primers (1 per column) and 8 Rev primers (1 per row)

8F-by-11R_PCR_test-2_switched.json

Run in OT-2 or Protocol builder (https://designer.opentrons.com/) to get the strategy and Labware needed.

### Fill a 384 well plate with sample coming from eppendorf tubes (2ml rack)

tube_to_384.ot2.py

** Check opentrons documentation for further info
