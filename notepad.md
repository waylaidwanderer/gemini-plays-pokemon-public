# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25973 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Heal Muscle with Hyper Potion.
- **Battle Plan:**
    1. **Current State:** Muscle (79/280, Burned). Charizard (~60%).
    2. **Danger:** 79 HP is lethal range for Flamethrower. Must Heal.
    3. **Action:** Open PACK -> Use Hyper Potion.
    4. **Next Turn (Attacking):** Use **ThunderPunch**.
       - Reason: Burn halves Attack (Strength becomes weak).
       - ThunderPunch (Special) is unaffected by Burn and is Super Effective.
- **Resources:** Muscle (79/280). 0 Max Revive. ~2 Hyper Potions. All other mons fainted.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.