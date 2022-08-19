init -10 python:
    import re, itertools
    from body_data import add_file as add_body_file, init as init_bodies
    from char_data import init as init_chars, define_chars

    # This function will run a countdown of the given length. It will
    # be white until 5 seconds are left, and then red until 0 seconds are
    # left, and then will blink 0.0 when time is up.
    def countdown(st, at, length=0.0):

        remaining = length - st

        if remaining > 3.0:
            return Text('%.1f' % remaining, color='#fff', size=72), .1
        elif remaining > 0.0:
            return Text('%.1f' % remaining, color='#f00', size=72), .1
        else:
            return anim.Blink(Text('0.0', color='#f00', size=72), on=0.0, off=0.0, rise=0.2, set=0.2, high=0.0, low=1.0), None

init -10 python hide:
    def sanitize_filename(fn):
        return re.sub('(^.*/|\.(png|jpg)$|_0*|_)', '', fn)

    # Load images
    for filename in renpy.list_files(True):
        filename_lower = filename.lower()
        if filename_lower.startswith('backgrounds/'):
            renpy.image('bg ' + sanitize_filename(filename_lower), filename)
        elif filename_lower.startswith('effects/'):
            renpy.image(sanitize_filename(filename_lower), filename)
        elif filename_lower.startswith('characters/'):
            if filename_lower.startswith('characters/misc/'):
                renpy.image(sanitize_filename(filename_lower), filename)
            else:
                add_body_file(filename)
        elif filename_lower.startswith('cg/'):
            name = ['cg']
            fields = re.sub('(^.*/|\.(png|jpg)$)', '', filename_lower).split('_')

            # Un-zero pad the digits
            if fields[-1].isdigit():
                fields[-1] = str(int(fields[-1]))

            # Remove type and add to cg tag (a bit hacky)
            if len(fields) > 3 or fields[-1] == 'base':
                name[0] += fields.pop(2)

            # Define
            name.extend(fields)
            renpy.image(tuple(name), filename)

    # Initialize bodies and characters
    init_bodies()
    init_chars()

# NVL Adjustments
init python:

    style.nvl_window.background = Frame("CG/Items/NVL_Background_001.png", 0, 0)

    style.nvl_window.top_padding = 55
    style.nvl_window.bottom_padding = 200
    style.nvl_window.left_padding = 230
    style.nvl_window.right_padding = 230

    style.nvl_window.top_margin = 0
    style.nvl_window.bottom_margin = 0
    style.nvl_window.left_margin = 0
    style.nvl_window.right_margin = 0

    style.nvl_vbox.box_spacing = 10
    style.nvl_dialogue.size = 15
    style.nvl_dialogue.color = "#000000"

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
## Custom Font Styles
## Use Font tag {=bio_font} to use. {/bio_font} will end it's use.

init:    
    style bio_font is text:
        size 18
        font "Fonts/Furore.otf"
    style tho_font is text:
        size 22
        font "Fonts/Days.otf"
        
        

# Fixes Image Moving

define config.optimize_texture_bounds = False
    
# Misc BGs
image bg black = Solid('#000000')
image bg white = Solid('#ffffff')
image bg earth gray = im.Grayscale('Backgrounds/Earth.jpg')
image overlay = Solid('#000000')

# Misc characters
image mansilhouette = im.MatrixColor(
    'Characters/Howard/Howard_Base_001.png',
    im.matrix.tint(0, 0, 0)
)

# Transitions
define wipeleft2 = CropMove(3.0, 'wipeleft')
define wiperight2 = CropMove(3.0, 'wiperight')
define slowdissolve = Dissolve(2.0)
define slowdissolve = Dissolve(2.0)
define slowfade = Fade(1.0, 0, 1.0)

define fdis = Dissolve(2.0)
define edis = Dissolve(1.5)
define ddis = Dissolve(1.0)
define cdis = Dissolve(0.5)
define bdis = Dissolve(0.5)
define dis = Dissolve(0.25)

define tran_rot = ImageDissolve("Effects/Tran_Rotation.png", 1.0, 8)
define tran_clockwise = ImageDissolve("Effects/Tran_Clockwise.png", 0.5, 8)
define tran_counterclockwise = ImageDissolve("Effects/Tran_Counterclockwise.png", 0.5, 8)
define tran_cirin = ImageDissolve("Effects/Tran_Circlein.png", 1.0, 8) ## For going out of places ironically
define tran_cirout = ImageDissolve("Effects/Tran_Circleout.png", 1.0, 8) ## For going into places... ironically
define tran_mind = ImageDissolve("Effects/Tran_Mind.png", 1.0, 8)
define tran_bioin = ImageDissolve("Effects/Tran_Bio_In.png", 1.0, 8)
define tran_bioout = ImageDissolve("Effects/Tran_Bio_Out.png", 1.0, 8)

#### Transforms

## Movement

transform lef:
    xcenter 150
    yalign 1.0
    ypos 600
transform cen:
    xcenter 400
    yalign 1.0
    ypos 600    
transform rit:
    xcenter 650
    yalign 1.0
    ypos 600
    
transform lefo:
    xcenter -500
    yalign 1.0
    ypos 600
transform rito:
    xcenter 1300
    yalign 1.0
    ypos 600     

transform leff:
    xcenter 275
    yalign 1.0
    ypos 600
transform ritt:
    xcenter 525
    yalign 1.0
    ypos 600     
    
transform le:
    xpos 150
transform ce:
    xpos 400
transform ri:
    xpos 650
    
transform lee:
    xpos 275
transform rii:
    xpos 525    

transform leo:
    xpos -500
transform rio:
    xpos 1300
    
## Character Card Positions    
    
transform card_name:
    ypos 100
    xpos 600
transform card_age:
    ypos 250
    xpos 475    
transform card_voice:
    ypos 250
    xpos 600        
transform card_height:
    ypos 250
    xpos 725       
transform card_trait:
    ypos 335
    xpos 600          
transform card_char:
    xpos 200  

# Countdowns
image countdownlong:
    DynamicDisplayable(countdown, length=30.0)
    xalign 1.0 yalign 0.0
image countdownten:
    DynamicDisplayable(countdown, length=10.0)
    xalign 1.0 yalign 0.0
image countdown:
    DynamicDisplayable(countdown, length=5.0)
    xalign 1.0 yalign 0.0
image countdownsmall:
    DynamicDisplayable(countdown, length=1.0)
    xalign 1.0 yalign 0.0
    
# Particle effects
transform particle(d, delay, speed=1.0, around=(config.screen_width/2, config.screen_height/2), angle=0, radius=200):
    d
    pause delay
    subpixel True
    around around
    radius 0
    linear speed radius radius angle angle

init python:
    class ParticleBurst(renpy.Displayable):
        def __init__(self, displayable, interval=(0.02, 0.04), speed=(0.15, 0.3), around=(config.screen_width/2, config.screen_height/2), angle=(0, 360), radius=(50, 75), particles=None, mouse_sparkle_mode=False, **kwargs):
            """Creates a burst of displayable...
            
            @params:
            - displayable: Anything that can be shown in Ren'Py (expects a single displayable or a container of displayable to randomly draw from).
            - interval: Time between bursts in seconds (expects a tuple with two floats to get randoms between them).
            - speed: Speed of the particle (same rule as above).
            - angle: Area delimiter (expects a tuple with two integers to get randoms between them) with full circle burst by default. (0, 180) for example will limit the burst only upwards creating sort of a fountain.
            - radius: Distance delimiter (same rule as above).
            - around: Position of the displayable (expects a tuple with x/y integers). Burst will be focused around this position.
            - particles: Amount of particle to go through, endless by default.
            - mouse_sparkle_mode: Focuses the burst around a mouse poiner overriding "around" property.
            
            This is far better customizable than the original ParticleBurst and is much easier to expand further if an required..
            """
            super(ParticleBurst, self).__init__(**kwargs)
            self.d = [renpy.easy.displayable(d) for d in displayable] if isinstance(displayable, (set, list, tuple)) else [renpy.easy.displayable(displayable)]
            self.interval = interval
            self.speed = speed
            self.around = around
            self.angle = angle
            self.radius = radius
            self.particles = particles
            self.msm = mouse_sparkle_mode
        
        def render(self, width, height, st, at):
                
            rp = store.renpy
                
            if not st:
                self.next = 0
                self.particle = 0
                self.shown = {}
                
            render = rp.Render(width, height)
            
            if not (self.particles and self.particle >= self.particles) and self.next <= st:
                speed = rp.random.uniform(self.speed[0], self.speed[1])
                angle = rp.random.randrange(self.angle[0], self.angle[1])
                radius = rp.random.randrange(self.radius[0], self.radius[1])
                if not self.msm:
                    self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, self.around, angle, radius)
                else:
                    self.shown[st + speed] = particle(rp.random.choice(self.d), st, speed, rp.get_mouse_pos(), angle, radius)
                self.next = st + rp.random.uniform(self.interval[0], self.interval[1])
                if self.particles:
                    self.particle = self.particle + 1
            
            for d in self.shown.keys():
                if d < st:
                    del(self.shown[d])
                else:
                    d = self.shown[d]
                    render.blit(d.render(width, height, st, at), (d.xpos, d.ypos))
                    
            rp.redraw(self, 0)
            
            return render

        def visit(self):
            return self.d

image clone_part = SnowBlossom("Effects/Clone_Flash.png", count=100, border=50, xspeed=(50, 50), yspeed=(300,400), start=0, fast=False, horizontal=False)
image boom = ParticleBurst([Solid("#%06x"%renpy.random.randint(0, 0xFFFFFF), xysize=(5, 5)) for i in range(50)], mouse_sparkle_mode=True)
image clone_burst = ParticleBurst("Effects/Clone_Flash.png", interval=(0.02, 0.04), speed=(0.15, 0.3), around=(config.screen_width/2, config.screen_height/2), angle=(0, 360), radius=(50, 75), particles=None)
    

# Special characters

define stud1 = Character('Student', color='#8dc9d2', show_two_window=True)
define stud2 = Character('Student', color='#34ea79', show_two_window=True)

define tiff = Character('Black-haired Girl', color='#7c6d80', show_two_window=True) ## Tiffany
define van = Character('Peach-haired Girl', color='#eca496', show_two_window=True) ## Vanellope
define jas = Character('Blue-haired Girl', color='#70a5eb', show_two_window=True) ## Jasmine
define curf = Character('Mrs. Curtain', color='#d4f3f9', show_two_window=True) ## Matilda Curtain; Megan's Mom
define curm = Character('Mr. Curtain', color='#d49825', show_two_window=True) ## Alvin Curtain; Megan's Father
define Ant = Character('Mr. Brightwell', color='#fbfd36', show_two_window=True) ## Anthony Brightwell; Timothy's Father
define Cha = Character('Mrs. Brightwell', color='#285311', show_two_window=True) ## Charlotte Brightwell; Timothy's Mother




init:
    $ tho = Character(_(''),
                         what_style='tho_font',
                         what_prefix='{i}',
                         what_suffix='{/i}')
      
    $ card = Character(_(''),
                         color="#c8ffc8",
                         window_left_margin=425,
                         window_right_margin=25,
                         window_bottom_margin=25,
                         window_top_margin=20,
                         window_yminimum=300) 
    
    $ red_card = Character(_(''),
                         color="#c8ffc8",
                         window_left_margin=425,
                         window_right_margin=25,
                         window_bottom_margin=25,
                         window_top_margin=20,
                         window_yminimum=300) 

# Dummy characters
define nv1 = Character()
define nv2 = Character()

# Misc CGs
image cg ashley robecut combine = im.Composite(
    (800, 600),
    (0, 0), 'CG/Ashley/Ashley_RobeCut_001.png',
    (0, 0), 'CG/Ashley/Ashley_RobeCut_002.png',
)

## JAINA MIND COLORS


image nurse ending:
    'cg nurse 11' with fade
    pause 5.0
    'cg nurse 12' with fade
    pause 5.0
    'cg nurse 13' with fade
    pause 5.0
    'cg nurse 14' with fade
    pause 5.0
    'cg nurse 15' with fade
    pause 5.0
    'cg nurse 16' with fade
    pause 5.0
    'cg nurse 17' with fade
    pause 5.0
    'cg nurse 18' with fade
    pause 5.0
    'cg nurse 19' with fade
    pause 5.0
    'cg nurse 20' with fade
     
# Main Menu    

image main_menu_back:
    "CG/Splash/Splash_001.png" with fdis
    pause 2.0
    "CG/Splash/Splash_002.png" with fdis
    pause 2.0
    "CG/Splash/Splash_001.png" with fdis
    pause 2.0
    "CG/Splash/Splash_002.png" with fdis
    pause 2.0
    "CG/Splash/Splash_001.png" with fdis
    pause 2.0
    "CG/Splash/Splash_002.png" with fdis
    pause 2.0
    "CG/Splash/Splash_000.png" with ddis
    pause 1.0
    repeat
    
image main_menu_back_char:
    "mika full 4 open2"
    pause 13.0
    block:
        choice:
            "alma full 10"
        choice:
            "amber full 10"
        choice:
            "anna full 10"
        choice:
            "april full 10"
        choice:
            "arelia full 10"
        choice:
            "ashley full 10"
        choice:
            "betty full macne 10"
        choice:
            "candice full 10"
        choice:
            "chastity full hairup reg 10"
        choice:
            "chris full 10"
        choice:
            "ciel full hair headband 10"
        choice:
            "cindy full 10"
        choice:
            "eliza full 10"
        choice:
            "erin full 10"
        choice:
            "fair full 10"
        choice:
            "hope full 10"
        choice:
            "howard full 10"
        choice:
            "iida full 10"
        choice:
            "jaina full 10"
        choice:
            "jenna full 10"
        choice:
            "jillian full 10"
        choice:
            "karyn full 10"
        choice:
            "martha full 10"
        choice:
            "megan full 10"
        choice:
            "megumi full 10"
        choice:
            "melina full 10"
        choice:
            "melody full 10"
        choice:
            "michelle full be1 10"
        choice:
            "mika full 10"
        choice:
            "mike full 10"
        choice:
            "miya full 10"
        choice:
            "mother full suit 10"
        choice:
            "nicole full 10"
        choice:
            "nurse full 10"
        choice:
            "olivian full 10"
        choice:
            "peter full 10"
        choice:
            "reina full 10"
        choice:
            "ruby full 10"
        choice:
            "shreya full fit 10"
        choice:
            "silease full 10"
        choice:
            "tim full 10"
        choice:
            "trista full 10"
        choice:
            "tristen full 10"
        choice:
            "vanessa full 10"
        choice:
            "yukina full 10"
        choice:
            "zoey full 10"
        pause 13.0
        repeat
            
    
  
## Splash
    
screen splash_001():
    frame:
        xalign 0.5 ypos 0
        text _("My Friend"):
            size 30
            outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]        
screen splash_002():
    frame:
        xalign 0.5 ypos 0
        text _("My Crush"):
            size 30
            outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]        
screen splash_003():
    frame:
        xalign 0.5 ypos 0
        text _("My Stupid Sisters"):
            size 30
            outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]        
screen splash_004():
    frame:
        xalign 0.5 ypos 0
        text _("Or the one person I thought might have a true interest in me..."):
            size 30
            outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]        
screen splash_005():
    frame:
        xalign 0.5 ypos 0
        text _("With the press of a button, I could be anyone!"):
            size 30
            outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]                                 
            
screen pending_001(path_name = "", author_note = ""):
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text _("{=bio_font}{size=+10}-This Path Is Pending Completion-{/size}{/bio_font}"):
                xalign 0.5
                outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]   
            text _("{=bio_font}{size=+5}{color=4579ef}[path_name]{/color}{/size}{/bio_font}"):
                xalign 0.5
                outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]       
            text _("{=bio_font}[author_note]{/bio_font}"):
                xalign 0.5   
                outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]       
screen ending_001(ending_name = "", author_note = ""):
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            text _("{=bio_font}{size=+10}-The End-{/size}{/bio_font}"):
                xalign 0.5
                outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]   
            text _("{=bio_font}{size=+5}{color=4579ef}[ending_name]{/color}{/size}{/bio_font}"):
                xalign 0.5
                outlines [ (absolute(3), "#000", absolute(0), absolute(0)) ]       
            text _("{=bio_font}[author_note]{/bio_font}"):
                xalign 0.5   
                outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]                  
            
# Character Bio Screen (old)

screen scr_1:
    frame:
        background Solid("#00000090")     # or use any semi-transparent image you like
        align (0.5, 0.2)
        
        side "c r":
            area (0, 0, 200, 300)

            viewport id "vp":
                draggable True

                vbox:
                    for i in range (20):
                        text "Line_[i]"

            vbar value YScrollValue("vp")
            bar value XScrollValue("vp")
            
            
           
## BIO SCREEN         
## Text is present/past tense, as if speaking to someone about it.
    

default bio_menu = "Yes" ## Determines if Bio Screen on main menu is being viewed or if it's from in-game. Causes you to lose access to history button.
default page = "main" ## What page will be displayed
default outfits_list = [""] ## Determines outfits which can be displayed. Leave a space after any named outfit like ["", "cas "]
default bio_mutate = "" ## Determines any character layer mutations which may be in effect, like headbands and accessories.
default profile_out = "" ## Is the outfit currently being displayed
            
screen bio_scr():
    modal True
    default zoom_var = 1.0
    default out_ind = 0
    default profile_ex = "1"
    default profile_ex_num = 0
    default profile_ex_list = ["1", "1 smile", "1 neutral", "1 empty", "2", "2 smile", "2 open", "3", "3 open", "3 open2", "3 irked", "3 irked2", "3 grit", "3 grin", "3 grin2", "4", "4 open", "4 open2", "4 smile", "5", "5 open", "5 open2", "5 smile", "5 smile2", "5 aroused", "5 aroused2", "6", "6 open", "6 open2", "6 smile", "6 smile2", "7", "7 open", "8", "8 open", "9", "9 closed", "10", "11", "12"]
    $ char_img = page + " full " + profile_out + bio_mutate + profile_ex
    
    frame:
        background "gui/Bio_View.jpg"
        xpos 0
        xpadding 0
        ypadding 0
        
        side "c":
             area (0, 0, 394, 600)
    
             viewport id "vp":
                 xinitial 0.5
                 yinitial 0.0
                 draggable True
                 
                 add char_img align (0.5, 1.0) zoom zoom_var
    
         
    frame:
        background "gui/Bio_Back.jpg"
        xpadding 15
        top_padding 42
        xpos 394
        
        side "r":
            area (0, 0, 390, 600)

            viewport id "vp2":
                draggable True

                vbox:
                    if page == "main":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Calvin Hintre"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'10"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n I have sharp features, which seem to only become more prominent with the lines of my glasses. Courtesy of my family genes, I am blessed with nice complexion, but, the female bias of those genes means I am a bit on the scrawny side for a guy."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n ---"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n I come from a rich family and am brother to two annoying sisters, and son to a mother who hardly knows I exist. I don't have any grand plans or hobbies, though I do enjoy people watching."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Everything, it's me!"
                        text "{=bio_font}- Hair color is naturally red."
                        
                    elif page == "anna":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Anna Greenfield"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 40"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'4"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A breathtaking woman, with one of the warmest faces I have ever seen. She always looked like she just walked off a catwalk with how nicely done she was. The makeup was there I am sure, but I could never tell."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n She was incredibly sweet and playful, much like I had always imagined a mother and proper beauty to be. Though Mika always told me she can be strict."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n Mika's mother. I had only met a couple times, and she left quite an impression on me, like I imagine she did with just about every other boy who has seen her. Beautiful as she was adorable, she and her equally attractive husband were a buzz about the country due to a random photo of them going viral under the title \"World's Best Looking Couple...\""    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Has a tendency to dip into a southern accent, but it seems intentional."
                        
                    elif page == "april":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} April Cox"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'5"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A pretty blond with fair, mildly sun damaged skin, catty eyes and pouty lips."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Blunt, tempermental, and often times smug. Unlike Mika, I have seen her be nice to people however."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n We have known each other since kindergarten. She was always very talkative and active in school, for better or for worse. Prior to my meeting with Mika, we were on good terms, with friendly smiles and greetings each morning -- perhaps maybe just a nod of recognizition."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Has an obsession with Mika for some reason."
                        text "{=bio_font}- Has a cat which follows her nearly everywhere she goes."
                        text "{=bio_font}- Loves animals of all kinds."
                        text "{=bio_font}- Used to be quite portly during elementary school."
                        text "{=bio_font}- Still has small hints of an Australian accent, but it has mostly faded over the years."
                        
                    elif page == "ashley":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Ashley Degard"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 18"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'9"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n An angel given flesh, with a warm complexion, inviting eyes, and a smile which took my voice away. Every part of her was perfect."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Innocent, kind, sweet, smart, but did have a habit of being very lecturing. She always meant well though."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n One of the four idols of the school and my personal favorite. I didn't know too much about her, other than that she was one of Mika's childhood friends. I also couldn't learn much about her, because despite being pretty experienced at talking with women, due to coming from an all female household, I could not form sentences to save my life when it came to her."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Plays the piano."
                        text "{=bio_font}- Likes to sing."
                        
                    elif page == "ciel":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Ciel Pire"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 26"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'11"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She was a pretty woman, with thin, fine features all to paralleled to her voice, which, when she was on the clock, was as proper as you would imagine a maid's to be."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n With others around, she was nice, obedient and tact. Around just me, she was cold, bitter and snarky."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My family's maid. Normally you would consider such a thing a novelty, a boon perhaps -- or maybe just a fetish, but once her employer was out of sight, she was just a normal woman. When she first took over to replace our former made Sylvia, I admit, I did not make a good first impression. I was bitter and annoyed, and that has resulted in us having a strained relationship since. I admit, even now, I have a hard time respecting someone who would wear something like that just to get a pay raise."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Started wearing the maid getup to get a pay raise (why Mom...?)."
                        text "{=bio_font}- Gets along really well with Eliza."
                        
                    elif page == "cindy":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Cindy Fable"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 25"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'8"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She was near identical to her sister in everyway, save for having {i}slightly{/i} rounder cheeks, hazel eyes, and a throaty, sort of boyish but somehow incredibly sexy voice."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n She was the rowdy, cheerful sort, with a tendency to poke fun at herself more than others. At other times, she seemed very docile and almost meek."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n Despite looking the part of a twin, Cindy was actually 4 years younger than her sister Reina. She was a long standing friend of my sister Jenna, and the only friend she ever had which was ever actually nice to me. I had/have a huge crush on her."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Works as a liquor sampler."
                        text "{=bio_font}- Childhood friend of Jenna."
                        text "{=bio_font}- Younger sister of Reina."
                        
                    elif page == "eliza":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Eliza Hintre"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 15"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'2"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n Contrary to the rest of my family, my little sister was the smaller, adorable member. All I could ever focus on was her bratty expressions and grating, whiny voice."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Bratty, whiny, talkative, dumb, incredibly superficial, vain and selfish. However, as her brother I also knew she was shy, insecure, lonely and sad..."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My annoying little sister. She was always using me as her talking post, almost exclusively because there was no one else. I felt bad for her, but I also couldn't stand her at times. It was difficult to balance it out. She always claimed to be super popular, and while I could believe that coming from her best friend Michelle, I knew it was a lie coming from her."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Attends an all girls highschool: Olivian's School for Girls."
                        text "{=bio_font}- Her voice gives me nightmares."
                        text "{=bio_font}- Her hobbies are whatever the popular girls are doing at the time. She's acquired quite a versatile skillset due to it."
                        text "{=bio_font}- Is obsessed with breasts because she doesn't have the same ridiculous size everyone else does."
                        
                    elif page == "mother":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Heather Hintre"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 43"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'8"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A natural redhead with a seductive face, with plump lips and cold blue eyes. Her figure was idolized by many."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Collected, cold, analytical, rational, but easily irritated. The only time I ever saw her get visibly angry to the point of shouting was with Jenna."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n A business woman, intellectual, employer, ex-wife, and mother in that order. Work was my mother's life; I only interacted with her through brief glimpses. For Eliza, it was even less. Jenna however was alive and aware through the golden period where my father was still around, and due to that, she is the only child who my mother talks to and treats like she is her child. Jenna told me mom used to smile then."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Owns a very successful advertisment company."
                        text "{=bio_font}- Is referenced often as a model for women to strive to be in magazines and online articles."
                        text "{=bio_font}- Tells me and others she left dad, but Jenna says it is the opposite."
                        text "{=bio_font}- Likes to go for runs."
                        text "{=bio_font}- Has a habit of rubbing her temples when irritated."
                        text "{=bio_font}- Has gone through a few surgeries to maintain her appearance."
                        
                    elif page == "iida":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Iida Hilard"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 35"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'5"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A sort of plain woman with round cheeks, a thin jaw, with matching lips. She was attractive enough, but she also wore a lot of makeup."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Emotional, lecturing, well-mannered, and strict, with a tendency to treat everyone like they were a child.."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My homeroom and history teacher. She was very strict about her lessons being taught in the same manner, and had a hard time taking questions from students. She also didn't like people interrupting her or trying to have fun at her expense. Very typical teacher. Still, she and I got along well enough."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Used to teach elementary school."
                        text "{=bio_font}- Has a halting way of speaking when explaining things, but speaks to people individually like they are five years old."
                        
                    elif page == "jenna":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Jenna Hintre"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 25"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 6'0"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A seductive face, with plump lips and cold lavender eyes. Her figure was idolized by many and she loved it. Though she has chicken thin legs in my opinion."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Egotistical, arrogant, smug, over-confident, self-righteous, with a quick temper. However, if I ever asked anyone about her, they always told me she was: confident, compassionate, caring, fun, and enjoyable."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My eldest sister and winner of the genetic lottery as she viewed it. She was a two-face -- praised by everyone except my mother and I. We carried a horrid relationship, what with her constant teasing and pranking of me while growing up. When she went to college, it was one of the best times of my life, but, sadly, all things come to an end, and in a horrible twist, she was now back in my life as my own math teacher."            
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Has a rocky relationship with our mother."
                        text "{=bio_font}- Is best friends with Cindy and Reina."
                        text "{=bio_font}- Loves to party and have fun, even at others' expense."
                        text "{=bio_font}- Has a habit of scrunching her hair when frustrated, and stroking it when trying to calm down."
                        
                    elif page == "megan":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Megan Curtain"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'4"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n Small, prim and neat, she always looked like she spent a lot of time on herself with every hair on her head placed just the way she liked it."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Insufferably cute, like a doll given life. Every aspect of her person, from mannerisms to her way of speaking was done to be as cute as possible. I suspected purposefully so. She seemed to love how cute she was."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n Vice president of the school council, one of the four school idols, and Megumi's right hand and polar opposite. Her overly \"cutesy\" mannerisms and doll-like appearance led her to be very sought after by clubs and such things. She had become like the mascot of the school, with many sports' teams trying to get her to attend their events as a good luck charm."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Is literally always with Megumi. Thus they are nicknamed M&M."
                        text "{=bio_font}- Tends to double-speak words to sound cute."
                        
                    elif page == "megumi":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Megumi Nalashibara"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'7"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She stood out in a crowd due to her long wavy hair and alert posture. Up close, she had very mature features, a noticeable dip in her bottom lip, and large cheeks which provided a childish look which contrasted well with her personality and other qualities."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Stoic, quick-witted, intelligent, athletic and seemingly very nice. She could be demanding and sometimes rude to people who disobeyed rules."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n President of the school council, and best female athlete. She was a wall in most instances, and with her deeper, matured voice and controlled way of speaking, it was hard not to view her as more woman than girl. I have heard others in the school take annoyance with her rather dutiful way of going about things -- even some teachers seemed to find her overbearing. However, as a person who was generally just a blur in the school, she was always really nice to me. As a result, I admit I was a bit smitten by her."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Is literally always with Megan. Thus they are nicknamed M&M."
                        text "{=bio_font}- Has a backwards way of speaking sometimes."
                        
                    elif page == "michelle":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Michelle Cloisewater"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 15"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'10"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n Entrancing defines her completely. Her entire body allured the eyes and sucked you in, from her thin shimmer lips to her curling eyes which seemed to roll you towards her, or her deep flavory voice -- she was a real life succubus. Her beauty was so alluring, I even caught my egomaniac sister Jenna whispering words of jealousy."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Critical, confident, stubborn, and always wondering if you were even worth her time."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n Eliza's best friend, and a person who did everything she could to ignore me. As a result, I knew little about her, other than the fact she looked like a model."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Attends an all girls highschool: Olivian's School for Girls."
                        
                    elif page == "mike":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Michael Geneway"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 18"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 6'2"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n Playboy eyes, an entrancing or endearing smile depending on his choice, and hair like a golden retriever -- that was our school heartthrob."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Confident, assertive, suave, smooth talking, a little manipulative, but seemingly fun and nice."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n While we had four female idols, there was one distinct male one, and it was him. I doubt there was one girl in the school who didn't have at least one fantasy with him. I didn't mind him too much, even if I was jealous -- just a bit. Seems his goal before the end of his senior year was to \"bang\" one of the teachers, and not just any, but my sister. Thus, why he even bothered ever interacting with me."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Has a sister."
                        text "{=bio_font}- Used to date Melina."
                        text "{=bio_font}- Wants to sleep with a teacher, specifically my sister."
                        
                    elif page == "mika":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Mika Greenfield"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'6"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n An incredibly thin, athletic girl with a cute face to go with her bubbly personality. Not the most attractive girl, but she fit her type well."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Energetic, sarcastically ambitious, self-depricating, playful, joke-loving, and otherwise booming with a positive glow."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n I'd only known her for about a month, but she was already the closest thing I had to a friend in that school. She was an odd girl, with interests in the paranormal and fantasy especially. She seemed like she wanted nothing more than for something bizarre to happen to her."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Has a sister named Miya."
                        text "{=bio_font}- Childhood friend and best friends with Ashley."
                        text "{=bio_font}- Childhood friends with Timothy."
                        text "{=bio_font}- Though she never stated it to me, she is clearly adopted as she isn't even the same race as her parents."
                        text "{=bio_font}- Likes Video Games, Anime, Science Fiction, Fantasy, and everything nerdy."
                        text "{=bio_font}- Goes for morning jogs."
                        text "{=bio_font}- Has some sort of beef with April."
                        
                    elif page == "nick":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Nick Laine"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 6'8"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n He was incredibly tall, a bit scary looking with slimey features, and a way of speaking which made him out to be a typical frat guy. Despite that, he was always pretty good at dealing with the ladies."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Laid back, confident, perverted, morally ambiguous, likes to give people shit, but was very intelligent."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My childhood friend. We used to be a lot closer than we are now, but when we ended up going to different schools due to financial differences, we sort of drifted apart. Despite looking and acting the way he does, he is actually quite a tech geek, or he was. Due to his family's \"addictive\" habits, all of which he himself has fallen into, he has become a lot different than he used to be. Still, the underlying friend I knew was still there, it was just buried under drugs, booze, and an addiction to sex and womanizing which started the first time he ever got laid."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Works at: Martin and Sherry's Diner."
                        text "{=bio_font}- Is poor."
                        text "{=bio_font}- Has fallen into bad habits."
                        text "{=bio_font}- Used to be into board games very heavily."
                        text "{=bio_font}- Loves flirting, parties and sex."
                        
                    elif page == "nicole":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Nicole Saginomiya"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 6'0"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A japanese beauty with intimidating features, and a constant gaze of superiority."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Egotistical? I don't know, she never spoke."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n One of the four idols of the school. This one was a bit more of a mystery than the others. She always had this expression like she was too good to even bother with you, and, quite aptly, didn't. She never spoke to anyone, or specifically, never spoke to {i}men{/i}. There was even a game put out by a few fellow male students to get footage or audio of her speaking. I would be lying if I said I wasn't at least a little curious about her, but she also kind of intimidated me."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        
                    elif page == "peter":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Peter Fable"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 33"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 6'0"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n He had a sly look to his smile, and the presentation of a salesman. Good looking guy though, of a similar type to my own, so I appreciated that."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Upbeat, expressive, playful and a bit aloof at times."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My science teacher. Despite looking the way he did, and unlike his wife, I rather enjoyed Peter's classes. He was fun, explosively expressive and tended to go the extra mile to prove his points for the class."       
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Husband to Reina."
                        text "{=bio_font}- One of the only male staff in school."
                        
                    elif page == "reina":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Reina Fable"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 29"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'8"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A kind, beautiful face, with soft features all too similar to Ashley's."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Malicious, stubborn, flirtatious and teasing."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My english teacher, elder sister to Cindy Fable, and one of Jenna's long-standing friends. Despite her alluring, inviting smile and friendly tone, she was just as venomous as my sister. My sister at least looked the part, Reina was a devil wearing an angel's skin. A lot of the teasing I underwent in my youth Jenna always told me were \"Reina's ideas.\" I wasn't sure how true that was, but I did hate how she acted like she was never mean to me."        
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Wife to Peter."
                        text "{=bio_font}- Elder sister to Cindy."
                        text "{=bio_font}- Friends with Jenna."
                        text "{=bio_font}- Has a popular blog channel online where she just talks about her day/thoughts."
                        text "{=bio_font}- Seems to enjoy teasing ms. Rowan just like the students."
                        
                    elif page == "ruby":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Ruby Barsotti"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 19"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'9"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n A traditional redhead with slightly aloof orange hair, fairer, mildly damaged skin and thin features."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Cheerful, empathetic, and playful."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My mother had made me rather frightened of my own natural red color, thus the blue, but Ruby here did the opposite, luring me back into the fire. Despite Nick's claims that she was somehow a \"classic redhead,\" I didn't see it. She was incredibly nice, sweet, and half the reason I went to that diner everyday."        
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Works as a waitress at: Martin and Sherry's Diner."
                        text "{=bio_font}- Dreams of being an actress and having her name known."
                        
                    elif page == "shreya":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Shreya Acharya"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 33"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'7"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She had a bold straight nose, thick hair, lips and eyes, and a body of similar description. Due to her darker skin, she stood out in the halls of our school."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Energetic, cheerful, ditsy, prideful, encouraging, nice and empathetic."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n She was the school's gym teacher, swim team coach, cheerleading coach, and just about every other activity she had time to participate in. Ms. Acharya was a fountain of energy and optimism, and more specifically, school optimism. It was a bit cringy at times, but she really was into the school pride thing. I often wondered if she had a life outside of school..."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        
                    elif page == "silease":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Silease Rowan"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 31"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 4'8"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n The tiniest little thing, with all of the features and qualities of a student below my own age. Perhaps if you looked close enough at her eyes you might be able to tell her age, but she looked like a child to me."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Quirky, timid, easily riled, and just adorable."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n My art teacher. She and I got along well enough, and she seemed to think I had talent in art. She genuinely seemed to want to help students get interested in it. However, her classes had a tendency to drift into nonsense as students just did not respect her at all."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Due to her size, is nicknamed \"Micro T\" in school. She hates it."
                        text "{=bio_font}- Posts informative tutorials/lectures online about her work. No one watches them."
                        text "{=bio_font}- Seems to have an issue with Reina."
                        
                    elif page == "tim":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Timothy Brightwell"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'4"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n Tiny, frail, weak, with a very boyish face."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Nice, timid, shy, insecure, meek and nerdy."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n I didn't know much about him on a personal level. The only thing that mattered was that he was Mika's childhood friend, and whether their relationship was more than that was something I was still trying to figure out."    
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Friends with Ashley and Mika."
                        text "{=bio_font}- Is into anime, video games and everything else Mika is into."
                        text "{=bio_font}- Mumbles a lot, and speaks as if someone was sucking the energy out of him."
                        
                    elif page == "trista":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Trista Garcia"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 36"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'6"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She was a very curvy woman, with a lot of motherly traits in her face."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Awkward, confusing, but cheerful, flirtatious, delightful and a bit quirky."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n Nick had told me once that Trista was the foundation of the diner, and had been there since it opened up. I felt that had to be true because she was part of the reason I came back each day. She was always cheery with the occassional spanish flare, a bit flirtatious, and otherwise just a nice person to watch."        
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Works as a waitress at: Martin and Sherry's Diner."
                        text "{=bio_font}- Has a spanish accent of some kind."
                        
                    elif page == "zoey":
                        text "{=bio_font}{color=7ce87d}{b}Name:{/b}{/color} Zoey Maxwell"
                        text "{=bio_font}{color=7ce87d}{b}Age:{/b}{/color} 17"
                        text "{=bio_font}{color=7ce87d}{b}Height:{/b}{/color} 5'9"
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Appearance:{/b}{/color}\n She had a very quirky face, with dusty tossed hair, and a very lanky figure."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Personality:{/b}{/color}\n Mischevious, playful and perhaps morally bankrupt."
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}Background:{/b}{/color}\n The resident school jokester would be the best description, I think. It was more that she just loved being a bit of a playful nuisance to everyone: Taking people's pencils, zipping around the room, ball tapping, skirt lifting -- she just loved to get up in everyone's personal space as much as possible."           
                        text "{=bio_font}{vspace=10}{color=7ce87d}{b}{u}Known Information:{/u}{/b}{/color}"
                        text "{=bio_font}- Seems to be friends with Nicole."
    hbox:
        yalign 0.0
        xalign 1.0
        
        if page == "main":
            pass
        elif bio_menu == "No":
            imagebutton auto "gui/Bio_Button_Mem_%s.png" action [Hide("bio_scr"), Call(page+"_memory")]
            
        imagebutton auto "gui/Bio_Button_Zoom_%s.png" action ToggleScreenVariable("zoom_var", 1.0, 0.5)
        imagebutton auto "gui/Bio_Button_Exup_%s.png" action If(profile_ex_num < (len(profile_ex_list)-1), SetScreenVariable("profile_ex_num", profile_ex_num+1), SetScreenVariable("profile_ex_num", 0)), SetScreenVariable("profile_ex", profile_ex_list[profile_ex_num])
        imagebutton auto "gui/Bio_Button_Exdown_%s.png" action If(profile_ex_num > 0, SetScreenVariable("profile_ex_num", profile_ex_num-1), SetScreenVariable("profile_ex_num", len(profile_ex_list)-1)), SetScreenVariable("profile_ex", profile_ex_list[profile_ex_num])
        #imagebutton auto "gui/Bio_Button_Outfit_%s.png" action If(out_ind < (len(outfits_list)-1), SetScreenVariable("out_ind", out_ind+1), SetScreenVariable("out_ind", 0)), SetVariable("profile_out", outfits_list[out_ind])
        imagebutton auto "gui/Bio_Button_Exit_%s.png" action Play("sound", "Sound/Device_Use.mp3"), Hide("bio_scr", transition=tran_bioout)
        
            
            
###

screen bio_button():
    frame:
        yalign 0.0 xalign 1.0
        vbox:
            imagebutton:
                idle Transform(page + "d" + " 1 neutral", crop_relative=True, crop=(0.33, 0.1, 0.33, 0.25), size=(100, 100))
                hover Transform(page + "d" + " 1 smile", crop_relative=True, crop=(0.33, 0.1, 0.33, 0.25), size=(100, 100))
                action Play("sound", "Sound/Device_Use.mp3"), Show("bio_scr", transition=tran_bioin)
                
            null height 5
            text "{=bio_font}{color=7ce87d}{b}{size=+5}Bio{/size}{/b}{/color}{/bio_font}" xalign 0.5
                

            
## Version Update Screen

screen version_scr():
    modal True
    frame:
        xalign 0.1
        yalign 0.3
        xysize(600, 550)
        right_padding 175
        vbox:
            xfill True
            yfill True
            text "{=bio_font}{color=4579ef}{b}{size=+20}{u}What's new!?{/u}{/size}{/color}{/bio_font}" xalign 0.5
            text "{=bio_font}- An extension to the \"Mass_Possession\" path. It is now playable until day 1 is over for... some of the options. Others will be their own thing."
            text "{=bio_font}- The bio screen is still a work in progress, but you can see hints of it with the new character introduction screens. Those are also a work in progress, so ignore the bad looking buttons that lead to them."
            text "{=bio_font}- I re-added my quips at the end of pending or ended routes, cause people wanted them back."
            text "{=bio_font}- I added in path names (if there is one) at the end of a path."
            text "{=bio_font}- A small but complicated update. Hopefully the next one goes a little faster. A simpler path to work on for me for sure... phew."
    add "megumi full 1 smile":
        xzoom -1
        xcenter 700
        ypos 0
        zoom 0.75
    textbutton "{=bio_font}{size=+10}{color=ffffff}Exit{/size}{/color}{/bio_font}" action Play("sound", "Sound/Device_Use.mp3"), Hide("version_scr", transition=tran_bioout):
        xalign 1.0 yalign 0.0    
        
screen version_button():
    frame:
        yalign 0.0 xalign 1.0
        vbox:
            textbutton "{=bio_font}{color=ffffff}{b}What's new!?{/color}{/bio_font}" action Play("sound", "Sound/Device_Use.mp3"), Show("version_scr", transition=tran_bioin)
    
# Entry point

label start:
    $ define_chars()
    $ tim.name = "Timothy"
    $ c.display = "ciel hair headband"
    $ C.display = "chastity hairup reg"
    $ me.display = "melody mefreckface"
    $ mic.display = "michelle be1"
    $ tay.display = "taylor tayhair"
    $ b.display = "betty macne"
    $ bio_menu = "No"
    $ p_name = "Calvin"
    scene black
    
    jump GameStart
