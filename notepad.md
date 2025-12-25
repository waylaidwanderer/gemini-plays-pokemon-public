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
- **Correction:** If Whirlpool fails, execute strict sequence: Turn 1: 'B' (Close). Turn 2: 'Down' (Face). Turn 3: 'Start' (Menu).
- **Menu Mechanics:** Directional inputs inside a menu move the cursor, NOT the player. To change facing, you MUST be in the Overworld.
- **Input Eating:** Inputs sent immediately after closing a menu often fail. Always wait a full turn or use `sleep` after closing a menu before moving/turning.