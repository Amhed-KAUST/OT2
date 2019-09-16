from opentrons import robot, labware, instruments

metadata = {
    'protocolName': 'Tube Resuspension: Resuspend 384 at 5 millimeters from bottom with 10 microliters',
    'author': 'Amhed Vargas <amhed.velazquez@kaust.edu.sa>',
    'source': 'KAUST - OT-2 Protocols'
    }


###Robot speed
##Default speeds 'x': 600, 'y': 400, 'z': 125, 'a': 125, 'b': 50, 'c': 50
robot.head_speed(x= 300, y= 200, z= 125, a= 125, b= 50, c= 50)


##Labware
#Tips
#p300rack = labware.load('opentrons_96_tiprack_300ul', '9')
p10rack1 = labware.load('tiprack-10ul', '4')
p10rack2 = labware.load('tiprack-10ul', '1')


#Plates
p384plate = labware.load('384-plate', '3')

#Samples
sample96plate = labware.load('96-PCR-tall', '2')


##Pippetes and tips definition
#p50 = instruments.P50_Single(mount='right', tip_racks=[p300rack])

p10m = instruments.P10_Multi(mount='right', tip_racks=[p10rack1,p10rack2])


##Commands
def run_custom_protocol():
    for r in range(12):
#        p10m.transfer(10, sample96plate.cols('1'), p384plate.cols(r).wells('A','C','E','G','I','K','M','O').bottom(5), new_tip='always', dispense_flow_rate=0.5, blow_out=True)
        p10m.transfer(10, sample96plate.cols('1'), p384plate.cols(r).wells('A','C','E','G','I','K','M','O').bottom(5), new_tip='always', dispense_flow_rate=0.5)

    for r in range(12):
        p10m.transfer(10, sample96plate.cols('2'), p384plate.cols(r).wells('B','D','F','H','J','L','N','P').bottom(5), new_tip='always', dispense_flow_rate=0.5)

run_custom_protocol()


##Robot home

robot.home()