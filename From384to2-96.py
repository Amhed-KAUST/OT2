from opentrons import robot, labware, instruments

metadata = {
    'protocolName': 'Tube Distribution Test: From two columns 384 to two 96',
    'author': 'Amhed Vargas <amhed.velazquez@kaust.edu.sa>',
    'source': 'KAUST - OT-2 Protocols'
    }

###Robot speed
##Default speeds 'x': 600, 'y': 400, 'z': 125, 'a': 125, 'b': 50, 'c': 50
robot.head_speed(x= 300, y= 200, z= 125, a= 125, b= 50, c= 50)


##Labware
#Tips
#p300rack = labware.load('opentrons_96_tiprack_300ul', '9')
p10rack1 = labware.load('tiprack-10ul', '1')
p10rack2 = labware.load('tiprack-10ul', '2')

#p10rack3 = labware.load('opentrons_96_tiprack_10ul', '4')
#p10rack4 = labware.load('opentrons_96_tiprack_10ul', '5')

#Plates
p384plate = labware.load('384-plate', '3')

p96plateA = labware.load('96-PCR-tall', '10')
p96plateB = labware.load('96-PCR-tall', '7')

##Pippetes and tips definition
#p50 = instruments.P50_Single(mount='right', tip_racks=[p300rack])

p10 = instruments.P10_Single(mount='left', tip_racks=[p10rack1,p10rack2])


##Commands
def run_custom_protocol():
    w96=p96plateA.wells('A1', to='H12')
    con=0
    for w in p384plate.wells('A1', to='P6'):
        p10.pick_up_tip()
        p10.mix(repetitions=5, volume=2, location=w.bottom(1), rate=0.5)
        p10.transfer(2, w.bottom(1), w96[con].bottom(1), new_tip='never', dispense_flow_rate=1, blow_out=False)
        p10.mix(repetitions=5, volume=2, location=w96[con].bottom(1), rate=0.5)
        p10.blow_out()
        p10.drop_tip()
        con = con + 1

    w96=p96plateB.wells('A1', to='H12')
    con=0
    for w in p384plate.wells('A7', to='P12'):
        p10.pick_up_tip()
        p10.mix(repetitions=5, volume=2, location=w.bottom(1), rate=0.5)
        p10.transfer(2, w.bottom(1), w96[con].bottom(1), new_tip='never', dispense_flow_rate=1, blow_out=False)
        p10.mix(repetitions=5, volume=2, location=w96[con].bottom(1), rate=0.5)
        p10.blow_out()
        p10.drop_tip()
        con = con + 1



run_custom_protocol()


##Robot home

robot.home()