# Dad Investigation Scratchpad

## Current Objective
Find Jackson (Dad) in Sovio City to clear the Metro turnstile block ("I should find dad first!").

## Verified Empirical Ground Truth
- Tremor occurred inside Sovio Metro Station (Turn 1437).
- Dad ran outside the station to investigate the tremor.
- Turnstiles at (19, 21) remain locked with "I should find dad first!" (tested Turn 5399).
- Route 2 east exit at (52, 19) remains blocked with "I can't go yet... I have things to do!".
- Sewer grunts vacated after Marie's radio broadcast (Turn 2682).
- Sewer storage room at (37, 14) inspected with 'A' -> "Its a simple storage room...". Dad was not inside.

## Rigorous Collision Testing Log (Plaza & North Corridor)
- (49, 17): Solid collision stepping north from (49, 18) (Turn 5409).
- (47, 13) & (47, 14): Solid collision stepping east from (46, 13) & (46, 14) (Turns 2824, 2984).
- (46, 12): Solid collision stepping north from (46, 13) into Pokémon Center corner (Turn 5421).
- (40, 8): Solid collision stepping north from (40, 9) into North Central House wall (Turn 5427).
- (41, 8): Solid collision stepping north from (41, 9) into building wall/curb (Turn 5433). Alley behind Pokémon Center is completely blocked from this approach.
- [ ] Plaza East Terrace Access: Residential House (Plaza East) was entered on Turns 1356-1364 (interior 64, 35; Little Girl & Nana). Access vector onto the terrace remains to be systematically mapped (e.g. col 50-52 east approach, or col 46-47 rows 15-16).

## Active Investigation Protocol
1. Complete interview with Blonde Girl at (44, 24) in the South Central park corridor.
2. Interview boy in pink shirt near Central Park pond.
3. Interview gathering at (33-35, 28) (Girl, Jigglypuff, Boy) and verify any remaining South Central residents.

## Updated Overworld Survey (Turns 5440-5461)
- Machop Family House (13, 15): Empirically tested on Turn 5444 with 'A'; confirmed locked/solid with no text prompt despite active quest.
- Three Bikers (13, 21-23): All three bikers interviewed (Turns 1496, 5440, 5446); all share identical ambient motorcycle gang dialogue ("vroom vroom", "Jealous kid?", "ultimate motorcycle gang"). No story leads.
- Route 2 East Exit (52, 19): Re-verified on Turn 5459/5461; stepping onto (52, 19) triggers "I can't go yet... I have things to do!" and forces Asher west to (51, 19).
- Note on Dad's Location: Discard speculative side-quest requirements (Machop's Toy / Rock Smash). The core narrative fact is that Dad ran outside into Sovio City to investigate the seismic tremor. We must systematically locate where Dad went or what event was triggered in Sovio City.

- (51, 18): Confirmed solid collision from south; right post of Metro Plaza Signpost. Interacting reads 'Sovio Metro Station / Route 2 ---->'.