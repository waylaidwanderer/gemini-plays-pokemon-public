# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross the whirlpool to reach the Dragon Shrine.

# Key Mechanics & Lessons
- **Field Moves:** If 'A' interaction fails (even when facing correctly), ALWAYS fallback to Menu -> Pokemon -> [Mon] -> [Move].
- **Whirlpool:** Requires facing the whirlpool tile directly. 'A' button might be unreliable; Menu is safer.

- **Hard Reset Protocol:** When stuck in a menu/facing loop, spend one FULL turn pressing 'B' (x3) to clear state. Do NOT mix with movement. Move in the NEXT turn.
- **Menu-Move Sequencing:** To avoid inputs being eaten by menu closing animations, use the 'sleep' command in `press_buttons`. Example: `["B", "sleep 500", "Down"]`.