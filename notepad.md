# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.

# Reflection (Turn 35564)
- **Menu Hygiene:** "Macro" sequences with `sleep` are safer, but visual confirmation is best. "Intermediate States" can be confusing; trust "Current Screen Text".
- **Economics:** Super Repel (500g/200steps = 2.5g/step) is more efficient than Max Repel (700g/250steps = 2.8g/step). Prioritize Super Repels.
- **Status:** Turn 35570 - Exiting Medicine Clerk menu (`B` x2). Moving Down to (11, 6) to talk to Item/Ball Clerk. Goal: Buy 4 Super Repels.
- **Goal:** Buy Super Repels (preferred) or Max Repels.

# Roamer Hunt Log
- **Session Start:** Turn 34090.
- **Goal:** Catch Raikou/Entei.
- **Current Phase:** Restocking Repels at Goldenrod Dept Store 2F.
- **Strategy:** Buy Repels -> Fly/Teleport to randomize -> Hunt.

# Lessons Learned
- **Menu Navigation:** Inputs can be eaten by animations. Pace them.
- **Roamer Mechanics:** Fly randomizes.
- **Mart Stock:** Ecruteak has no Repels. Goldenrod 2F has them.
- Checked Goldenrod 2F Right Clerk (Balls/Repels): Only sells standard Repel.
- Checked Goldenrod 2F Left Clerk (Medicine): No Repels.
- Goldenrod Dept Store does NOT sell Super Repels.
- Celadon Dept Store 2F Left Clerk: Has Super Repels (500g) and Max Repels (700g).
- Purchased 4 Super Repels. Exiting Celadon Dept Store.
- Next Step: Fly to Ecruteak City and hunt Roamers on Route 37/38.

# Reflection (Turn 35620)
- **Immediate Execution:** Close menu, exit store.
- **Goal Clarity:** Clear. Exit -> Fly -> Hunt.
- **Inventory Check:** 4 Super Repels, 244 Yen. Ready.
- Currently at Indigo Plateau (Route 23).
- Mistake: Accidentally opened Pokegear in Turn 35631.
- Correction Plan: Open Start Menu -> Pokemon -> Mistral -> Fly.
- Fly Navigation: Indigo Plateau -> Left x10 (to Cianwood) -> Right x2 (to Ecruteak).
- Menu Navigation Corrected: Cursor was on POKEGEAR. Moving Up x2 to POKEMON.
- Fly Sequence: Pokemon -> Mistral (Slot 4) -> Fly -> Left x3 (Indigo -> Blackthorn -> Mahogany -> Ecruteak).
- Executing Fly sequence now.
- Previous Fly attempt failed (Menu was not open, inputs moved player).
- Current State: Overworld, Route 23.
- Action: Open Start Menu and verify cursor position.
- Next: Navigate to Pokemon -> Mistral -> Fly -> Ecruteak.
- Fly Debugging (Turn 35656):
  - Previous attempts failed to reach Ecruteak. Player remains at Indigo Plateau (9,6).
  - Hypothesis: Navigation "hops" (Left inputs) might be insufficient or mapping is different than expected.
  - Action: Reset to Overworld -> Open Fly Map -> Move Left x3 -> STOP.
  - Goal: Read Screen Text to confirm which city is selected before confirming flight.
  - Sequence: Bx3 (Reset) -> Start -> A (Party) -> A (Mistral) -> A (Fly) -> Wait -> Left x3.