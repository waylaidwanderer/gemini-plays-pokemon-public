[50-Turn Reflection]
- Error Analysis: Menu navigation during text-heavy events (like Vending Machines) is prone to desyncs if inputs are entered too quickly. Mashing leads to buying the wrong items or exiting the menu.
- UI/Menu Learnings: Must wait for menus to fully render before sending directional inputs. Cannot use consecutive sleep commands in move_sequence.