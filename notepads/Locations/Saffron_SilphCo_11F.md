# Saffron Silph Co. 11F Verified Layout & Exploration Records (Map 0_235)

## Overview & Coordinates
- **Elevator**: Located at (13, 0) (leads to all floors 1F-11F).
- **Stairs**: N/A (elevator and warps only).
- **Cleared Status**: Under exploration.

## Exploration & Combat Log
- Entering 11F to confront Team Rocket, find Card Key doors, defeat Boss Giovanni, and rescue the Silph President!
- **Rocket Grunt**: Standing at (15, 9) in the eastern corridor. Defeated on Turn 42130 (Rattata L25, Zubat L25, Rattata L25, Ekans L25).

## Empirical Partition Verification (Burden of Proof - Turn 42154)
- **Test Target**: Column 4 vertical partition (Row 2).
- **Methodology**: On Turn 42151, the player stood at (5, 2) facing Left and pressed 'A' to interact with (4, 2) with the CARD KEY in inventory.
- **Result**: No overworld response, no text box, and no tile change.
- **Conclusion**: Column 4 at (4, 2) is verified as a solid, permanent wall (TYPE_2889). The western compartment (columns 0-3) is physically isolated on foot on this floor, confirming we must use a warp tile to access it.

## Empirical Center Area Partition Verification (Burden of Proof - Turn 42156)
- **Test Target**: Row 3 center area partition (Row 3, Column 12).
- **Methodology**: On Turn 42154, the player stood at (12, 2) and attempted to walk Down onto (12, 3).
- **Result**: Player collided with the wall and remained at (12, 2) facing Down (visited 7 tiles out of 8 inputs, proving a collision at (12, 3)).
- **Conclusion**: (12, 3) is verified as a solid, permanent wall (TYPE_2889). The southern center area (columns 5-12, rows 5-16) has been physically proven to be completely isolated on foot on this floor.