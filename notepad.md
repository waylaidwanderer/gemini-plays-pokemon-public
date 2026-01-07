# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25956 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Attack with Strength.
- **Battle Plan:**
    1. **Charizard (Lv77):** Active. Muscle (161/280 HP).
    2. **Current Turn:** Execute Strength (Physical, 80 BP).
       - Charizard attacks first (Flamethrower, ~119 dmg). Muscle drops to ~42 HP.
       - Muscle hits with Strength.
    3. **Next Turn:**
       - If Muscle survives: Assess if another attack kills or if healing is needed.
       - If Muscle faints: Send Gyarados -> Max Revive Muscle -> Sacrifice Gyarados -> Muscle returns.
    4. **Snorlax:** Muscle's Cross Chop.
    5. **Venusaur:** Ice Punch or Strength.
    6. **Blastoise:** Cross Chop.
- **Resources:** Muscle (161/280). 1 Hyper Potion left (approx). 1 Max Revive. Gyarados alive.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.