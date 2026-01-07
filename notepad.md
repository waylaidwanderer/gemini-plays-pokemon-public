# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25973 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Select FIGHT -> Switch to ThunderPunch.
- **Battle Plan:**
    1. **Current State:** Muscle (243/280, Burned). Charizard (~60%).
    2. **Insight:** Burn halves Attack (Physical). Strength is now weak (~40 BP eff).
    3. **New Tactic:** Use ThunderPunch (Special).
       - Electric vs Flying = 2x.
       - Base 75 * 2 = 150 BP.
       - Burn does NOT lower Special Attack.
       - Even with low SpAtk, 150 BP Special > 40 BP Physical.
    4. **Action:** Select FIGHT to open move menu.
    5. **Next:** Select ThunderPunch.
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