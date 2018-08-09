from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db, cache
from task_list.models import Task

bp = Blueprint('task_list', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        name = request.form['name']
        if not name:
            flash('Task name is required.')
        else:
            db.session.add(Task(name=name))
            db.session.commit()

    tasks = cache.get('all_tasks')
    if tasks == None:
        tasks = Task.query.all()
        cache.set('all_tasks', tasks)
    return render_template('task_list/index.html', tasks=tasks)

@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('task_list.index'))
