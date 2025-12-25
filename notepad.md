# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross the whirlpool to reach the Dragon Shrine.

# Key Mechanics & Lessons
- **Field Moves:** If 'A' interaction fails (even when facing correctly), ALWAYS fallback to Menu -> Pokemon -> [Mon] -> [Move].
- **Whirlpool:** Requires facing the whirlpool tile directly. 'A' button might be unreliable; Menu is safer.

- Status: Correction - Resetting to Face Down.
- Reason: Game State shows 'Facing: up'. Menu interaction likely requires correct facing. Previous attempts to face down failed due to input sanitization.
- Action: Use slow_press to Close Menu (B) -> Face Down (Down) -> Interact (A).
- Note: Using slow_press to allow mixing B and Down.