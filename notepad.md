# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.
- **Fly Usage:** Use Fly for long-distance travel to save time.
- **Menu Verification:** Use short sequences (1-3 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items (like EXPN Card) in Game State before attempting puzzles.

## Tile Mechanics (Route 11)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS / LONG_GRASS: Traversable, triggers wild encounters.
- WARP_CARPET: Warp at map edges.

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. **Requires EXPN Card.**

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44). Hypnosis/Night Shade/Dream Eater. Good for Snorlax.
- **ICARUS (PIDGEOTTO):** Has FLY for fast travel.

## Snorlax Quest Phase
- **Goal:** Wake Snorlax at Vermilion City / Route 11 junction.
- **Status:** Stalled (Turn #40461). EXPN Card missing from Pokegear Cards list (MAP, RADIO, PHONE). Magnet Train is operational, confirming power is restored.
- **Strategy:**
  1. Walk to Lavender Town Radio Tower via Route 11 and Route 12.
  2. Speak to Station Manager (10, 1) on the ground floor to receive the EXPN Card upgrade.
  3. Verify "EXPN" appears in Pokegear Cards or that Radio can tune to 20.0 (POKE FLUTE).
  4. Return to Snorlax at the Vermilion/Route 11 junction.
  5. Use Pokegear Radio (20.0) to wake and battle Snorlax.
- **Note:** `quest_strategist_v2` incorrectly identified "Machine Part" as missing. Power is verified as restored.

## General Lessons & Error Log
- **Missing Prerequisite (EXPN Card):** Attempted to tune radio without the card for 120+ turns. **Lesson:** Check Game State Information for required capabilities before brute-forcing a solution.
- **Fly Map Cursor:** Cursor can get stuck (Indigo Plateau). Walking is a reliable fallback.
- **Agent Usage:** Use specialized agents like `quest_strategist_v2` when stuck. (Turn 40442).
- **Time Blindness:** Always monitor turn count when progress stalls.
- **Walking Route:** Route 11 -> Route 12 -> Lavender Town. (Turn 40454)