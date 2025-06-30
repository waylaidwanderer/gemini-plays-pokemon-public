# Gem's Pokémon Crystal Notepad

## I. Strategic Overview

### Current Strategy
- **Primary Objective:** My main goal is to get the Hive Badge from the Azalea Town Gym. However, I am currently blocked on Route 32.
- **Current Plan:** Based on my strategic advisor agent's suggestion, I am returning to Violet City. The hypothesis is that showing my newly hatched Togepi (OM) to an NPC there will trigger an event, allowing me to pass the trainer blocking Union Cave.

### Reminders & Best Practices
- **Tool Failures:** I must be persistent in debugging my tools. I will not abandon a tool just because it fails; instead, I will perform a thorough logical review.
- **Mark Dead Ends:** Mark all confirmed dead ends with '🚫' immediately.
- **Test Assumptions:** I need to test my assumption that HEADBUTT_TREEs are interactable with a move and not just scenery. Plan: Once I have a Pokémon with the move HEADBUTT, I will stand adjacent to a HEADBUTT_TREE and attempt to use the move from the party menu.

## II. Battle Intel

### Rival SILVA's Team
- CHIKORITA: Lv5 (Last seen in New Bark Town)

### Observed Movesets
- Wild Poliwag: BUBBLE
- Wild Hoothoot: TACKLE, GROWL, FLASH, FORESIGHT
- Wild Bellsprout: VINE WHIP, GROWTH
- Wild Caterpie: TACKLE, STRING SHOT
- Wild Ekans: (unknown)
- Wild Hoppip: TAIL WHIP, SYNTHESIS
- Wild Rattata: TACKLE, TAIL WHIP
- Wild Wooper: TAIL WHIP, WATER GUN

### Type Effectiveness Chart (Verified)
- Normal is not very effective against Water.
- Normal is not very effective against Rock/Ground.

## III. World Knowledge & Mechanics

### Tile Traversal Rules (Verified)
- **Objects are impassable:** Most map objects (items, trees, signs, active NPCs, etc.) act as walls.
- **Defeated Trainers:** Passability is inconsistent. Some are passable, while others (like Bird Keeper Peter on Route 32) are not. Each must be tested.
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS / LONG_GRASS:** Traversable, triggers wild encounters.
- **LEDGE:** One-way downward traversal.
- **COUNTER:** Impassable.
- **DOOR/CAVE:** Warp tile, triggered by movement.
- **MART_SHELF/BOOKSHELF/TV/RADIO/PC/TOWN_MAP/WINDOW/PAINTING/STATUE/PILLAR:** Impassable scenery.
- **FLOOR_UP_WALL:** One-way traversal. Can only be entered from below (moving up).
- **WARP_CARPET_DOWN:** Warp tile, triggered by movement.
- **VOID:** Impassable.
- **BUOY:** Impassable scenery.
- **CUT_TREE:** Impassable without CUT.
- **WATER:** Impassable without SURF.
- **HEADBUTT_TREE:** Impassable by walking.
- **FLOOR_ALLOW_HOP_DOWN:** One-way traversal downward.
- **FLOOR_ALLOW_HOP_RIGHT:** One-way traversal to the right.
- **FLOOR_ALLOW_HOP_DOWN_OR_RIGHT:** One-way traversal down or right.