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
                "message": "You hear the sound of your hibernation pod opening and drowsily clamber out. You vomit all over the floor and then start to callibrate with reality. A scan of the ship is necessary to make sure that everything is in order and that the cargo is safe. You enter into the cargo room, relieved to finally be off the mining planet 31-XCT. Something catches your eye. You rub your eyes to make sure you aren't hallucinating. A metalic slimy egg is in the corner of the bay. You walk over to inspect the anomaly. As you get closer, you see something move inside. You pull out your laser gun and approach with caution. When you reach the mysterious egg, the top begins to fold open.",
                "choices": ["shoot", "run", "inspect"]
            }

        if action == 'shoot':
            return {
                "scene": "death",
                "message": "You run over to the egg and fire your laser gun at the creature inside. When the laser hits the alien, acid sprays all over your head. You scream and writhe around on the floor before turning into a headless corspe."
            }

        elif action == 'run':
            return {
                "scene": "death",
                "message": "Fear takes over and you sprint out of the cargo bay. You run to where your crew are still in hibernation and try to wake them up. As you approach their pods, you see that all of your crew mates have spider like aliens wrapped around their faces. You stagger back in shock. What was that... you turn around and the facehugger leaps onto you. You feel its legs wrap around your head, tail tighten around your neck and then an alien tube enters your mouth. You pass out."
            }

        elif action == 'inspect':
            return {
                "scene": "laser_weapon_armory",
                "message": "You keep edging towards the slimy metalic egg. You peer inside the egg, laser gun shaking in your hand. You see a spider like alien begin to emerge from the egg. Its time to think fast. Where can you hide and stay safe. You remember the Lasor Amory can be totally sealed off and begin sprinting towards it"
            }

        else:
            return {
                "scene": "central_corridor",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "run", "inspect"]
            }

class LaserWeaponArmory(Scene):
    
    def enter(self, guess=None):
        code = f'{randint(1,9)}{randint(1,9)}{randint(1,9)}'
        
        if guess is None:
            return {
                "scene": "laser_weapon_armory",
                "message": "You dive roll into the Lasor Amory. You are dripping in sweat and are drowning in adrenaline. Quickly close and lock all the doors. You reach the last door and it is jammed. A code needs to be entered into the door's keypad to force it shut. What is the code! You know it! Come on! As your hand touches the key pad you hear a noise coming from the end of the corridor. The facehugger has found you and is scurrying as fast as it can. The facehugger is hell bent on laying an egg inside you. You have ten attempts to close the door. the code is four digits long and the keypad range is 1-9.",
                "prompt": "Enter the code:",
                "attempts_remaining": 10  # initial number of attempts
            }

        if guess == code:
            return {
                "scene": "the_bridge",
                "message": "The door slams shut and a milisecond later the facehugger smashes against the reinforced glass. You sit in corner of the armory rocking backwards and forwards. It dawns on you that you will die in this room. You need to get to The Bridge and activate the escape pods. You look up and see a vent cover. You blast the cover off and climb up. You start crawling along the vent shaft towards The Bridge. Hold on... If I can fit up here, then so can that alien. Don't think, MOVE"
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
                    "message": "You entered the code for the last time. The door is fixed open. The facehugger scuttles into the armory. You unload your laser gun but can't hit the sporadic target. The facehugger leaps up. You feel its legs wrap around your face, tail tighten around your neck and then an alien tube enter your mouth. You wake up eight hours later with a dead facehugger next to you. The relief is palapable. That evening you are making yourself a cup of tea when you hear the first crunch of your chest bones breaking."
                }

class TheBridge(Scene):
    
    def enter(self, action=None):
        if action is None:
            return {
                "scene": "the_bridge",
                "message": "You crawl through the vent shafts for what feels like eternity. You are covered in sweat and stink of fear. After three hours of scrabbling along vents, you reach The Bridge. You blast a vent cover off and then jump down. There, before you, is a metalic alien monstrosity. Its forehead is long and its metalic skin reflects the clinical lights of The Bridge. The alien is eight feet tall and is connected to some sort of organic sack. You realise that this alien is a queen and she is laying eggs. You stand there in horror at the sight of her. Your jaw drops as you see that Earth is not far away. The alien screams and prepares to fight. She detaches herself from her sack, her tail is lashing and her tongue is out. You freeze and can't decide what to do. Do you shoot the alien or run to the control panel to activate the escape pods. You scream.",
                "choices": ["shoot", "activate the escape pods"]
            }

        if action == 'shoot':
            return {
                "scene": "death",
                "message": "You unload your laser gun into the alien queen. Acid sprays all over your body and you can feel it burning through you. The Queen picks you up with her metalic arms. she looks at you sqaure in face. She can sense you fear and wants to bask in it. Once she is satisfied she launches her tongue into your head"
            }

        elif action == 'activate the escape pods':
            return {
                "scene": "escape_pod",
                "message": "You fire your laser gun at the fire detectors. Loud noises and flashing lights fill the spaceship. The Queen is disorientated. You sprint to the control panel and activate the escape pods. You begin to run to the pods but then realise that the Queen will land on Earth. You sprint back and activate the self-destruct sequence"
            }

        else:
            return {
                "scene": "the_bridge",
                "message": "DOES NOT COMPUTE! Try again.",
                "choices": ["shoot", "activate the escape pods"]
            }
        
class EscapePod(Scene):
    
    def enter(self, guess=None):
        good_pod = randint(1, 5)
        
        if guess is None:
            return {
                "scene": "escape_pod",
                "message": "You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes or the Queen tears you apart. You reach the pods but can't remember which one you activated. Which one will you choose. You only have time to pick one. The Queen is rampaging towards you.",
                "pod_numbers": range(1, 6)  # Generate pod numbers 1 to 5
            }

        if int(guess) != good_pod:
            return {
                "scene": "death",
                "message": f"You jump into pod {guess} and hit the eject button. Nothing happens. The Queen reaches you and you pass out from fear. You come around and are plastered to a wall with an unknown alien goo. You can't move and no one can hear you scream. You look down and see an egg slowly open. The facehugger knows its prey is helpless. It slowly crawls out of the egg and up your body. You feel its legs wrap around your face, tail tighten around your neck and a slimey alien tube enter your mouth."
            }
        
        else:
            return {
                "scene": "finished",
                "message": f"You jump into pod {guess} and hit the eject button. The pod easily slides out into space heading to the Earth. As it flies to our home planet, you look back and see your ship implode and then explode like a bright star. You breathe deeply and your body turns to jelly. You survived. WHAT... you look out of the window and see another escape pod heading to earth. You check the computer system and an alien life form is detected in the other pod. Over the next twenty years humanity will be eradicated"
            }
        
class Finished(Scene):
    
    def enter(self):
        return {
            "scene": "finished",
            "message": "You made it!"
        }
