# Suicune Hunt Strategy (Crystal)
- Status: ROAMING (Post-Tin Tower). Suicune entered the roaming phase after the scripted encounter at the Tin Tower.
- Lead: XENON (Gastly Lv21). Moves: Mean Look (prevents fleeing), Hypnosis (induces sleep).
- Strategy: Boundary cycling between Route 38 and Ecruteak City is the most efficient method. Move between maps and check the Pokedex 'Area' map snapshot. When Suicune is on your current route, search the grass.
- Goal: Obtain the Quick Claw to ensure XENON can move first and land Mean Look or Hypnosis before Suicune acts.

# Suicune Battle Plan
- Turn 1: MEAN LOOK. This is mandatory to prevent Suicune from fleeing immediately.
- Turn 2+: HYPNOSIS. Suicune must be kept asleep at all times. Roar will end the battle and force Suicune to a new location even if Mean Look is active.
- Turn 3+: NIGHT SHADE. This move deals fixed damage equal to the user's level, which is perfect for chipping away at Suicune's HP without accidental KOs.

# Quick Claw Quest
- NPC: A woman sitting on a bench in the northeast section of the National Park.
- Pathing: Enter the National Park from the south entrance on Route 35 (3, 5). Navigate through the grass towards the north. Follow the perimeter fence east towards the gatehouse that leads to Route 36. The NPC is located on a bench in this northeast corner.

# Tile Mechanics (Verified)
- FLOOR: Standard traversable ground.
- WALL: Impassable collision. Includes buildings and dense trees.
- WATER: Traversable only while using the HM move Surf.
- TALL_GRASS / LONG_GRASS: Traversable ground that triggers wild Pokemon encounters.
- HEADBUTT_TREE: Impassable tree that can be interacted with using the move Headbutt to trigger encounters.
- LEDGE_HOP_DOWN: One-way traversable ledge. Allows movement only in the downward direction.
- CUT_TREE: Small, impassable tree that can be removed permanently (until map reload) using the HM move Cut.
- DOOR / WARP_CARPET: Interaction or movement onto these tiles triggers a map transition (warp).
- BUOY: Impassable water obstacle found in the Olivine City harbor and Route 40/41 areas.

# Resources & PC Inventory
- Poke Balls: 1 Ultra Ball, 23 Great Balls, 2 Poke Balls.
- Healing/Utility: 3 Super Repels, 1 Max Ether, 1 Max Revive, 2 Lemonades, 1 Fresh Water, 1 Full Restore.
- PC Box Status: 10/20 slots filled in Box 1.
- Stored Pokemon: RICOTTA (Raticate), CINNABAR (Goldeen), VORTEX (Poliwag), INTERCEPT (Yanma), ROCKY (Onix), EGG (Cleffa), XFDW (Meowth), FRITTATA (Togepi), SHUCKIE (Shuckle), Blarney (Sudowoodo).

# Menu Navigation & Fly Map Logic
- Rule: Always press the B button multiple times to clear the screen of any prompts, dialogue, or menus before starting a new input sequence. This ensures a consistent starting state.
- Rule: To avoid accidentally re-entering buildings, move at least one tile away from the door (warp tile) before opening the Start menu.
- Menu Wrapping: The main Start menu wraps around. Pressing 'Up' from POKEDEX will select EXIT. Pressing 'Down' from EXIT will select POKEDEX.
- Fly Map: In Olivine City, the cursor on the Fly map defaults to New Bark Town. This has been verified through observation.

# Swarms & Tracking
- Yanma Swarm: Reported by Arnie via phone call on Turn 19540. The swarm is located in the tall grass of Route 35. This should be verified using the Pokegear's Radio or Phone features to ensure it is still active.
- Suicune Tracking: Suicune's location changes every time the player crosses a map boundary. Pokedex 'Area' checks provide a snapshot of its current location.