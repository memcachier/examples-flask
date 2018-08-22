from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db, cache
from task_list.models import Task

bp = Blueprint('task_list', __name__)

def is_post():
    return (request.method == 'POST')

@bp.route('/', methods=('GET', 'POST'))
@cache.cached(unless=is_post)
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Task(name=name))
            db.session.commit()
            cache.delete_memoized(get_all_tasks)
            cache.delete('view//')

    tasks = get_all_tasks()
    return render_template('task_list/index.html', tasks=tasks)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
        cache.delete_memoized(get_all_tasks)
        cache.delete('view//')
    return redirect(url_for('task_list.index'))

@cache.memoize()
def get_all_tasks():
    return Task.query.all()


from flask import Flask, session
@bp.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@bp.route('/get/')
def get():
    return session.get('key', 'not set')
