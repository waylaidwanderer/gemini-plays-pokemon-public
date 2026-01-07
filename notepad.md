# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25979 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Use Lemonade on Muscle.
- **Battle Plan:**
    1. **Current State:** Muscle (135/280, Burned). Charizard (~60%).
    2. **Critical Update:** 0 Hyper Potions left. Using Lemonade (80 HP).
    3. **Math:** 135 + 80 = 215. Charizard Hit (~115) -> 100. Burn -> 82. Survives.
    4. **Loop:** Heal with Lemonade until safe range or opening (Fire Spin/Miss).
    5. **Offense:** Switch to **THUNDERPUNCH** (Special, 150 BP) once safe. Strength is nerfed by Burn.
- **Resources:** Muscle (135/280). 0 Max Revive. 0 Hyper Potions. 9 Lemonades. All other mons fainted.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.