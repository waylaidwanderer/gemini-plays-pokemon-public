# Gem's Pokémon Crystal Knowledge Base

## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with HM Surf.
- TALL_GRASS: Traversable, triggers wild encounters.
- DOOR/WARP: Step on to enter buildings/areas.
- LEDGE_HOP_DOWN: One-way traversal (North to South).
- COUNTER: Impassable Wall. Interact from adjacent tile.
- STAIRCASE: Warp tile that transitions between floors.
- LADDER: Traversable.
- BIG_SNORLAX: Impassable object. Interact from adjacent tile (36, 8) facing left. Note: Snorlax occupies (34, 8), (35, 8), (34, 9), (35, 9).

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.
- **Reflection (Turn 40377):**
    - Immediate Execution: Swapping Xenon to lead and setting up radio.
    - Notepad Hygiene: Reorganized for better clarity.
    - Map Hygiene: Snorlax and warps marked. Missing markers for Route 11 trainers and objects added.
    - Automation: Tools used for pathing and menus.
    - Goal Clarity: Objectives are outcome-focused.
    - Error Analysis: Verified Poke Flute frequency (20.0) for Kanto.

## Menu Mechanics
- **Start Menu Order (from top):**
  0. POKEDEX
  1. POKEMON
  2. PACK
  3. POKEGEAR (labeled as <gear icon> GEAR)
  4. GEM (Player Name)
  5. SAVE
  6. OPTION
  7. EXIT
- **Pokegear:** 4 clicks down from POKEDEX in the Start menu (POKEDEX, PKMN, PACK, GEAR). Wait, looking at screen text, it's 3 clicks: POKEDEX -> POKEMON -> PACK -> GEAR.
- **Radio:** Frequency 20.0 (Poke Flute) is at the very top of the dial in Kanto. Requires EXPN Card upgrade. Set once, stays until changed.
- **Swap Sequence:** Start -> Reset to Top (Up x7) -> Down (PKMN) -> A -> Down x2 (Xenon) -> Select -> Up x2 (Calcifer) -> Select -> B -> B.

## Party & PC Management
- **Lead Pokémon:** Calcifer (TYPHLOSION Lv58).
- **HM Users:** KIMCHI (FLASH, CUT), GNEISS (STRENGTH), LAPIS (SURF, WHIRLPOOL, WATERFALL), ICARUS (FLY).
- **Xenon (Haunter):** Lead for Snorlax (Normal immunity, Hypnosis).

## Kanto Progression Tracking
- **Magnet Train:** Operational.
- **EXPN Card:** Obtained from Lavender Radio Tower (Turn 40164).
- **Snorlax Roadblock:** Route 11 west end. Requires Poke Flute to wake. Interaction tile: (36, 8).

## Snorlax Quest Phase
- Goal: Wake Snorlax at Vermilion City / Route 11 junction.
- Start Turn: 40317 (2026-01-11 00:00:00).
- Interaction tile: (36, 8) facing Left.
- Status: Positioned at (36, 8) facing Up (Turn 40396). Executing swap and radio setup.
- Method: Use Pokegear Radio (Frequency 20.0 - Poke Flute) to wake him.
- Swap Plan: Lead with XENON (Haunter).
- Interaction: Face Left from (36, 8) and press A.

## General Lessons & Error Log
- **Dialogue Boxes:** Close dialogue boxes before attempting movement.
- **Menu Depth:** Verify cursor position and menu level before executing button sequences.
- **Select Button:** Pressing Select in menus can register items/PKMN; clear with 'B' if 'registered for use' message appears.
- **Start Menu Wrap:** The menu wraps around (Up from POKEDEX -> EXIT).