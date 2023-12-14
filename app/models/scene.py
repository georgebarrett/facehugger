from random import randint

class Scene:
    def enter(self):
        raise NotImplementedError('subclass it and implement enter()')

class Death(Scene):
    quips = [
        'Look what you have done',
        'you have gone and got yourself dead',
        'who is going to pay the extortionate energy bills now',
        'you died. You kinda suck at this',
        'you have disgraced your family',
        'such a luser'
    ]

    def enter(self):
        return {
            'scene': 'death',
            'message': self.quips[randint(0, len(self.quips) -1 )]
        }

class CentralCorridor(Scene):
    
    def enter(self):
        print(('''
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.
            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and lashing tail whipping around its hate
            filled body. It's blocking the door to the Armory and
            about to pull a weapon to blast you.
        '''))

        action = input("['shoot', 'dodge' or 'tell a joke']> ")

        if action == 'shoot':
            print(('''
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. Its snapping tail and metalic scales
                disorientate you, which throws off your aim. Your laser 
                hits its tails but misses its body. This completely ruins 
                its glamorous and deadly tail, which makes it fly into an 
                insane rage and blast you repeatedly in the face until 
                you are dead. Then he eats you.
            '''))

            return 'death'

        elif action == 'dodge':
            print(('''
                Like a world class boxer you dodge, weave, slip and
                slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. You wake up shortly after only to
                die as the Gothon stomps on your head and eats you.
            '''))

            return 'death'

        elif action == 'tell a joke':
            print(('''
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While it's laughing you run up and shoot it square in
                the head putting it down, then jump through the
                Weapon Armory door.
            '''))

            return 'laser_weapon_armory'

        else:
            print('DOES NOT COMPUTE!')
            return 'central_corridor'
