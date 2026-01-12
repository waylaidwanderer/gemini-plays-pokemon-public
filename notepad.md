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
- Fly Debugging (Turn 35682):
  - Current Location: Pewter City (Confirmed).
  - Failure Analysis (Turn 35681): `Up` worked (Viridian -> Pewter). `Right` failed (Pewter -> Cerulean failed, stayed at Pewter).
  - Hypothesis: Input dropped or connection doesn't exist.
  - Action: Right (to Cerulean) -> Wait (2s) -> Down (to Saffron).
  - Expected Outcome:
    - If Saffron: Success.
    - If Viridian: `Right` failed (Pewter -> Viridian via Down).
    - If Cerulean: `Down` failed.