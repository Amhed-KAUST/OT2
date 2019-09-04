from opentrons import labware, instruments

metadata = {
    'protocolName': 'Tube Distribution Test: Fill 384 and transfer to 4*96',
    'author': 'Amhed Vargas <amhed.velazquez@kaust.edu.sa>',
    'source': 'KAUST - OT-2 Protocols'
    }

##Labware
#Tips
p300rack = labware.load('opentrons_96_tiprack_300ul', '9')
p10rack1 = labware.load('opentrons_96_tiprack_10ul', '1')
p10rack2 = labware.load('opentrons_96_tiprack_10ul', '2')
p10rack3 = labware.load('opentrons_96_tiprack_10ul', '4')
p10rack4 = labware.load('opentrons_96_tiprack_10ul', '5')

#Plates
p384plate = labware.load('corning_384_wellplate_112ul_flat', '3')
p96plateA = labware.load('biorad_96_wellplate_200ul_pcr', '10')
p96plateB = labware.load('biorad_96_wellplate_200ul_pcr', '7')
p96plateC = labware.load('biorad_96_wellplate_200ul_pcr', '11')
p96plateD = labware.load('biorad_96_wellplate_200ul_pcr', '8')

#Samples
sample_tubes = labware.load('opentrons_24_tuberack_generic_2ml_screwcap', '6')


##Pippetes and tips definition
p300 = instruments.P300_Single(mount='right', tip_racks=[p300rack])

p10 = instruments.P10_Single(mount='left', tip_racks=[p10rack1,p10rack2,p10rack3,p10rack4])


##Commands
def run_custom_protocol():
    #Fill first 384 well plate from sample tubes. Dispense and mix.
    p300.transfer(20,sample_tubes.wells('A1'), p384plate.wells('A1', to='P6'), new_tip='once')
    p300.transfer(20,sample_tubes.wells('A2'), p384plate.wells('A7', to='P12'), new_tip='once')
    p300.transfer(20,sample_tubes.wells('A3'), p384plate.wells('A13', to='P18'), new_tip='once')
    p300.transfer(20,sample_tubes.wells('A4'), p384plate.wells('A19', to='P24'), new_tip='once')
    
    #From 384 well plate fill
    p10.transfer(10,p384plate.wells('A1', to='P6'), p96plateA.wells('A1', to='H12'), new_tip='always', touch_tip=True, mix_before=2)
    p10.transfer(10,p384plate.wells('A7', to='P12'), p96plateB.wells('A1', to='H12'), new_tip='always', touch_tip=True, mix_before=2)
    p10.transfer(10,p384plate.wells('A13', to='P18'), p96plateC.wells('A1', to='H12'), new_tip='always', touch_tip=True, mix_before=2)
    p10.transfer(10,p384plate.wells('A19', to='P24'), p96plateD.wells('A1', to='H12'), new_tip='always', touch_tip=True, mix_before=2)
    
run_custom_protocol()
