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
