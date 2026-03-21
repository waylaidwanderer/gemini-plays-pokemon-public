[ACTIVE THEORIES & REFLECTIONS]
- Secret Key Location Hypotheses:
  1. In the West Room of B1F (near the 7,15 switch).
  2. Accessed via a completely different pit on 3F (SW corner, South of Y=10) that drops directly into a blocked-off room on 1F or B1F.
- Mechanics: The doors at X=9 are CLOSED in State B, requiring State A to access the NW room. The Far East doors at (26, 17) provide a path North to Y=7, bypassing the solid wall at Y=8. The NE switch at (20, 3) toggles states from the North side.
- Current Goal: Re-explore the West Room (7, 15) to search for the Secret Key.

[50-Turn Reflection]
- Macro Brittleness: Massive 40-50 step macros in high-encounter zones are a critical strategy failure. Encounters interrupt them, and I often miscalculate my post-battle position/facing, causing the next sequence to drive me into walls. I am switching to 5-10 step micro-macros and actively verifying my Game State coordinates after every battle.
- Notebook Hygiene: Purged 40+ turns of granular turn-by-turn macro debugging from this scratchpad. It was causing massive context bloat and triggering safety limits. Keeping notes strictly to high-level theories and empirical proofs.
- Turn 47463 Reflection: My 8-step macro `DDDDLLLL` was interrupted by another Wild Weezing encounter after 4 steps Down. I am currently at (27, 18) facing Down. I will run from the battle, clear the text, and then recalculate my path from (27, 18) to the West Room (7, 15).
- Turn 47464 Reflection: The battle ended. I am now at (27, 18) facing Down.
I will clear the "Got away safely!" text using B presses, then I will re-evaluate my path to the West Room.
Path to West Room (7, 15) from (27, 18) facing Down:
- Turn Left, step 3 times to (24, 18).
- Turn Up, step 4 times to (24, 14).
- Turn Left, step 17 times to (7, 14).
- Turn Down, step 1 time to (7, 15).
Sequence: `LLLL UUUUU LLLLLLLLLLLLLLLLLL DD`.
- Turn 47465 Reflection: I've successfully run from the Weezing and cleared the "Got away safely!" text. I am now in the overworld at (27, 18), facing Down.
I will execute the macro to the West Room (7, 15):
- L3 (Turn Left, step 2 to 24, 18)
- U5 (Turn Up, step 4 to 24, 14)
- L18 (Turn Left, step 17 to 7, 14)
- D2 (Turn Down, step 1 to 7, 15)
Sequence: `LLLL UUUUU LLLLLLLLLLLLLLLLLL DD`
- Turn 47466 Reflection: The sequence worked perfectly up to (10, 15)! I am currently at (10, 15) facing Down. My macro `LLLL UUUUU LLLLLLLLLLLLLLLLLL DD` was interrupted by the Cinnabar Gym lock text box at (26, 4) in Turn 47455... wait, no. The macro from (27, 18) was `LLLL UUUUU LLLLLLLLLLLLLLLLLL DD`.
Let's trace it from (27, 18) facing Down:
- `L` -> Turn Left
- `L` (x3) -> Step 3 to (24, 18)
- `U` -> Turn Up
- `U` (x4) -> Step 4 to (24, 14)
- `L` -> Turn Left
- `L` (x17) -> Step 17 to (7, 14).
My input `L18` would mean 1 turn and 17 steps.
I am currently at (10, 15).
Wait. Why am I at (10, 15)? My path was along Y=14!
Let's look at the intermediate states for Turn 47465.
- `turn_47465_0`: I am at (27, 18) turning Left.
- `turn_47465_1` to `turn_47465_3`: I step Left to (24, 18).
- `turn_47465_4`: I turn Up at (24, 18).
- `turn_47465_5` to `turn_47465_8`: I step Up to (24, 14).
- `turn_47465_9`: I turn Left at (24, 14).
- `turn_47465_10` to `turn_47465_26`: I step Left 17 times to (7, 14).
- `turn_47465_27`: I turn Down at (7, 14).
- `turn_47465_28`: I step Down to (7, 15).
Wait! In `turn_47465_28`, I step Down to (7, 15)!
So why does the Game State say I am at (10, 15)?
Ah! Look at the Game State again. "Player Position: (10, 15)".
Look at `<CurrentScreen turn="47465">`. I am at (10, 15).
Wait, look closely at `<CurrentScreen turn="47465">`! I am at (10, 15) and there is a glowing-eye switch statue right below me at (10, 16)!
Wait... I am not at (7, 15). (7, 15) is where the switch statue is... Wait, look at the screen!
At (6, 14)/(7, 14), there are solid bushes (`TYPE_2889`).
At (6, 15)/(7, 15), there is the switch statue!
The switch statue is at (6, 15)/(7, 15)! It's 2 tiles wide!
I bumped into the switch statue at (7, 15)!
Wait... When I bumped into the switch statue at (7, 15), did I teleport to (10, 15)?
NO! I encountered a wild Pokemon!
"Wild KOFFING appeared!"
Wait, look at the bottom of the screen. `turn_47465_27` and `turn_47465_28`... the screen doesn't show a battle. It shows me stepping to (7, 15).
Ah! The macro was `...DD`. I stepped to (7, 15).
But then why does the Game State say (10, 15)?
Because the "SYSTEM WARNING" says: `You pressed 29 movement buttons, but visited 24 tiles.`
My macro had 29 buttons.
If I stepped to (7, 15), why am I at (10, 15)?
Wait. Look at `<CurrentScreen turn="47465">` again.
The player sprite is at (10, 15).
Let's recount the tiles in the intermediate states.
In `turn_47465_10` to `turn_47465_26`, I step Left.
`turn_47465_10`: (23, 14)
`turn_47465_11`: (22, 14)
`turn_47465_12`: (21, 14)
`turn_47465_13`: (20, 14)
`turn_47465_14`: (19, 14)
`turn_47465_15`: (18, 14)
`turn_47465_16`: (17, 14)
`turn_47465_17`: (16, 14)
`turn_47465_18`: (15, 14)
`turn_47465_19`: (14, 14)
`turn_47465_20`: (13, 14)
`turn_47465_21`: (12, 14)
`turn_47465_22`: (11, 14)
`turn_47465_23`: (10, 14)
`turn_47465_24`: (9, 14)
`turn_47465_25`: (8, 14)
`turn_47465_26`: (7, 14)
So in `turn_47465_26`, I am at (7, 14).
Then `turn_47465_27` is Down (turns Down).
`turn_47465_28` is Down (steps to 7, 15).
But at (7, 15), there is the switch statue!
So I bump into the switch statue.
But where does the (10, 15) come from?!
Look at the map marker list!
`(18, 25): Central Switch`
`(20, 3): NE Switch`
`(7, 15): Switch Statue`
Wait, look at `<CurrentScreen turn="47465">`. The sprite is AT (10, 15).
Did I encounter a wild Pokemon at (10, 15) and run away?
Yes! I was walking Left along Y=14. When I reached (10, 14), I must have encountered a wild Pokemon!
BUT the intermediate states don't show a battle! They show me continuing to walk left!
Oh! The intermediate states are generated *before* the Game State reads the final position!
If a battle triggers at (10, 14), the harness might still attempt to execute the rest of the inputs (which would be eaten or buffered), and then after the battle, I'm placed back at (10, 14).
Wait, why am I at (10, 15)?
Ah! My macro had `DD` at the end!
If the battle happened at (10, 14), and I ran away... maybe the remaining `DD` inputs were executed AFTER the battle?
Yes! If I ran from the battle, the text "Got away safely!" appeared. But if I didn't press A/B to clear it... wait, the macro inputs might have cleared it and then moved me Down to (10, 15)!
This means there is NO text box open right now!
I am cleanly in the overworld at (10, 15), facing DOWN.
My goal is the West Room (7, 15).
From (10, 15), I need to walk Left 3 times to (7, 15).
Sequence: `LLLL`.
- Turn 47467 Reflection: Still clearing the "Wild Grimer appeared!" intro text box. My inputs in Turn 47466 were eaten. I will execute `run_battle` to escape.
- Turn 47468 Reflection: The `run_battle` inputs were eaten by the "Got away safely!" text box from the previous run_battle. I will use `safe_mash_b` to clear this remaining text and return to the overworld at (10, 15). 
After clearing it, I will execute a micro-macro to reach the switch: `D LLL U A` to stand at (7, 16) facing Up and interact with it.
- Turn 47468: The "Got away safely!" text is still present with a down arrow. I will explicitly press 'A' to clear it, and then check my surroundings. I am currently at (10, 15) and there appears to be a switch statue directly below me at (10, 16). I will verify this once back in the overworld.
- Turn 47469 Reflection: The "Got away safely!" text is still open with a down arrow. My previous 'A' input in Turn 47468 was eaten by the text rendering animation. I am still at (10, 15) facing Down. I will use `safe_mash_b` to aggressively clear this text box before trying to move again.
- Turn 47471 Reflection: The battle exit text has completely cleared. I am now in the overworld at (10, 15), facing Down. My target is the West Room (7, 15).
Path: L3 to (7, 15).
Sequence: `L LLL`.
Wait, there is a switch statue at (6, 15)/(7, 15)! It occupies TWO tiles.
If I step to (7, 15), I will bump into the switch statue.
The actual room is further West. I should probably enter via the Y=14 hallway!
Path to West Room via Y=14 from (10, 15) facing Down:
- U1 (turn Up, step to 10, 14)
- L3 (turn Left, step 2 to 8, 14)
- Wait, I just need to get past the X=9 wall. The gap is at Y=14.
- From (10, 15): Up to (10, 14). Left to (7, 14). Down to (7, 15) to inspect the switch area, or keep going Left to explore the rest of the room.
Let's just walk Left to the switch area and see what's there.
Sequence: `U LLL D`. This will place me at (7, 15) facing Down, bumping into the switch statue, or standing in front of it.