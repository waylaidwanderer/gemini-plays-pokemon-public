# Post-Game Mewtwo Quest Plan & Logs (REVISED Turn 126621)
- Quest Started: Turn 111394
- Active Goal: Reach Cerulean Cave B1F and capture Mewtwo.

## Topological Connectivity and Progression Path to Mewtwo:
- **The Core Flaw Discovered (Turn 126615)**: Our previous map-routing model of Map 0_226 (2F West) incorrectly marked the entire Column 1 as impassable based on a wall collision at (1, 11) from (2, 11).
- **The Real Layout**: In standard Generation 1 Cerulean Cave, Column 1 on 2F West is a wide-open, continuous vertical corridor from Row 1 to Row 17.
- **2F Connectivity Proof (Turn 126924)**: Our programmatic component analysis has proven that the main section of 2F is fully connected on foot! The component starting at Ladder 5 (9, 1) has 540 tiles and contains ALL standard ladders on 2F on foot: Ladder 5, Ladder 6, Ladder 4, Ladder 3, and Ladder 2! This means we can cross between any of these ladders on 2F on foot.
- **The Only Isolated Ladder**: The Northwest Ladder at (1, 3) on 2F is completely isolated on foot, consisting of only 2 tiles: (1, 2) and (1, 3). This ladder is the ONLY gateway to the Northwest isolated quadrant of 1F and the B1F stairs. Since it is isolated, the only way to reach (1, 3) on 2F is by climbing UP the Northwest Ladder from 1F at (1, 3). But 1F Northwest is completely isolated on foot, meaning we must descend to B1F directly once we are in that northwest corner of 1F!
- **Wait, how do we reach the B1F stairs?** Let's review standard Gen 1 Cerulean Cave layout.
  In vanilla Pokémon Red/Blue, the ladder at (29, 1) on 2F (Ladder 2) descends to 1F at (27, 1).
  And the ladder at (9, 1) on 2F (Ladder 5) descends to 1F at (7, 1).
  And the ladder at (3, 11) on 2F (Ladder 6) descends to 1F at (3, 11).
  Wait! Let's check: is the ladder at (1, 3) on 2F a ladder that goes to B1F? No, it goes to 1F.
  But wait! If the main section of 2F contains Ladder 5, Ladder 6, Ladder 4, Ladder 3, and Ladder 2...
  And we can walk from Ladder 5 at (9, 1) to any of those ladders...
  Wait, let's trace the standard vanilla path to B1F!
  In standard Gen 1 Cerulean Cave:
  The stairs to B1F are located at the bottom-left/south-west of the main floor? Or the northwest?
  Let's check where the stairs to B1F are in standard Gen 1!
  Wait! In vanilla Pokémon Red/Blue, the stairs to B1F are located at (29, 3) or (3, 11) or is there a ladder on 1F that goes directly to B1F?
  Wait! Let's check our notes in Locations/CeruleanCave:
  `To access the basement (B1F) where Mewtwo is, the player must locate the northwest ladder on 2F. This ladder descends into the isolated northwestern quadrant of 1F, which contains the stairs leading to B1F.`
  Wait, let's verify if the stairs to B1F are actually located on 1F at some coordinates.
  Are they on 1F at (1, 3)? Or is (1, 3) on 1F a ladder going up?
  And is there a staircase at (3, 11)? Or is the staircase to B1F at (3, 11) on B1F?
  Let's check!

## Active 2F West Corridor Verification Plan:
- Standing at (9, 1) on foot on Map 0_226.
- Let's walk Left along Row 1 to (5, 1) to see if we can continue leftwards.
- Coordinates to traverse:
  - (9, 1) -> (8, 1) -> (7, 1) -> (6, 1) -> (5, 1).
  - Let's do this step-by-step and inspect Column 4/3/2/1 passability next.
- Turn 126634: Investigating the path Left along Row 1. We are currently at (5, 1). To our left, (4, 1) and (3, 1) are TYPE_3fe2 (passable floor). Let's step left to (4, 1) and verify.
- Turn 126642: Tried stepping Left onto (2, 1). Result: BUMP collision, player remained at (3, 1). This empirically proves that (2, 1) is a solid, impassable wall on foot on Map 0_226.
- Conclusion: There is indeed NO connection on foot between (3, 1) and (1, 1)/(2, 1) on 2F West. This confirms that the Northwest Ladder at (1, 3) cannot be reached via Row 1 from (9, 1). We must backtrack and descend to 1F. Let's do this now. Our path back to Ladder 5 at (9, 1) is: (3, 1) -> (4, 1) -> (5, 1) -> (6, 1) -> (7, 1) -> (8, 1) -> (9, 1). That's 6 steps Right.
- Turn 126706: We are on 2F (Map 0_226) standing on the ladder at (9, 1). Let's step off to the left (8, 1) and then step back onto (9, 1) to go down to 1F at (7, 1). We verified that 2F Northwest is disconnected from 2F West because (2, 1) is solid rock, which we bumped into on Turn 126642.
- Let's verify our position after stepping off and back on.

## Turn 126846: Discovery of Separated Sections
- We have visually verified on Map 0_228 (1F) that the northernmost corridor (Rows 0-2) is completely blocked from reaching the area below it (Row 4 and lower) on foot.
- (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3) are solid rock walls (TYPE_2889).
- Column 4 is solid rock (TYPE_2889) on Rows 0, 1, 2, 3.
- This means there is NO on-foot path between the northernmost platform (Columns 5-15, Rows 0-2) and the rest of 1F Northwest.
- The northernmost platform is a complete dead end on foot. The only ways out are ascending Ladder 5 at (7, 1) or surfing south from Water Ramp 4 at (15, 3).
- Our previously assumed on-foot route to Northwest Ladder (1, 3) via Row 4 is completely disproved because we cannot cross from Row 2 to Row 4.
- Let's rethink our topological route. How do we reach Northwest Ladder (1, 3) on Map 0_228?
- Wait, where does Northwest Ladder (1, 3) lead on 2F? It warps to 2F at (1, 3).
- But on 2F, (1, 3) is located in the westernmost column. We've verified that the southwestern pocket on 2F (Southwest Ladder 6 at 3, 11) is completely isolated on foot, and that 2F Northwest (Ladder 5 landing at 9, 1) is also an isolated pocket.
- Wait, does 2F Northwest (9, 1) connect to (1, 3) on 2F?
- Let's re-read our disproven theories and log. On Turn 126642, we bumped into (2, 1) from (3, 1) on 2F, proving that (2, 1) is solid rock on foot on 2F.
- But wait! Let's look at the 2F layout of Cerulean Cave.
- In standard Gen 1 Cerulean Cave, 2F has an northwest ladder at (1, 3).
- Let's check where the stairs to B1F are.
- In standard Gen 1, the stairs to B1F are actually located at (3, 11)? Or (4, 11)? Or (29, 3)?
- Wait! Let's search all our notepads for "B1F" to see where the entrance to B1F actually is! This is extremely important because we might have the coordinates or the ladder name wrong.
- Let's execute search_notepads with query "B1F".
## Turn 126895: Row 0/1 Bypass Disproved
- We have visually verified on Map 0_226 (2F West) that the entire Row 0 is blocked from Column 2 to Column 6 by solid rock walls of TYPE_2889.
- Row 1 is blocked at (2, 1) by a solid rock wall of TYPE_2889.
- This means there is NO on-foot path between (9, 1) and (1, 3) on 2F West. The "2F Row 0 bypass route" was an unverified hypothesis that has now been definitively disproved.
- We will immediately backtrack to Ladder 5 at (9, 1) and descend back to 1F.

- We are currently standing at (6, 1) on Map 0_226.
- The path back to (9, 1) is: (6, 1) -> (7, 1) -> (8, 1) -> (9, 1). That's 3 steps Right.
## Turn 127000: Realization of the Southwest-Water Bypass Route
- Stand at (15, 9) on Map 0_228 (1F), on foot, facing DOWN.
- Based on <CurrentScreen turn="127000">, let's document the actual blockages observed:
  - Row 12 is fully open horizontally: (11, 12) through (18, 12) are all TYPE_2770 (passable platform).
  - Row 13 is blocked on Columns 16-17: (16, 13) and (17, 13) are solid rock walls (TYPE_2889).
  - Row 13 Column 18 (18, 13) is open flat floor (TYPE_2770).
  - Columns 14 and 15 on Rows 10 and 11 are solid rock walls (TYPE_2889).
  - Column 18 has the ladder warp at (18, 9).
  - Thus, to reach the stairs down at (17, 15) safely, we can walk via Column 18 to bypass the rock wall at (16, 13) / (17, 13):
    - (15, 9) -> Right to (16, 9) -> Right to (17, 9).
    - (17, 9) -> Down to (17, 10) -> Down to (17, 11) -> Down to (17, 12).
    - (17, 12) -> Right to (18, 12) -> Down to (18, 13) -> Down to (18, 14) -> Down to (18, 15) -> Left to (17, 15) [Stairs].
  - The step sequence is: Right, Right, Down, Down, Down, Right, Down, Down, Down, Left. (Total 10 steps).
  - Let's execute this path!