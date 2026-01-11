# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.
- **Support:** Maelstrom (Lugia).

# Objectives
- **Primary:** Hunt Roamers (Raikou/Entei).
- **Secondary:** Complete Pokedex.
- **Strategy:**
    1. **Travel:** Reach Ecruteak City (Hub).
    2. **Hunt:** Cycle Route 37. Lead with Lugia (Speed 143) to outspeed roamers.
    3. **Action:** Whittle HP or throw Ultra Balls immediately.

# Key Items Status
- **Master Ball:** **MISSING / USED** (Confirmed used on Lugia).
- **Inventory:** 13 Max Repels, Ultra Balls.

# Lessons Learned
- **Fly Map:** Inputs must be SLOW (1 per second or manual verification).
- **Navigation:** Always verify `current_map_id`.

# Current Status
- **Location:** Route 37 (Grass).
- **Next:** Grass Check (Round 2) -> Shuffle if empty.
- **Python/XML:** `xml.etree.ElementTree` does not support `..` parent traversal. Iterate strictly downwards when parsing map XML.
- **Roamer Hunt:** Taking a detour to check the Pokegear Map for Raikou/Entei locations since I accidentally opened it. Use `A` to exit Clock view, then select Map card.
- **Roamer Status:** Visual confirmation on Pokegear Map: Icons spotted on Route 38, Route 42, and potentially Route 30/31.
- **Hunting Strategy:** Since Roamers are nearby (Rt 38/42), I will cycle between Route 37 and Ecruteak City to shuffle their positions.
  1. Move North into Ecruteak.
  2. Move South into Route 37.
  3. Run in grass with Max Repel active (Gyarados Lv36 lead).
  4. Repeat.