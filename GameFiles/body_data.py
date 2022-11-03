import re
from body import Body, Mutation, Pose

bodies = {
    'alma': Body(
        color='#6b5c52',
        poses={
            (): {
                1: (346, 548),
            },
            ('full',): {
                1: (691, 2122),
            },
        },
    ),
    'amber': Body(
        color='#78dab6',
        poses={
            (): {
                1: (353, 620),
                2: (353, 620),
            },
            ('full',): {
                1: (706, 1323),
                2: (706, 1323),
            },
        },
    ),
    'anna': Body(
        color='#e49fbc',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (312, 569),
                2: (312, 569),
            },
            ('full',): {
                1: (590, 2202),
                2: (590, 2202),
            },
            ('ar',): {
                1: (314, 577),
                2: (314, 577),
            },
            ('ar', 'full',): {
                1: (627, 2199),
                2: (627, 2199),
            },
        },
    ),
    'aprika': Body(
        color='#c7d9f1',
        poses={
            (): {
                1: (326, 527),
                2: (326, 527),
            },
            ('full',): {
                1: (651, 1308),
                2: (651, 1308),
            },
        },
    ),
    'april': Body(
        color='#fff7dd',
        ignore_bases=["Preg", "Spreg"],
        poses={
            (): {
                1: (492, 536),
                2: (492, 536),
            },
            ('full',): {
                1: (1581, 2115),
                2: (1581, 2115),
            },
            ('male',): {
                1: (379, 543),
            },
            ('male', 'full',): {
                1: (505, 892),
            },
        },
        mutations={
            'br': Mutation(
                group='breast',
                depth=1,
            ),
            'glasses': Mutation(
                group='face',
            )
        },
    ),
    'arelia': Body(
        color='#7c584c',
        poses={
            (): {
                1: (385, 542),
                2: (385, 542),
            },
            ('full',): {
                1: (981, 2111),
                2: (981, 2111),
            },
        },
    ),
    'aurora': Body(
        color='#f8da76',
        poses={
            (): {
                1: (273, 878),
            },
            ('full',): {
                1: (364, 1170),
            },
        },
    ),
    'ashley': Body(
        color='#ffe9e4',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (375, 532),
                2: (375, 532),
            },
            ('full',): {
                1: (1508, 2113),
                2: (1508, 2113),
            },
            ('male',): {
                1: (307, 560),
            },
            ('male', 'full'): {
                1: (613, 1370),
            },
        },
    ),
    'betty': Body(
        color='#745b9f',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (452, 530),
                2: (452, 530),
            },
            ('full',): {
                1: (904, 2072),
                2: (904, 2072),
            },
        },
        mutations={
            'acne': Mutation(
                group='face',
                depth=1,
            ),
            'macne': Mutation(
                group='face',
                depth=1,
            )
        },
    ),
    'candice': Body(
        color='#c8d2ee',
        poses={
            (): {
                1: (336, 570),
                2: (336, 570),
            },
            ('full',): {
                1: (837, 2169),
                2: (837, 2169),
            },
        },
    ),
    'cards': Body(
        color='#c8d2ee',
        poses={
            (): {
                1: (500, 250),
                2: (500, 250),
                3: (500, 250),
                4: (500, 250),
                5: (500, 250),
                6: (500, 250),
                7: (500, 250),
                8: (500, 250),
                9: (500, 250),
                10: (500, 250),
            },
        },
    ),
    'cassandra': Body(
        color='#d4eaf7',
        poses={
            (): {
                1: (327, 545),
            },
            ('full',): {
                1: (653, 2194),
            },
        },
        mutations={
            'mind': Mutation(
                group='eyes',
                depth=1,
            )
        },
    ),
    'chastity': Body(
        color='#c83245',
        poses={
            (): {
                1: (385, 593),
                2: (385, 593),
            },
            ('full',): {
                1: (770, 2167),
                2: (770, 2167),
            },
        },
        ignore_bases=["Preg", "PBDSM"],
        mutations={
            'hairdown': Mutation(
                group='hair',
            ),
            'hairup': Mutation(
                group='hair',
            ),
            'reg': Mutation(
                group='body',
            ),
            'stretch': Mutation(
                group='body',
            ),
        },
    ),
    'chris': Body(
        color='#8b4b50',
        poses={
            (): {
                1: (342, 421),
                2: (342, 421),
                3: (342, 421),
            },
            ('full',): {
                1: (798, 1988),
                2: (798, 1988),
                3: (798, 1988),
            },
        },
        mutations={
            'hair': Mutation(
                name='',
                depth=2,
            )
        },
    ),
    'ciel': Body(
        color='#623d3d',
        poses={
            (): {
                1: (421, 564),
                2: (421, 564),
                3: (421, 564),
            },
            ('full',): {
                1: (841, 2195),
                2: (841, 2195),
                3: (841, 2195),
            },
        },
        ignore_bases=["Swim"],
        mutations={
            'hair': Mutation(
                group='hair',
            ),
            'hairblue': Mutation(
                group='hair',
            ),
            'haireliza': Mutation(
                group='hair',
            ),
            'hairjenna': Mutation(
                group='hair',
            ),
            'hairheather': Mutation(
                group='hair',
            ),
            'glasses': Mutation(
                group='face',
            ),
            'headband': Mutation(
                group='headband',
            )
        },
    ),
    'cindy': Body(
        color='#4b779a',
        poses={
            (): {
                1: (509, 543),
                2: (509, 543),
            },
            ('full',): {
                1: (1018, 2129),
                2: (1018, 2129),
            },
        },
        ignore_bases=["Preg"],
        mutations={
            'cig': Mutation(
                group='accessory',
            )
        },
    ),
    'dilbert': Body(
        color='#a69b6d',
        poses={
            (): {
                1: (335, 600),
            },
        },
    ),
    'donald': Body(
        color='#525c60',
        poses={
            (): {
                1: (382, 543),
            },
            ('girl',): {
                1: (382, 543),
            },
        },
    ),
    'eliza': Body(
        color='#ffdea4',
        poses={
            (): {
                1: (417, 497),
                2: (417, 497),
                3: (417, 497),
            },
            ('full',): {
                1: (834, 1444),
                2: (834, 1444),
                3: (834, 1444),
            },
        },
        ignore_mut=["cirlet", "circlet", "ears"],
        mutations={
            'short': Mutation(
                group='hair',
                below=True,
            ),
            'ponytail': Mutation(
                group='hair',
                below=True,
            ),
            'pigtails': Mutation(
                name='',
                group='hair',
                below=True,
            )
        },
    ),
    'erin': Body(
        color='#a188b6',
        poses={
            (): {
                1: (493, 534),
                2: (493, 534),
                3: (493, 534),
            },
            ('full',): {
                1: (986, 2087),
                2: (986, 2087),
                3: (986, 2087),
            },
        },
    ),
    'ermach': Body(
        color='#a188b6',
        poses={
            (): {
                1: (290, 507),
            },
            ('full',): {
                1: (580, 2151),
            },
        },
    ),
    'fair': Body(
        color='#5e2a14',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (326, 511),
                2: (326, 511),
            },
            ('full',): {
                1: (651, 2047),
                2: (651, 2047),
            },
        },
    ),
    'hillary': Body(
        color='#fdc363',
        poses={
            (): {
                1: (350, 459),
            },
        },
    ),
    'hoover': Body(
        color='#c8d2ee',
        poses={
            (): {
                1: (353, 570),
                2: (353, 570),
            },
            ('full',): {
                1: (706, 2131),
                2: (706, 2131),
            },
        },
    ),
    'hope': Body(
        color='#a5dca4',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (300, 549),
                2: (300, 549),
            },
            ('full',): {
                1: (599, 2055),
                2: (599, 2055),
            },
        },
    ),
    'howard': Body(
        color='#b8b1bd',
        poses={
            (): {
                1: (339, 590),
                2: (339, 590),
            },
            ('full',): {
                1: (678, 2125),
                2: (678, 2125),
            },
        },
    ),
    'iida': Body(
        color='#bf7e74',
        poses={
            (): {
                1: (292, 495),
                2: (292, 495),
            },
            ('full',): {
                1: (583, 2086),
                2: (583, 2086),
            },
        },
    ),
    'jaina': Body(
        color='#defffb',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (267, 386),
                2: (267, 386),
            },
            ('full',): {
                1: (805, 1835),
                2: (805, 1835),
            },
        },
    ),
    'jenna': Body(
        color='#7a434b',
        poses={
            (): {
                1: (486, 581),
                2: (486, 581),
            },
            ('full',): {
                1: (1610, 2239),
                2: (1610, 2239),
            },
        },
        ignore_bases=["Preg"],
        mutations={
            'ponytail': Mutation(
                name='',
                group='hair',
                depth=1,
                below=True,
            ),
            'twintails': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'down': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'bob': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'headband': Mutation(
                group='headband',
                depth=1,
            ),
            'headband2': Mutation(
                group='headband',
                depth=1,
            )
        },
    ),
    'jennifer': Body(
        color='#ab9ec7',
        poses={
            (): {
                1: (296, 535),
            },
        },
    ),
    'jillian': Body(
        color='#babedb',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (437, 512),
                2: (437, 512),
            },
            ('full',): {
                1: (874, 1995),
                2: (874, 1995),
            },
        },
    ),
    'julie': Body(
        color='#d37777',
        poses={
            (): {
                1: (352, 489),
            },
            ('full',): {
                1: (748, 2116),
            },
        },
        mutations={
            'mind': Mutation(
                group='eyes',
                depth=1,
            ),
            'hat': Mutation(
                group='head',
                depth=1,
            ),
            'bandage': Mutation(
                group='head',
                depth=1,
            ),
            'cuts': Mutation(
                group='face',
                depth=1,
            ),
            'scar': Mutation(
                group='neck',
                depth=1,
            )
        },
    ),
    'kayla': Body(
        color='#fdb3c1',
        poses={
            (): {
                1: (347, 404),
            },
        },
    ),
    'karyn': Body(
        color='#8bd4a8',
        poses={
            (): {
                1: (293, 481),
                2: (293, 481),
                3: (293, 481),
            },
            ('full',): {
                1: (585, 1436),
                2: (585, 1436),
                3: (585, 1436),
            },
        },
    ),
    'kenichi': Body(
        color='#657296',
        poses={
            (): {
                1: (251, 480),
            },
        },
    ),
    'main': Body(
        color='#505cf1',
        poses={
            (): {
                1: (349, 542),
            },
            ('full',): {
                1: (698, 1524),
            },
        },
        mutations={
            'tie': Mutation(
                group='tie',
                depth=1,
            ),
            'swt': Mutation(
                group='swt',
                depth=2,
            ),
            'hair': Mutation(
                group='hair',
                depth=1,
            ),
            'hairred': Mutation(
                group='hair',
                depth=1,
            )
        },
    ),
    'martha': Body(
        color='#f5dcb3',
        poses={
            (): {
                1: (392, 513),
                2: (392, 513),
                3: (392, 513),
            },
            ('full',): {
                1: (784, 2119),
                2: (784, 2119),
                3: (784, 2119),
            },
        },
    ),
    'megan': Body(
        color='#e5ddc7',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (369, 513),
                2: (369, 513),
            },
            ('full',): {
                1: (738, 1961),
                2: (738, 1961),
            },
        },
    ),
    'megumi': Body(
        color='#5c90cc',
        poses={
            (): {
                1: (524, 535),
                2: (524, 535),
            },
            ('full',): {
                1: (1047, 2180),
                2: (1047, 2180),
            },
        },
        mutations={
            'mind': Mutation(
                group='eyes',
                depth=1,
            ),
            'empty': Mutation(
                group='eyes',
                depth=1,
            )
        },
    ),
    'melina': Body(
        color='#567171',
        poses={
            (): {
                1: (529, 601),
                2: (529, 601),
            },
            ('full',): {
                1: (1057, 2214),
                2: (1057, 2214),
            },
        },
        ignore_bases=["Preg", "preg"],
        ignore_mut=["melbunnyband"],
        mutations={
            'melheadband': Mutation(
                group='head',
                depth=1,
            ),
        },
    ),
    'melody': Body(
        color='#d7aa84',
        poses={
            (): {
                1: (394, 502),
                2: (394, 502),
            },
            ('full',): {
                1: (788, 1934),
                2: (788, 1934),
            },
        },
        mutations={
            'freckface': Mutation(
                group='face',
                depth=1,
            ),
            'freckbody': Mutation(
                group='freckles',
                depth=1,
            )
        },
    ),
    'michelle': Body(
        color='#928ba6',
        poses={
            (): {
                1: (294, 518),
                2: (294, 518),
                3: (294, 518),
            },
            ('full',): {
                1: (587, 1454),
                2: (587, 1454),
                3: (587, 1454),
            },
        },
    ),
    'mika': Body(
        color='#3287cb',
        poses={
            (): {
                1: (452, 546),
                2: (452, 546),
            },
            ('full',): {
                1: (903, 2201),
                2: (903, 2201),
            },
            ('ap',): {
                1: (343, 498),
                2: (343, 498),
            },
            ('ap', 'full',): {
                1: (686, 2109),
                2: (686, 2109),
            },
            ('male',): {
                1: (242, 528),
            },
            ('male', 'full',): {
                1: (483, 2187),
            },
        },
        ignore_bases=["_AP_", "Preg"],
        mutations={
            'ponytail': Mutation(
                name='',
                group='hair',
                depth=1,
                below=True,
            ),
            'down': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'twintail': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'lowtail': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'backtail': Mutation(
                group='hair',
                depth=1,
                below=True,
            ),
            'oil': Mutation(
                group='face',
                depth=1,
            ),
            'robefront': Mutation(
                group='face',
                depth=1,
            )
        },
    ),
    'mike': Body(
        color='#a86c62',
        poses={
            (): {
                1: (418, 622),
            },
            ('full',): {
                1: (688, 2115),
            },
        },
    ),
    'miya': Body(
        color='#578de7',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (384, 549),
                2: (384, 549),
            },
            ('full',): {
                1: (768, 2106),
                2: (768, 2106),
            },
        },
    ),
    'mori': Body(
        color='#726177',
        poses={
            (): {
                1: (540, 1763),
            },
        },
    ),
    'fwoman': Body(
        color='#578de7',
        poses={
            (): {
                1: (345, 548),
            },
        },
    ),
    'mother': Body(
        color='#c9373f',
        poses={
            (): {
                1: (436, 517),
                2: (436, 517),
            },
            ('full',): {
                1: (872, 2154),
                2: (872, 2154),
            },
        },
        ignore_bases=["Preg"],
        mutations={
            'hand': Mutation(
                group='hand',
                depth=1,
            ),
            'board': Mutation(
                group='hand',
                depth=1,
            )
        },
    ),
    'nelson': Body(
        color='#91766e',
        poses={
            (): {
                1: (443, 637),
            },
        },
    ),
    'nick': Body(
        color='#595b60',
        poses={
            (): {
                1: (321, 644),
            },
            ('full',): {
                1: (357, 938),
            },
        },
    ),
    'nicole': Body(
        color='#546e9e',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (404, 609),
                2: (404, 609),
            },
            ('full',): {
                1: (978, 2211),
                2: (978, 2211),
            },
        },
    ),
    'nurse': Body(
        color='#a38e4a',
        poses={
            (): {
                1: (413, 423),
                2: (413, 423),
                3: (413, 423),
            },
            ('full',): {
                1: (825, 1424),
                2: (825, 1424),
                3: (825, 1424),
            },
        },
    ),
    'olivian': Body(
        color='#c8ae98',
        poses={
            (): {
                1: (355, 533),
                2: (355, 533),
            },
            ('full',): {
                1: (709, 2088),
                2: (709, 2088),
            },
        },
    ),
    'peter': Body(
        color='#987747',
        poses={
            (): {
                1: (303, 566),
                2: (303, 566),
            },
            ('full',): {
                1: (605, 2250),
                2: (605, 2250),
            },
        },
    ),
    'reina': Body(
        color='#ff9ab0',
        ignore_bases=["Preg", "preg"],
        poses={
            (): {
                1: (330, 523),
                2: (330, 523),
            },
            ('full',): {
                1: (620, 2057),
                2: (620, 2057),
            },
        },
    ),
    'rosa': Body(
        color='#ac837c',
        poses={
            (): {
                1: (374, 1725),
            },
        },
    ),
    'ruby': Body(
        color='#ff9e5d',
        poses={
            (): {
                1: (390, 528),
                2: (390, 528),
            },
            ('full',): {
                1: (779, 2050),
                2: (779, 2050),
            },
        },
    ),
    'sadiya': Body(
        color='#968775',
        poses={
            (): {
                1: (353, 933),
            },
            ('full',): {
                1: (470, 1244),
            },
        },
    ),
    'sakajou': Body(
        color='#817586',
        poses={
            (): {
                1: (359, 440),
                2: (441, 423),
            },
        },
    ),
    'scarlet': Body(
        color='#be3166',
        ignore_bases=["Preg"],
        poses={
            (): {
                1: (407, 515),
                2: (407, 515),
            },
            ('full',): {
                1: (814, 2093),
                2: (814, 2093),
            },
        },
    ),
    'sean': Body(
        color='#cbad77',
        poses={
            (): {
                1: (287, 634),
            },
            ('ar',): {
                1: (320, 617),
            },
        },
    ),
    'shreya': Body(
        color='#dad0c5',
        poses={
            (): {
                1: (464, 511),
                2: (464, 511),
            },
            ('full',): {
                1: (1113, 2122),
                2: (1113, 2122),
            },
        },
    ),
    'silease': Body(
        color='#f18759',
        poses={
            (): {
                1: (456, 432),
                2: (456, 432),
            },
            ('full',): {
                1: (911, 1916),
                2: (911, 1916),
            },
        },
    ),
    'taylor': Body(
        color='#c34e4e',
        poses={
            (): {
                1: (317, 536),
            },
            ('full',): {
                1: (373, 1196),
            },
        },
        mutations={
            'hair': Mutation(
                name='',
                group='hair',
                depth=1,
            )
        },
    ),
    'tessa': Body(
        color='#ecd194',
        poses={
            (): {
                1: (504, 1734),
            },
        },
    ),
    'test': Body(
        color='#798773',
        poses={
            (): {
                1: (468, 512),
            },
            ('bunny',): {
                1: (468, 591),
            },
        },
    ),
    'tim': Body(
        color='#798773',
        poses={
            (): {
                1: (260, 480),
            },
            ('full',): {
                1: (520, 1854),
            },
        },
    ),
    'tracy': Body(
        color='#f1d0a1',
        poses={
            (): {
                1: (498, 941),
            },
            ('full',): {
                1: (664, 1255),
            },
        },
    ),
    'trista': Body(
        color='#d5a479',
        poses={
            (): {
                1: (308, 499),
                2: (308, 499),
            },
            ('full',): {
                1: (616, 2079),
                2: (616, 2079),
            },
        },
    ),
    'tristen': Body(
        color='#cfa985',
        poses={
            (): {
                1: (529, 634),
                2: (529, 634),
            },
            ('full',): {
                1: (1058, 1440),
                2: (1058, 1440),
            },
        },
    ),
    'valerie': Body(
        color='#a37da4',
        poses={
            (): {
                1: (487, 1567),
            },
        },
    ),
    'vanessa': Body(
        color='#fdafb1',
        poses={
            (): {
                1: (400, 468),
                2: (400, 468),
                3: (400, 468),
            },
            ('full',): {
                1: (800, 1394),
                2: (800, 1394),
                3: (800, 1394),
            },
        },
    ),
    'will': Body(
        color='#d5c9c2',
        poses={
            (): {
                1: (321, 487),
            },
        },
    ),
    'waitress': Body(
        color='#e65fac',
        poses={
            (): {
                1: (293, 574),
            },
        },
    ),
    'yukina': Body(
        color='#8d918c',
        poses={
            (): {
                1: (313, 513),
                2: (313, 513),
            },
            ('full',): {
                1: (625, 2076),
                2: (625, 2076),
            },
        },
    ),
    'zoey': Body(
        color='#eccf9a',
        poses={
            (): {
                1: (263, 570),
                2: (263, 570),
            },
            ('full',): {
                1: (526, 1288),
                2: (526, 1288),
            },
        },
    ),
}

FOLD = (
    (frozenset(('naked', 'bra', 'panties')), 'under'),
    (frozenset(('naked', 'bra')), 'bra'),
    (frozenset(('naked', 'panties')), 'panties'),
    (frozenset(('naked', 'skirt')), 'skirt'),
    ('punk', None),
)

def add_file(filename):
    # Extract information from the filename
    m = re.match('^.*/(.+)\\.png$', filename.lower())
    if not m:
        return

    basename = m.groups()[0]

    # Split filename data
    fields = basename.split('_')
    body_name = fields.pop(0)

    # Add to body object
    if body_name not in bodies:
        return
    bodies[body_name].add_image(fields, filename)

## ACTUAL code

def init():
    for body_name, body in bodies.items():
        body.define_images(body_name, FOLD)

# For TESTING / Fast Loading
# def init():
#     for body_name, body in bodies.items():
#         if body_name in ['main', 'candice','mika','ashley','april', 'megumi', 'karyn']:
#             body.define_images(body_name, FOLD)
