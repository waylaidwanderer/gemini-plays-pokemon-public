# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25952 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Clear Text -> Tank Charizard's Hit.
- **Battle Plan:**
    1. **Charizard (Lv77):** Active. Muscle (251 HP).
    2. **Action:** Press B to clear healing text.
    3. **Opponent Turn:** Charizard attacks (Flamethrower/Wing Attack). Muscle tanks.
    4. **My Turn:** Use Strength.
       - Math confirmed: Strength (Physical, 80 BP) > ThunderPunch (Special, 150 BP effective).
       - Machoke's Atk is ~2x SpAtk, and Charizard's Def < SpDef.
    5. **Snorlax:** Muscle's Cross Chop.
    6. **Venusaur:** Ice Punch or Strength.
    7. **Blastoise:** Cross Chop.
- **Resources:** Muscle (251/280). 3 Hyper Potions. 1 Max Revive. Gyarados alive.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.