# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25968 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Send out Muscle.
- **Battle Plan:**
    1. **Current State:** Gyarados fainted. Muscle revived (280/280).
    2. **Action:** Select Muscle (Slot 1).
    3. **Next Turn:** Muscle vs Charizard.
       - Charizard attacks (Flamethrower/Wing Attack). Muscle tanks.
       - Muscle uses Strength (Physical > Special ThunderPunch).
    4. **Sweeping:** Snorlax, Venusaur, Blastoise remaining.
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