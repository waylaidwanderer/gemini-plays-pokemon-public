# Saffron Silph Co. 11F Verified Layout & Exploration Records (Map 0_235)

## Overview & Coordinates
- **Elevator**: Located at (13, 0) (leads to all floors 1F-11F).
- **Stairs**: N/A (elevator and warps only).
- **Cleared Status**: Under exploration.

## Exploration & Combat Log
- Entering 11F to confront Team Rocket, find Card Key doors, defeat Boss Giovanni, and rescue the Silph President!
- **Rocket Grunt**: Standing at (15, 9) in the eastern corridor. Defeated on Turn 42130 (Rattata L25, Zubat L25, Rattata L25, Ekans L25).
- **Rocket Grunt**: Standing at (3, 13) in the western boardroom corridor. Defeated on Turn 42410 (Cubone Lv 32, Drowzee Lv 32, Marowak Lv 32).

## Empirical Partition Verification (Burden of Proof - Turn 42154)
- **Test Target**: Column 4 vertical partition (Row 2).
- **Methodology**: On Turn 42151, the player stood at (5, 2) facing Left and pressed 'A' to interact with (4, 2) with the CARD KEY in inventory.
- **Result**: No overworld response, no text box, and no tile change.
- **Conclusion**: Column 4 at (4, 2) is verified as a solid, permanent wall (TYPE_2889). The western compartment (columns 0-3) is physically isolated on foot on this floor, confirming we must use a warp tile to access it.

## Empirical Center Area Partition Verification (Burden of Proof - Turn 42156)
- **Test Target**: Row 3 center area partition (Row 3, Column 12).
- **Methodology**: On Turn 42154, the player stood at (12, 2) and attempted to walk Down onto (12, 3).
- **Result**: Player collided with the wall and remained at (12, 2) facing Down (visited 7 tiles out of 8 inputs, proving a collision at (12, 3)).
- **Conclusion**: (12, 3) is verified as a solid, permanent wall (TYPE_2889). Testing has only proven that column 12 is blocked at row 3; the full isolation of the southern center area remains an active hypothesis until columns 5-11 are physically tested.

## Saffron 11F Boardroom Climactic Battle Prep Checklist
- **Primary Objective**: Confront and defeat Boss Giovanni in the isolated western boardroom on 11F.
- **Combat Lead**: GEMMY (BLASTOISE L53) to lead the battle for type coverage against Ground/Normal types.
- **Level Audit**:
  - GEMMY (Blastoise) is Lv 53 (vast level advantage over Giovanni's ~Lv 40-42 team).
  - SPARKY (Pikachu) is Lv 25 (reserve for Flying/Water targets).
- **Combat Recovery Protocols**:
  - **Healer Access**: If GEMMY's HP or PP are depleted during the Rival Blue fight, we must backtrack to the Saffron 9F Healer at (3, 14) to restore 100% HP and PP before stepping on the warp to the boardroom.
  - **Inventory Reserves**: Hyper Potions (11) and Elixir (1) are ready in inventory to heal mid-battle if needed.
  - **Status Treatment**: Full Heals (1) and Parlyz Heals (2) are reserved to cure sleep, poison, or paralysis during the boss fight.

- **Test Target**: Column 4 vertical partition door at (4, 6).
- **Methodology**: On Turn 42372, the player stood at (3, 6) facing Right and pressed 'A' with the CARD KEY in inventory.
- **Result**: No overworld response, no text box, and no tile change.
- **Conclusion**: Column 4 at (4, 6) is verified as a solid, permanent wall (TYPE_2889). There is no functional door at row 6.
- **Rocket Grunt**: Standing at (6, 13) behind the Card Key gate. Discovered on Turn 42414 after unlocking the gate.