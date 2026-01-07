# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25970 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Execute Strength.
- **Battle Plan:**
    1. **Current State:** Muscle (280/280) vs Charizard. Cursor on STRENGTH.
    2. **Action:** Press A to use STRENGTH.
    3. **Opponent Turn:** Charizard attacks (Flamethrower/Wing Attack). Muscle tanks (~120-160 dmg).
    4. **My Turn:** Strength hits (~80-100 dmg).
    5. **Next:** Assess HP. If low, Heal. If high, Attack.
- **Resources:** Muscle (280/280). 0 Max Revive. 2 Hyper Potions. All other mons fainted.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.