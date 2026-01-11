# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.
- **Menu Verification:** Use short button sequences (1-5 presses) and verify screen state. Long sequences (20+) are prone to failure due to menu memory.
- **Start Menu Memory:** The cursor stays on the last selected item. To "home" the cursor, press a direction multiple times, but be aware of wrapping.

## Tile Mechanics (Vermilion City)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- DOOR: Warp tile.
- CAVE: Warp tile (Diglett's Cave).
- BIG_SNORLAX: Impassable object. Interact from (36, 8) facing Left.

## Menu Mechanics
- **Start Menu Order:**
  1. POKEDEX
  2. POKEMON
  3. PACK
  4. POKEGEAR
  5. GEM (Player Name)
  6. SAVE
  7. OPTION
  8. EXIT
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. Requires EXPN Card.

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44). Hypnosis/Night Shade/Dream Eater. Good for Snorlax.

## Snorlax Quest Phase
- Goal: Wake Snorlax at Vermilion City / Route 11 junction.
- Start Turn: 40317.
- Method: Use Pokegear Radio (Frequency 20.0 - Poke Flute) to wake him.
- **Current Status (Turn 40437):** Dialogue "SNORLAX is snoring peacefully..." open. XENON lead. Radio setup failed 3 times (Turns 40422, 40423, 40437). Cursor is on GEAR.
- **Plan:**
  1. Close dialogue (B).
  2. Open Start menu (Start).
  3. Open GEAR (A).
  4. Move to Radio tab (Right x3).
  5. Press A, then mash Up (x20) to reach Poke Flute (Frequency 20.0).
  6. Exit (B, B) and interact with Snorlax (A).

## General Lessons & Error Log
- **Dialogue Boxes:** Close dialogue boxes before menuing.
- **Menu Cursor Memory:** The Start menu remembers the last position. In Turn 40428, it started on PACK.
- **Phone Calls:** NPCs can call and interrupt. Check screen state before proceeding.
- **Root Hypothesis Check:** If a sequence fails, check if the starting assumption (e.g., cursor position) was correct. Use intermediate states to verify.