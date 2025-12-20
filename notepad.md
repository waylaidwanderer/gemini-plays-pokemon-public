# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Cure Jasmine's Ampharos (Lighthouse).
- **Secondary Goal:** Travel to Cianwood City to get the SecretPotion (Completed).
- **Olivine Gym:** Defeated Leader Jasmine.
    - **Badge:** Mineral Badge (Raises Defense).
    - **TM:** TM23 Iron Tail.
    - **Battle:** Muscle (Machoke) swept with Karate Chop. Mistral was sacrificed to reset stats.
- **Immediate Plan:** Fly to Violet City (Confirmed). Head East to Route 31. Find the recipient for Kenya's mail.

- **Quest Update:** Successfully escaped the Lighthouse using Dig. Amphy is cured.
- **Party Status:**
  - **Muscle (Machoke):** Lv 40.
  - **Garnet (Quilava):** Lv 28.
  - **Hematite (Pinsir):** Lv 15.
  - **Azurite (Heracross):** Lv 13.
  - **Lapis (Poliwag):** Lv 12. (Surf)
  - **Mistral (Pidgey):** Lv 13. (Fly)
- **Rocky (Onix):** Deposited in Box 3.

## Quests
- **Webster:** Deliver mail to Route 31 (KENYA is in Box 1).
- **Jasmine:** Potion administered. Amphy is cured! Jasmine returning to Gym.

## Tile Mechanics
- **FLOOR:** Traversable.
- **WALL:** Impassable.
- **WATER:** Traversable with SURF.
- **DOOR:** Traversable. Warps to another map.
- **WARP_CARPET:** Traversable. Transitions map.
- **TALL_GRASS:** Traversable. Wild encounters.
- **LEDGE:** One-way traversable (usually Down).

## Navigation Log
- **Olivine & Route 40:** Cleared Lighthouse. Surfed West to Route 41.
- **Route 41 (Whirl Islands):** Navigated maze-like buoys. Found passage West to Cianwood.
- **Cianwood City:**
    - **Key Locations:** Pokemon Center (23, 43), Pharmacy (15, 47), Lugia House (15, 37), Mania's House (17, 41), Poke Seer (5, 17), Gym (8, 43).
    - **Events:** Defeated Eusine. Obtained SecretPotion. Defeated Chuck.

## Gym Log
- **Cianwood Gym:** Defeated Leader Chuck.
    - **Badge:** Storm Badge (Allows Fly).
    - **TM:** TM01 DynamicPunch.
    - **Puzzle:** Strength boulders.
- **Gym Guide Advice:** Jasmine uses the newly discovered Steel-type Pokémon. They have high defense and many resistances. Fire and Fighting moves are recommended.
- **Battle vs Jasmine:**
    - **Magnemite (Lv 30):** Defeated by Muscle's Karate Chop (OHKO).
    - **Steelix (Lv 35):** Resists Normal (Strength). Weak to Fighting/Ground/Fire/Water. High Defense. Muscle's Defense lowered by Iron Tail.
- **Strategy Update:** Switching to Mistral (Lv 13) to reset Muscle's Defense drop. Mistral will likely faint (Sacrifice). Then send Muscle back out, heal, and use Karate Chop.
- **Battle vs Jasmine Update:**
    - Mistral fainted after using Sand-Attack (Steelix Accuracy -1).
    - Muscle's stats are reset (Defense normal).
    - **Next Step:** Switch Muscle in (Slot 1). **CRITICAL:** Use Hyper Potion immediately as Muscle has 23/130 HP and Steelix deals ~40 damage with Iron Tail.
- **Tool Maintenance:** Need to review `smart_battle_move` usage/logic to correctly handle Gen 2 cursor memory (cursor stays on last used move) before next battle.
- **Events:** Received phone call from Wade (Bug Catcher). He talked about his Pokemon growing fast and a wild Bellsprout escaping.
- **Tool Note:** `smart_battle_move` logic verified as correct for wrapping. Must ensure `current_slot` argument is passed correctly in future battles to handle cursor memory.
- **Battle State:** Muscle's last used move was Slot 4 (Karate Chop). Battle cursor is likely at Slot 4.
- **Route 31:** Picked a Bitter Berry from the tree at (16, 7).
- **Route 31:** Found the recipient for Kenya's mail (Fisher at 17, 7). Handing over Kenya now.
- **Critical Issue:** Kenya is NOT holding the mail, and I don't have it in my bag.
- **Hypothesis:** I lost/stored the original mail.
- **Solution:** Go to Violet City Poké Mart, buy Flower Mail (if available), give it to Kenya, and retry delivery.
- **Navigation:** Walking West to Violet City is blocked by ledges at (13, 6-8).
- **Plan:** Use Fly (Mistral) to reach Violet City to buy Flower Mail.
- **Status:** In Party Menu. Cursor on Hematite (Slot 2). Mistakenly opened submenu.
- **Immediate Plan:** Back out (B). Scroll down to Mistral (Slot 5). Select Fly. Go to Violet City.
- **Location Correction:** Currently in Cherrygrove Mart.
- **Plan:** Checking if Cherrygrove Mart sells Flower Mail. If not, will Fly to Violet City.
- **Fly Map Navigation:** Cursor starts at New Bark Town.
- **Action:** Pressing LEFT to select Cherrygrove. Will press UP next turn to reach Violet City (avoiding input skipping).
- **Tool Definition:** Defined `slow_press` to handle sticky menus/maps by adding delays between inputs.
- **Immediate Action:** Attempting manual `Left` press. If it fails, will use `slow_press` next turn with the full sequence.
- **Task:** Buy Flower Mail at Violet City Mart to replace the missing mail for Kenya.