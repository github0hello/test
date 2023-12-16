from flask import *
from flask import render_template
from blueprint.login import login_bp
from blueprint.upload import upload_bp
from blueprint.file import my_file_bp
import os
# from gevent import pywsgi

on = 'android'
if on == 'android':   
     os.chdir('/storage/emulated/0/Android/data/org.qpython.qpy/files/projects3/flask')

app = Flask(__name__)

app.secret_key = '5s9s.dd9&@8s.da36lm_4qw97nwo3_pq.,is.h'
# 定义文件上传的路径
UPLOAD_FOLDER = "/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(login_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(my_file_bp)


@app.route('/')
def index():
    user_info=session.get('user_info')
    if not user_info:
        return redirect('/login')
    return render_template("index.html", name=user_info, name1=user_info)
    
    
    
@app.route('/forget')
def Forget_the_data():
    session.pop('name', None)
    session.pop('user', None)
    session.pop('user_info', None)
    session.pop('user_password', None)
    return redirect('/login')


@app.route('/count_down')
def count_down():
    if not session.get('user_info'):
        return redirect('/login')
    return render_template("倒计时.html")  # 调用render_template函数，传入html文件参数


@app.route('/socket')
def websocket():
    if not session.get('user_info'):
        return redirect('/login')
    return render_template("socket.html")  # 调用render_template函数，传入html文件参数


@app.route('/flask')
def flask_html():
    return render_template("flask_html.html")
    
    
@app.route('/root')
def root():
    try:
        if session['root_name'] == 'root' and session['root_password'] == '123456':
            return render_template("root.html", date=open('file/date.json').read())
    except:  
        return redirect('/login_for_root')




    
if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    # erver.serve_forever()
    app.run(debug=True)
