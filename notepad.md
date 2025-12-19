# Ilex Forest & Azalea Town
## Strategy: HM Cut
- **Goal**: Reach Goldenrod City.
- **How**: Teach HM01 CUT to KIMCHI (Oddish) and clear tree at (8, 25).
- **Recruitment**: KIMCHI caught in Ilex Forest, now in party slot 6.

## Lessons Learned
- **Menu Loops**: Turn 3169-3217. Caused by inaccurate `press_sequence` calls and hallucinating menu state.
- **Fix**: Always verify "Current Screen Text" before multi-button sequences. Use dedicated tools for item/HM usage.
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb). Switch to Flying/Fire for Grass types.
- **Notepad Hygiene**: Avoid redundant logs. Keep "HOW" plans detailed.

## Area Knowledge: Ilex Forest
- **Pokemon**: Caterpie, Metapod, Weedle, Kakuna, Pidgey, Venonat, Oddish, Paras, Psyduck.
- **Mechanics**: LEDGE_HOP (one-way), CUT_TREE (requires Cut), HEADBUTT_TREE.

## Area Knowledge: Azalea Town
- **Pokemon Center**: PC at (9, 1).

## Battle Lessons
- Ekans cannot learn CUT.
- Running is efficient with fast leads (Calcifer).