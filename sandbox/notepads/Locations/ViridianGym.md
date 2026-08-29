# Viridian Gym Navigation & Mapping Log

## Gym Status
- Unlocked and Accessible! We have 7 Badges and are currently inside the Viridian Gym at `(4, 22)`.
- Goal: Defeat Gym Leader Giovanni for the Earth Badge (8th Badge).

## Gym Layout & Topography (Verified Ground Truth)
- **Rhydon Statues:** Column 3 is a solid vertical boundary line of Rhydon statues (from Row 18 down to Row 26).
- **Spinner (Arrow) Tiles:** Row 23 contains circular spinner tiles across Columns 4 to 9. These force the player in specific directions.
- **Horizontal Ledges/Dividing Walls:** Row 19 is a solid horizontal dividing wall/ledge running across Columns 4 to 17.
- **Trainers:** There is a Gym Trainer standing at `(5, 26)` (SPRITE_853c) who wanders or patrols.
- **Gym Floor:** Green chequered tiles.
- **Wild Encounters:** Due to a classic Gen 1 design oversight, the Viridian Gym contains wild Pokémon encounters (Grimer, Koffing, Ponyta, Rattata, Pidgey) in the walkable areas.

## Navigation Route to Giovanni (Top-Right/Top-Left)
- Giovanni is located at the top-left of the Gym around `(2, 2)`.
- We need to navigate past the arrow spinner tiles on Row 23 and the horizontal ledges on Row 19 to reach him.
- Safe paths and spinner alignments must be tested step-by-step.