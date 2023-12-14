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
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "central_corridor",
                "message": "The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew. You are the last surviving member and your last mission is to get the neutron destruct bomb from the Weapons Armory, put it in the bridge, and blow the ship up after getting into an escape pod. You're running down the central corridor to the Weapons Armory when a Gothon jumps out, red scaly skin, dark grimy teeth, and lashing tail whipping around its hate filled body. It's blocking the door to the Armory and about to pull a weapon to blast you.",
                "choices": ["shoot", "dodge", "tell a joke"]
            }

        if action == 'shoot':
            return {
                "scene": "death",
                "message": "Quick on the draw you yank out your blaster and fire it at the Gothon. Its snapping tail and metalic scales disorientate you, which throws off your aim. Your laser hits its tails but misses its body. This completely ruins its glamorous and deadly tail, which makes it fly into an insane rage and blast you repeatedly in the face until you are dead. Then he eats you."
            }

        elif action == 'dodge':
            return {
                "scene": "death",
                "message": "Like a world class boxer you dodge, weave, slip and slide right as the Gothon's blaster cranks a laser past your head. In the middle of your artful dodge your foot slips and you bang your head on the metal wall and pass out. You wake up shortly after only to die as the Gothon stomps on your head and eats you."
            }

        elif action == 'tell a joke':
            return {
                "scene": "laser_weapon_armory",
                "message": "Lucky for you they made you learn Gothon insults in the academy. You tell the one Gothon joke you know: Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr. The Gothon stops, tries not to laugh, then busts out laughing and can't move. While it's laughing you run up and shoot it square in the head putting it down, then jump through the Weapon Armory door."
            }

        else:
            return {
                "scene": "central_corridor",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "dodge", "tell a joke"]
            }

class LaserWeaponArmory(Scene):
    
    def enter(self, guess=None):
        code = f'{randint(1,3)}{randint(1,3)}{randint(1,3)}'
        
        if guess is None:
            return {
                "scene": "laser_weapon_armory",
                "message": "You do a dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. It's quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. There's a keypad lock on the box and you need the code to get the bomb out. The code is 3 digits long and the keypad has the numbers 1 to 3.",
                "prompt": "Enter the code:",
                "attempts_remaining": 10  # initial number of attempts
            }

        if guess == code:
            return {
                "scene": "the_bridge",
                "message": "The container clicks open and the seal breaks, letting gas out. You grab the neutron bomb and run as fast as you can to the bridge where you must place it in the right spot."
            }
        else:
            # Decrease the number of attempts left and provide feedback
            attempts_left = 10 - len(guess)  # assuming guess is a list of attempts
            if attempts_left > 0:
                return {
                    "scene": "laser_weapon_armory",
                    "message": "BZZZZZEDDDDDD! The code is incorrect.",
                    "prompt": "Enter the code:",
                    "attempts_remaining": attempts_left
                }
            else:
                return {
                    "scene": "death",
                    "message": "The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fused together. You decide to sit there, and finally the Gothons return to their ship and fire the torpedoes."
                }

class TheBridge(Scene):
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "the_bridge",
                "message": "You burst onto the Bridge with the neutron destruct bomb under your arm and surprise 5 Gothons who are trying to take control of the ship. They haven't fired their weapons yet, as they can see the active bomb under your arm. You have two options: Throw the bomb at the Gothons and run for the escape pods, or slowly place the bomb on the floor and edge towards the pods with your gun pointed towards the explosive device.",
                "choices": ["throw the bomb", "slowly place the bomb"]
            }

        if action == 'throw the bomb':
            return {
                "scene": "death",
                "message": "In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically try to disarm the bomb. You die knowing they will probably blow up when it goes off."
            }

        elif action == 'slowly place the bomb':
            return {
                "scene": "escape_pod",
                "message": "You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat. You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't get out. Now that the bomb is placed you run to the escape pod to get off this tin can."
            }

        else:
            return {
                "scene": "the_bridge",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["throw the bomb", "slowly place the bomb"]
            }
        
class EscapePod(Scene):
    
    def enter(self, guess=None):
        good_pod = randint(1, 5)
        
        if guess is None:
            return {
                "scene": "escape_pod",
                "message": "You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes. It seems like hardly any Gothons are on the ship, so your run is clear of interference. You get to the chamber with the escape pods, and now need to pick one to take. Some of them could be damaged but you don't have time to look. There are 5 pods, which one do you take?",
                "pod_numbers": range(1, 6)  # Generate pod numbers 1 to 5
            }

        if int(guess) != good_pod:
            return {
                "scene": "death",
                "message": f"You jump into pod {guess} and hit the eject button. The pod escapes out into the void of space, then implodes as the hull ruptures, crushing your body into jam jelly."
            }
        
        else:
            return {
                "scene": "finished",
                "message": f"You jump into pod {guess} and hit the eject button. The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back and see your ship implode and then explode like a bright star, taking out the Gothon ship at the same time. You made it out alive!"
            }
        
class Finished(Scene):
    
    def enter(self):
        print('You made it!')
        return 'finished'