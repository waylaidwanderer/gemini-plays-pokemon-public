# Cerulean City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **West Entrance (from Route 4):** Connects to the paved brick road of Cerulean City at x=0, y=19. (Verified at Turn 4062).
- **Bike Shop:** Large building located south of (13, 15). Roof spans row 24 on columns 12-16. Front of the building is on row 25.
- **Cerulean Gym:** Large building located on the east side, north of the Mart. Sign reads "GYM" at (26, 18) / (27, 18).
- **Poké Mart:** Building located south of the Gym. Sign reads "MART" at (26, 24) / (27, 24) with entrance at (25, 25).
- **Route 24 Bridge (Nugget Bridge Path):** Accessible from the north-center area.

## Northern Bypass to Route 24
- **No South-to-North Direct Passage:** The horizontal barrier at row 15 blocks all columns. The eastern lane on column 33 has a horizontal one-way ledge facing down on row 19, preventing any northward walk. The Burgled House front door is at (27, 11) (north of the barrier), so it is inaccessible from the south side of the city. Therefore, the Route 4 Alignment Offset Bypass is the only way to transition from the south side to the north side of Cerulean City.

- **Passage barrier at Row 15:** Fences and roofs block vertical transit across row 15 across all columns in Cerulean City, including column 0 which is blocked by a cliff and water.
- **Route 4 Map Connection Bypass:** Because of the Gen 1 Map Connection Alignment Offset (Route 4 offset is -8), walking Left from Cerulean City at y=16 transitions to Route 4 at y=8 (completely bypassing the river barrier on Route 4 which is at y=16+). From there, walk Up to y=4, then Right to transition back to Cerulean City at y=12, which is completely north of the horizontal barrier!
- **Route 24 Entrance:** Paved brick road at columns 20-21 on rows 10-13 is completely clear and leads north directly onto Route 24.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (19, 17)     | Pokémon Center        | Pokémon Center                            | Functional Pokémon Center! Stand at (3, 3) and talk to Nurse Joy to heal. |
| (13, 15)     | Melanie's House       | Melanie's House                           | Contains Jynx trade NPC, styled as a house. No healing. |
| (25, 25)     | Poké Mart             | Melanie's House                           | Contains Jynx trade NPC, styled as a house. No healing. |
| (9, 11)      | Badge Guy's House     | Badge Guy's House                         | Contains Badge Guy NPC. Rendered with a misleading Pokémon Center tileset (PC on right, counter on top), but has NO healing function. |
| (13, 25)     | Bike Shop             | Bike Shop                                 | Standard Bike Shop interior. |
| (30, 19)     | Cerulean Gym          | Cerulean Gym                              | Standard Gym interior. Misty is here. |
| (27, 11)     | Burgled House         | Bill's House Interior (Mod Swap)          | Mapped to Bill's House. Entering (27, 11) warps to Bill's House. Exiting Bill's House warps back to (27, 11). |

## Trainers & Defeated Status
- **Team Rocket Grunt (Burgled House Backyard):** Located at (30, 8).
  - **Roster:** Machop (Lv 15), Drowzee (Lv 17)
  - **Status:** Defeated on Turn 4897.
  - **Reward:** ¥510 and TM28 (Dig).