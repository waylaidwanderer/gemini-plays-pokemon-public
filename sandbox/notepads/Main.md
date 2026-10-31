# Nuzlocke Dashboard — Attempt #2

## Active Rules & Status
- **Attempt**: #2
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configured & verified Turn 505; Text Speed `Fast`)
- **Unlimited Items & In-Battle Bag Restriction**: Rare Candies & any Berries currently in the Bag (`Cheri Berry` cures Paralysis, `Pecha Berry` cures Poison, `Oran Berry` +10 HP) auto-refill to 99 at the **turn boundary** in the overworld (never consume the last copy `x 1 -> x 0` of a newly harvested Berry before ending a turn in the free overworld!). **Using Berries/healing items directly from the Bag during battle is disabled** (selecting a Berry in battle only shows `>CANCEL`; Berries work as held items in battle or from the Bag in the overworld).
- **Key Items Obtained**: `Pokedex`, `Running Shoes`, `Old Rod` (registered to `Select`).

## Attempt #1 Post-Mortem & Key Tactical Lessons
- **Result**: Wiped at Turn 497 against **PKMN Trainer Red** (`(29, 8)` on Route 104 North, 8 tiles south of Rustboro City).
- **Root Causes & Fixes for Attempt #2**:
  1. **Pre-Level Before Ambush Bosses**: In Attempt #1, we entered the 5-Pokemon **Team Magma Grunt ambush** at `(26, 23)` in Petalburg Woods (`Magnemite` Lv 8, `Houndour` Lv 9 with `Super Fang` + `Pursuit` + `Ember`, `Bagon` Lv 8, `Koffing` Lv 8 with `Protect` + `Thief`, `Duskull` Lv 8 with `Protect` + `Shadow Sneak` + `Leftovers`) at Lv 10–12 and lost 3 party members (`Triton`, `Calypso`, `Midas`). In Attempt #2, use unlimited Rare Candies to pre-level our full 6-Pokemon party to **Lv 14–15** with held `Oran Berries` *before* fighting the Team Magma Grunt!
  2. **Keep a Full 6-Pokemon Active Party**: We have 7+ available encounters before Petalburg Woods/Route 104 North (`Starter`, `Littleroot Pond`, `Route 101`, `Route 103`, `Route 102`, `Petalburg City Pond`, `Route 104 South`, `Petalburg Woods`). Never enter Petalburg Woods or Route 104 North with empty/fainted party slots when healthy encounters are available in the Petalburg City PC (`(20, 16)`).
  3. **Cheri Berry Auto-Refill (`(3, 25)` on Route 104 North)**: Immediately after harvesting the `Cheri Berry` tree at `(3, 25)` outside the Pretty Petal Flower Shop, end a turn in the free overworld (with no textbox or menu open) so `Cheri Berries` auto-refill from `2 -> 99`!
  4. **Countering PKMN Trainer Red (`(29, 8)` on Route 104 North)**: Red has a 6-Pokemon team leading with `Eevee` (M, Lv 9, 31 Max HP, holds `Sitrus Berry`, moves: `Curse`, `Rest`, `Snore`, `Quick Attack`). The AI spams `Curse` + `Rest`/`Snore` until `+1` priority `Quick Attack` enters KO range or `Curse` is maxed. Do NOT let `Eevee` stack `Curse` boosts—hit it hard on the Special side (since `Curse` only boosts physical `Defense`, not `Sp.Def`), use Fighting moves / `Leech Seed` / `Encore`, or finish it from `> 50%` HP before it can `Rest`.

## Level Cap Schedule
1. **Roxanne (Rustboro Gym)**: Lv 16
2. **Brawly (Dewford Gym)**: Lv 20
3. **Wattson (Mauville Gym)**: Lv 29
4. **Flannery (Lavaridge Gym)**: Lv 42
5. **Norman (Petalburg Gym)**: Lv 48
6. **Winona (Fortree Gym)**: Lv 55
7. **Tate & Liza (Mossdeep Gym)**: Lv 70
8. **Wallace / Juan (Sootopolis Gym)**: Lv 77
9. **Champion (Pokemon League)**: Lv 100

## Notepad Index
- `Locations/Encounters`: Route-by-route Nuzlocke encounter tracking & status
- `Mechanics/UI_And_Tools`: Verified menu, Bag, fishing, and overworld mechanics
- `Scratchpad/Routing`: Verified early-game maps, trainers, and routing