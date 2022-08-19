import renpy.exports as renpy
from renpy.character import Character

from char import CharInfo, Person
from body_data import bodies

characters = {
    # Named characters
    'M': CharInfo('main', 'Calvin'),
    'e': CharInfo('eliza', 'Eliza'),
    'n': CharInfo('nicole', 'Nicole'),
    'm': CharInfo('mika', 'Mika'),
    'Mo': CharInfo('mother', 'Heather'),
    'N': CharInfo('nick', 'Nick'),
    'a': CharInfo('april', 'April'),
    'A': CharInfo('ashley', 'Ashley'),
    'An': CharInfo('anna', 'Anna'),
    'b': CharInfo('betty', 'Betty'),
    'C': CharInfo('chastity', 'Chastity'),
    'c': CharInfo('ciel', 'Ciel'),
    'Cin': CharInfo('cindy', 'Cindy'),
    'h': CharInfo('hope', 'Hope'),
    'j': CharInfo('jenna', 'Jenna'),
    'mel': CharInfo('melina', 'Melina'),
    'mic': CharInfo('michelle', 'Michelle'),
    'miya': CharInfo('miya', 'Miya'),
    'R': CharInfo('reina', 'Reina'),
    'I': CharInfo('iida', 'Iida'),
    'f': CharInfo('fair', 'Fair'),
    'ali': CharInfo('alice', 'Alice'),
    'em': CharInfo('emma', 'Emma'),
    't': CharInfo('tina', 'Tina'),
    'mi': CharInfo('mike', 'Michael'),
    'Se': CharInfo('sean', 'Sean'),
    'k': CharInfo('karyn', 'Karyn'),
    'v': CharInfo('vanessa', 'Vanessa'),
    'Di': CharInfo('dilbert', 'Dilbert'),
    'ja': CharInfo('jaina', 'Jaina'),
    'me': CharInfo('melody', 'Melody'),
    'ru': CharInfo('ruby', 'Ruby'),
    'Sh': CharInfo('shreya', 'Shreya'), ### Shreya Acharya
    'Sil': CharInfo('silease', 'Silease'),
    'tay': CharInfo('taylor', 'Taylor'),
    'tri': CharInfo('trista', 'Trista'),
    'tr': CharInfo('tristen', 'Tristen'), ### Erins' cousin
    'zo': CharInfo('zoey', 'Zoey'),
    'tim': CharInfo('tim', 'Tim'),
    'Pet': CharInfo('peter', 'Peter'),
    'meg': CharInfo('megan', 'Megan'),
    'megu': CharInfo('megumi', 'Megumi'),
    'How': CharInfo('howard', 'Howard'), ### Howard
    'fwom': CharInfo('fat woman', 'Fat Woman'), ## Random person
    'Sc': CharInfo('scarlet', 'Scarlet'), ## Scarlet Ryan (Heather's sister)

    'sad': CharInfo('sadiya', 'Sadiya'),
    'tra': CharInfo('tracy', 'Tracy'),
    'aur': CharInfo('aurora', 'Aurora'), 


    'test': CharInfo('test', 'Test'), ## Test bot


    'Ros': CharInfo('rosa', 'Rosa'), ## Rosa from famswap ending (Newtown Porn Actress)
    'Tes': CharInfo('tessa', 'Tessa'), ## Tessa from famswap ending (Newtown Porn Actress)
    'Val': CharInfo('valerie', 'Valerie'), ## Valerie from famswap ending (Newtown Porn Actress)
    'Mor': CharInfo('mori', 'Mori'), ## Mori from famswap ending (Newtown Porn Actress)

    'Ju': CharInfo('julie', 'Julie'), ### Julie (Police Officer 24y/o)
    'Cas': CharInfo('cassandra', 'Cassandra'), ### Cassandra (Julie's friend) (26 y/o)

    'cards': CharInfo('cards', 'Cards'), ## Board game cards

    ## Silboy 3 Want to be each other because they are in love with each others' girlfriend // is sick, runny nose
    ## Silboy 4 Want to be each other because they are in love with each others' girlfriend
    ## Silgirl 1&2 Want to be each other because they prefer each others' look


    # Unknown names at start


    'Ol': CharInfo('olivian', 'Olivian'), ### Christine Olivian, Christine's mother.
    'Wi': CharInfo('william', 'William'), ### William Olivian, Christine's father.
    'Ar': CharInfo('arelia', 'Woman'), ### Arelia Olivian
    'Can': CharInfo('candice', 'Woman'), ### Candice
    'Ho': CharInfo('hoover', 'Woman'), ### Candice Alt
    'Am': CharInfo('amber', 'Woman'), ### Amber, Candice's assistant
    'nur': CharInfo('nurse', 'Nurse'), ### The Nurse, also Candice's assistant
    'Nel': CharInfo('Large Man', 'Nelson'), ### Nelson, Candice's associate

    'ch': CharInfo('chris', 'Oddly Dressed Student'), ### Christine
    'ma': CharInfo('martha', 'Teacher'), ### Martha

    'er': CharInfo('erin', 'Student'), ### Erin
    'ermach': CharInfo('ermach', 'Student'), ### Merger of Erin/Martha/Christine
    'hi': CharInfo('hillary', 'Fat Student'), ### Hillary
    'waitress': CharInfo('waitress', 'Waitress'), ### Unnamed waitress
    'ka': CharInfo('kayla', 'Student'), ### Kayla, one of Erin's loyal followers
    'je': CharInfo('jennifer', 'Student'), ### Jennifer, one of Erin's loyal followers
    'Do': CharInfo('donald', 'Teacher'), ### Donald Barron, one of the teachers at Eliza's school
    'ji': CharInfo('jillian', 'Cute Girl'), ### Jillian Maxwell (Christine's housekeeper)
    'Al': CharInfo('alma', 'Woman'), ### Erins' mother: Alma, #a78f80

    'Yu': CharInfo('yukina', 'Yukina'), ### Nicole's' mother: Yukina ::: Girlfriend of Dilbert

    #'Cha': CharInfo('charlotte', 'Charlotte'), ### Timothy's' mother: Charlotte, #
    #'Ant': CharInfo('anthony', 'Anthony'), ### Timothy's' father: Anthony, #



    # No sprites for these characters

    'May': CharInfo('may', 'May'), ### April's Mother
    'Luc': CharInfo('lucas', 'Lucas'), ### April's Father



    'Ver': CharInfo('veronica', 'Veronica'), ### Nick's Mother
    'Mat': CharInfo('mathew', 'Mathew'), ### Nick's Father

    'Te': CharInfo('teacher', 'Teacher'), ### Teacher woman in class #4 of Eliza day 1, #978aa6
    'Tr': CharInfo('tristen', 'Tristen'), ### Erins' brother: Tristen, #a78f80
    'De': CharInfo('deater', 'Deater'), ### Erins' father: Deater, #a78f80
    'nur2': CharInfo('nurse2', 'Nurse'), ### Nurse in Eliza's route, #a38e4a
    'misc1': CharInfo('teacher', 'Teacher'), ### Used for random people
    'misc2': CharInfo('teacher', 'Teacher'), ### Used for random people
    'misc3': CharInfo('teacher', 'Teacher'), ### Used for random people
    'misc4': CharInfo('teacher', 'Teacher'), ### Used for random people
    'misc5': CharInfo('teacher', 'Teacher'), ### Used for random people
    'misc6': CharInfo('teacher', 'Teacher'), ### Used for random people

    'Chloe': CharInfo('chloe', 'Chloe'), ### Green-haired girl in Nicole's archery CG

    'dal': CharInfo('daliah', 'Voice'), ### Daliah, for that special arc
    'daw': CharInfo('dawiah', 'Sister'), ### Dawiah, for that special arc
    'yume': CharInfo('yume', 'Beautiful Woman'), ### Yume, for that special arc
    'nat': CharInfo('natsuki', 'Stern Woman'), ### Natsuki, for that special arc
    'cel': CharInfo('celia', 'Cute Girl'), ### Celia, for that special arc
    'cro': CharInfo('crown', 'Crown'), ### Crown, for that special arc
}

def init():
    dummychar = Character()
    for char_name, char_info in characters.items():
        char_info.define_images(char_name)
        setattr(renpy.store, char_name, dummychar)

def define_chars():
    for char_name, char_info in characters.items():
        setattr(renpy.store, char_name, Person(char_info))

        color = bodies[char_info.body_name].color if char_info.body_name in bodies else '#ffffff'
        setattr(renpy.store, char_name + '_nvl', Character(char_info.display_name, color=color, kind=renpy.store.nvl))
        setattr(renpy.store, char_name + '_tho', Character(char_info.display_name + "'s thoughts", color=color, what_style='tho_font', what_prefix='{i}', what_suffix='{/i}'))
