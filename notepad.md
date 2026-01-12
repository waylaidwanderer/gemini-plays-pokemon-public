# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.

# Reflection (Turn 35045)
- **Lesson:** Shop inventory varies significantly. Kanto Marts (Viridian/Vermilion) lacked Repels entirely. Goldenrod 2F Bottom Clerk only has standard Repels. Top Clerk appears to be Medicine-focused.
- **Strategy:** If Top Clerk lacks Super/Max Repels, I will compromise and buy standard Repels from the Bottom Clerk to avoid further delays. 
- **Efficiency:** Better to hunt with standard Repels than spend 50 turns finding Super ones.

# Roamer Hunt Log
- **Session Start:** Turn 34090.
- **Goal:** Encounter Raikou/Entei on Route 37.
- **Strategy:** Shuffle (Route 37 <-> Ecruteak) -> Check Map. Repeat.
- **Party:** Gyarados (Lv36) w/ Repel.
- **Status:** Turn 35291 - Back on Route 37 (post-Center reset). Checking Map.
- **Note:** Deleted `perform_roamer_shuffle` (unreliable). Using `open_pokegear_map` and manual steps.

# Lessons Learned
- **Static Roamers:** Border hopping (Route 37 <-> Ecruteak) failed to move Roamers from Routes 38/42 for >100 turns.
- **RNG Reset:** Entering a building (Pokemon Center) did not immediately move them either.
- **Solution:** Using Fly to randomize positions is the next logical step when soft methods fail.