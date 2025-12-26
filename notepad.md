# Global Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. Rock faces and boundaries. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction only. [Verified]
- CUT_TREE: Impassable. Can be removed with Cut. [Verified]
- FLOOR_UP_WALL: Impassable ledge (one-way down). [Verified]
- CAVE: Traversable. Warp point leading to interiors. [Verified]
- WARP_CARPET: Traversable. Transition between maps/gatehouses. [Verified]
- TALL_GRASS: Traversable. Wild Pokémon encounters. [Verified]
- PC: Standing below (facing up) and pressing A allows access to item and Pokémon storage. [Verified]

# Strategy: Suicune Hunt (Johto)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood (Complete)
- Sighting 3: Route 42 island grove. [Start Turn 21694]
- Sighting 3 HOW: Enter Route 42 from Ecruteak. Surf east to the island floor at (22, 12). Land and move to (24, 12). Use CUT on tree at (24, 13). Approach Suicune in the grove (approx 26, 14) to trigger flee.
- Sighting 4: Route 36. Triggered at the Sudowoodo junction after Route 42.
- Sighting 5: Fuchsia City (Kanto).
- Final Battle: Tin Tower 1F (Requires Clear Bell).
- Primary Goal HOW: Complete all 5 sightings. Enter Tin Tower 1F. Use Xenon (Gastly) for Hypnosis and Mean Look. Use Ultra/Great Balls.
- Note: Pokedex "Area" is for Raikou/Entei. Suicune is scripted.

# Week Siblings Strategy
- Arthur (Thursday): Route 36. Provides Hard Stone. [COMPLETED - Turn 21872]
- Hard Stone Mystery: Found held by GNEISS (Turn 21872).
- Lesson: Moving NPCs like Arthur can be difficult to interact with. Use `stun_npc` to freeze them in place.
- Lesson: Never mix directional inputs and the A button in the same turn; the system will strip the A button to prevent errors. Move first, then interact.

# Gym Progress
- Rising Badge (Clair): Next Gym Badge required. Need to travel to Blackthorn City.
- Badges Obtained: Zephyr, Hive, Plain, Fog, Mineral, Storm, Glacier. (7/8 Johto Badges).

# PC Storage Inventory
- Box 1: RICOTTA (Raticate), CINNABAR (Goldeen), VORTEX (Poliwag), INTERCEPT (Yanma), ROCKY (Onix), EGG (Cleffa), XFDW (Meowth), FRITTATA (Togepi), SHUCKIE (Shuckle), Blarney (Sudowoodo).

# NPC & Interaction Lessons
- PC "MOVE PKMN W/O MAIL" is the most reliable way to check stored items.
- Check held items if an NPC dialogue loops or item seems missing.
- Menu Navigation: Use menu_navigator_v3_fixed_borders to handle borders.
- Task: Route 42 Suicune Search/Apricorn Harvest. [Start Turn 21898]
- Inventory: Hard Stone confirmed in bag (Turn 21901).
- Suicune Sighting 3 Mystery: Sprite not appearing on island (26, 14). 
- Troubleshooter Insight (Turn 21907): Since I have 3 Green, 3 Pink, and 2 Yellow Apricorns (harvested from this island earlier), the sighting at Route 42 was likely triggered already, even if I missed the animation.
- Strategy: If Suicune is not at Mt. Mortar entrance (28, 9), I will check Route 36 (Sudowoodo spot) and then attempt to enter Tin Tower (possess Clear Bell).
- Task: Final sweep of Route 42 for Suicune. [Start Turn 21909]
- Reflection (Turn 21907):
  1. Immediate Execution: Deferred using npc_troubleshooter_agent for Suicune mystery. Performing now.
  2. Notepad Hygiene: Organized. Added Suicune search task tracking.
  3. Map Hygiene: Relevant locations marked.
  4. Automation: Using Troubleshooter agent to investigate missing Suicune trigger.
  5. Goal Clarity: Primary goal is Tin Tower Suicune. Secondary is Route 42 trigger.
  6. Root Hypothesis: Suicune should be on Route 42 island. Investigation: Sprite is missing. Root cause may be a missing prerequisite or incorrect sequence.
- Task: Investigating Suicune Sighting 3 requirements. [Start Turn 21907]
- Lesson: Turn mismatch detected at Turn 21914. Must verify game state thoroughly. [Turn 21914]
- Strategy: Heading to Route 36 via Violet City to trigger Suicune Sighting 4. [Turn 21914]