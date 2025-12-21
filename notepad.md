# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Deliver Kenya to Route 31.
- **Secondary Goal:** Travel to Mahogany Town (Route 42).
- **Tertiary Goal:** Train Party to Level 30+.

## Quest: Deliver Kenya (Route 31)
- **Status:** Recovery & Manual Entry.
- **Context:** Automated tool failed and saved game. Checking Kenya's mail status.
- **Objective:** Ensure mail reads exactly: "Dark Cave leads to another road." (Mixed case, period at end).
- **Action Plan:**
    1. Inspect current mail on Kenya.
    2. If incorrect/garbage: Remove mail -> Pack -> Give Flower Mail -> Type MANUALLY.
    3. If correct (unlikely): Deliver.

## Knowledge Base
- **Fisher (Route 31):** Rejected all previous attempts. Requires exact text matching.
- **Wade (Route 31):** Called (Turn 9576). Waiting on Route 31.
- **Dark Cave:** Connects Route 31, 45, 46. Needs Flash.

## Mechanics Log
- **Mail:** Prevents deposit. PC Full -> Mail goes to Bag. Must hold nothing to attach.
- **Inputs:** Pressing Start in Mail menu triggers Printer Error. Use B.
- **Lesson:** Pressing 'Start' in the Mail menu causes a "Printer Error" loop or crash behavior. Use 'B' to exit or 'END' to finish.
- **Menu Nav:** Cursor positions are remembered. Always verify position before confirming.
- **Automation Lesson:** Do not use "fire and forget" tools for complex, state-sensitive menus like Mail without extreme error checking.

## Critical Recovery Note
- **Turn 9804:** Save file overwritten during tool failure.
- **Current Task:** Manual verification of Kenya's held item.
- Turn 9829: Attempting to TAKE Kenya's mail using slow_press to bypass potential Read loop and verify text in Bag. Sequence: A (Open), Downx3 (Mail), A (Select), Down (Take), A (Confirm).
- Turn 9830: Selected 'NO' to "Send to PC?" prompt to keep mail in Bag for inspection. Used slow_press ["Down", "A"].