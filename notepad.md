# Party
- GNEISS (GRAVELER) Lv29: STAB Magnitude.
- Calcifer (QUILAVA) Lv28: QUICK ATTACK, HEADBUTT, SMOKESCREEN, EMBER. (Turn #5187)
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv10
- EGG (CLEFFA) Lv5

# Trainer Rosters
- Sage Ping, Medium Grace, Sage Jeffrey, Medium Martha: Defeated.
- Leader Morty: Gastly Lv21 (D), Gengar Lv25 (D), Haunter Lv21 (Active). (Turn #5187)

# Gym Strategy: Morty (Ghost/Poison)
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS with Magnitude. Rock typing resists Shadow Ball (Physical in Gen 2).
- Invisible Path: Avoid all tiles with `is-warp='true'` or `type='PIT'`. Use find_path_v2 tool.

# Lessons Learned
- Pit Warps: XML `is-warp='true'` is the source of truth for hazards.
- Switching: 'Will you switch?' prompt is YES/NO. Selecting 'YES' opens party menu.
- Party Menu: Cursor persistence varies; use 'Up' to reset to top for reliability. (Turn #5172)
- Ecruteak Gym Path: The safe path follows the trainers' sightlines. (Turn #5110)