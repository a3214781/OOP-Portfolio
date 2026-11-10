from cursed_undead import CursedUndead
from death_knight import DeathKnight
from necromancer import Necromancer
from summoning_ritual import (
    death_knight_ritual,
    phantom_guardian_ritual,
    putrid_zombie_ritual,
    skeleton_warrior_ritual,
    vengeful_ghost_ritual,
)
from undead import Undead
from warrior_undead import WarriorUndead

# Create a necromancer with an initial collection of resources.
print("=== Necromancer Game ===")
necromancer = Necromancer(
    "Malachar", necrotic=20, spirit=20, bone=15, flesh=10, ectoplasm=40
)
print(necromancer)
print()

# Perform several successful summons.
print("--- Successful summons ---")
skeleton = necromancer.summon_undead(skeleton_warrior_ritual)
ghost = necromancer.summon_undead(vengeful_ghost_ritual)
print(f"Resources after summoning: {necromancer.inventory}")
print(f"Controlled undead: {len(necromancer.controlled_undead)}")
print()

# Attempt a ritual that cannot currently be performed.
print("--- Failed summon ---")
failed_attempt = necromancer.summon_undead(phantom_guardian_ritual)
print(f"Summon result: {failed_attempt}")
print(f"Resources unchanged: {necromancer.inventory}")
print()

# Collect additional resources and perform the ritual again.
print("--- Collect more and retry ---")
necromancer.collect_resources(
    necrotic=40, spirit=40, bone=40, flesh=40, ectoplasm=100
)
print(f"Resources after collecting: {necromancer.inventory}")
guardian = necromancer.summon_undead(phantom_guardian_ritual)
zombie = necromancer.summon_undead(putrid_zombie_ritual)
print()

# Level one controlled undead creature.
print("--- Levelling ---")
print(f"Before levelling: {skeleton}")
necromancer.level_undead(skeleton.unit_id)
print(f"After levelling:  {skeleton}")
print()

# Dismiss one controlled undead creature.
print("--- Dismissing ---")
necromancer.dismiss_undead(ghost.unit_id)
print(f"Ghost still controlled: {ghost in necromancer.controlled_undead}")
print()

# Inheritance checks.
print("--- Inheritance ---")
for undead in necromancer.controlled_undead:
    print(
        f"{undead.name}: type = {type(undead).__name__}, "
        f"is Undead = {isinstance(undead, Undead)}"
    )
print("skeleton is a WarriorUndead:", isinstance(skeleton, WarriorUndead))
print("guardian is a WarriorUndead:", isinstance(guardian, WarriorUndead))
print("zombie is a WarriorUndead:", isinstance(zombie, WarriorUndead))
print()

print("--- command() overrides ---")
necromancer.command_undead(skeleton.unit_id)
necromancer.command_undead(zombie.unit_id)
print()

# Death Knight.
print("--- Death Knight ---")
necromancer.collect_resources(
    necrotic=40, spirit=40, bone=40, flesh=40, ectoplasm=100
)
knight = necromancer.summon_undead(death_knight_ritual)
print(knight)
print()

print("isinstance checks:")
print("  Undead:", isinstance(knight, Undead))
print("  WarriorUndead:", isinstance(knight, WarriorUndead))
print("  CursedUndead:", isinstance(knight, CursedUndead))
print("  DeathKnight:", isinstance(knight, DeathKnight))
print()

print("MRO:")
for cls in DeathKnight.__mro__:
    print("  ", cls.__name__)
print()

print("combat_style() via super():", knight.combat_style())
print("compare_combat_styles():", knight.compare_combat_styles())
print()

necromancer.command_undead(knight.unit_id)
print(f"Before levelling: {knight}")
necromancer.level_undead(knight.unit_id)
print(f"After levelling:  {knight}")
print()

print(necromancer)
