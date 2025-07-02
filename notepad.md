# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified & In-Progress)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, BOOKSHELF, TV, TOWN_MAP, WINDOW, RADIO, HEADBUTT_TREE, PC, COUNTER, PILLAR.
- **Traversable:** FLOOR, GRASS.
- **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_RIGHT, WARP_CARPET_DOWN.
- **Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_RIGHT, WARP_CARPET_LEFT.
- **One-Way Down:** LEDGE / FLOOR_ALLOW_HOP_DOWN (Horizontal movement needs to be tested).
- **Complex One-Way:** FLOOR_UP_WALL (Can be entered from below, but not exited up or down. Sideways movement is permitted).
- **One-Way Down:** LEDGE / FLOOR_ALLOW_HOP_DOWN (Horizontal movement needs to be tested).
- **Complex One-Way:** FLOOR_UP_WALL (Can be entered from below, but not exited up or down. Sideways movement is permitted).

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.
- The `stun_npc` tool is essential for interacting with moving NPCs.

## II. Quest Progression

### Current Objective: Clear Team Rocket from Azalea Town
- **Status:** I am currently stuck trying to get Kurt to help me deal with Team Rocket. The grunts at the Slowpoke Well and the Gym are blocking progress.
- **Active Hypothesis (from `quest_strategist`):** The correct event sequence is: 
  1. Talk to the Rocket Grunt at the Slowpoke Well (Complete).
  2. Interact with the Farfetch'd statue in Kurt's house (Complete).
  3. Talk to the apprentice in Kurt's house (In Progress).
  4. Talk to Kurt.

### Blocked Path: Ilex Forest
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. I will return here after dealing with the Azalea Town situation.

## III. Data Management Reminders
- I MUST use `manage_world_knowledge` IMMEDIATELY after every map transition to keep my World Knowledge Graph accurate.