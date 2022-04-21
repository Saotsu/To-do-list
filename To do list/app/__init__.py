from flask import Flask, session, render_template, request, url_for, redirect


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "91a65cc7-f6db-45cf-9bc7-a3c80b91aa0b"

    @app.route('/')
    def index():
        return render_template('todolist.html', session=session)

    @app.route('/add/', methods=['POST'])
    def add():
        task = request.form['todo']
        if not session:
            session['1'] = {'task': task, 'completed': False}
        else:
            new_id = int([*session.keys()][-1])+1
            session[str(new_id)] = {'task': task, 'completed': False}
        return redirect(url_for('index'))


    @app.route('/delete/', methods=['POST'])
    def delete():
        task_id = request.form['taskid']
        session.pop(task_id)
        return redirect(url_for('index'))
    

    @app.route('/check/', methods=['POST'])
    def check():
        task_id = request.form['taskid']
        if session[task_id]['completed']:
            session[task_id] = {'task': session[task_id]['task'], 'completed': False}
        else:
            session[task_id] = {'task': session[task_id]['task'], 'completed': True}
        return redirect(url_for('index'))
    
    @app.route('/deleteall/', methods=['POST'])
    def delete_all():
        session.clear()
        return redirect(url_for('index'))

    return app