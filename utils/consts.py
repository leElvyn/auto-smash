"""
This file contains consts like the layout of the switch keyboard, or the stage list.
"""
from enums import Controls

KEYBOARD_LOWERCASE_0 = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "",
]  # first row is the digits row
KEYBOARD_LOWERCASE_1 = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", ""]
KEYBOARD_LOWERCASE_2 = ["q", "s", "d", "f", "g", "h", "j", "k", "l", "m", ""]
KEYBOARD_LOWERCASE_3 = ["w", "x", "c", "v", "b", "n", "", "", "", "", ""]

# currently, empty and normal are the same, since stage names aren't registered.

STAGE_LIST = [
    [
        None,
        "battlefield",
        "small_battlefield",
        "big_battlefield",
        "final_destination",
        "peachs_castle",
        "kongo_jungle",
        "hyrule_castle",
        "super_happy_tree",
        "dream_land",
        "saffron_city",
    ],
    [
        "mushroom_kingdom",
        "princess_peachs_castle",
        "rainbow_cruise",
        "kongo_falls",
        "jungle_japes",
        "great_bay",
        "temple",
        "brinstar",
        "yoshis_island_(melee)",
        "yoshis_story",
        "fountain_of_dreams",
    ],
    [
        "green_greens",
        "corneria",
        "venom",
        "pokémon_stadium",
        "onett",
        "mushroom_kingdom_ii",
        "brinstar_depths",
        "big_blue",
        "fourside",
        "delfino_plaza",
        "mushroomy_kingdom",
    ],
    [
        "figure-8_circuit",
        "warioware,_inc.",
        "bridge_od_eldin",
        "norfair",
        "frigate_orpheon",
        "yoshis_island",
        "halberd",
        "lylat_cruise",
        "pokémon_stadium_2",
        "port_town_aero_drive",
        "castle_siege",
    ],
    [
        "distant_planet",
        "smashville",
        "new_pork_city",
        "summit",
        "sky_world",
        "shadow_moses_island",
        "luigis_mansion",
        "pirate_ship",
        "spear_pillar",
        "75_m",
        "mario_bros.",
    ],
    [
        "hanenbow",
        "green_hill_zone",
        "3d_land",
        "golden_plains",
        "paper_mario",
        "gerudo_valley",
        "spirit_train",
        "dream_land_gb",
        "unova_pokémon_league",
        "prism_tower",
        "mute_city_snes",
    ],
    [
        "magicant",
        "arena_ferox",
        "reset_bomb_forest",
        "tortimer_island",
        "balloon_fight",
        "living_room",
        "find_mii",
        "tomodachi_life",
        "pictochat_2",
        "mushroom_kingdom_u",
        "mario_galaxy",
    ],
    [
        "mario_circuit",
        "skyloft",
        "the_great_cave_offensive",
        "kalos_pokémon_league",
        "coliseum",
        "flat_zone_x",
        "palutenas_temple",
        "gamer",
        "garden_of_hope",
        "town_and_city",
        "wii_fit_studio",
    ],
    [
        "boxing_ring",
        "gaur_plain",
        "duck_hunt",
        "wrecking_crew",
        "pilotwings",
        "wuhu_island",
        "windy_hill_zone",
        "wily_castle",
        "pac-land",
        "super_mario_maker",
        "suzaku_castle",
    ],
    [
        "midgar",
        "umbra_clock_tower",
        "new_donk_city_hall",
        "great_plateau_tower",
        "moray_towers",
        "draculas_castle",
        "mementos",
        "yggdrasils_altar",
        "spiral_mountain",
        "king_of_fighters_stadium",
        "garreg_mach_monastery",
    ],
    [
        "spring_stadium",
        "minecraft_world",
        "northern_cave",
        "cloud_sea_of_alrest",
        "mishima_dojo",
        "hollow_bastion",
    ],
]

STAGE_LIST_EMPTY = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
]

# This is the order in which controls are displayed when selecting a button

CONTROLS_ORDER_BUTTONS = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB,
]
CONTROLS_ORDER_STICK = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB,
    Controls.SMASH_ATTACKS,
]
CONTROLS_ORDER_DPAD = [
    Controls.NORMAL_ATTACK,
    Controls.SPECIAL_ATTACK,
    Controls.JUMP,
    Controls.SHIELD,
    Controls.GRAB,
    Controls.TAUNT,
]

RULESET_ORDERS = [
    # This is only for stocks
    [
        # major options
        "style",
        "stock",
        "time",
        "fs_meter",
        "spirits",
        "cpu_lvl",
        "damage_handicap",
        "stage_selection",
    ],
    ["items"],
    ["stages"],
    [
        # advanced
        "first_to",
        "stage_morph",
        "stage_hazards",
        "friendly_fire",
        "launch_rate",
        "underdog_boost",
        "pause",
        "score",
        "show_damage",
    ],
]
