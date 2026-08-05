# Route 12 - Overworld Mapping & Navigation

## Map Transitions & Connections
- **North Connection (Lavender Town):** Transition at Row 16, Columns 8-9 to Lavender Town.
- **Route 12 Gatehouse (North Entrance):** Door at `(10, 15)` (warps player inside gatehouse at `(4, 0)`).
- **Route 12 Gatehouse (South Exit):** Exit inside gatehouse at `(4, 7)` (warps player to Route 12 South at `(10, 21)`).

## Physical Layout & Navigation - The Slalom Docks
Because of numerous water blocks and obstacles (such as the defeated Fisherman Barney permanently standing at `(11, 52)`), traversing Route 12 requires navigating a specific back-and-forth slalom path:

1. **Route 12 North to Gatehouse (y=0 to y=15):**
   - The docks start at columns 8-9 at the Lavender Town transition.
   - Walk south to `(8, 10)`, turn East to column 10, then walk south on columns 10-11 to enter the Route 12 Gatehouse at `(10, 15)`.

2. **Gatehouse South Exit to y=44 (y=21 to y=44):**
   - Exit the gatehouse at `(10, 21)` on columns 10-11.
   - Walk south on columns 10-11 to Row 26.
   - At `(11, 26)`, walk East across the horizontal bridge to columns 14-15.
   - Walk south on columns 14-15 to Row 30.
   - At Row 30, walk West to column 11.
   - Walk south on column 11 to Row 34.
   - At Row 34, walk West to columns 4-5.
   - Walk south on columns 4-5 to Row 48.

3. **Row 48 to Row 57 Slalom (Bypassing Barney and water blocks):**
   - Row 54 and Row 55 are completely blocked by water with railings across columns 8-15.
   - Bypassing this requires walking north/south along columns 4-5:
     - If going South from row 53: from `(8, 53)` walk Up to `(8, 49)`, walk West to columns 4-5 at `(4, 49)`.
     - Walk South on columns 4-5 to Row 57.
     - At `(4, 57)`, walk East along Row 57 to columns 10-11 at `(10, 57)` / `(11, 57)`.
   - From `(11, 57)`, columns 10-11 form a continuous vertical dock going South.

4. **Row 57 to Route 13 (y=57 to y=107):**
   - Walk South on columns 10-11 from Row 57 directly to Row 95. (Note: detour around Snorlax at Row 62 by walking Left onto column 10 to bypass the signpost at `(11, 63)`).
   - At Row 95, columns 10-11 are blocked by water. Walk East to columns 14-15.
   - Walk South on columns 14-15 to Row 99.
   - At Row 99, columns 14-15 are blocked by water. Walk West to columns 12-13.
   - Walk South on columns 12-13 to Row 105.
   - At Row 105, columns 12-13 are blocked by water. Walk West to columns 10-11.
   - Walk South on columns 10-11 to Row 107 to enter Route 13 at `(11, 107)`.
   - Walk West along Row 82 to the main western dock at columns 4-5 at `(4, 82)`.
   - Walk South on columns 4-5 to Row 104.
   - Walk East to columns 12-13 on Row 103, and then South to Route 13 at `(11, 107)`.

- There is a signpost outside the Fishing Guru's brother's house at `(9, 40)` that reads "The FISHING FOOL vs. POKéMON KID!".

## Defeated Trainers
- **Jr. Trainer (Male):** Standing at `(11, 92)` after challenging from `(11, 92)` (facing left) on Turn 19094. Defeated on Turn 19114. Roster: Nidoran♂ Lv 29, Nidorino Lv 29. Prize money: ¥580.
- **Fisherman Ned:** Standing at `(11, 31)` after challenging from `(14, 31)`. Defeated on Turn 18942. Roster: Goldeen Lv 22, Poliwag Lv 22, Goldeen Lv 22. Prize money: ¥770.
- **Fisherman Hank:** Standing at `(5, 36)` after challenging from `(5, 39)`. Defeated on Turn 18956. Roster: Tentacool Lv 24, Goldeen Lv 24. Prize money: ¥840.
- **Fisherman Kyle:** Standing at `(9, 40)` after challenging from `(9, 40)` on Turn 18959. Defeated on Turn 18962. Roster: Goldeen Lv 27. Prize money: ¥945.
- **Fisherman Barney:** Standing at `(11, 52)` after challenging from `(9, 52)` on Turn 18971. Defeated on Turn 18972. Roster: Poliwag Lv 21, Shellder Lv 21, Goldeen Lv 21, Horsea Lv 21. Prize money: ¥735.

- **Rocker:** Standing at `(14, 74)` after challenging from `(14, 76)`. Defeated on Turn 19052. Roster: Voltorb Lv 29, Electrode Lv 29. Prize money: ¥725.

## Cleared Obstacles
- **Snorlax:** Level 30 sleeping Snorlax located at `(10, 62)`. Awakened with the Poké Flute and defeated on Turn 19022. The docks at row 62 are now clear and walkable, opening access to southern Route 12 and Route 13.

## Points of Interest
- **Fishing Guru's Brother's House:** Located at `(11, 77)`. Inside, the Fishing Guru's brother lives. On Turn 19079, the player entered the house, spoke to him at `(2, 4)`, and obtained the **SUPER ROD** after freeing a bag slot by consuming an Elixer.
