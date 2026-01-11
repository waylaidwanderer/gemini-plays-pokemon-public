# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred.
- **Fly Usage:** Use Fly for long-distance travel. If cursor seems stuck, verify with `press_buttons`.
- **Menu Verification:** Use short sequences (1-3 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items (like EXPN Card) in Game State before attempting puzzles. If a repetitive action fails 5-10 times, audit the root assumption: "Is this even possible right now?"
- **Agent Usage:** Use specialized agents like `quest_strategist_v2` if progress stalls for 20+ turns.

## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Storm Badge and a Pokémon with the move SURF).
- TALL_GRASS / LONG_GRASS: Traversable, triggers wild encounters.
- DOOR / WARP: Step on to enter buildings/areas.
- LADDER / PIER: Traversable. Used for bridge-like structures. Stepping on a pier stops surfing.
- CAVE: Warp tile.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- WARP_CARPET: Warp at map edges.
- BIG_SNORLAX: Impassable object. Interact from (36, 8) facing Left.

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. **Requires EXPN Card.**

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44).
- **HM Users:** ICARUS (FLY), LAPIS (SURF, WATERFALL, WHIRLPOOL), KIMCHI (CUT, FLASH), GNEISS (STRENGTH).

## Snorlax Quest Phase
- **Goal:** Wake Snorlax at Vermilion City / Route 11 junction.
- **Start Turn:** 40317.
- **Status:** Power restored (Magnet Train operational), but EXPN Card is missing. (Turn 40471).

## EXPN Card Sub-Quest
- **Goal:** Acquire EXPN Card from Lavender Radio Tower Station Manager.
- **Start Turn:** 40441.
- **Status:** In Lavender Town, heading to Radio Tower entrance (14, 5).
- **Plan:**
  1. Enter Radio Tower at (14, 5).
  2. Speak to Station Manager (10, 1) on 1F to get EXPN Card.
  3. Verify EXPN Card in Pokegear Cards.
  4. Return to Snorlax.

## General Lessons & Error Log
- **Missing Prerequisite:** Spent 120+ turns trying to wake Snorlax without the EXPN Card. Always check Game State for required capabilities.
- **Pathing (Route 12):** Surfing is required to bypass broken piers between y=16 and y=13. (Turn 40467).