import re

import renpy.exports as renpy
from renpy.python import RevertableObject, RevertableDict, RevertableSet
from renpy.character import ADVCharacter
from renpy.display.layout import DynamicDisplayable

from body import all_expressions
from body_data import bodies

def parse_display(display):
    # Split into attribs based on camelcase
    attribs = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', display).lower().split(' ')
    return attribs[0], tuple(attribs[1:])

# A displayable that will display the proper character graphics based on their
# body at the time of showing the character
class PersonDisplayable(renpy.Displayable):

    def __init__(self, person_name, expr, **kwargs):
        super(PersonDisplayable, self).__init__(**kwargs)
        self.person_name = person_name
        self.expr = expr
        self.current_body = None
        self.current_attribs = None

    def per_interact(self):
        renpy.display.render.redraw(self, 0)

    def render(self, width, height, st, at):
        # Ensure we have the current display parsed
        if st == 0.0 or at == 0.0 or self.current_body is None:
            person = getattr(renpy.store, self.person_name)
            self.current_body, current_attribs = parse_display(person.display)
            self.current_attribs = frozenset(current_attribs + self.expr)

        # Get the correct image based on current_body + current_attribs
        img = bodies[self.current_body].images.get(self.current_attribs)
        if not img:
            print "Missing image for body {0}".format(self.current_body)
            img = bodies[self.current_body].images[frozenset(('1',))]

        # Render and return render
        render = renpy.Render(*img.size)
        render.blit(renpy.load_image(img), (0, 0))
        return render

    def visit(self):
        return []

    # Don't preserve current body and current attributes when saving,
    # and make sure to redraw the displayable when loading a game
    nosave = ['current_body', 'current_attribs']

    def after_setstate(self):
        self.current_body = None
        self.current_attribs = None
        renpy.display.render.redraw(self, 0)

class CharInfo:

    def __init__(self, body_name, display_name):
        self.body_name = body_name
        self.display_name = display_name

    def define_images(self, person_name):
        # Create dynamic displayables for all expressions for this character
        for expr in all_expressions:
            renpy.image((self.body_name + 'd',) + expr, PersonDisplayable(person_name, expr))


class Person(RevertableObject, ADVCharacter):

    def __init__(self, charinfo, **kvargs):
        ADVCharacter.__init__(self, charinfo.display_name, renpy.store.adv, show_two_window=True, **kvargs)
        self.who_args = RevertableDict(self.who_args)
        self.default_body = charinfo.body_name
        self.display = charinfo.body_name

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, value):
        self._display = value
        body = bodies.get(parse_display(value)[0])
        self.who_args['color'] = '#ffffff' if body is None else body.color

    @property
    def color(self):
        return self.who_args['color']

    @color.setter
    def color(self, value):
        self.who_args['color'] = value
