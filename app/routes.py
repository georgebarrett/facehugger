from app import app
from flask import request, render_template, redirect, url_for
from .models.scene import Death, CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod, Finished

@app.route('/central_corridor', methods=['GET', 'POST'])
def central_corridor():
    central_corridor_scene = CentralCorridor()

    if request.method == 'POST':
        action = request.form.get('action')
        result = central_corridor_scene.enter(action)
    else:
        result = central_corridor_scene.enter()

    if result['scene'] != 'central_corridor':
        return redirect(url_for(result['scene']))
    
    return render_template('central_corridor.html', result=result)


@app.route('/laser_weapon_armory', methods=['GET', 'POST'])
def laser_weapon_armory():
    armory = LaserWeaponArmory()

    if request.method == 'POST':
        guess = request.form.get('guess')
        result = armory.enter(guess)
    else:
        result = armory.enter()
    
    if result['scene'] != 'laser_weapon_armory':
        return redirect(url_for(result['scene']))
    
    return render_template('laser_weapon_armory.html', result=result)


@app.route('/the_bridge', methods=['GET', 'POST'])
def the_bridge():
    bridge = TheBridge()
    if request.method == 'POST':
        action = request.form.get('action')
        result = bridge.enter(action)
    else:
        result = bridge.enter()
    
    if result["scene"] != "the_bridge":
        return redirect(url_for(result["scene"]))

    return render_template('the_bridge.html', result=result)