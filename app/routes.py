from flask import Flask, request, render_template, redirect, url_for, session
from .models.scene import CentralCorridor, LaserWeaponArmory, TheBridge, EscapePod, Finished

def setup_routes(app):
    @app.route('/')
    def home():
        return redirect(url_for('central_corridor'))

    @app.route('/central_corridor', methods=['GET', 'POST'])
    def central_corridor():
        scene = CentralCorridor()
        if request.method == 'POST':
            action = request.form.get('action')
            result = scene.enter(action)
            if result['scene'] == 'death':
                session['message'] = result['message']
                return redirect(url_for('death'))
            elif result['scene'] == 'laser_weapon_armory':
                return redirect(url_for('laser_weapon_armory'))
        else:
            result = scene.enter()
        return render_template('central_corridor.html', result=result)

    @app.route('/laser_weapon_armory', methods=['GET', 'POST'])
    def laser_weapon_armory():
        armory = LaserWeaponArmory()
        if request.method == 'POST':
            guess = request.form.get('guess')
            result = armory.enter(guess)
            if result['scene'] == 'death':
                session['message'] = result['message']
                return redirect(url_for('death'))
            elif result['scene'] == 'the_bridge':
                return redirect(url_for('the_bridge'))
        else:
            result = armory.enter()
        return render_template('laser_weapon_armory.html', result=result)

    @app.route('/the_bridge', methods=['GET', 'POST'])
    def the_bridge():
        bridge = TheBridge()
        if request.method == 'POST':
            action = request.form.get('action')
            result = bridge.enter(action)
            if result['scene'] == 'death':
                session['message'] = result['message']
                return redirect(url_for('death'))
            elif result['scene'] == 'escape_pod':
                return redirect(url_for('escape_pod'))
        else:
            result = bridge.enter()
        return render_template('the_bridge.html', result=result)

    @app.route('/escape_pod', methods=['GET', 'POST'])
    def escape_pod():
        pod = EscapePod()
        if request.method == 'POST':
            guess = request.form.get('pod_number')
            result = pod.enter(guess)
            if result['scene'] == 'finished':
                session['message'] = result['message']
                return redirect(url_for('finished'))
            elif result['scene'] == 'death':
                session['message'] = result['message']
                return redirect(url_for('death'))
        else:
            result = pod.enter()
        return render_template('escape_pod.html', result=result)

    @app.route('/finished')
    def finished():
        message = session.pop('message', 'Congratulations, you made it!')
        return render_template('finished.html', message=message)

    @app.route('/death')
    def death():
        message = session.pop('message', 'You have died.')
        return render_template('death.html', message=message)