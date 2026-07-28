# Cerulean City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **West Entrance (from Route 4):** Connects to the paved brick road of Cerulean City at x=0, y=19. (Verified at Turn 4062).
- **Bike Shop:** Large building located south of (13, 15). Roof spans row 24 on columns 12-16. Front of the building is on row 25.
- **Cerulean Gym:** Large building located on the east side, north of the Mart. Sign reads "GYM" at (26, 18) / (27, 18).
- **Poké Mart:** Building located south of the Gym. Sign reads "MART" at (26, 24) / (27, 24) with entrance at (25, 25).
- **Route 24 Bridge (Nugget Bridge Path):** Accessible from the north-center area.

## Northern Bypass to Route 24
- **No South-to-North Direct Passage:** The horizontal barrier at row 15 blocks all columns. The eastern lane on column 33 has a horizontal one-way ledge facing down on row 19, preventing any northward walk. The Burgled House front door is at (27, 11) (north of the barrier), so it is inaccessible from the south side of the city.
- **Route 24 Entrance:** Paved brick road at columns 20-21 on rows 10-13 is completely clear and leads north directly onto Route 24.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (19, 17)     | Pokémon Center        | Pokémon Center                            | Functional Pokémon Center! Stand at (3, 3) and talk to Nurse Joy to heal. |
| (13, 15)     | Melanie's House       | Melanie's House                           | Contains Jynx trade NPC, styled as a house. No healing. |
| (25, 25)     | Poké Mart             | Melanie's House                           | Exiting warps to (25, 25). Contains Jynx trade NPC. |
| (9, 11)      | Badge Guy's House     | Badge Guy's House                         | Contains Badge Guy NPC. Rendered with a misleading Pokémon Center tileset (PC on right, counter on top), but has NO healing function. |
| (13, 25)     | Bike Shop             | Melanie's House                           | Shared interior. Exiting from (2, 8) warps to (13, 25). |
| (27, 21)     | Fighting Dojo         | Unreachable                              | Decorative only. Exposing water canal (24, 22 to 27, 22) blocks southern access. |
| (30, 19)     | Cerulean Gym          | Cerulean Gym                              | Standard Gym interior. Misty is here. |
| (27, 11)     | Burgled House         | Bill's House Interior (Mod Swap)          | Mapped to Bill's House. Entering (27, 11) warps to Bill's House. Exiting Bill's House warps back to (27, 11). |

## Trainers & Defeated Status
- **Team Rocket Grunt (Burgled House Backyard):** Located at (30, 8).
  - **Roster:** Machop (Lv 15), Drowzee (Lv 17)
  - **Status:** Defeated on Turn 4897.
  - **Reward:** ¥510 and TM28 (Dig).

## Verified Southern Barriers (Turn 5421)
- **Route 4 East transition always warps to (0, 18) in Cerulean City:** Transitioning from Route 4 to Cerulean City on rows 0, 3, 4, or 5 always warps the player to (0, 18) on the south side of Cerulean City. The Route 4 Alignment Offset Bypass to the north side (y=12) is NOT functional in this mod.
- **Saffron Road (Columns 16-17) Ledge Block:** Standing at (16, 28) and pressing Down is blocked by the vertical logs at (16, 29). Saffron Road is completely impassable.
- **Row 28 Barrier (MANUALLY VERIFIED):** Row 28 is completely blocked by dark green trees across columns 12-35, and Saffron Road (columns 16-17) is blocked on row 29 by vertical logs at (16, 29) and a signpost at (17, 29). Columns 36 and 37 on row 28 are visually clear of trees. However, reaching columns 36-37 from the south-west side (Saffron Road / Poké Mart area) is **currently impassable and unverified** because column 35 is blocked by logs on rows 20-27 and trees on rows 28-29, and rows 16-23 on columns 32-35 are blocked by the water canal, forming a solid vertical obstruction across all walkable rows.
- **Column 35 Log Barrier (MANUALLY VERIFIED):** Column 35 is completely blocked by a solid wall of vertical logs on rows 23-27, and by trees on rows 28-29. This prevents any direct horizontal passage from the west side of Cerulean City to the eastern lane (columns 36-37) on the south side of the city. (Verified at Turn 5638).

## Verified Southern & Central Barriers (Turn 5769 Update)
- **Column 7 Central Wall:** Empirically verified that column 7 contains a solid vertical wall of grey pillars/walls on rows 12-16, blocking all westward passage to column 0 on those rows.
- **Row 15 Barrier Details:**
  - **Saffron Road Blockage:** Saffron Road (columns 16-17) is completely blocked on row 15 by Melanie's House building (spanning columns 13-17 on row 15).
  - **Ledge Blockage (Columns 8-11):** Column 9 (and columns 8-11) has a horizontal one-way ledge facing down on row 15, which blocks all upward (south-to-north) passage.
- **Row 19 Ledge Blockage:** Columns 32-35 on row 19 have a horizontal one-way ledge facing down, allowing downward jumps but blocking upward passage.
- **Saffron Gym Layout:** Saffron Gym occupies columns 27-31 on rows 16-19.



## Burgled House Backdoor & Backyard Shortcut (Turn 9005-9007 Discovery)
- **Front Door:** (27, 11). Entering warps the player to Bill's House Interior (Mod Swap).
- **Backdoor/Hole in Wall:** Walking north to the top-center (3, 0) inside Bill's House Interior warps the player directly outside to the Backyard of the Burgled House at `(27, 9)`.
- **Bypassing the Column 32 Log Barrier:** This backyard path allows the player to enter the Burgled House front door on the south side at `(27, 11)` (bypassing the Row 15 barriers), exit through the backdoor to `(27, 9)`, and then walk west/east on the north side, completely bypassing the Column 32/33 ledge and log barriers!
