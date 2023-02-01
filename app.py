from flask import Flask, jsonify
from flask_migrate import Migrate
import config
from extension import db
from blueprints.anno import anno
from blueprints.order import order
from blueprints.file import file
from blueprints.code import code

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(anno)
app.register_blueprint(order)
app.register_blueprint(file)
app.register_blueprint(code)



if __name__ == '__main__':
    # app.debug=True
    app.run()
