# Vermilion City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Northern Entrance:** Connects from Route 6. The transition from Route 6 at y=36 warps the player to Vermilion City at `(18, 0)` due to a +10 horizontal alignment offset (Route 6 x=8 connects to Vermilion City x=18).
- **Visual Grid Alignment:** No coordinate offset in Vermilion City; the visual grid exactly matches internal memory coordinates.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (11, 3)      | Pokémon Center        | Pokémon Center                            | Functional! Nurse Joy is behind the counter at (3, 2). Healed party on Turn 6257. |
| (7, 3)       | House                 | Melanie's House Interior                  | Shared interior warp. Exits to (7, 4). |
| (15, 13)     | House                 | Melanie's House Interior                  | Shared interior warp. Exits to (15, 14). |
| (23, 19)     | Machop House          | Melanie's House Interior                  | Shared interior warp. Exits to (23, 20). |
| (23, 13)     | Poké Mart             | Melanie's House Interior                  | Shared interior warp. Exits to (23, 14). |

## Water, Pond & Hedge Barriers
- **Central Pond Boundaries:**
  - Row 8: Blocks columns 10-15 with soil/water.
  - Row 18: Blocks columns 16-19 with soil/water.
  - Row 22: Blocks columns 20-25 with soil/water.
- **Hedge/Bush Blockages:**
  - Row 18 & 19: Columns 13 and 14 have green hedges/trees that block southward transit to row 20, separating the northern and southern parts of the city.