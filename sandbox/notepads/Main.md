# Main Notepad

## Game Info
- **Version:** Pokémon Blue Version (colorized GBC ROM with battle EXP bar visible under HP; verify any QoL features in-game)
- **Trainer:** NEON | **Rival:** RED
- **Options:** Text Speed FAST, Battle Animation OFF, Battle Style SHIFT (verified turn 16)
- **Progress:** Defeated Brock (turn 180, Boulder Badge + TM34), evolved **RIPTIDE into Wartortle** (turn 309) & **KAISER into Nidoking** (turn 347), cleared Mt. Moon B2F (**Helix Fossil** turn 390), arrived in **Cerulean City** (turn 399), defeated **Rival RED #2** (turn 422), rescued **Bill** (**S.S. Ticket** turn 533–534), defeated **Gym Leader Misty** (turn 578, **Cascade Badge 2/8** + **TM11 Bubblebeam** -> RIPTIDE turn 585), cleared Cerulean burgled house (**TM28 Dig** -> RIPTIDE turn 611), arrived in **Vermilion City** (turn 632), claimed **Bike Voucher** (turn 643), cleared **S.S. Anne** (**TM08 Body Slam** -> KAISER turn 663, defeated **Rival RED #3** turn 679, **HM01 Cut** -> PGHP turn 685), defeated **Gym Leader Lt. Surge** (turn 707, **Thunder Badge 3/8** + **TM24 Thunderbolt** -> KAISER turn 712), claimed **Bicycle** in Cerulean City (turn 730), and cleared **Route 9 & Rock Tunnel without Flash** (turn 854; **PGHP learned Sleep Powder** turn 822)! Entering **Lavender Town**, then heading west via Route 8 -> Underground Path -> Route 7 to **Celadon City**!

## Harness / Input Notes
- Emulator runs continuously during thinking/fade transitions; transitions like stairs/fades complete quickly after landing on the warp tile (adding a trailing `sleep 500` after a warp lets the new map settle).
- `B` advances Gen 1 dialogue without accidentally selecting menu options; `hold B 500` + `B` fast-forwards multi-box dialogue safely.
- In battle: the cursor inside `FIGHT` persists on the last used move. Include `sleep 200` between `A` (open `FIGHT`) and `A` (confirm move) so both presses register reliably. Stat-change messages (`Harden`, `String Shot`, `Screech`, etc.) take ~4.5–5.0s total before printing their `▼` prompt, so allow `sleep 4800` before pressing `B` when chaining turns (verified turns 231–235).
- In `run_code`: `mgba.get_coordinates()` still returns the last overworld coordinates during a battle; to verify a battle ended mid-script, issue a single movement step and confirm coordinates actually changed before running a multi-step walk.
- Overworld tiles: flat brown tile with two tiny white dashes embedded in a ledge row is a walkable gap/passage (verified Route 1 `(5,19)` turn 55 and Viridian City `(19,27)` turn 68).
- Pokémon Center Nurse Joy (at `(3,3)` facing Up): requires 6 `A` presses spaced by ~500ms to get past `"Welcome..."`, `"We heal your POKéMON"`, `"back to perfect health!"`, and select `HEAL`, followed by ~4.5s for healing animation, then `B` presses to finish (verified turn 83 & 86 filmstrips).
- Poké Mart BUY flow: `A` (open qty `x01`) -> `Up`*(N-1) -> `A` (`"That will be ▼"`) -> `A` (`"¥XXXX. OK?" YES/NO`) -> `A` (confirm `YES` -> `"Here you are! Thank you! ▼"`) -> `B` (returns to BUY item list with cursor **reset to Slot 1**!) (verified turns 86 & 188 filmstrips).
- Battle Shift prompt: `"<TRAINER> is about to use <PKMN>!"` splits across two `▼` presses before `"Will NEON change POKéMON?"` YES/NO (verified turn 178 filmstrip).
- Pewter City navigation: Pewter Gym (`(16,17)`) is bounded south by a `y=21` tree wall (`x=4..17`) and east fence (`x=18, y=18..21`); travel north of the Gym (`x=10, y=13 -> x=19, y=13`) and down the main east avenue `x=19` to reach Pewter Pokémon Center (`(13,25)`) and Poké Mart (`(23,17)`) (verified turn 186).
- Battle `PKMN` and SHIFT (`"Bring out which POKéMON?"`) switch cursors both persist on the last switched-in slot within a battle (verified turns 122–123 & 198). Use `Left, Up` / `Right, Up` to reliably select `FIGHT` / `PKMN` regardless of previous Battle Menu cursor.
- Overworld Bag healing: after `A` heals a Pokémon (`"...recovered by 20!"`), 4 `B` presses exit cleanly (dismiss message -> close Party -> close Bag -> close Start Menu) (verified turn 208 filmstrip). Start Menu cursor resets to `POKéDEX` after battles and saves, but **persists** across building warps/map transitions (verified turns 206 & 349). Using an item on a party slot (e.g. Rare Candy) persists the party selection cursor on that slot for the next item; Stone evolutions return to Bag Slot 1 upon completion (verified turns 345–347).
- Escape Rope in Gen 1 warps directly outside the last visited Pokémon Center door, not just the cave entrance (verified turn 348).
- Sleep/Disable in battle: while asleep (`SLP`), pressing `A` on `FIGHT` skips move selection directly; when Disable wears off, `"<PKMN>'s disabled no more! ▼"` prints before the attack and needs `B`/`A` (verified turns 249–254).
- Evolution safety & Gen 1 quirks: NEVER press `B` after a battle where a Pokémon reached an evolution level (use `A` and wait ~9s for the evolution animation to finish; verified turn 309). In Gen 1, Bug moves (like Zubat's Leech Life) are **2x super effective** against Poison types (verified turn 299). Drain moves (`Absorb`, `Leech Life`) display two `▼` prompts (`It's super/not very effective!` + `Sucked health!`), taking ~5.5s total.
- Cerulean City navigation: Center `(19,17)`, Poké Mart `(25,25)` (reached south via alley `x=16` between Bike Shop and south block, turn 403), Nugget Bridge north exit `(20..21,8)` (reached via west ledge gap `(8,15)` -> `y=12`, turn 407–408); southbound return from Nugget Bridge can hop one-way south ledge `(22,17)` directly beside Cerulean Center (turn 459).
- Battle `ITEM` & 0-PP cursor behavior: In battle `ITEM`, the Bag scroll/selection cursor **persists** on the last-used item slot within a battle (verified turn 568); pressing `A` on a Potion skips `USE/TOSS` and goes straight to the Party screen (where the party cursor persists on the active/last-switched Pokémon slot, verified turn 503); after using `ITEM`, Battle Menu cursor stays on `ITEM` (verified turn 455). Selecting a 0-PP move inside `FIGHT` does NOT update the persisted move cursor (resets to Slot 1 next time `FIGHT` is opened; verified turns 452–453).
- Naming keyboard hygiene: always open the naming screen and confirm it is settled before typing; use `sleep 200` (not `120`) between consecutive directional presses and visually verify the spelling before pressing `Start` (lesson from turn 488 `PGHP`).
- Wild battle RUN timing: after pressing `B` on `"Wild X appeared!"`, `"Go! <PKMN>!"` takes ~3.2s before the Battle Menu accepts inputs (`sleep 3500`, then `Down`, `sleep 200`, `Right`, `sleep 200`, `A`, `sleep 1000`, `B`, `sleep 1500`) (verified turn 139).
- Gen 1 `Thrash` rampage: lasts 3–4 turns and auto-executes each subsequent turn without reopening the Battle Menu; still prompts Shift `YES/NO` between enemy Pokémon (`B` stays in and continues Thrash; verified turns 626–628).
- Overworld `POKéMON` & Mart `SELL` quirks: after teaching an HM/TM, the overworld `POKéMON` cursor persists on that slot, and field moves (`DIG`, `CUT`) appear as the top option (`CUT/STATS/SWITCH/CANCEL`) (verified turn 689). Nidoking cannot learn `TM28 Dig` in Gen 1; Wartortle can (turns 608–611). In Poké Mart `SELL`, confirming `YES` returns immediately to the SELL list without a `▼` prompt (turn 637). Using `HM01 Cut` prints `"<PKMN> hacked away with CUT! ▼"` requiring `B` + `sleep 2000` before stepping onto the cleared tile (turns 716 & 728).
- Route 5 northbound shortcut: `x=15` is a clear 1-tile northbound path from Route 5 Underground Path straight to Cerulean City's south Cut bush `(19,28)` (verified turns 725–728).
- Dark cave & trainer battle timing: in unlit Rock Tunnel (without Flash), cave walls and ladders remain faintly visible in dark maroon/brown on `latest.png`/`latest_grid.png`, while trainers are invisible (detectable via coordinate-checking steps in `run_code`, turns 773–776). Trainer sendout + `"Go! <PKMN>!"` requires `sleep 5500` before Battle Menu accepts inputs (verified turn 768).

## Party
- **KAISER** (Nidoking, Lead/Slot 1) - Lv 31 (103 HP; **Thrash**, **Body Slam**, **Horn Attack**, **Thunderbolt**) — evolved turn 347
- **RIPTIDE** (Wartortle, Slot 2) - Lv 21 (57 HP; **Dig**, Tail Whip, **Bubblebeam**, Water Gun) — evolved turn 309
- **BRIAR** (Bellsprout, Slot 3) - Lv 18 (47 HP; **Vine Whip**, Growth, **HM01 Cut**, **Sleep Powder**) — caught turn 485, renamed turn 867
- **Bag:** Poké Ball x4, TM34 (Bide), Antidote x3, Helix Fossil, **TM45 (Thunder Wave)**, **S.S. Ticket**, **Super Potion x7**, **Repel x1**, **HM01 (Cut)**, **Bicycle** | **Cash:** ¥13000+ | **Respawn:** Lavender Town Center `(3,5)`

## Badges
- 1/8: **Boulder Badge** (Pewter City, turn 180)
- 2/8: **Cascade Badge** (Cerulean City, turn 578)
- 3/8: **Thunder Badge** (Vermilion City, turn 707)

## Notepad Index
- `notepads/Main.md` - High-level dashboard and index
