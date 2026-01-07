# Current Strategy: Battle vs Red
- **Timestamp:** Turn 25953 (Jan 6, 2026)
- **Primary Goal:** Defeat Red.
- **Immediate Task:** Use Hyper Potion on Muscle.
- **Battle Plan:**
    1. **Charizard (Lv77):** Active. Muscle (133/280 HP).
    2. **Turn 1 (Current):** Heal. 133 HP is risky range (Charizard deals ~118).
       - Use Hyper Potion -> 280/280 (Cap is 280, heals 200).
       - Charizard attacks -> ~162 HP.
    3. **Turn 2:** Attack with Strength.
       - Charizard attacks -> ~44 HP.
    4. **Turn 3:** Heal again or Attack (risk).
       - Likely Heal cycle to deplete Charizard PP or fish for misses? No, just trade HP for damage.
    5. **Snorlax/Venusaur/Blastoise:** As planned.
- **Resources:** Muscle (133/280). 2 Hyper Potions. 1 Max Revive. Gyarados alive.

# Recent Discoveries
- Found Max Revive at (6, 3) in the isolated Left Section of the Item Room.

# Tile Mechanics
- **FLOOR_UP_WALL:** Acts as a South-facing Ledge (verified). Blocks North movement.
- **Warp Carpet:** Located at Row 29/31. Avoid stepping on them unless exiting.
- **Waterfalls:** Found at Row 28/29. Requires HM07 Waterfall.
- **Waterfall Mechanics:** Walking into a waterfall causes a slide-back, setting facing to DOWN. To ascend, ensure facing UP (move away and back if needed) then press A to interact. Requires HM07.
- **Tile Mechanics Update:** `FLOOR_UP_WALL` at Row 4 blocked South movement. Treating as impassable for now.
- **Map Structure:** Upper Ledge is segmented. Center (13) connects to Left (6), but Right (17) is blocked by Wall at Col 16.