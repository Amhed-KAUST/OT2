from opentrons import robot, labware, instruments

metadata = {
    'protocolName': 'Tube Distribution Test: Fill 384 and transfer to 4*96',
    'author': 'Amhed Vargas <amhed.velazquez@kaust.edu.sa>',
    'source': 'KAUST - OT-2 Protocols'
    }

###Robot speed

robot.head_speed(x= 100, y= 100, z= 100, a= 125, b= 50, c= 50)


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

#p96plateC = labware.load('biorad_96_wellplate_200ul_pcr', '11')
#p96plateD = labware.load('biorad_96_wellplate_200ul_pcr', '8')

#Samples
sample_tubes = labware.load('opentrons-tuberack-2ml-eppendorf', '6')


##Pippetes and tips definition
#p50 = instruments.P50_Single(mount='right', tip_racks=[p300rack])

p10 = instruments.P10_Single(mount='left', tip_racks=[p10rack1,p10rack2])


##Commands
def run_custom_protocol():
    w96=p96plateA.wells('A1', to='H12')
    con=0
    flag=0
    for w in p384plate.wells('A1', to='P6'):
        if ((flag % 2) == 0):
            sw='A1'
        else:
            sw='A2'
        p10.pick_up_tip()
        p10.transfer(10, sample_tubes.wells('A1'), w.bottom(5), new_tip='never', dispense_flow_rate=1)
        p10.delay(seconds=10)
        p10.mix(repetitions=5, volume=5, location=w.bottom(1))
        p10.transfer(5, w, w96[con], new_tip='never', dispense_flow_rate=1, mix_before=5, blow_out=True)
        p10.drop_tip()
        con = con + 1
        flag = flag + 1
        if ((con % 16) == 0):
            flag = flag +1

    w96=p96plateB.wells('A1', to='H12')
    con=0
    flag=0
    for w in p384plate.wells('A7', to='P12'):
        if ((flag % 2) == 0):
            sw='A1'
        else:
            sw='A2'
        p10.pick_up_tip()
        p10.transfer(10, sample_tubes.wells('A2'), w.bottom(5), new_tip='never', dispense_flow_rate=1)
        p10.delay(seconds=10)
        p10.mix(repetitions=5, volume=5, location=w.bottom(1))
        p10.transfer(5, w, w96[con], new_tip='never', dispense_flow_rate=1, mix_before=5, blow_out=True)
        p10.drop_tip()
        con = con + 1
        flag = flag + 1
        if ((con % 16) == 0):
            flag = flag +1



run_custom_protocol()


##Robot home

robot.home()