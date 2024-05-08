import tkinter as tk
from tkinter import messagebox
import random

# Initialize Tkinter
root = tk.Tk()
root.title("Malik's Really Stupid Quiz Game")
# Adjust the Size
root.geometry("1280x720")

#Adjust the background color
root.configure(bg="turquoise1")

# Define global variables
score = 0
current_question = None
current_question_index = 0
category = None
difficulty = None
questions_answered = 0
windowX = 1280
windowy = 720
x = 0
global questions

# Define the questions
questions = {
    "Harry Potter": {
        "Easy": [
            {"question": "What is the name of Harry Potter's pet owl?", "options": ["Hedwig", "Scabbers", "Crookshanks", "Fawkes"], "correct_index": 0},
            {"question": "How many years did Sirius Black spend in Azkaban?", "options": ["10", "13", "12", "11"], "correct_index": 2},
            {"question": "Who slayed the creature in the Chamber of Secrets?", "options": ["Ron Weasley", "Harry Potter", "Neville Longbottom", "Gilderoy Lockhart"], "correct_index": 1},
            {"question": "What house is Fred Weasley in?", "options": ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"], "correct_index": 0},
            {'question': 'In what year did Harry first meet Buckbeak/Witherwings?', 'options': ['Year 2','Year 5','Year 4','Year 3'], 'correct_index': 3},
            {"question": "Who created Harry Potter's wand?", "options":["Gregorovich","Ollivander","Dumbledore","Oliver"], "correct_index":1 },
            {"question": "What color is Hedwig?", "options":["Cloud Grey","Brown","Snow White","Jet Black","Golden"], "correct_index":2},
            {"question": "Who are Harry Potter's best friends?", "options":["Hailey/Tom","Hannah/Ray","Hermione/Ron","Heather/Ronan","Hermione/Tom","Hannah/Ron"], "correct_index":2},
            {"question": "What shape is the scar on Harry's forehead?", "options":["Circle","Banana","Crescent","Lightning Bolt","Arrow","Triangle","Cross"], "correct_index":3},
            {"question": "What animal does Neville Longbottom keep as a pet?", "options":["Owl","Rat","Cat","Toad"], "correct_index": 3},
        ],
        "Medium": [
            {"question": "What is the core of Voledmort's original wand made of?", "options":["Unicorn Hair","Spider Silk","Dragon Heartstring","Thestral Hair","Phoenix Feather","Werewolf Fur"], "correct_index":4},
            {"question": "What creature is hidden in the Chamber of Secrets?", "options":["Cockatrice","Acromatula","Runespoor","Thestral","Basilisk"], "correct_index":4},
            {"question": "What is the name of Hagrid's pet spider?", "options":["Arachno","Aragorn","Aragog","Tarantulo","Arachne","Aranea"], "correct_index": 2},
            {"question": "The original name for Voldemort's followers is?", "options":["Knights of Walpurgis","Paladins of Death","Warlocks of Wuspire","Death Defiliers"], "correct_index":0 },
            {"question": "Who was killed the first time Lord Voldemort opened the Chamber of Secrets?", "options":["Colin Creevey","Myrtle Warren","Tom Riddle","Adrian Diggle"], "correct_index":1},
            {"question": "The three unforgivable curses are Avada Kedavra, Crucio, and what?", "options":["Sectumsempra","Flagrante","Geminio","Imperio","Reducto","Calvorio"], "correct_index":3},
            {"question": "Who killed Nagini?", "options":["Harry Potter","Ron Weasley","Neville Longbottom","Dean Thomas","Draco Malfoy"], "correct_index":2},
            {"question": "What dragon did Viktor Krum end up facing in the first task of the Tri Wizard Tournament?", "options":["Chinese Fireball","Romanian Longhorn","Welsh Green","Hungarian Horntail","Swedish Short-Snout","Ukranian Ironbelly"], "correct_index":0 },
            {"question": "What is James Potter's nickname among the Maurauders?", "options":["Padfoot","Moony","Prongs","Wormtail","Batwing"], "correct_index":2 },
            {"question": "At Hogwarts each house has it's own ghost, what is Hufflepuff's?", "options":["The Grey Lady","Peeves","Nearly Headless Nick","The Fat Friar","The Bloody Baron","Moaning Myrtle","Professor Bins"], "correct_index":3},
        ],
        "Hard": [
            {"question": "What is the name of the knockback jinx?", "options":["Stupefy","Flipendo","Sectumsempra","Expelliarmus","Diffindo"], "correct_index":1},
            {"question": "Whose Death Day party did Harry Potter attend at Hogwarts?", "options":["The Fat Friar","The Bloody Baron","The Grey Lady","Nearly Headless Nick"], "correct_index":3},
            {"question": "Who was the true owner of the Elder Wand right after Dumbledore's death?", "options":["Severus Snape","Draco Malfoy","Lord Voldemort","Harry Potter","Gellert Grindelwald"], "correct_index":1 },
            {"question": "What is the incantation for the Extension Charm?", "options":["Engorgio","Cistem Aperio","Molliare","Capacious Extremis","Colloportuss"], "correct_index":3},
            {"question": "Who told Tom Riddle what a Horcrux is?", "options":["Professor Dumbledore","Professor Umbridge","Professor Carrow","Professor Rookwood","Professor Fig","Professor Lockhart","Professor Slughorn"], "correct_index":6},
            {"question": "In Hogwarts Legacy the sister of Sebastian Sallow, Anne is cursed by which character?", "options":["Ranrok","Ominis Gaunt","Victor Rookwood","Isidora Morganach","Voldemort"], "correct_index":2 },
            {"question": "What did Mrs. Weasley give to Harry for his 17th birthday?", "options":["A Book","A Sneakoscope","Chocolates","A Watch","Enchanted Razor"], "correct_index":3 },
            {"question": "What fake name did Harry use to attend Bill and Fleur's wedding?", "options":["Barry Weasley","Bailey Weasley","Percy Weasley","Arnold Weasley","Barney Weasley","Billius Weasley"], "correct_index":4},
            {"question": "What creature gave Isolt Sayre part of their body to create a wand for her son Chadwick?", "options":["Wampus","Horned Serpent","Snallygaster","Pukwudgie","Thunderbird","Qilin","Nundu"], "correct_index":1 },
            {"question": "What is the name of the oldest Peverell brother?", "options":["Cadmus","Ignotus","Antioch","Hardwin","Iolanthe","Aldrich"], "correct_index":2},
        ]
    },
    "Mythology": {
        "Easy": [
            {"question": "Who is the king of the gods in Greek mythology?", "options": ["Zeus", "Poseidon", "Hades", "Apollo"], "correct_index": 0},
            {"question": "The world ending event in Norse mythology is called?", "options":["Armageddon","Renovation","Revelations","Ragnarok","Doomsday"], "correct_index": 3},
            {"question": "Who is the king of the Underworld in Greek mythology?", "options": ["Charo", "Hades", "Tartaros", "Nyx"], "correct_index": 1},
            {"question": "Who is the Norse god of Thunder?", "options":["Odin","Baldur","Thor","Borr","Frigg"], "correct_index":2},
            {"question": "What kind of creature is Medusa?", "options":["Siren","Minotaur","Harpy","Gorgon"], "correct_index":3},
            {"question": "In Egyptian mythology which god is known to have the head of a Jackal(dog)?", "options":["Osiris","Hathor","Anubis","Ra","Isis","Bastet"], "correct_index": 2},
            {"question": "What is the name of the hammer weilded by the Norse god Thor?", "options":["Gungir","Mjolnir","Stormbreaker","Gram","Excalibur"], "correct_index": 1},
            {"question": "Which Norse god is known as the one eyed god?", "options":["Tyr","Thor","Odin","Sif","Frigg","Balder"], "correct_index": 2},
            {"question": "Who is the Greek goddess of love, sex, and beauty?", "options":["Demeter","Athena","Hera","Gaia","Nyx","Aphrodite","Persephone","Artemis"], "correct_index":5},
            {"question": "Which god is known as the trickster in Norse mythology?", "options":["Loki","Odin","Freya","Baldur","Heimdall"], "correct_index": 0},
            {"question": "What Greek hero is known to have only one weakness?", "options":["Hercules","Theseus","Heracles","Ares","Perseus","Achilles","Percy","Oedipus"], "correct_index":5},
            {"question": "What is the name of the sacred mountain in Japanese mythology, believed to be the dwelling place of the gods and goddesses?", "options":["Mount Fuji","Mount Olympus","Mount Hiei","Mount Wuda","Mount Asahi"], "correct_index": 0},
        ],
        "Medium": [
            {"question": "What is the name of the ruling god in Egyptian mythology?", "options":["Isis","Sobek","Anubis","Horus","Amun"], "correct_index":3 },
            {"question": "In Chinese mythology the Four Directional Guardians are creatures that include: Dragon, Phoenix, White Tiger, and ?", "options":["Turtle","Snake","Qilin","Nian"], "correct_index": 0},
            {"question": "The Roman god Jupiter is also known by what name to the Greeks?", "options":["Hades","Ares","Poseidon","Hermes","Zeus","Hephestaus","Apollo"], "correct_index": 4},
            {"question": "Which Japanese god/goddess is widely recognized as the head/ruling diety?", "options":["Susanoo","Tsukiyomi","Amaterasu","Ama-no-Uzume","Inari"], "correct_index": 2},
            {"question": "In Norse mythology, what is the name of the realm inhabited by the giants?", "options":["Anaheim","Alfheim","Helheim","Midgard","Jotunheim","Asgard","Niðavellir"], "correct_index":4},
            {"question": "What is the name of the legendary sword in Japanese mythology, one of the three imperial regalia, said to represent valor and protection?", "options":["Muramasa","Kusanagi","Totsuka-no-Tsurugi","Masamune"], "correct_index": 1},
            {"question": "What is the name of the giant serpent that encircles the world in Norse mythology?", "options":["Fenrir","Jormungander","Sleipnir","Nidhogg","Skoll","Kraken"], "correct_index":1},
            {"question": "What is the name of the legendary creature in Japanese mythology, often depicted as a giant cat with a flaming tail, believed to cause earthquakes?", "options":["Nekomata","Bakeneko","Raiju","Gashadokuro","Yurei"], "correct_index": 2},
            {"question": "In Norse mythology, what is the name of the realm of fire, home to the fire giants?", "options":["Jotunheim","Svartalfheim","Niflheim","Muspelheim","Midgard","Asgard"], "correct_index": 3},
            {"question": "Who is the goddess of the moon in Chinese mythology, often associated with the Mid-Autumn Festival and depicted as a beautiful woman holding a rabbit?", "options":["Fei Lian","Change'e","Nezha","Nian","Pixiu"], "correct_index":1 },            
        ],
        "Hard": [
            {"question": "What animal is said to become a dragon after climbing a waterfall in Chinese/Japanese mythology?", "options":["Shrimp","Carp/Koi","Seahorse","Salmon","Eel"], "correct_index":1},
            {"question": "Who is the monkey god in Hindu mythology?", "options":["Vishnu","Shiva","Hanuman","Krishna"], "correct_index":2 },
            {"question": "In Hindu mythology who is known as 'The Destroyer?", "options":["Vishnu","Indra","Brahma","Shiva","Lakshmi","Ganesha"], "correct_index":3},
            {"question": "In Norse mythology, what is the name of the sword weilded by the god Freyr, which fights on its own and is a symbol of fertility?", "options":["Gram","Hofund","Laevateinn","Tyrfing","Mjolnir"], "correct_index":2 },
            {"question": "What is the name of the monstrous dragon goddess in Mesopotamian mythology, often depicted as a primordial chaos serpent who battles against the gods?", "options":["Ishtar","Ninhursag","Ereshkigal","Enki","Shedu","Tiamat"], "correct_index": 5},
            {"question": "What is the name of the winged bull with a human head, a protective deity often depicted at the entrances of Mesopotamian palaces and temples?", "options":["Apkallu","Shedu","Anzu","Ishtar","Lamassu","Tiamat"], "correct_index": 4},
            {"question": "In Cherokee mythology, what is the name of the giant horned serpent that is believed to inhabit bodies of water and is associated with healing and fertility?", "options":["Tlanuwa","Uktena","Mishipeshu","Piasa","Kokopelli"], "correct_index": 1},
            {"question": "What is the name of the giantess who in Norse mythology, guards the apples of immortality in her orchard in Asgard?", "options":["Hel","Idun","Ran","Buri","Skadi","Ymir"], "correct_index": 1},
            {"question": "Who is the god of the sea in Celtic mythology, often depicted as a powerful, bearded figure wielding a trident?", "options":["Manannán mac Lir","Taranis","Nuada","Aengus"], "correct_index": 0},
            {"question": "Who is the creator goddess in Chinese mythology, often depicted as a cosmic mother figure who gave birth to the world?", "options":["Hou Yi","Guanyin","Nuwa","Chang'E","Xihe"], "correct_index": 2},
        ]
    },
    "Anime": {
        "Easy": [
            {"question": "In which anime series can you find the character Eren Yeager?", "options": ['One Piece', 'Dragon Ball Z', 'Naruto', 'Attack on Titan'], "correct_index": 3},
            {"question": "Who is the main character of the anime/manga One Piece?", "options": ['Monkey D Ruffy', 'Monkey D Luffy', 'Monkey D Goofy', 'Monkey D Loogey'], "correct_index": 1},
            {"question": "What is the first Pokemon Ash gets on his journey in Kanto?", "options": ['Squirtle', 'Charmander', 'Bulbasaur', 'Pikachu'], "correct_index": 3},
            {"question": "What is the name of Yusuke Urameshi's signature attack?", "options": ["Kamehameha", "Rasengan", "Spirit Gun", "Janken", "Spirit Bomb"], "correct_index": 2},
            {"question": "What is the name of Luffy's pirate crew?", "options": ["Heart Pirates", "Kid Pirates", "Blackhair Pirates", "Strawhat Pirates", "Luffy Pirates"], "correct_index": 3},
            {"question": "In the anime Kakegurui most things are settled via what?", "options":["Fighting","Sports","Gambling","Debate","Music"], "correct_index":2},
            {"question": "Who is the main character in Nisekoi, a high school student torn between his supposed love interests Chitoge Kirisaki and Kosaki Onodera?", "options":["Raku Ichijo","Seishiro Tsugumi","Ruji Kirisaki","Shu Maiko"], "correct_index":0 },
            {"question": "In YuYu Hakusho, what is the name of the demon who serves as the ruler of the Spirit World and assigns Yusuke Urameshi as a Spirit Detective?", "options":["Sensui","Koenma","Botan","Genkai","Raizen","Hiei","Kuwabara"], "correct_index": 1},
            {"question": "In Tokyo Ghoul, what is the name of the coffee shop where Kaneki Ken works and frequents, which serves as a safe haven for ghouls?", "options":["Anteiku","Cafe Moka","CG Coffee House","Ghoul Grounds","Central Cafe"], "correct_index":0 },
            {"question": "What is the name of the female protagonist in Attack on Titan who possesses exceptional combat skills and is deeply devoted to Eren Yeager?", "options":["Sasha","Annie","Ymir","Hagne","Mikasa","Historia"], "correct_index": 4},
        ],
        "Medium": [
            {"question": "What is the name of the four-tailed beast in the series Naruto?", "options": ['Son Goku', 'Kurama', 'Isobu', 'Matatabi'], "correct_index": 0},
            {"question": "In Sailor Moon, how many Sailor Scouts are there originally?", "options": ["3", "5", "4", "6", "7"], "correct_index": 1},
            {"question": "Who destroyed planet Vegeta in Dragon Ball Z?", "options": ['Frieza', 'Cell', 'Majin Buu', 'Babidi'], "correct_index": 0},
            {"question": "In the series Katekyo Hitman Reborn how many colors of sky flames are there?", "options": ["8", "10", "6", "9", "7"], "correct_index": 4},
            {"question": "How many tailed beasts are there in the series Naruto?", "options": ["6", "8", "13", "10", "7"], "correct_index": 3},
            {"question": "What race do the characters Goku, Vegeta, Nappa, and Broly belong to?", "options": ["Tuffles", "Heaters", "Saiyans", "Cerealians", "Humans", "Namekians"], "correct_index": 2},
            {"question": "In the anime/manga sword art online the protagonist Kirito is widely known as a what?", "options":["Cheater","Beater","Beta Tester","Noob","Hacker","Pro"], "correct_index": 1},
            {"question": "In Black Clover, what is the name of the ancient demon dwelling within Asta's grimoire", "options":["Zagred","Licht","Lumiere","Liebe","Asta"], "correct_index": 3},
            {"question": "Who is the primary antagonist in Bleach, the leader of the Quincy army who seeks to exterminate all Soul Reapers and destroy the Soul Society?", "options":["Yhwach","Aizen","Gin","Starkk"], "correct_index":0 },
            {"question": "What is the name of Ippo's pet dog in Hajime no Ippo?", "options":["Hachi","Aoki","Taihei","Toto","Wanpo"], "correct_index": 4},
        ],
        "Hard": [
            {"question": "What movie did 'Demon Slayer the Movie: Mugen Train' replace as the highest-grossing anime movie?", "options": ["One Piece Film Red", "Suzume", "Naruto the Movie: The Last", "Spirited Away", "Howls Moving Castle", "Your Name"], "correct_index": 3},
            {"question": "What is the name of the bankai used by Ichigo Kurosaki in Bleach?", "options": ['Tensa Zangetsu', 'Senbonzakura Kageyoshi', 'Katen Kyokotsu', 'Zangetsu'], "correct_index": 0},
            {"question": "What is the name of the mecha piloted by Shinji Ikari in Neon Genesis Evangelion?", "options": ['EVA-03', 'EVA-01', 'EVA-02', 'EVA-04'], "correct_index": 1},
            {"question": "What is the name of the devil fruit eaten by the One Piece villain Crocodile/Mr.0", "options": ["Gomu Gomu","Goro Goro","Suna Suna","Mera Mera"], "correct_index":2},
            {"question": "How many different openings are there for Naruto Shippuden?", "options":["15","19","11","14","16","20","13"], "correct_index":5 },
            {"question": "What is the longest running anime?", "options":["One Piece","Naruto","Doraemon","Case Closed","Nintama Rantaro","Sazae-San","Crayon Shin-chan"], "correct_index":4},
            {"question": "In Hajime no Ippo, what is the name of the professional boxer known as the Wind God due to his exceptional speed and footwork?", "options":["Takeshi Sendo","Ricardo Martinez","Mamoru Takamura","Miyata Ichiro"], "correct_index": 1},
            {"question": "Who is the rival actress of Kyoko Mogami and childhood friend of Ren Tsuruga in Skip Beat?", "options":["Maria Takarada","Kyoko Mogami","Kanae Kotonami","Lory Takarada"], "correct_index": 2},
            {"question": "In Naruto, what is the name of the ninja village led by the main antagonist Pain, which seeks to bring peace through pain and suffering?", "options":["Amegakure","Kumogakure","Sunagakure","Iwagakure"], "correct_index": 0},
            {"question": "What is the name of the secret base where the group of friends used to hang out in Anohana?", "options":["The Treehouse","The Super Tree","The Secret Garden","Forever Retreat","Super Peace Busters Hideout"], "correct_index": 4},
        ]
    },
    "Gaming": {
        "Easy": [
            {"question": "Which popular video game features a character named Link?", "options": ['The Legend of Zelda', 'Super Mario Bros.', 'Sonic the Hedgehog', 'Final Fantasy'], "correct_index": 0},
            {"question": "What is the best-selling video game of all time?", "options": ['Tetris', 'Minecraft', 'Pong','Grand Theft Auto V', 'Wii Sports'], "correct_index": 1},
            {"question": "What is the name of the city where the events of Grand Theft Auto: 4 take place?", "options": ['Los Santos', 'Vice City', 'Anywhere City', 'San Fierro', 'Liberty City' 'Las Venturas'], "correct_index": 4},
            {"question": "Which Call of Duty game first introduced the game mode Zombies?", "options": ['Call of Duty: World at War', 'Call of Duty 4: Modern Warfare', 'Call of Duty: Black Ops', 'Call of Duty: Modern Warfare 2'], "correct_index": 0},
            {"question": "What is the name of the landlord in Animal Crossing: New Horizons?", "options":["Jim Nook","Tom Nook","Ken Nook","Bob Nook","Todd Nook","Rob Nook","Tim Nook"], "correct_index": 1},
            {"question": "The game Skyrim is part of the Elder ____ series, what is missing?", "options":["Books","Papyrus","Scrolls","Ledgers","Prophecies","Notes"], "correct_index":2 },
            {"question": "What kingdom is Mario's home located in?", "options":["Star","Fire Flower","Floral","Mushroom"], "correct_index": 4},
            {"question": "In Sonic Adventure Battle 2 what song is playing during the level City Escape?", "options":["Hydro City Zone","Countdown to Continue","Drowning","Escape from the City"], "correct_index":3},
            {"question": "What Pokemon is on the cover of the game Pokemon Crystal?", "options":["Lugia","Entei","Suicuine","Ho-Oh","Kyogre"], "correct_index": 2},
            {"question": "In Mario Kart what power-up grants you both a speed boost and invincibility?", "options":["Star","Mushroom","Flower","Red Shell","Blue Shell"], "correct_index":0},
        ],
        "Medium": [
            {"question": "What is the name of the third game in the Pokémon series that did not release in America?", "options": ['Pokémon Emerald', 'Pokémon Crystal', 'Pokémon FireRed', 'Pokémon Green', 'Pokemon Yellow'], "correct_index": 3},
            {"question": "What is the best-selling video game console of all time?", "options": ['Nintendo Switch','Playstation 4','PlayStation 2', 'Nintendo DS', 'Game Boy', 'Wii'], "correct_index": 2},
            {"question": "Which video game franchise features a protagonist named Samus Aran?", "options": ['Metroid', 'Halo', 'Doom', 'Gears of War'], "correct_index": 0},
            {"question": "The game Pokemon Stadium was originally released on which console?", "options":["Nintendo Gamecube","Nintendo Switch","Nintendo DS","Nintendo 64","Nintendo Wii"], "correct_index":3},
            {"question": "In what Mario Bros title was Rosalina introduced in?", "options":["Super Mario Odyssey","Super Mario Galaxy","Super Mario Sunshine","Super Mario Bros. 3"], "correct_index": 1},
            {"question": "What is the name of Sam's arch-nemesis, a mischievous character who serves as the main antagonist in the first Pajama Sam game?", "options":["Captain Chaos","King Nox","Dr. Dark","Darkness","Mr. Night"], "correct_index":3},
            {"question": "In Persona 5 what is the name of the cafe where the protagonist lives and his friends gather to plan their activities?", "options":["Cafe Soiree","Leblanc","Cafe Velvet","Cafe Ame","D'Andy"], "correct_index":1 },
            {"question": "What is the name of the city where the events of Grand Theft Auto: San Andreas take place?", "options": ['Los Santos', 'Vice City', 'San Fierro', 'Las Venturas'], "correct_index": 0},
            {"question": "In Power Rangers: Battle for the Grid, what is the name of the main villain who seeks to conquer multiple dimensions and control the Morphin Grid?", "options":["Lord Zedd","Goldar","Rita Repulsa","Lord Drakkon","Master Vile","Ivan Ooze"], "correct_index":3 },
            {"question": "In the game Ratchet & Clank: Rift Apart, who is the main antagonist?", "options":["Annihilus","Captain Quark","Nefarious","Darkseid"], "correct_index": 2},
        ],
        "Hard": [
            {"question": "Which famous musical artist contributed to the soundtrack of Sonic the Hedgehog 3?", "options": ['David Bowie', 'Prince', 'Madonna', 'Michael Jackson', 'Tupac'], "correct_index": 3},
            {"question": "Which video game is scientifically proven to help people with PTSD?", "options": ['Tetris', 'Minecraft', 'Call of Duty', 'Sonic the Hedgehog'], "correct_index": 0},
            {"question": "What species of animal is the rarest in Animal Crossing: New Horizons?", "options":["Cat","Dog","Hippo","Koala","Squirrel","Mouse","Penguin","Rhino","Tiger","Bear","Duck","Octopus","Gorilla","Horse","Deer","Dragon","Salmon","Elephant"], "correct_index": 11},
            {"question": "In Mario Kart: Double Dash the hardest difficulty is known as what?", "options":["200cc","150cc","Reverse","250cc","Turbo","Mirror","Extreme"], "correct_index": 5},
            {"question": "In the National Pokedex, what Pokemon is #708?", "options":["Amaura","Phantump","Avalugg","Pumpkaboo","Goomy","Noivern"], "correct_index": 1},
            {"question": "Which character serves as the commisioner/referee in the Backyard Sports video game series, overseeing various sports competitions among neighborhood kids?", "options":["Pablo Sanchez","Ricky Johnson","Annie Frazier","Kenny","Reese","Mr. Clanky","Mikey Thomas"], "correct_index":5},
            {"question": "In Persona 5: Royal, what is the name of the new confidant introduced exclusively in this version, who is a counselor at Shujin Academy?", "options":["Kasumi Yoshizawa","Ichiko Ohya","Takuto Maruki","Sadayo Kawakami"], "correct_index":2 },
            {"question": "In the Spongebob Squarepants The Movie game for Gameboy Advance, what is the first level called?", "options":["Manager Material","Manager Ahoy","I'm Ready","Manager Ready","The Krusty Krab 2"], "correct_index":0 },
            {"question": "In the Gameboy Advance version of Yu-Gi-Oh! World Championship Tournament 2004, which character is featured on the right side of the cover?", "options":["Tea","Tristan","Bakura","Marik","Joey","Rare Hunter","Arcana","Yami Yugi(Atem)"], "correct_index": 4},
            {"question": "In the mobile game Dragon Ball Z: Dokkan Battle, what LR characters were released for the 4th year Anniversarry", "options":["SSB Goku/Vegeta","UI Goku/Evo Blue Vegeta","SSJ4 Goku/Vegeta","Goku/SSJ4 Vegeta","Beast Gohan/Orange Piccolo","Gamma #1/Gamma #2","SSJ Broly/SSB Gogeta"], "correct_index":2},
        ]
    },
    "Science": {
        "Easy": [
            {"question": "What is the chemical makeup of water?", "options":["O2","CO2","H2O","NaCI"], "correct_index":2 },
            {"question": "What is the name of the force that pulls objects towards the center of the Earth?", "options":["Inertia","Gravity","Magnetism","Friction"], "correct_index":1},
            {"question": "What planet is the fourth planet in our solar system?", "options":["Earth","Venus","Jupiter","Mars","Mercury"], "correct_index":3},
            {"question": "The process by which plants make their own food using sunlight?", "options":["Photosynthesis","Decomposition","Respiration","Fermetation","Dehydration"], "correct_index":0 },
            {"question": "The powerhouse of the cell is known as the?", "options":["Nucleus","Mitochondria","Ribosome","Vacuole","Endoplasmic reticulum"], "correct_index": 1},
            {"question": "Which of the following is NOT a type of blood cell?", "options":["Red blood cell","White blood cell","Platelets","Osteoblasts"], "correct_index": 3},
            {"question": "Which of the following is NOT a type of cloud?", "options":["Cumulus","Cumulonimbus","Altolonimbus","Cirrus","Stratus"], "correct_index": 2 },
            {"question": "What is the name of the theory that explains the origin of the universe and its subsequent evolution?", "options":["Theory of Relativity","Quantum Mechanics","Big Bang Theory","String Theory","Atomic Theory"], "correct_index":2},
            {"question": "What is the chemical name for table salt?", "options":["Potassium Nitrate","Calcium Carbonate","Magnesium Sulfate","Calcium Sulfate","Sodium Chloride"], "correct_index": 4},
            {"question": "Which part of the atom has a positive charge?", "options":["Proton","Neutron","Electron","Nucleus"], "correct_index": 0},
        ],
        "Medium": [
            {"question": "What are insect exoskeletons made out of?", "options":["Bone","Marrow","Skin","Keratin","Chitin"], "correct_index": 4},
            {"question": "What type of weathering involves the breakdown of rocks due to the action of water, ice, or wind?", "options":["Chemical Weathering","Physical Weathering","Erosional Weathering","Biological Weathering"], "correct_index":1},
            {"question": "Which type of rock forms from the cooling and solidification of magma or lava?", "options":["Sedimentary","Metamorphic","Igneous","Conglomerate"], "correct_index": 2},
            {"question": "What is the unit of measurement for electrical current?", "options":["Joules","Volts","Ohms","Amperes"], "correct_index":3},
            {"question": "Which scientist is credited with the discovery of gravity after observing an apple fall from a tree?", "options":["Albert Einstein","Galileo Galilei","Isaac Newton","Nikola Tesla"], "correct_index": 2},
            {"question": "Which planet in our solar system has the largest number of moons?", "options":["Jupiter","Neptune","Saturn","Earth","Mercury","Mars"], "correct_index": 0},
            {"question": "What is the name of the protein responsible for carrying oxygen in red blood cells?", "options":["Insulin","Hemoglobin","Collagen","Keratin"], "correct_index": 1},
            {"question": "What is the unit of measurement for frequency?", "options":["Ohms","Watts","Joules","Newtons","Kelvins","Amps","Hertz","Cadellas"], "correct_index": 6},
            {"question": "Roughly how long does it take for the sun’s light to reach Earth?", "options":["10 minutes","10 seconds","10 hours","8 seconds","12 minutes","8 minutes","5 seconds","1 month"], "correct_index": 5},
            {"question": "What does DNA stand for?", "options":["Deoxyribonucleic Acid","Double Nitrogen Atom","Dynamic Nucleotide Assembly","Digital Neural Algorithm"], "correct_index": 0},
        ],
        "Hard": [
            {"question": "Which organelle is responsible for protein synthesis in eukaryotic cells?", "options":["Mitochondria","Golgi Apparatus","Endoplasmic Reticulu","Ribosome","Nucleus","Cytoskeleton"], "correct_index":3 },
            {"question": "What is the name of the region surrounding a black hole where the gravitational pull is so strong that nothing can escape?", "options":["Event Horizon","Accretion Disk","Photon Sphere","Singularity","Gravity Well"], "correct_index": 0},
            {"question": "Which of the following is NOT a type of soil horizon found in a soil profile?", "options":["Topsoil","Subsoil","Bedrock","Parent Material"], "correct_index": 2},
            {"question": "Which gas is produced during the process of anaerobic respiration in humans?", "options":["Oxygen","Nitrogen","Carbon Dioxide","Methane","Carbon Monoxide"], "correct_index": 3},
            {"question": "What is the chemical formula for sulfuric acid?", "options":["H2SO3","H2SO4","H2S2","H2O3"], "correct_index": 1},
            {"question": "Which type of electromagnetic radiation has the shortest wavelength?", "options":["Radio Waves","Ultraviolet","X-Rays","Infrared","Gamma Rays"], "correct_index": 4},
            {"question": "How much DNA do humans and chimpanzees roughhly share?", "options":["90%","85%","82%","92%","91%","99%","77%","98%","83%","89%"], "correct_index": 7},
            {"question": "What is the chemical formula for methane?", "options":["CH4","CO2","H2O","NH3","H2SO3","C2H3","H2C2O2"], "correct_index": 0},
            {"question": "At what temperature are Celsius and Fahrenheit equal?", "options":["0C","10C","100C","20C","-20C","-100C","35C","28C","-40C"], "correct_index": 8},
        ]
        
    }
}
# Define functions
def select_category(cat):
    global category
    category = cat
    hide_category_buttons()
    show_difficulty_buttons()
    
def select_difficulty(diff):
    #print("Working select difficulty")
    global difficulty
    difficulty = diff
    hide_difficulty_buttons()
    start_quiz()

def hide_category_buttons():
    #print("Working hide category")
    harry_potter_button.pack_forget()
    mythology_button.pack_forget()
    anime_button.pack_forget()
    gaming_button.pack_forget()
    science_button.pack_forget()

def hide_difficulty_buttons():
    #print("Working hide difficulty")
    easy_button.pack_forget()
    medium_button.pack_forget()
    hard_button.pack_forget()

def show_category_buttons():
    #print("Working show category")
    harry_potter_button.pack(side="top",padx= 50, pady=10, anchor='center')
    mythology_button.pack(side="top",padx= 50, pady=10, anchor='center')
    anime_button.pack(side="top",padx= 50, pady=10, anchor='center')
    gaming_button.pack(side="top",padx= 50, pady=10, anchor='center')
    science_button.pack(side="top",padx= 50, pady=10, anchor='center')

def show_difficulty_buttons():
    global category, difficulty, score, questions_answered, current_question, current_question_index, questions, option_buttons, easy_button, medium_button, hard_button
    #print("Working show difficulty")
    easy_button.pack(side="top", anchor ="center", padx=50, pady=10, fill='x')
    medium_button.pack(side="top",anchor ="center", padx=50, pady=10 ,fill='x')
    hard_button.pack(side="top", anchor ="center", padx=50, pady=10 ,fill='x')
    
def start_quiz():
    global questions_answered, score, options_buttons
    #print("Start Quiz")
    questions_answered = 0
    score = 0
    score_label.config(text="Score: 0")
     # Clear the existing option buttons
    for button in option_buttons:
        button.destroy()

    # Reset the list of option buttons
    option_buttons.clear()
    
    # Get the current question
    current_question = questions[category][difficulty][current_question_index]
    
    # Set the question label
    question_label.config(text=current_question["question"])
        
    for option in current_question["options"]:
        button = tk.Button(root, text=option, command=lambda idx=current_question["options"].index(option): check_answer(idx))
        button.pack(side="top", padx=50, pady=10, anchor='center', fill="x")
        option_buttons.append(button)
    next_question()

def reset_game():
    global category, difficulty, score, questions_answered, current_question, current_question_index, questions, option_buttons
    category = None
    difficulty = None
    current_question = None
    current_question_index = 0
    question_label.config(text="")
    for button in option_buttons:
        button.destroy()  # Destroy the previous buttons
    option_buttons = []  # Reset the list of option buttons
    show_category_buttons()  # Show category buttons again
    
def next_question():
    global current_question_index, current_question
    if category and difficulty:
        questions_list = questions[category][difficulty]
        if questions_list:
            if current_question_index < len(questions_list):
                current_question = questions_list[current_question_index]
                #print(current_question)
                question_label.config(text=current_question["question"])
                
                # Clear existing option buttons
                for button in option_buttons:
                    button.destroy()
                
                # Create buttons for each option
                for option in current_question["options"]:
                    button = tk.Button(root, text=option, command=lambda idx=current_question["options"].index(option): check_answer(idx))
                    button.pack(side="top", padx=50, pady=10, anchor="center",fill='x')
                    option_buttons.append(button)
                
                current_question_index += 1  # Increment here
                #print(current_question_index)
            else:
                show_end_game_options()
        else:
            show_end_game_options()
    else:
        messagebox.showwarning("Category or Difficulty not selected", "Please select a category and difficulty.")
        
def check_answer(answer):
    global score, questions_answered, category, difficulty, current_question
    #print("Check answer working")
    if current_question is not None:
        correct_index = current_question["correct_index"]
        if answer == correct_index:
            score += 1
            score_label.config(text=f"Score: {score}")
        questions_answered += 1
        if questions_answered >= len(questions[category][difficulty]):
            show_end_game_options()
        else:
            next_question()
    else:
        #print(category)
        #print(difficulty)
        #print(current_question)
        messagebox.showerror("No Question", "No question to answer. Please select a category and difficulty first.")

def show_end_game_options():
    messagebox.showinfo("Quiz Finished", f"Your final score is: {score}")
    choice = messagebox.askquestion("Game Over", "Do you want to play again?")
    if choice == "yes":
        reset_game()
    else:
        root.destroy()
        
################################################
## Actual Start of the program loop
welcome_label = tk.Label(root, text="Welcome to the Quiz Game!",bg="turquoise1", font=("Times New Roman", 18))
welcome_label.pack(side="top", anchor = "center", padx=50, pady=50,fill='x')

score_label = tk.Label(root, text="Score: 0",bg="turquoise1", font=("Times New Roman", 12))
score_label.pack(side="top", anchor = "w", padx=50, pady=10)

harry_potter_button = tk.Button(root, text="Harry Potter",fg='firebrick4', command=lambda: select_category("Harry Potter"))
harry_potter_button.pack(side="top", padx=50, pady=10, anchor="center",fill='x')

mythology_button = tk.Button(root, text="Mythology", fg ='goldenrod4',command=lambda: select_category("Mythology"))
mythology_button.pack(side="top", anchor = "center", padx=50, pady=10 ,fill='x')

anime_button = tk.Button(root, text="Anime", fg = 'DarkOrchid4',command=lambda: select_category("Anime"))
anime_button.pack(side="top", anchor = "center", padx=50, pady=10 ,fill='x')

gaming_button = tk.Button(root, text="Gaming", fg='brown', command=lambda: select_category("Gaming"))
gaming_button.pack(side="top", anchor = "center", padx=50, pady=10 ,fill='x')

science_button = tk.Button(root, text="Science", fg = "forest green", command=lambda: select_category("Science"))
science_button.pack(side="top", anchor = "center", padx=50, pady=10 ,fill='x')

question_label = tk.Label(root, text="",bg="turquoise1", font=("Times New Roman", 14))
question_label.pack(side="top", padx=30, pady=30 ,fill='x')

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", anchor = "w", padx=10, pady=10)

option_buttons = []

easy_button = tk.Button(root, text="Easy", fg ="green", command=lambda: select_difficulty("Easy"))
easy_button.pack(side="top",padx=50, pady=10, anchor = "center")

medium_button = tk.Button(root, text="Medium",fg ="blue", command=lambda: select_difficulty("Medium"))
medium_button.pack(side="top", anchor = "center", padx=50, pady=10)

hard_button = tk.Button(root, text="Hard",fg ="red", command=lambda: select_difficulty("Hard"))
hard_button.pack(side="top", anchor = "center", padx=50, pady=10)

hide_difficulty_buttons()

root.mainloop()
