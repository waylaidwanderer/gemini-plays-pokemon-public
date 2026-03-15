[Movement Rules]
- Turning vs Stepping: If you change direction from a standstill, your character will "turn in place" first. This consumes an input/turn without changing your (x, y) coordinates. Account for this in long movement sequences!
- Ledges & Obstacles: Gym statues have 2-tile bases. Ledges (like the water barriers in Cerulean Gym) act as one-way drops or solid walls depending on the side. 
- ALWAYS use short, 1-3 step movements to test unfamiliar collisions before committing to long tool sequences.
[Gen 1 Movement Mechanics]
- HARNESS AUTOMATION: The harness automatically handles turning. Pressing a direction ALWAYS results in a step (or a bump if blocked). DO NOT add extra presses just to turn!
- Bumping: To face a solid object (like a Cut bush), simply press the direction towards it. You will bump it and end up facing it.
- [Gen 1 Ledge Mechanics] Ledges can face South OR East/West! Turn 33137 PROVED that an East-facing ledge (TYPE_44f6) at (23, 28) in Fuchsia City CAN be jumped by walking Right into it. Previous assumption that only South-facing ledges work is false.
- HM FIELD MOVES: You MUST face the target tile (e.g., Cut bush, Water) BEFORE opening the Start Menu. The game checks your facing direction at the exact moment you select the move in the menu. Being adjacent is not enough.
- [Cycling Road] Route 17 has an automatic downward slope that forces the player South. Travel NORTH is IMPOSSIBLE with this harness due to the 500ms input delay allowing gravity to trigger. Must use Eastern routes to travel North.