# CyberSlice Keyboard

![Picture of the CyberSlice42](https://github.com/MReavley/CyberSliceKeyboard/blob/main/Photos/IMG_1311.JPG)

42/36 key split keyboard using RP2040, with the same layout (in 36 key configuration) as my previous design, the Slice 36. The goal was primarily to experience designing a microcontroller directly on the PCB, but I also wanted to try to take advantage of the large number of GPIO pins on the RP2040. There are 8 additional GPIO (2 analog capable) on the PCB with the intention of adding functionality through magnetic pogo connectors, but that is still a work in progress. 

## Features

- Reversible PCB designed for PCB assembly services  
- RP2040 per side, with 16MB of flash  
- Laser cut aluminium plate, custom designed 3D printed case with magnets  
- Footprints for magnetic pogo connectors on each side

![Picture of the CyberSlice42 plugged in](https://github.com/MReavley/CyberSliceKeyboard/blob/main/Photos/IMG_1325.JPG)

## If you want to build:
This board is just a prototype, and there are a couple pointers to watch out for:

Reversible PCB: Since the PCB is reversible, solder on the trrs connector on opposite sides of the PCB for each half. The USB-C connector for the left half will be on the bottom side, which does necessitate taller rubber feet unfortunately.

Components on the rear:  
These components will not be assembled by basic PCBa, but the parts can be scavenged from spare assembled PCBs (per side)
- C7 (100nF 0603 MLCC capacitor)
- R1 and R2 (5.1k 0603 resistors)
- R12 and R13 (Optional, 4.7k 0603 pullups for split over I2C, not needed for UART)

Additional components:
- PJ320D trrs connectors (x1 per side), solder on opposite side of PCB for the different halves
- 2.54mm magnetic pogo connectors (5 contacts) (2x per side) (optional, can solder directly instead)
- 6mm diameter x 3mm height magnets x6 per side for case (optional, can use screw holes instead)

Reset and boot switches may need to be renamed in the BOM file (not using SW1 and SW2) for them to be auto-selected by PCBa service  
- Otherwise shorting the pads on the PCB will have the same effect

Case:
- Tolerances were very loose on my case, but this does depend on the printer
- Ideally, one would redesign the plate to mount directly to the case (add screw holes)
- Tolerance for the magnet holes can be a bit too tight, probably increase from 6 to 6.1 or 6.2mm diameter

![Picture of the CyberSlice42 case rear](https://github.com/MReavley/CyberSliceKeyboard/blob/main/Photos/IMG_1313.JPG)



## Things to improve

- Rename the reset and boot switches from SW1 and SW2 to something else to not clash with the names of the switches (caused me to make a mistake in my order)  
- Shift the few SMD parts on the back side to the front for PCBa  
- Add a few more LEDs for status indicators on the PCB itself  
- Change the plate the design for better mounting of PCB and plate to case, or alternatively integrate the plate into the case  


![Picture of the CyberSlice42 pcb rear](https://github.com/MReavley/CyberSliceKeyboard/blob/main/Photos/IMG_1315.JPG)
