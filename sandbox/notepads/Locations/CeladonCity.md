# Celadon City — Verified Coordinates & Notes

## Overworld Landmarks (Verified Turns 600–604)
- **East Entrance (from Route 7 `(0, 3)`)**: Enters at **`Celadon City (49, 11)`**.
- **Celadon Pokémon Center**: Door at **`(41, 9)`** *(Note: always attach post-warp `"sleep 700"` to the `"Up"`/`"Down"` button rather than a standalone `press_buttons(["sleep ..."])`, which is prohibited)*.
- **Main East-West Boulevard**: `y = 11..13` runs straight from `(41, 12)` to the east wall of Celadon Dept. Store (`x = 14`), dropping to `y = 14` in front of the store doors.
- **Celadon Department Store**: Doors at **`(8, 13)`** and **`(10, 13)`** (`MART` sign at `(12, 13)`).

## Celadon Department Store Interior (Verified Turns 604–608)
- Entering `(10, 13)` spawns at **`1F (16, 7)`**.
- **Stair Visual Rule**: **White treads = UP stairs**; **dark checkerboard stairwell = DOWN stairs**. Stepping onto a stair warp automatically steps the player south onto `y = 2` on the destination floor.
