class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class PathGroup:
    tiles = []
    current_cordinates = None
    path_history = []

    def __repr__(self):
        return "[X] {} -- {} \n".format(self.tiles, self.path_history)


grid = [
    [
        "SPHINX",
        "urn",
        "vulture",
        "arch",
        "snake",
        "urn",
        "bug",
        "plant",
        "arch",
        "staff",
        "SPHINX",
    ],
    [
        "plant",
        "foot",
        "bug",
        "plant",
        "vulture",
        "foot",
        "staff",
        "vulture",
        "plant",
        "foot",
        "bug",
    ],
    [
        "arch",
        "staff",
        "urn",
        "Shrine",
        "Shrine",
        "Shrine",
        "plant",
        "bug",
        "staff",
        "urn",
        "arch",
    ],
    [
        "snake",
        "vulture",
        "foot",
        "Shrine",
        "Shrine",
        "Shrine",
        "urn",
        "snake",
        "vulture",
        "foot",
        "vulture",
    ],
    [
        "staff",
        "urn",
        "bug",
        "Shrine",
        "Shrine",
        "Shrine",
        "foot",
        "staff",
        "bug",
        "snake",
        "staff",
    ],
    [
        "snake",
        "plant",
        "bug",
        "urn",
        "foot",
        "vulture",
        "bug",
        "urn",
        "arch",
        "foot",
        "urn",
    ],
    [
        "SPHINX",
        "arch",
        "staff",
        "plant",
        "snake",
        "staff",
        "bug",
        "plant",
        "vulture",
        "snake",
        "SPHINX",
    ],
]

for x in grid:
    for y in x:
        print(str(y).ljust(8, " "), end="")
    print()


def print_grid_with_path_group(grid, pg):
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if (i, j) in pg.path_history:
                print(str(y).upper().ljust(8, " "), end="")
            else:
                print(str("NOPE").ljust(8, " "), end="")
        print()


unique_tiles = 8
starting_tile = (3, 10)


def try_get_tile(tile_tuple):
    try:
        return grid[tile_tuple[0]][tile_tuple[1]], (tile_tuple[0], tile_tuple[1])
    except Exception as e:
        return None


def get_adjacent_tiles(tile_tuple):
    """
    Any compass direction is an adjacent tile.
    """
    tiles = []

    n_tile = try_get_tile((tile_tuple[0], tile_tuple[1] + 1))
    s_tile = try_get_tile((tile_tuple[0], tile_tuple[1] - 1))
    w_tile = try_get_tile((tile_tuple[0] - 1, tile_tuple[1]))
    e_tile = try_get_tile((tile_tuple[0] + 1, tile_tuple[1]))

    nw_tile = try_get_tile((tile_tuple[0] + 1, tile_tuple[1] + 1))
    ne_tile = try_get_tile((tile_tuple[0] + 1, tile_tuple[1] - 1))
    sw_tile = try_get_tile((tile_tuple[0] - 1, tile_tuple[1] - 1))
    se_tile = try_get_tile((tile_tuple[0] - 1, tile_tuple[1] + 1))

    for x in (nw_tile, n_tile, ne_tile, w_tile, e_tile, sw_tile, s_tile, se_tile):
        if x is not None and x[0] != "SPHINX":
            tiles.append(x)
    return tiles


starting_path = PathGroup()
starting_path.tiles = ["vulture"]
starting_path.current_cordinates = starting_tile
starting_path.path_history = [starting_tile]


def step_breadth_first_search(path_group):
    sub_paths = []
    for tile in get_adjacent_tiles(path_group.current_cordinates):
        sub_path = PathGroup()

        # Add in the new tile
        sub_path.tiles = path_group.tiles.copy()
        sub_path.tiles.append(tile[0])

        sub_path.current_cordinates = tile[1]  # Location of new tile

        # Save our route
        sub_path.path_history = path_group.path_history.copy()
        sub_path.path_history.append(tile[1])
        sub_paths.append(sub_path)

    # # Check for invalid paths
    for sub_path in list(sub_paths):
        # Are there duplicate tiles?
        if len(set(sub_path.tiles)) != len(sub_path.tiles):
            sub_paths.remove(sub_path)
            continue

        # Someone died here so it's wrong (3,9)
        if sub_path.current_cordinates == (3, 9):
            sub_paths.remove(sub_path)
            continue

        # Don't walk through shrine
        if "Shrine" in sub_path.tiles:
            sub_paths.remove(sub_path)
            continue

        # Must end touching the shrine
        if len(sub_path.tiles) == 8 and "Shrine" not in [
            x[0] for x in get_adjacent_tiles(sub_path.current_cordinates)
        ]:
            sub_paths.remove(sub_path)
            continue

        # Always move left
        if len(sub_path.tiles) == 8:
            if len(set([x[1] for x in sub_path.path_history])) != 8:
                sub_paths.remove(sub_path)
                continue

    return sub_paths


num_steps = 2

path_list = step_breadth_first_search(starting_path)
while num_steps < 8:
    print("Steps : {}".format(num_steps))
    n_path_list = []
    for path in path_list:
        n_path_list.extend(step_breadth_first_search(path))
    num_steps += 1
    path_list = n_path_list

for path_group in path_list:
    print(path_group)
    print_grid_with_path_group(grid, path_group)
