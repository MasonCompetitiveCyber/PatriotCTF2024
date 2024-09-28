### Puzzle Room

As you delve deeper into the tomb in search of answers, you stumble upon a puzzle room, its floor entirely covered in pressure plates. The warnings of the great necromancer, who hid his treasure here, suggest that one wrong step could lead to your doom.

You enter from the center of the eastern wall. Although you suspect you’re missing a crucial clue to guide your steps, you’re confident that everything you need to safely navigate the traps is already within reach.

At the center of the room lies the key to venturing further into the tomb, along with the promise of powerful treasures to aid you on your quest. Can you find the path, avoid the traps, and claim the treasure (flag) on the central platform?

# Difficulty

3/10 Either a reverse engineering challenge or a programming challenge. Both on the easier side.

# Flag
pctf{Did_you_guess_it_or_apply_graph_algorithms?}

*** There are two separate paths that satisfy all of these constraints, however the two paths both form the same composite key for the flag, so they will both decrypt and output the same flag.

# Author

Christopher Roberts (caffix)

# Challenge provided files

puzzle_room.py

# Write up

It's a pretty easy python reverse engineering problem involving a handful of simple constraints inspired by a dungeons and dragon puzzle I really like.

1. Each tile must be stepped on once and only once.
2. Must always move west
3. Don't step on 3,9
4. Don't step on sphinx
5. Must end on shrine

Optionally there is a really cool graphing approach you can take to a seen in my solution.py. 

The original puzzle offered a guide through an item embedded in a wall in another room, however you don't have a character who will die when reverseing the problem. So it's okay to fail many times here, which makes it much easier.

Graphing approach :
    Breadth first searching adhering to:
        Every tile type stepped on once.
        (3,9) is bad.
        Want to end up near or at the shrine in the center.

This is a finite problem, and so you get dozens upon dozens of paths. Looking through them it's clear that a single path sticks out from the rest of them.
The only path that reaches the end while adhering to these rules offers no traceback... which just means we always move "west"

# Don't share this as a hint
Note: inspired by WotC Tomb of Annihilation D&D module
In the Tomb of Anhilation book In the tomb of the nine gods/end tomb of the module. I think it's on the third floor? It's probably in the book.

This is the Tomb of Ijin.

The image in this folder is just from the original game, so you can see it too, but won't be provided with the challenge.

[X] ['vulture', 'snake', 'arch', 'plant', 'bug', 'staff', 'foot', 'urn'] -- [(3, 10), (4, 9), (5, 8), (6, 7), (6, 6), (6, 5), (5, 4), (5, 3)] 
# Final Key built ends as "vulturesnakearchplantbugstafffooturnShrine"
# encrypted blob : b'FFxxg1OK5sykNlpDI+YF2cqF/tDem3LuWEZRR1bKmfVwzHsOkm+0O4wDxaM8MGFxUsiR7QOv/p904UiSBgyVkhD126VNlNqc8zNjSxgoOgs='
