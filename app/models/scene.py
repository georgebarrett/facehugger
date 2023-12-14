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

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print(('''
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits long and the keypad has the numbers 1 to 3.
        '''))

        code = f'{randint(1,3)}{randint(1,3)}{randint(1,3)}'
        guess = input('[keypad]> ')
        guesses = 0

        while guess != code and guesses < 10:
            print('[BZZZZZEDDDDDD!]')
            guesses += 1
            guess = input('[keypad]> ')

        if guess == code:
            print(('''
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron bomb and run as fast as
                you can to the bridge where you must place it in the
                right spot.
            '''))

            return 'the_bridge'

        else:
            print(('''
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fused
                together. You decide to sit there, and finally the
                Gothons return to their ship and fire the torpedoes.
            '''))

            return 'death'

class TheBridge(Scene):
    
    def enter(self):
        print(('''
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship. They haven't fired their weapons 
            yet, as they can see the active bomb under your arm. You 
            have two options. Throw the bomb at the Gothons and run 
            for the escape pods, or slowly place the bomb on the floor 
            and edge towards the pods with your gun pointed towards 
            the explosive device. 
        '''))

        action = input("['throw the bomb' or 'slowly place the bomb']> ")

        if action == 'throw the bomb':
            print(('''
                In a panic you throw the bomb at the group of Gothons
                and make a leap for the door. Right as you drop it a
                Gothon shoots you right in the back killing you. As
                you die you see another Gothon frantically try to
                disarm the bomb. You die knowing they will probably
                blow up when it goes off.
            '''))

            return 'death'

        elif action == 'slowly place the bomb':
            print(('''
                You point your blaster at the bomb under your arm and
                the Gothons put their hands up and start to sweat.
                You inch backward to the door, open it, and then
                carefully place the bomb on the floor, pointing your
                blaster at it. You then jump back through the door,
                punch the close button and blast the lock so the
                Gothons can't get out. Now that the bomb is placed
                you run to the escape pod to get off this tin can.
            '''))

            return 'escape_pod'

        else:
            print('DOES NOT COMPUTE!')
            return 'the_bridge'
        
class EscapePod(Scene):
    
    def enter(self):
        print(('''
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There are 5 pods, which one do you take?
        '''))

        good_pod = randint(1,5)
        guess = input('[pod#]> ')

        if int(guess) != good_pod:
            print(f'''
                You jump into pod {guess} and hit the eject button.
                The pod escapes out into the void of space, then
                implodes as the hull ruptures, crushing your body into
                jam jelly.
            ''')

            return 'death'
        
        else:
            print((f'''
                You jump into pod {guess} and hit the eject button.
                The pod easily slides out into space heading to the
                planet below. As it flies to the planet, you look
                back and see your ship implode and then explode like a
                bright star, taking out the Gothon ship at the same
                time. You made it out alive!
            '''))

            return 'finished'
        
class Finished(Scene):
    
    def enter(self):
        print('You made it!')
        return 'finished'