from flask import Flask
from controllers.main_controller import main

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
