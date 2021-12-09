from flask import Flask, render_template, request, redirect
from base import mybase, mycursor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list', methods = ['GET', 'POST'])
def List():
    mycursor.execute("SELECT * FROM todo")
    lists = mycursor.fetchall()
    return render_template('list.html', lists = lists)

@app.route('/add', methods=['GET','POST'])
def Add():
    if request.method == 'GET':
        return render_template('add.html')
    if request.method == 'POST':
        _task_name = request.form['task_name']
        _task_description = request.form['task_description']
        _importance = request.form['importance']
        _time = request.form['time']
        _date = request.form['date']
        sql = 'INSERT INTO todo (task_name, task_description, importance, time, date) VALUES (%s, %s, %s, %s, %s)'
        val = (_task_name, _task_description, _importance, _time, _date)
        mycursor.execute(sql, val)
        mybase.commit()
        return redirect('/list')

@app.route('/list')
def View():
    if request.method == 'GET':
        return render_template('list.html')

@app.route('/delete/<int:id>')
def delete_lists(id):
    sql = f'DELETE FROM todo WHERE ID = {id}'
    mycursor.execute(sql)
    mybase.commit()
    return redirect('/list')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_list(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM todo WHERE ID={id}')
        list = mycursor.fetchone()
        return render_template('update_list.html', list = list)
    if request.method == 'POST':
        _task_name = request.form['task_name']
        _task_description = request.form['task_description']
        _importance = request.form['importance']
        _time = request.form['time']
        _date = request.form['date']
        sql = f'UPDATE todo SET task_name = %s, task_description = %s, importance = %s, time = %s, date = %s WHERE ID = %s'
        values = (_task_name, _task_description, _importance, _time, _date, id)
        mycursor.execute(sql, values)
        mybase.commit()
        return redirect('/list')

if __name__ == '__main__':
    app.run()