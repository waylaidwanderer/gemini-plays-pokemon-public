# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Cross the whirlpool to reach the Dragon Shrine.

# Key Mechanics & Lessons
- **Field Moves:** If 'A' interaction fails (even when facing correctly), ALWAYS fallback to Menu -> Pokemon -> [Mon] -> [Move].
- **Whirlpool:** Requires facing the whirlpool tile directly. 'A' button might be unreliable; Menu is safer.

- **Hard Reset Protocol:** When stuck in a menu/facing loop, spend one FULL turn pressing 'B' (x3) to clear state. Do NOT mix with movement. Move in the NEXT turn.
- **Menu-Move Sequencing:** To avoid inputs being eaten by menu closing animations, use the 'sleep' command in `press_buttons`. Example: `["B", "sleep 500", "Down"]`.
- **Facing Issue:** Game state reports 'Facing: Up' despite attempted 'Down' input. Likely caused by mixing 'B' (menu close) and 'Down' in the same turn.
- **Correction:** Executing strict sequence to fix facing: Close Menu -> Face Down -> Open Menu. Using 1000ms delays to prevent input eating.
- **Menu Mechanics:** Directional inputs inside a menu move the cursor, NOT the player. To change facing, you MUST be in the Overworld.
- **Input Eating:** Inputs sent immediately after closing a menu often fail. Always wait a full turn or use `sleep` after closing a menu before moving/turning.
- **Whirlpool Usage:** Attempting to use Whirlpool from the menu while facing the wrong way results in "Can't use that here." Must face the whirlpool tile first.
- Attempting to use Whirlpool via Menu (Start -> Pokemon -> Lapis).
- Assumed Start Menu cursor resets to POKÉDEX (Top).
- Whirlpool interaction via 'A' failed (no text).
- Party Menu Cursor persistence: It started on Slot 5 (Kunai). Always verify cursor position before blind navigation.
- Whirlpool interaction confirmed: "Can't use that here" when facing wrong way.
- Requirement: Must be in Overworld, Facing Whirlpool (DOWN), then select Move.
- Current State: Lapis Submenu Open. Cursor on SURF.
- Action: Press Down -> A to select WHIRLPOOL.
- Next: Observe text. If "Can't use that here", facing is wrong. If animation plays, success.
- Note: Game State still reports "Facing: Up" (Turn 18118). This is the moment of truth for the "Input Eating" hypothesis.
- Field moves: Surf (1), Whirlpool (2).
- Turn 18116: Previous attempt to open menu (Start, A) yielded no screen text.
- Hypothesis: Menu didn't open, or text extraction failed.
- Action: Pressing Down (to ensure facing/bump), then Start, then A.
- Goal: Open Start Menu and select the current option (hopefully Pokémon or Pokedex) to verify state.
- Note: If Party Menu opens, cursor might be on Slot 5 (Kunai) based on previous notes.
- Turn 18119: "Can't use that here" confirmed.
- Cause: Player was Facing UP. Menu navigation (Down) moves cursor, not player.
- Lesson: To change facing, I MUST be in the Overworld.
- Plan:
  1. Close Menus (Current Turn).
  2. Face Down (Next Turn).
  3. Verify Facing matches target.
  4. Open Menu -> Whirlpool.
- Turn 18127: "Can't use that here" persisted.
- Diagnosis: Input `Down` from Turn 18126 likely failed to update facing, or was eaten.
- Current Status: Deep in menus/text.
- Action: HARD RESET. Pressing B x4 to return to Overworld.
- Next Turn Plan:
  1. Verify Game State "Facing".
  2. If not DOWN, press DOWN.
  3. Once Facing is CONFIRMED DOWN, press A to interact (Primary).
  4. Fallback: Menu -> Whirlpool (only if A fails AND facing is confirmed).

# Anomaly (Turn 18132)
- **Facing Mismatch:** Turn 18131 State said `Facing: down`. I pressed `Start`. Turn 18132 State says `Facing: up`.
- **Visual Evidence:** Sprite in Turn 18132 appears to be facing DOWN (face visible, not backpack).
- **Hypothesis:** Game State `Facing` attribute might be unreliable or reporting "last movement direction" rather than "current facing" in some contexts? Or `Start` press caused a state glitch?
- **Decision:** Trusting Visuals + Turn 18131 State. Proceeding with Whirlpool attempt assuming Facing DOWN.
- **Cursor State:** Start Menu cursor is on `POKéMON` (2nd slot), not `POKéDEX` (1st). This might imply a buffered `Down` input from 18130 affected the menu, but didn't affect facing? Or maybe I just left it there? (Unlikely, last menu use was chaotic).

# Interaction Log
- **Turn 18133:** Party Menu Open. Cursor found on Slot 3 (Lapis) automatically. Pressing 'A' to open Field Move menu. Assuming facing is correct (DOWN).

# Reflection (Turn 18139)
- **Status:** Party Menu Open. Cursor on Lapis.
- **Critical Failure:** Game State reports `Facing: UP`.
- **Analysis:** My previous attempt to "Face Down" (Turn 18137) failed because the menu was likely still open (or reopened immediately), so `Down` moved the menu cursor instead of the player. The "Can't use that here" message confirms the game logic thinks I'm facing the wrong way.
- **Conclusion:** I MUST close the menu fully to rotate the player character.
- **Plan:**
  1. Turn 18139: Close ALL menus (B spam).
  2. Turn 18140: Verify Overworld. Press `Down`.
  3. Turn 18141: Verify `Facing: DOWN`. Open Menu -> Whirlpool.

# Protocols
- **Facing Correction:**
  1. If in Menu: Press `B` repeatedly until Overworld.
  2. **WAIT** 1 turn.
  3. Press Direction in Overworld.
  4. Verify Game State `Facing`.

# Reflection (Turn 18140)
- **Status:** Hard Reset Successful. Menu Closed. Game State confirms `Facing: down`.
- **Observation:** Player sprite visually faces DOWN.
- **Plan:**
  1. Open Start Menu (Check Cursor Position).
  2. Navigate to Party -> Lapis -> Whirlpool.

# Reflection (Turn 18141)
- **Status:** Start Menu Open. Cursor on `POKéMON`.
- **Action:** Pressing `A` to open Party Menu.
- **Hypothesis:** Game might remember the last cursor position in Party Menu (Lapis).
- **Test:** If Party Menu opens with Lapis selected, Memory Cursor is active. If Gyarados, it resets.

# Reflection (Turn 18145 - RESOLVED)
- **Status:** Hard Reset complete. Player confirmed Facing DOWN at (15, 22).
- **Action:** Attempting interaction via 'A' button.
- **Strategy:** If 'A' fails, fallback to Start Menu -> Pokemon -> Lapis -> Whirlpool.

# Protocols
- **Facing Correction:**
  1. If in Menu: Press `B` repeatedly until Overworld.
  2. **WAIT** 1 turn.
  3. Press Direction in Overworld.
  4. Verify Game State `Facing`.

# Anomaly (Turn 18148)
- **Status:** Start Menu Open.
- **Conflict:** Game State reports `Facing: up`. Visual Sprite at (15, 22) clearly shows face/belly (Facing DOWN).
- **Conclusion:** Game State `Facing` attribute is UNRELIABLE when the Start Menu is open. Trusting visual sprite.
- **Action:** Proceeding with `A` to open Party Menu, assuming player is physically facing the Whirlpool.

# Mechanics Confirmation (Turn 18149)
- **Memory Cursor:** Confirmed. Opening the Party Menu placed the cursor directly on 'LAPIS' (Slot 3), which was the last selected Pokémon.
- **Implication:** Menu navigation logic must check the current cursor position before issuing directional inputs. Blindly assuming 'reset to top' is dangerous.