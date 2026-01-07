# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25957 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Send out Gyarados (Last Resort).
- **Battle Plan:**
    1. **Status:** Muscle Fainted (Crit Flamethrower).
    2. **Current Action:** Clear "Critical hit!" text -> "Muscle fainted!" -> Send Gyarados.
    3. **Next Turn (Gyarados):** Use **MAX REVIVE** on Muscle.
       - Gyarados will faint to Charizard.
    4. **Turn X (Muscle):** Muscle returns with Full HP (280).
       - Charizard attacks (~100 dmg). Muscle survives.
       - Muscle uses Strength (or Rock Slide if I had it... wait, check moveset).
       - Moveset: Strength, ThunderPunch, Ice Punch, Cross Chop.
       - Stick with Strength (Physical) or try ThunderPunch (2x Super Effective but Special).
    5. **Sweeping:** Snorlax, Venusaur, Blastoise remaining.
- **Resources:** Muscle (Fainted). Gyarados (117/117). 1 Max Revive. 2 Hyper Potions.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.