# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25986 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Execute ThunderPunch.
- **Battle Plan:**
    1. **Current State:** Muscle (65/280, Burned). Charizard (~60%).
    2. **Menu State:** In Move Selection. Cursor on STRENGTH.
    3. **Action:** Press Down -> Select **THUNDERPUNCH**.
    4. **Opponent Turn:** Charizard attacks.
       - High chance Muscle faints (65 HP is critical).
       - Small chance to survive if Fire Spin or Miss.
    5. **If Muscle Survives:** ThunderPunch hits (150 BP Special vs 40 BP Physical).
    6. **If Muscle Faints:** Game Over (White out).
- **Resources:** Muscle (65/280). 8 Lemonades. No Revives. Last Stand.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.