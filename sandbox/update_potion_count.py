path = "notepads/Progression_And_Party_Stats.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Update Potion count
old_potion = "- **Potion:** 1 (used on TRUFFLE on Turn 1671, found 1 at (2, 20) on Mt. Moon 1F on Turn 2068)"
new_potion = "- **Potion:** 2 (used on TRUFFLE on Turn 1671, found 1 at (2, 20) on Mt. Moon 1F on Turn 2068, found 1 at (20, 33) on Mt. Moon 1F on Turn 2711)"

if old_potion in content:
    content = content.replace(old_potion, new_potion)
    print("Successfully updated Potion count!")
else:
    print("Potion string not found!")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
