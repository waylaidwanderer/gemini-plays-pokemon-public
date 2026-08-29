# Map Verification Protocol (MVP)

## Protocol Objectives
To prevent cognitive loops, spatial hallucinations, and multi-thousand-turn coordinate desyncs across map transitions.

## Strict Procedures on Map Transition
Whenever a `SYSTEM NOTE: Map Transition Detected` is received, or when entering a new area, the player MUST execute the following verification steps:

1. **Town Map Verification:**
   - Immediately open the in-game Town Map via the Start Menu (Bag/Items).
   - Visually confirm the blinking player icon on the global map and note the verbatim location name displayed at the top-left (e.g., "VIRIDIAN CITY", "ROUTE 1").

2. **Visual Asset Audit:**
   - Do not rely on speculative memory. Inspect the surrounding overworld tiles to find distinctive, unique assets:
     - Check if wild overworld battles can occur (Gyms vs. Grass).
     - Locate distinctive building styles (Pokémon Center, Poké Mart, specific roofs/doors).
     - Locate unique, stationary NPCs (such as the Gym Guide or gym statues) and read signposts.

3. **Coordinate & Boundary Checks:**
   - Move 1–2 steps and verify that coordinates change exactly as expected.
   - Cross-reference coordinates with the official layout to confirm that no coordinate shifts or offsets exist.
   - If a movement fails (bumps), treat the target tile as a solid wall/obstacle and update map data.

4. **Hypothesis-First Mindset:**
   - Every prior note, layout summary, or route plan is an unverified hypothesis until proven by in-game empirical evidence on the current turn.