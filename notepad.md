# Global Tile Mechanics
- FLOOR: Traversable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. (e.g., 28,14) [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. (e.g., 24,13) [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]

# Suicune Hunt Strategy (Crystal)
- Started: Turn 22256.
- Trigger Logic: Proximity-based sighting sequence. Suicune roams ONLY after the Tin Tower event if not caught.
- Sighting 3 (Route 42): Proximity trigger on central island (X:22-30, Y:12-17). Landing at (26, 15) from south is the recommended approach.
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final).
- Current Reset Strategy: Gatehouse hopping. [Started Turn 23337]
    1. Travel to Route 42 West Gatehouse at (0, 9).
    2. Toggle map transitions between Route 42 and the Gatehouse (or Ecruteak City).
    3. Check Pokédex after each transition.
    4. Once Suicune is on Route 42, surf to the central island and land at (26, 15).
- Failed Trigger Attempts: (26, 13), (27, 14), (26, 14), (25, 14), (24, 14), exhaustive sweep, and Hard Map Reset (Fly).
- Resets attempted: Ecruteak Gate, Mt. Mortar Entrance, Mahogany Gate, Ecruteak City (Fly).

# Battle Strategy: Suicune
- Status: Leading with XENON (Gastly).
- Overworld: Scripted fleeing events. Mean Look not required.
- Scripted Battle (Tin Tower): Focus on Hypnosis/Sleep Powder and chip damage.

# Type Effectiveness (Verified)
- Fire -> Grass: Super Effective
- Water -> Fire: Super Effective
- Electric -> Water: Super Effective
- Ground -> Poison: Super Effective
- Ghost -> Psychic: Super Effective

# Observed Movesets
- GASTLY (Xenon): Hypnosis, Lick, Night Shade, Mean Look.
- KRABBY (Ravioli): Bubble, Leer, Surf.
- PIDGEY (Icarus): Quick Attack, Sand-Attack, Gust, Fly.
- GRAVELER (Gneiss): Earthquake, Defense CURL, Strength, Rollout.
- TYPHLOSION (Calcifer): Flame Wheel, HEADBUTT, SMOKESCREEN, THUNDERPUNCH.
- GLOOM (KimCHI): Absorb, Sweet Scent, Cut, Sleep Powder.

# PC Storage Inventory
- Box 1: RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Route 42 Tile Mechanics
- WATER: Traversable with HM03 Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interacting with Headbutt may trigger encounters. [Verified]
- CUT_TREE: Impassable. Removed with HM01 Cut. [Verified]
- CAVE: Warp to Mount Mortar. [Verified]
- WARP_CARPET_LEFT: Warp to Ecruteak Gatehouse. [Verified]
- FLOOR_UP_WALL: Impassable. Visual boundary. [Verified]
## Sighting 3 (Route 42) - Attempt Log
- Turn 23306: Map reset via Mt. Mortar performed. Approaching (26, 14) from the south via Surf.
- Hypothesis: Eusine battle flag in Cianwood is the primary gate. If Suicune doesn't appear now, I must return to Cianwood and verify Eusine's defeat.
- Observation: (26, 14) was previously stepped on without trigger. Cave-exit reset is the current test.
## Roaming Suicune Hypothesis (Crystal)
- Turn 23321: Pokédex confirms Suicune is roaming (icon visible on map).
- Observation: Suicune is currently on the east side of Johto.
- Hypothesis: Scripted sightings in Crystal may require the roaming icon to be present on the current route to trigger the overworld event.
- Plan: Cycle map transitions at the Route 42/Ecruteak gatehouse until Suicune is on Route 42.
- Turn 23337: Mt. Mortar reset failed (sprite did not appear at (26, 14)). 
- New Strategy: Gatehouse hopping. Cross the Route 42/Ecruteak boundary repeatedly and check the Pokédex until Suicune is on Route 42. Then check the island.
- Reason: Scripted sightings in Crystal may be tied to the roaming Suicune's current map location.

# Reflection & Lessons Learned
- **Turn 23357 Reflection:**
    1. **Immediate Execution:** No deferred tasks.
    2. **Notepad Hygiene:** Added "Reflection & Lessons Learned" and strategy timestamps.
    3. **Map Hygiene:** Planned move of Suicune trigger marker to (26, 15).
    4. **Automation Strategy:** Decided to rely on menu_navigator_v4_robust for Pokedex checks.
    5. **Goal Clarity:** Goals are concrete.
    6. **Error Analysis:** Corrected turn count hallucination.
- **Lesson:** Turn count in `tools_to_call` must match the current turn number provided in the Game State.
- **Lesson:** Pokedex Area screen is purely visual; interpret the Johto map based on blue square (city) positions. Ecruteak is (20, 8), Mahogany is (22, 8).

# Suicune Hunt Strategy (Crystal)
- Started: Turn 22256.
- Gatehouse hopping started Turn 23337.
- Current observation: Suicune is currently in the east (approx. Route 44/45) as of Turn 23357.