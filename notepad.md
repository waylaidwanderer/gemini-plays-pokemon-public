# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- DOOR/STAIRS/CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below, likely a ledge or wall variant. [Verified]

# Battle and Pokemon Information
## Type Effectiveness (Verified)
- Fire -> Grass: Super Effective
- Water -> Fire: Super Effective
- Electric -> Water: Super Effective
- Ground -> Poison: Super Effective
- Ghost -> Psychic: Super Effective

## Party Movesets
- Calcifer (TYPHLOSION): Flame Wheel, Headbutt, Smokescreen, Thunderpunch.
- ICARUS (PIDGEY): Quick Attack, Sand-Attack, Gust, Fly.
- GNEISS (GRAVELER): Earthquake, Defense Curl, Strength, Rollout.
- Ravioli (KRABBY): Bubble, Leer, Surf.
- XENON (GASTLY): Hypnosis, Lick, Night Shade, Mean Look.
- KIMCHI (GLOOM): Absorb, Sweet Scent, Cut, Sleep Powder.

## PC Storage Inventory
- Box 1: RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Suicune Hunt Strategy (Crystal)
- Status: Suicune is a visible overworld sprite.
- Trigger: The "Tower Shook" event in Ecruteak City is required to progress the hunt.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. Approaches from east side (Mahogany) or resetting map via Mt. Mortar may be required. [Pokedex shows Route 42]
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [IN PROGRESS]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell.

# Money & Economy
- Current Balance: ¥373. Very low. Need to prioritize trainer battles for cash.

# Metadata
- Current Turn: 23780
- Suicune Hunt Duration: 80 turns (since turn 23700)

# General Lessons Learned
- **Interaction Mechanics:** When interacting with NPCs, ensure you are stationary and facing them. Do not mix movement and action buttons in the same sequence.
- **Sequential Progression:** Suicune sightings must follow a strict order. Since the Pokédex still shows Suicune on Route 42, the Route 42 sighting at (26, 14) is a hard prerequisite for the Wise Trio battle.
- **NPC Tracking:** Stun moving NPCs before interacting to ensure they stay in range.
- **Root Hypothesis Testing:** Use the Pokédex as a primary source of truth for legendary tracking. If it says an area is active, that area's trigger must be cleared first.
## Wise Trio Roster (Tin Tower Gatehouse)
- Sage GAKU: Noctowl (Lv32)
- Sage MASA: Flareon (Lv32), Jolteon (Lv32)
- Sage KOJI: Kadabra (Lv32)
- Prerequisite: Must have encountered Suicune at Route 42 and Route 36 sightings before they will battle.

# Suicune Hunt Progress Log
- Sighting 3 (Route 42): 5 failed attempts at (26, 14). Hypothesis: Approach direction or map script reset is required.
- Current Status: Wise Trio in Ecruteak will not battle. Pokedex shows Suicune on Route 42.
- Plan: Fly to Ecruteak, head to Route 42, enter/exit Mt. Mortar, stand on (26, 14).
- Turn 23773: Final conversation check with Gramps confirmed he is still in "lore mode". Heading to Route 42 now.