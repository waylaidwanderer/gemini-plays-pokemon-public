# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross the whirlpool to reach the Dragon Shrine.

# Key Mechanics & Lessons
- **Field Moves:** If 'A' interaction fails (even when facing correctly), ALWAYS fallback to Menu -> Pokemon -> [Mon] -> [Move].
- **Whirlpool:** Requires facing the whirlpool tile directly. 'A' button might be unreliable; Menu is safer.

- Status: Correcting Facing for Whirlpool (Final Attempt).
- Reason: Game State consistently reports 'Facing: up' despite previous inputs. Menu is currently open.
- Plan: Close Menu (B) -> Wait -> Face Down (Down).
- Logic: Separating the 'Face Down' action from the 'Open Menu' action to ensure the state update is confirmed before proceeding.
- Next Turn: If Facing is 'Down', Open Menu and use Whirlpool.