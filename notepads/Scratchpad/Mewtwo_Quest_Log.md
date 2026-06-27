# Post-Game Mewtwo Quest Plan & Logs (REVISED Turn 129402)
- Quest Started: Turn 111394 on Sunday, June 21, 2026 at 9:15 PM PDT
- Current Turn: Turn 129787
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
  - **The (1, 3) B1F Ladder**: The ladder at (1, 3) on 1F Northwest connects directly to 2F Northwest at (1, 3), serving as the critical entrance gateway to the isolated 1F Northwest landmass and the B1F stairs. Our previous logs incorrectly labeled this as (29, 3) or other coordinates. We have verified that (1, 3) is the correct B1F gateway.

## Turn 129871 Live Progress:
- Current Turn: Turn 129871
- Current Position: On foot at (15, 3) on Map 0_228 (1F) on Turn 129871.
- Active Goal: Reach Cerulean Cave B1F and capture Mewtwo.
- **Progress**: We successfully descended from 2F West, walked across the northern platform of 1F on foot, and arrived at Water Ramp 4 at (15, 3) on foot.
- **The True Path to B1F Stairs**: In standard Gen 1, Rows 4 and 5 on 1F (Map 0_228) are open water from Column 0 to Column 12, allowing continuous surfing to the northwest corner!
- **Next Step**: We are standing at (15, 3) on foot. We will use SURF to board the water canal at (15, 4), and then navigate through Column 14 and Rows 6-7 to bypass the Column 13 Row 4-5 blockage. Once we reach the western canal (Columns 8-9), we will surf Up to Rows 4-5 and surf directly west to (2, 4) on water! From there, we will dismount onto the northwest platform (2, 3) on foot and walk to the B1F stairs.