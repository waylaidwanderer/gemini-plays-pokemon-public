# Vermilion City - Locations, Landmarks & Barriers

## Overworld Layout & Navigation
- **Northern Entrance:** Connects from Route 6. The transition from Route 6 at y=36 warps the player to Vermilion City at `(18, 0)` due to a +10 horizontal alignment offset (Route 6 x=8 connects to Vermilion City x=18).
- **Visual Grid Alignment:** No coordinate offset in Vermilion City; the visual grid exactly matches internal memory coordinates.

## Verified Outside Door & Warp Mappings
| Outside Door | Standard Map Location | Verified Interior Room / Warp Destination | Notes / Functionality |
|--------------|-----------------------|-------------------------------------------|-----------------------|
| (11, 3)      | Pokémon Center        | Pokémon Center                            | Functional! Nurse Joy is behind the counter at (3, 2). Functional. |
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

## S.S. Anne Pier Layout & Map Transitions (Vermilion Dock)
- **Pier Structure:** Consists of two vertical walkable columns: Column 18 and Column 19, running from row 27 down to row 35.
- **Statues/Pillars:** Present on columns 14-17 and columns 20-23 on rows 30 and 31.
- **Boarding Warp Transitions:**
  - **Column 18 (left side):** Walking south on Column 18 past row 35 warps the player to S.S. Anne Entryway (Map 91) at `(14, 0)` (facing Down).
  - **Column 19 (right side):** Walking south on Column 19 past row 35 warps the player to S.S. Anne Entryway (Map 91) at `(14, 2)` (facing Down), right next to the S.S. Anne Deck warp!
- **Sailor Ticket Checker:** Sits at `(19, 30)`. No longer blocks passage.

## Vermilion Gym Layout & Geometry
- **Entrance:** Located at `(12, 19)` (connects to Vermilion City at `(12, 20)` after clearing the cuttable bush at `(15, 18)`).
- **Gym Guide:** Stands at `(4, 14)`.
- **Rhydon Statues:** Located at `(3, 13)` / `(3, 14)` and `(6, 13)` / `(6, 14)`.
- **Trash Can Grid (3x5):**
  - Row 11: `(1, 11)`, `(3, 11)`, `(5, 11)`, `(7, 11)`, `(9, 11)`
  - Row 9: `(1, 9)`, `(3, 9)`, `(5, 9)`, `(7, 9)`, `(9, 9)`
  - Row 7: `(1, 7)`, `(3, 7)`, `(5, 7)`, `(7, 7)`, `(9, 7)`
- **Trainers:**
  - **Sailor Dwayne:** Located at `(0, 10)` (facing Right). Roster: Pikachu (Lv 21).
  - **Rocker Harrison:** Located at `(3, 8)` (facing Down). Roster: Voltorb (Lv 20).
  - **Gentleman Tucker:** Located at `(9, 6)` (facing Down). Roster: Pikachu (Lv 23). Defeated on Turn 6897, earning ¥1610.

  - **Gym Leader Lt. Surge:** Located at (5, 1) inside the Vermilion Gym. Roster: Voltorb (Lv 21), Pikachu (Lv 18), Raichu (Lv 24). Defeated.