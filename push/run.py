from push.app import create_app
from flask import render_template

app = create_app()

@app.route('/push')
def push():
    return render_template('push_service.html')

if __name__ == '__main__':
    app.run(debug=True)