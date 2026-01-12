# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.

# Roamer Hunt Log
- **Session Start:** Turn 34090.
- **Goal:** Catch Raikou/Entei.
- **Current Phase:** Transit to Ecruteak City.
- **Strategy:** Fly to Ecruteak -> Check Pokegear -> Hunt/Shuffle.

# Current Problem: Fly Map Navigation
- **Status:** Map Cursor at Fuchsia City (Kanto).
- **Goal:** Fly to Saffron City to take Magnet Train.
- **Navigation:** Pressing UP from Fuchsia should lead towards Saffron.
- **Plan:**
  1. Navigate Cursor to Saffron City.
  2. Fly to Saffron.
  3. Walk to Station -> Take Train -> Arrive Goldenrod.
  4. Fly to Ecruteak from Goldenrod.

# Lessons Learned
- **Menu Hygiene:** Visual confirmation is required before entering complex sequences.
- **Economics:** Super Repels > Max Repels.
- **Fly Mechanics:** 'Select' button toggles map regions in Gen 2. Indigo Plateau is the connection point.
- Fly Debugging (Turn 35685):
  - Current Location: Pallet Town.
  - Previous Tests: `Right` from Pallet blocked. `Right` from Pewter/Viridian failed/blocked in previous turns.
  - Hypothesis: Vertical spine (Pewter-Viridian-Pallet-Cinnabar) is isolated from Central Kanto on the West side?
  - New Route Idea: Try the Southern Connection. Cinnabar -> Right -> Fuchsia.
  - Action: Down (to Cinnabar) -> Right (to Fuchsia).
  - Goal: Reach Fuchsia City. From there, Up -> Left to Saffron.