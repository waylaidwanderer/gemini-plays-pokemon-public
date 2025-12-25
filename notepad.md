# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross the whirlpool to reach the Dragon Shrine.

# Key Mechanics & Lessons
- **Field Moves:** If 'A' interaction fails (even when facing correctly), ALWAYS fallback to Menu -> Pokemon -> [Mon] -> [Move].
- **Whirlpool:** Requires facing the whirlpool tile directly. 'A' button might be unreliable; Menu is safer.

- **Hard Reset Protocol:** When stuck in a menu/facing loop, spend one FULL turn pressing 'B' (x3) to clear state. Do NOT mix with movement. Move in the NEXT turn.
- **Menu-Move Sequencing:** To avoid inputs being eaten by menu closing animations, use the 'sleep' command in `press_buttons`. Example: `["B", "sleep 500", "Down"]`.
- **Facing Issue:** Game state reports 'Facing: Up' despite attempted 'Down' input. Likely caused by mixing 'B' (menu close) and 'Down' in the same turn.
- **Correction:** Executing strict sequence to fix facing: Close Menu -> Face Down -> Open Menu. Using 1000ms delays to prevent input eating.
- **Menu Mechanics:** Directional inputs inside a menu move the cursor, NOT the player. To change facing, you MUST be in the Overworld.
- **Input Eating:** Inputs sent immediately after closing a menu often fail. Always wait a full turn or use `sleep` after closing a menu before moving/turning.
- **Whirlpool Usage:** Attempting to use Whirlpool from the menu while facing the wrong way results in "Can't use that here." Must face the whirlpool tile first.
- Attempting to use Whirlpool via Menu (Start -> Pokemon -> Lapis).
- Assumed Start Menu cursor resets to POKÉDEX (Top).
- Whirlpool interaction via 'A' failed (no text).
- Party Menu Cursor persistence: It started on Slot 5 (Kunai). Always verify cursor position before blind navigation.
- Whirlpool interaction confirmed: "Can't use that here" when facing wrong way.
- Requirement: Must be in Overworld, Facing Whirlpool (DOWN), then select Move.
- Current State: Facing DOWN at (15, 22). Menu Closed.
- Action: Open Menu (Start) -> Select Pokemon (A).
- Next: Navigate to Lapis -> Select Whirlpool.
- Note: Verifying Party Menu cursor position before navigation.
- Field moves: Surf (1), Whirlpool (2).
- Turn 18116: Previous attempt to open menu (Start, A) yielded no screen text.
- Hypothesis: Menu didn't open, or text extraction failed.
- Action: Pressing Down (to ensure facing/bump), then Start, then A.
- Goal: Open Start Menu and select the current option (hopefully Pokémon or Pokedex) to verify state.
- Note: If Party Menu opens, cursor might be on Slot 5 (Kunai) based on previous notes.