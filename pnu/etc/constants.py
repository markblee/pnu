ACTIVE = "ACTIVE"
ENROLL = "ENROLL"
RESUME = "RESUME"
STOP = "STOP"
PAUSE = "PAUSE"
RESPONSE_STATUS_LIST = [PAUSE, RESUME, STOP]

# Alerter.py
MAX_SMS_MESSAGE_LEN = 159
SMTP_RECONNECT_SLEEP_TIME = 3

POKEMON_ID_TO_NAME = [
    "bulbasaur",
    "ivysaur",
    "venusaur",
    "charmander",
    "charmeleon",
    "charizard",
    "squirtle",
    "wartortle",
    "blastoise",
    "caterpie",
    "metapod",
    "butterfree",
    "weedle",
    "kakuna",
    "beedrill",
    "pidgey",
    "pidgeotto",
    "pidgeot",
    "rattata",
    "raticate",
    "spearow",
    "fearow",
    "ekans",
    "arbok",
    "pikachu",
    "raichu",
    "sandshrew",
    "sandslash",
    "nidoran-f",
    "nidorina",
    "nidoqueen",
    "nidoran-m",
    "nidorino",
    "nidoking",
    "clefairy",
    "clefable",
    "vulpix",
    "ninetales",
    "jigglypuff",
    "wigglytuff",
    "zubat",
    "golbat",
    "oddish",
    "gloom",
    "vileplume",
    "paras",
    "parasect",
    "venonat",
    "venomoth",
    "diglett",
    "dugtrio",
    "meowth",
    "persian",
    "psyduck",
    "golduck",
    "mankey",
    "primeape",
    "growlithe",
    "arcanine",
    "poliwag",
    "poliwhirl",
    "poliwrath",
    "abra",
    "kadabra",
    "alakazam",
    "machop",
    "machoke",
    "machamp",
    "bellsprout",
    "weepinbell",
    "victreebel",
    "tentacool",
    "tentacruel",
    "geodude",
    "graveler",
    "golem",
    "ponyta",
    "rapidash",
    "slowpoke",
    "slowbro",
    "magnemite",
    "magneton",
    "farfetchd",
    "doduo",
    "dodrio",
    "seel",
    "dewgong",
    "grimer",
    "muk",
    "shellder",
    "cloyster",
    "gastly",
    "haunter",
    "gengar",
    "onix",
    "drowzee",
    "hypno",
    "krabby",
    "kingler",
    "voltorb",
    "electrode",
    "exeggcute",
    "exeggutor",
    "cubone",
    "marowak",
    "hitmonlee",
    "hitmonchan",
    "lickitung",
    "koffing",
    "weezing",
    "rhyhorn",
    "rhydon",
    "chansey",
    "tangela",
    "kangaskhan",
    "horsea",
    "seadra",
    "goldeen",
    "seaking",
    "staryu",
    "starmie",
    "mr-mime",
    "scyther",
    "jynx",
    "electabuzz",
    "magmar",
    "pinsir",
    "tauros",
    "magikarp",
    "gyarados",
    "lapras",
    "ditto",
    "eevee",
    "vaporeon",
    "jolteon",
    "flareon",
    "porygon",
    "omanyte",
    "omastar",
    "kabuto",
    "kabutops",
    "aerodactyl",
    "snorlax",
    "articuno",
    "zapdos",
    "moltres",
    "dratini",
    "dragonair",
    "dragonite",
    "mewtwo",
    "mew"
]

POKEMON_NAME_TO_ID = {
    "charmeleon": 5,
    "krabby": 98,
    "spearow": 21,
    "arcanine": 59,
    "venusaur": 3,
    "charmander": 4,
    "articuno": 144,
    "pinsir": 127,
    "weezing": 110,
    "mewtwo": 150,
    "cloyster": 91,
    "dragonite": 149,
    "tauros": 128,
    "fearow": 22,
    "paras": 46,
    "kadabra": 64,
    "jigglypuff": 39,
    "sandslash": 28,
    "abra": 63,
    "hitmonlee": 106,
    "lickitung": 108,
    "machamp": 68,
    "haunter": 93,
    "wigglytuff": 40,
    "kangaskhan": 115,
    "machop": 66,
    "goldeen": 118,
    "gengar": 94,
    "poliwhirl": 61,
    "hitmonchan": 107,
    "clefable": 36,
    "ditto": 132,
    "gloom": 44,
    "tentacool": 72,
    "primeape": 57,
    "magnemite": 81,
    "squirtle": 7,
    "vulpix": 37,
    "koffing": 109,
    "bellsprout": 69,
    "kingler": 99,
    "dratini": 147,
    "nidoqueen": 31,
    "magneton": 82,
    "psyduck": 54,
    "omastar": 139,
    "persian": 53,
    "raichu": 26,
    "kabutops": 141,
    "electrode": 101,
    "golem": 76,
    "farfetchd": 83,
    "moltres": 146,
    "mew": 151,
    "gyarados": 130,
    "vaporeon": 134,
    "doduo": 84,
    "muk": 89,
    "marowak": 105,
    "wartortle": 8,
    "gastly": 92,
    "slowpoke": 79,
    "rhydon": 112,
    "cubone": 104,
    "chansey": 113,
    "geodude": 74,
    "parasect": 47,
    "pidgeotto": 17,
    "venomoth": 49,
    "victreebel": 71,
    "nidorino": 33,
    "nidorina": 30,
    "rhyhorn": 111,
    "tentacruel": 73,
    "lapras": 131,
    "grimer": 88,
    "ninetales": 38,
    "mankey": 56,
    "scyther": 123,
    "dodrio": 85,
    "ekans": 23,
    "seadra": 117,
    "nidoking": 34,
    "zapdos": 145,
    "voltorb": 100,
    "jolteon": 135,
    "metapod": 11,
    "growlithe": 58,
    "rattata": 19,
    "eevee": 133,
    "snorlax": 143,
    "kabuto": 140,
    "poliwrath": 62,
    "electabuzz": 125,
    "ivysaur": 2,
    "omanyte": 138,
    "drowzee": 96,
    "graveler": 75,
    "caterpie": 10,
    "diglett": 50,
    "hypno": 97,
    "machoke": 67,
    "horsea": 116,
    "exeggutor": 103,
    "sandshrew": 27,
    "golduck": 55,
    "aerodactyl": 142,
    "pidgeot": 18,
    "exeggcute": 102,
    "nidoran-f": 29,
    "nidoran-m": 32,
    "onix": 95,
    "clefairy": 35,
    "meowth": 52,
    "dugtrio": 51,
    "porygon": 137,
    "slowbro": 80,
    "alakazam": 65,
    "zubat": 41,
    "staryu": 120,
    "weedle": 13,
    "seel": 86,
    "blastoise": 9,
    "oddish": 43,
    "flareon": 136,
    "bulbasaur": 1,
    "beedrill": 15,
    "arbok": 24,
    "ponyta": 77,
    "butterfree": 12,
    "tangela": 114,
    "venonat": 48,
    "charizard": 6,
    "magikarp": 129,
    "pikachu": 25,
    "pidgey": 16,
    "jynx": 124,
    "seaking": 119,
    "dewgong": 87,
    "dragonair": 148,
    "kakuna": 14,
    "starmie": 121,
    "shellder": 90,
    "magmar": 126,
    "weepinbell": 70,
    "golbat": 42,
    "mr-mime": 122,
    "poliwag": 60,
    "vileplume": 45,
    "rapidash": 78,
    "raticate": 20
}
