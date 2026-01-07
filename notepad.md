# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25972 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Attack with Strength.
- **Battle Plan:**
    1. **Current State:** Muscle (243/280, Trapped) vs Charizard (~65% HP).
    2. **Last Turn:** Charizard used Fire Spin. Muscle used Strength.
    3. **Action:** Press A (Select STRENGTH).
    4. **Opponent Turn:** Charizard attacks (Fire Spin continues or new move).
    5. **Next:** Check HP. Keep attacking with Strength.
- **Resources:** Muscle (243/280). 0 Max Revive. 2 Hyper Potions. All other mons fainted.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.