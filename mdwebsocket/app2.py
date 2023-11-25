import markdown2
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)



@socketio.on('render_markdown')
def render_markdown(data):
    markdown_text = data['markdown']
    print(markdown_text)
    
    html = markdown2.markdown(markdown_text)

    socketio.emit('rendered_html', html)
    socketio.emit('get_input', markdown_text)

@socketio.on('save_markdown')
def save_markdown(data):
    
    markdown_text = data['markdown']
    print(markdown_text)
    with open('user_input.md', 'w') as file:
        file.write(markdown_text)

@app.route('/')
def index():
    with open('user_input.md', 'r') as file:
        markdown_text = file.read()
        html = markdown2.markdown(markdown_text)
    return render_template('index.html', initial_markdown=html,initial_input_text=markdown_text)
    
@app.route('/markdown/')
def markdown():
    with open('user_input.md', 'r') as file:
        markdown_text = file.read()
        html = markdown2.markdown(markdown_text)
    return render_template('/markdown_render/index.html', initial_markdown=html,initial_input_text=markdown_text)


if __name__ == '__main__':
    socketio.run(app,host="192.168.0.109",port=5001, debug=True)