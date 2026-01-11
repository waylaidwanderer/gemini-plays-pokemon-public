# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred.
- **Fly Usage:** Use Fly for long-distance travel. If cursor seems stuck, use `press_buttons`.
- **Menu Verification:** Use short sequences (1-5 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items (like EXPN Card) in Game State before attempting puzzles. If a repetitive action fails 5-10 times, audit the root assumption.
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
  1. Talk to Gentleman (9, 1) at (9, 2) facing Up.
  2. Check Sign at (5, 0) and Directory at (11, 0).
  3. Talk to Receptionist (6, 6) from (6, 5) facing Down.
  4. Talk to Super Nerd (14, 6) from (13, 6) facing Right.
  5. If EXPN Card is still missing, revisit the Power Plant (Route 10) to ensure the Manager is satisfied.
  6. Once EXPN Card is obtained (verify in Game State), return to Snorlax.

## General Lessons & Error Log
- **Missing Prerequisite:** Spent 180+ turns trying to wake Snorlax without the EXPN Card. Always check Game State for required capabilities.
- **Pathing (Route 12):** Surfing is required to bypass broken piers between y=16 and y=13. (Turn 40467).
- **Overwatch Note:** Trust Game State over self-placed markers. (Turn 40501).
- **Fly Map:** Cursor may require D-pad `press_buttons` if `press_menu_buttons_v2` fails. (Turn 40450).
- **Insanity Loop:** Repeating menu sequences without verifying prerequisites is a failure of the scientific method.
- **Time Blindness:** Always monitor turn count when progress stalls.
- **Strategy for Avoiding "Insanity Loops":** If a repetitive action fails 5-10 times, stop and verify if a hidden requirement is missing. Audit the root assumption.
- **Menu Cursor Memory:** The Start menu remembers the last position. Always verify start position. (Turn 40501).
- **Dialogue Boxes:** Close dialogue boxes before menuing. (Turn 40501).
- **Phone Calls:** NPCs can call and interrupt. Check screen state before proceeding. (Turn 40501).
- **Failed Pathing:** Attempted to move Right from (7, 4) into a WALL at (8, 4). (Turn 40516).