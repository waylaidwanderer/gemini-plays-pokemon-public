# Dad Investigation Scratchpad

## Current Objective
Find Jackson (Dad) in Sovio City to clear the Metro turnstile block ("I should find dad first!").

## Verified Empirical Ground Truth
- Tremor occurred inside Sovio Metro Station (Turn 1437).
- Dad ran outside the station to investigate the tremor.
- Turnstiles at (19, 21) remain locked with "I should find dad first!" (tested Turn 5399).
- Route 2 east exit at (52, 19) remains blocked with "I can't go yet... I have things to do!".
- Sewer grunts vacated after Marie's radio broadcast (Turn 2682).
- Sewer storage room at (36-37, 14) fully tested (Turns 5628-5633): 'A' -> 'Its a simple storage room...'; stepping north into (37, 11) hits solid wall; stepping south into void arrow hits solid collision; east at (38, 12) terminates at void. Confirmed no interior room or warp exists.

## Rigorous Collision Testing Log (Plaza & North Corridor)
- (49, 17): Solid collision stepping north from (49, 18) (Turn 5409).
- (47, 13) & (47, 14): Solid collision stepping east from (46, 13) & (46, 14) (Turns 2824, 2984).
- (46, 12): Solid collision stepping north from (46, 13) into Pokémon Center corner (Turn 5421).
- (40, 8): Solid collision stepping north from (40, 9) into North Central House wall (Turn 5427).
- (41, 8): Solid collision stepping north from (41, 9) into building wall/curb (Turn 5433). Alley behind Pokémon Center is completely blocked from this approach.
- [x] Plaza East Terrace Access: Verified completely bounded by solid curbs on south and west (Turns 5409, 5531-5541); columns 50-52 blocked by Metro signpost and Route 2 barrier. Interior from Turns 1356-1364 is an unverified historical anomaly.

## Active Investigation Protocol
1. Empirically test (41, 9) and (41, 8) right now to see if passage exists along the Pokémon Center west/north edge.
2. If (41, 8) is blocked, test access to the terrace via the eastern side (columns 50-52) or southern terrace gaps.
3. Check Machop Family house at (13, 15) and talk to all 3 Bikers at (13, 21-23).

## Updated Overworld Survey (Turns 5440-5461)
- Machop Family House (13, 15): Empirically tested on Turn 5444 with 'A'; confirmed locked/solid with no text prompt despite active quest.
- Three Bikers (13, 21-23): All three bikers interviewed (Turns 1496, 5440, 5446); all share identical ambient motorcycle gang dialogue ("vroom vroom", "Jealous kid?", "ultimate motorcycle gang"). No story leads.
- Route 2 East Exit (52, 19): Re-verified on Turn 5459/5461; stepping onto (52, 19) triggers "I can't go yet... I have things to do!" and forces Asher west to (51, 19).
- Note on Dad's Location: Discard speculative side-quest requirements (Machop's Toy / Rock Smash). The core narrative fact is that Dad ran outside into Sovio City to investigate the seismic tremor. We must systematically locate where Dad went or what event was triggered in Sovio City.

- (51, 18): Confirmed solid collision from south; right post of Metro Plaza Signpost. Interacting reads 'Sovio Metro Station / Route 2 ---->'.