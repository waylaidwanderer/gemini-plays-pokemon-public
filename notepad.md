# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred.
- **Fly Usage:** Use Fly for long-distance travel. If cursor seems stuck, use `press_buttons`.
- **Menu Verification:** Use short sequences (1-5 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items in Game State before attempting puzzles.
- **Agent Usage:** Use specialized agents if progress stalls for 20+ turns.

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

## Kanto Radio & Snorlax Quest
- **Objective:** Wake Snorlax at Vermilion City / Route 11 junction using the Poke Flute radio channel.
- **Prerequisite:** EXPN Card (Missing from Game State).
- **Quest Status:** Power restored (Magnet Train operational).
- **Strategy:**
  1. Talk to Mr. Fuji (ID 1) at (4, 2) in the Soul House. (Done, no item received).
  2. Use `quest_analyst` to determine missing triggers for EXPN Card.
  3. Revisit Radio Tower 1F and talk to Gentleman (9, 1) and Music Director (14, 6).
  4. If card is still missing, revisit the Power Plant Manager (Route 10).
  5. Once EXPN Card is obtained (verify in Game State), return to Snorlax.

## General Lessons & Error Log
- **Missing Prerequisite:** Spent 180+ turns trying to wake Snorlax without the EXPN Card. Always check Game State for required capabilities.
- **Dialogue vs. Items:** "With that thing..." dialogue does NOT guarantee item receipt if not in Game State.
- **Pathing (Route 12):** Surfing is required to bypass broken piers between y=16 and y=13. (Turn 40467).
- **Time Blindness:** Always monitor turn count when progress stalls.
- **Menu Cursor Memory:** Start menu remembers last position. Always verify start position. (Turn 40501).
- **Dialogue Boxes:** Close dialogue boxes before menuing. (Turn 40501).