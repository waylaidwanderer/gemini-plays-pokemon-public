# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.
- **Fly Usage:** Use Fly for long-distance travel to save time.
- **Menu Verification:** Use short sequences (1-3 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items (like EXPN Card) in Game State before attempting puzzles.

## Tile Mechanics (Vermilion City)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- DOOR: Warp tile.
- CAVE: Warp tile (Diglett's Cave).
- BIG_SNORLAX: Impassable object. Interact from (36, 8) facing Left.
- CUT_TREE: Impassable until Cut is used.
- WARP_CARPET_DOWN: Warp at map edge.

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. **Requires EXPN Card.**

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44). Hypnosis/Night Shade/Dream Eater. Good for Snorlax.
- **ICARUS (PIDGEOTTO):** Has FLY for fast travel.

## Snorlax Quest Phase
- **Goal:** Wake Snorlax at Vermilion City / Route 11 junction.
- **Status:** Stalled (Turn 40442). Prerequisite EXPN Card missing from Pokegear Cards list.
- **Strategy:**
  1. Fly to Lavender Town using ICARUS.
  2. Enter Radio Tower and speak to Station Manager (10, 1) to get EXPN Card.
  3. Verify EXPN Card in Pokegear Cards.
  4. Fly back to Vermilion City.
  5. Tune Radio to 20.0 (Poke Flute) and interact with Snorlax.

## General Lessons & Error Log
- **Missing Prerequisite (EXPN Card):** Attempted to tune radio without the card for 120+ turns. **Lesson:** Check Game State Information for required capabilities before brute-forcing a solution.
- **Time Blindness:** Always monitor turn count when progress stalls.
- **Menu Sequence Failure:** Long button sequences in `press_menu_buttons_v2` are unreliable. Stick to 1-3 buttons.
- **Agent Underutilization:** Use specialized agents like `quest_strategist` when stuck. (Turn 40442).