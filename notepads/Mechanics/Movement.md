[Movement Rules]
- Turning vs Stepping: If you change direction from a standstill, your character will "turn in place" first. This consumes an input/turn without changing your (x, y) coordinates. Account for this in long movement sequences!
- Ledges & Obstacles: Gym statues have 2-tile bases. Ledges (like the water barriers in Cerulean Gym) act as one-way drops or solid walls depending on the side. 
- ALWAYS use short, 1-3 step movements to test unfamiliar collisions before committing to long tool sequences.
[Gen 1 Movement Mechanics]
- 1st directional press turns the character in place.
- 2nd consecutive press in the same direction moves the character to the next tile.
- Custom tools MUST include a short sleep (e.g., 'sleep 150') between these presses to ensure the emulator registers them as distinct inputs, otherwise the character will just spin in place forever without triggering encounters.