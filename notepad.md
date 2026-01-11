# Gem's Pokémon Crystal Knowledge Base

## Core Principles & Strategy
- **Immediate Execution:** Perform tasks the moment they are identified.
- **Scientific Method:** Observe -> Hypothesize -> Test -> Conclude.
- **Efficiency:** Running from wild battles is preferred.
- **Fly Usage:** Use Fly for long-distance travel.
- **Menu Verification:** Use short sequences (1-5 buttons) and verify screen state.
- **Prerequisite Check:** Always verify required items/capabilities in Game State before attempting puzzles.
- **Internal Upgrades:** Some "cards" like the EXPN Card are software upgrades and do not appear as items or separate cards in the Game State.

## Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision.
- WALL: Impassable.
- WATER: Traversable with SURF (requires Storm Badge and a Pokémon with the move SURF).
- TALL_GRASS / LONG_GRASS: Traversable.
- DOOR / WARP: Step on to enter buildings/areas.
- LADDER / PIER: Traversable. Stepping on a pier stops surfing.
- CAVE: Warp tile.
- COUNTER: Impassable Wall. Interact from adjacent tile.
- WARP_CARPET: Warp at map edges.
- BIG_SNORLAX: Impassable object. Interact from (36, 8) facing Left.

## Menu Mechanics
- **Start Menu Order:** 1. POKEDEX, 2. POKEMON, 3. PACK, 4. POKEGEAR, 5. GEM, 6. SAVE, 7. OPTION, 8. EXIT.
- **Pokegear Radio:** Frequency 20.0 (Poke Flute) is at the top of the dial in Kanto. Requires EXPN Card upgrade.
- **Precision Tuning:** The Poke Flute station (20.0) requires exact cursor placement; "TUNING" means you're close but not quite there.

## Party Management
- **Lead Pokémon:** XENON (HAUNTER Lv44).
- **HM Users:** ICARUS (FLY), LAPIS (SURF, WATERFALL, WHIRLPOOL), KIMCHI (CUT, FLASH), GNEISS (STRENGTH).

## Kanto Radio & Snorlax Quest
- **Objective:** Wake Snorlax at Vermilion City / Route 11 junction using the Poke Flute radio channel.
- **Status:** EXPN Card active. Standing at (34, 10) facing Up (interaction point for Snorlax).
- **Strategy:**
  1. Open Pokegear Radio and tune PRECISELY to 20.0 (top center) until "POKE FLUTE" appears.
  2. Close menu and interact with Snorlax (A).
  3. Battle and catch/defeat Snorlax.
  4. Enter Diglett's Cave to reach Pewter City.

## General Lessons & Error Log
- **Dialogue vs. Items:** "With that thing..." dialogue is the definitive indicator of the EXPN Card upgrade receipt. (Turn 40496).
- **Pathing (Route 12):** Surfing is required to bypass broken piers between y=16 and y=13. (Turn 40467).
- **Precision Tuning:** Ensure the needle is at the absolute top of the dial for the Poke Flute. (Turn 40535).
- **Menu Cursor Memory:** Start menu remembers last position. Always verify start position. (Turn 40501).
- **Dialogue Boxes:** Close dialogue boxes before menuing. (Turn 40501).