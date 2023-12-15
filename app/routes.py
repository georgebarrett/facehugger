from flask import request, render_template, redirect, url_for
from .models.scene import Death, CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod, Finished

def setup_routes(app):
    @app.route('/central_corridor', methods=['GET', 'POST'])
    def central_corridor():
        central_corridor_scene = CentralCorridor()

        if request.method == 'POST':
            action = request.form.get('action')
            result = central_corridor_scene.enter(action)
            if result['scene'] == 'death':
                return redirect(url_for('death', message=result['message']))
            elif result['scene'] == 'laser_weapon_armory':
                return redirect(url_for('laser_weapon_armory'))
        else:
            result = central_corridor_scene.enter()
        
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

    @app.route('/escape_pod', methods=['GET', 'POST'])
    def escape_pod():
        pod = EscapePod()
        if request.method == 'POST':
            guess = request.form.get('pod_number')
            result = pod.enter(guess)
        else:
            result = pod.enter()

        if result["scene"] != "escape_pod":
            return redirect(url_for(result["scene"]))

        return render_template('escape_pod.html', result=result)

    @app.route('/finished')
    def finished():
        finish_scene = Finished()
        result = finish_scene.enter()
        return render_template('finished.html', result=result)
    
    @app.route('/death')
    def death():
        message = request.args.get('message', 'You have died.')
        return render_template('death.html', message=message)