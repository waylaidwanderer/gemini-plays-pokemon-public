# Gem's Gameplay Log & Strategies

## 1. Game Mechanics & Rules
- **NPC Interaction Rule:** If an NPC with a trainer sprite only provides dialogue on the first interaction, assume they are a non-battler. Mark them and move on.
- **Poison Damage:** Poisoned Pokémon lose 1 HP every four steps.
- **Level Cap EXP:** Pokémon at the level cap will show an EXP gain message, but their actual EXP value does not increase. This is a visual bug.
- **Move Categories:** In Gen 1, move categories are based on type. Flying-type moves like Gust are Physical, so their damage IS affected by moves like Growl.
- **ROM Hack Type Changes:**
    - Sandshrew is a NORMAL type, not Ground.

## 2. Battle Intel & Movesets
- **Mankey (Route 22):** Low Kick can cause flinching.

## 3. Gym Leader Intel
### Pewter City Gym - Brock
- **Status:** Defeated.
- **Team:** Geodude (Lv 12), Onix (Lv 14).

### Cerulean City Gym - Misty
- **Status:** Failed Attempt 1 (Blacked out).
- **Team:** Psyduck (Lv 18), Goldeen (Lv 18), Starmie (Lv 21).
- **Key Intel:** Starmie (Water/Psychic) is fast and powerful, using Bubblebeam and Confusion.
- **Strategy:** Need a strong counter for Starmie. SPARKY (Electric) is a good option, but needs more levels. Exploring Route 24/25 for EXP and potential counters is the current plan.

## 4. Rival Battle Intel
- **BLAZe @ Oak's Lab:** Eevee (Lv 5).
- **BLAZe @ Route 22:** Pidgeotto (Lv 9), Rattata (Lv 8), Eevee (Lv 10).
- **BLAZe @ Cerulean City (North):** Pidgeotto (Lv 18), Raticate (Lv 17), Kadabra (Lv 16), Vaporeon (Lv 20).

## 5. Major Encounters
- **Team Rocket (Jessie & James) @ Mt. Moon:** Ekans (Lv 15), Meowth (Lv 16), Koffing (Lv 15).
- **Super Nerd @ Mt. Moon:** Grimer (Lv 12), Voltorb (Lv 12), Magnemite (Lv 12), Clefairy (Lv 12).

## 6. Navigation & Exploration Notes
- **Route 4:** Confirmed one-way path EAST to Cerulean City.
- **Route 25:** Northern maze area is currently inaccessible from the south. Path to Bill's house must be to the east. Item at (23, 3) is unreachable from current path.
- **Sleeping Electrode @ Cerulean (29, 27):** Interaction currently does nothing.

## 7. Defeated Trainers
- **Route 24:** Jr. Trainer @ (6, 21), Lass @ (11, 23), Youngster @ (12, 26), Bug Catcher @ (12, 32), Rocket Grunt @ (12, 16).
- **Route 25:** Hiker @ (9, 5), Lass @ (19, 9), Hiker @ (24, 10).

## 8. Non-Battling NPCs
- **Cerulean City:** Cool Trainer F @ (30, 27), Cool Trainer M @ (32, 21).
- **Cerulean Mart:** Cool Trainer M @ (4, 6) (gives advice).
- **Route 24:** Cool Trainer M @ (7, 6) (gives Charmander).
- **Route 25:** Hiker @ (14, 8), Cool Trainer F @ (19, 9).

## 9. Agent Development Log
- **`battle_action_advisor`:** Updated to correctly identify and handle disabled moves.
- **`battle_navigator_agent`:** Needs review for reliability in complex sequences.

## Turn 9329 Reflection
- **Notepad:** Looks okay for now, but could be reorganized later.
- **New Agents:** An `exp_tracker_agent` could be useful for monitoring level caps and training progress.
- **Agent Usage:** No missed opportunities for agent use recently.
- **Agent Updates:** Agents are performing as expected.
- **Agent Deletion:** No agents are obsolete.
- **Map Markers:** Will mark the Youngster at (33,4) as defeated after the battle. Will also start marking non-battling NPCs.
- **Redundant Markers:** None found.
- **Hindsight:** Should have healed the party, especially THISTLE, before venturing this far. Using `pathfinder_agent` for Route 25 might have been more efficient.
- **Goals:** Current goals remain valid and I am making progress.
- **Assumptions:**
    1. The path to Bill's house is east.
    2. My party can handle all remaining trainers without healing.
    3. The item at (23,3) is non-essential.
    4. Defeating all trainers will clear the path to Bill's house.
    5. SPROUT can handle this Ekans despite the type disadvantage.