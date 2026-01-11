# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred unless training or catching.
- **Menu Verification:** Use short button sequences (1-5 presses) and verify screen state.
- **Start Menu Memory:** The cursor stays on the last selected item.

## Tile Mechanics (Vermilion City)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- DOOR: Warp tile.
- CAVE: Warp tile (Diglett's Cave).
- BIG_SNORLAX: Impassable object. Interact from (36, 8) facing Left.

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. **Requires EXPN Card.**

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44). Hypnosis/Night Shade/Dream Eater. Good for Snorlax.

## Snorlax Quest Phase
- **Goal:** Wake Snorlax at Vermilion City / Route 11 junction.
- **Status:** Stalled (Turn 40441). Failed to tune Radio to 20.0 after 120+ turns.
- **Observation:** Game State "Pokegear Cards" lists only "MAP, RADIO, PHONE". **EXPN Card is MISSING.**
- **Conclusion:** I cannot wake Snorlax without the EXPN Card. I must return to Lavender Town to acquire it.
- **Strategy:**
  1. Close current dialogue (B).
  2. Travel to Lavender Town Radio Tower.
  3. Speak to the Station Manager to obtain the EXPN Card.
  4. Verify "EXPN" appears in Pokegear Cards list.
  5. Return to Snorlax.

## General Lessons & Error Log
- **Time Blindness:** Spent 120+ turns on a single interaction due to missing prerequisite (EXPN Card). Always check Game State for required items/cards.
- **Insanity Loop:** Repeating the same menu sequence without verifying prerequisites is a failure of the scientific method.
- **Agent Usage:** Failed to use `quest_strategist` when stuck. Corrected by analyzing Game State manually.
- **Menu Memory:** The cursor was on PACK/GEAR, causing sequence failures. Always verify start position.