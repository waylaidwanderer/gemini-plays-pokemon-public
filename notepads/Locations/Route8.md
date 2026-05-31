# Route 8 Location Records (Map 0_19)

## Overview & Map Transitions
- **Exploration Started**: Turn 29240 (Friday, May 29, 2026 at 12:20 PM PDT).
- **Eastern Exit**: Connects to Lavender Town (Map 0_4) at (0, 8) via the narrow corridor at (59, 8) (verified on Turn 29240).
- **Western Exit**: Leads towards Saffron City Gatehouse.
- **Underground Path**: Connects Route 8 to Route 7, bypassing Saffron City entirely and leading to Celadon City.

## Points of Interest
- **Tall Grass Patches**:
  - Located in the central and northern areas of Route 8.
  - Contains wild Pokémon (to be cataloged).

## NPC & Trainer Directory
- Lass at (51, 12): Defeated on Turn 29293. Gained 319 EXP, got ¥330. Had CLEFAIRY L22. Dialogue: "Stop! Don't be so mean to my CLEFAIRY!"
- Lass Paige at (26, 5): Defeated on Turn 29399. Gained ¥285. Had PIDGEY L19, RATTATA L19, NIDORAN♂ L19, MEOWTH L19, PIKACHU L19. Dialogue: "We must look silly standing here like this!" Note: Her battle was triggered on Turn 29377 by interacting with the Biker at (26, 6) from (26, 7) facing Up, revealing a Gen 1 sprite-to-script mapping glitch.
- Lass Andrea at (26, 3): Defeated on Turn 29437. Gained 576 EXP, got ¥345. Had NIDORAN♀ L23, NIDORINA L23. Dialogue: "Why? Why??"
- Lass Julia at (26, 5): Defeated on Turn 29452. Gained ¥432. Had MEOWTH L24, MEOWTH L24, MEOWTH L24. Dialogue: "MEOWTH is so cute, meow, meow, meow!" Triggered on Turn 29440 when walking to (25, 5).
- Biker at (26, 6): Standing at (25, 6) facing Right and talking to him on Turn 29457, he says: "SAFFRON's gate keeper won't let people through." He is an NPC, not a battleable trainer from this side, or his script has been overridden/linked with Lass Paige.
- Gambler at (46, 13): Defeated on Turn 29312. Gained ¥1680. Had GROWLITHE L24, VULPIX L24. Dialogue: "I'm a rambling, gambling dude!" and "Lanslides!..."
- Super Nerd Erik at (11, 5): Defeated on Turn 29522. Gained ¥500. Had VOLTORB L20, KOFFING L20, VOLTORB L20, MAGNEMITE L20. Dialogue: "Ow! Meltdown!"

## Saffron Gatehouse & Route 8 Underground Path Verification
- **Route 8 Underground Path Verification**:
  - **Step 1 (Verified Turn 29506)**: External building door is located at (13, 3) on Route 8 (Map 0_19).
  - **Step 2 (Verified Turn 29529)**: Entered the building. Internal Map ID is 0_80 (Route 8 Underground Path Entrance). We spawn at (3, 7) facing Up.
  - **Step 3 (Verified Turn 29529)**: The stairs warp to the Underground Tunnel are located at (4, 4) on Map 0_80.
  - **Step 4 (Verified Turn 29535 & 29556)**: Entered the Underground Path (Map 0_121), spawned at (47, 2), walked the horizontal corridor west, and exited via the stairs at (2, 5) to the Route 7 Gatehouse (Map 0_77).
  - **Step 5 (Verified Turn 29562)**: Spawned inside Map 0_77 at (4, 4), walked south through the door warp at (4, 7), and successfully emerged on Route 7 (Map 0_18) at (5, 14) on Turn 29562, establishing a complete overworld verification. We marked the Route 7 Gatehouse Door on Map 0_18 at (5, 13).

## Local Habitat & Wild Encounters
- **Wild Encounters Template (To be documented on future backtracks)**:
  - Species: [Species Name] | Level Range: [Min-Max] | Est. Encounter Rate: [Low/Medium/High] | Notes: [Details]

## Strategic Routing & Passability Discoveries (Turn 29326 - 29334)
- **Ledge Test**: Standing at (44, 13) on Turn 29326, pressed Down. Successfully jumped south over the horizontal barrier to (44, 14), proving the barrier between row 13 and row 14 is a jumpable LEDGE.
- **Fence Passability**: The vertical fence on columns 42/43 ends at row 13. Rows 14 and 15 are open path tiles, which allowed us to walk westward underneath the fence to reach column 41.
- **Cut Bush**: Discovered a cuttable bush at (41, 10) (TYPE_5519) blocking column 41. We positioned ourselves at (41, 11) facing Up on Turn 29334 to cut it using Bellsprout (PETAL).
- **Wall Openings**: Standing at (41, 11) on Turn 29343, we walked Up to (41, 10), Left to (40, 10), and Left again to (39, 10) on Turn 29344. This physical traverse definitively proves that (40, 10) is fully passable with no invisible collision boundaries or map-connection discrepancies, granting us access to the western grass area.
- **Second Cut Bush**: Standing at (30, 12) facing Left on Turn 29353, we successfully cut and cleared the bush at (29, 12) on Turn 29361 using PETAL's CUT. This opened a fully clear pathway to the vertical paved corridor.