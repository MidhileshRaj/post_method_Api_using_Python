from flask import *

from DBConnection import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add_course')
def add_course():
    db=Db()
    qry="select * from users"
    res=db.select(qry)
    return jsonify(status='ok', data=res)

@app.route('/trial_post', methods=['POST'])
def trial_post():
    name =  request.form['name']
    email =  request.form['email']
    phone =  request.form['phone']
    password =  request.form['password']
    db =Db()
    qey = "INSERT INTO `users`(`name`,`email`,`password`,`phone`) VALUE ('"+name+"','"+email+"','"+password+"','"+phone+"')"
    res = db.insert(qey)
    return jsonify(status="ok")


@app.route('/update_user', methods=['PUT'])
def update_user():
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    db =Db()
    qry =  "UPDATE `users` SET `name`='"+name+"',`email`='"+email+"',`phone`='"+phone+"' WHERE `in`='"+id+"'"
    res = db.update(qry)
    return  jsonify(status ="ok")

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    id = request.form['id']
    db= Db()
    qry="DELETE FROM`users` WHERE `in`='"+id+"'"
    res = db.delete(qry)
    return  jsonify(status ="ok")



if __name__ == '__main__':
    app.run(debug=True,port=4000,host="0.0.0.0")
