# Victory Road 1F
- Map ID: 0_108
- Entrance from Route 23 is at (8, 17).
- Puzzle 1: Boulder started at (5, 15). Switch is at (9, 12).
- Solution:
  1. Use Strength.
  2. Walk to (5, 14) and push boulder DOWN to (5, 16).
  3. Walk to (4, 16) and push boulder RIGHT to (9, 16).
  4. Walk to (9, 17) and push boulder UP to (9, 12).
- Current puzzle state: The boulder is at (9, 16) and is being pushed UP toward the switch at (9, 12).
- Player is at (9, 17).
- Status: Strength needs to be reactivated to push the boulder.
[Turn 49984 Progress]
- The Party menu is open.
- Visual confirmation: The cursor is on CLEO (index 2).
- Cleo has STRENGTH.
- Using `use_hm_field` to activate Strength.
[Turn 49985 Progress]
- Executed `use_hm_field`.
- Visual confirmation: The cursor successfully navigated to CLEO, opened her sub-menu, and selected STRENGTH (index 3).
- The prompt "Choose a POKéMON." is on screen.
- Wait, I used Strength, why is it asking me to choose a Pokemon?
- Ah! Look at the text in the Intermediate States: "No SURFing on HYDRO here!"
- The `use_hm_field` tool failed! It pressed A on HYDRO (index 1), selected SURF (index 1), and then failed because I'm not on water.
- WHY did it do that?
- Reviewing Turn 49984: The Party menu was open. I said "The cursor is on CLEO (index 2)". But my `current_index` argument to `use_hm_field` was `2`.
- Let's look at the Turn 49984 screenshot. The arrow `→` is pointing at `SURF` in HYDRO's sub-menu!
- HALLUCINATION CORRECTION: The cursor was NOT on Cleo! I was looking at the overworld sprite or something. The cursor in the Party menu was actually still on HYDRO from when I healed him with the Hyper Potion!
- Because I passed `current_index=2` to the tool, but the actual cursor was at index 1, the tool's relative navigation was completely wrong. It calculated `target(2) - current(2) = 0 presses`, so it just pressed A on Hydro!
- I am now back at the Party menu root. The cursor is on HYDRO (index 1).
- I need to manually move the cursor down to CLEO (index 2) and select STRENGTH (index 3).
- Executing `Down`, `A` to select Cleo.