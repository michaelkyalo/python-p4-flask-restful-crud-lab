from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Plant API</h1>'

# ✅ GET all plants
@app.route('/plants')
def get_plants():
    plants = Plant.query.all()
    return jsonify([p.to_dict() for p in plants]), 200

# ✅ GET one plant by ID
@app.route('/plants/<int:id>')
def get_plant(id):
    plant = db.session.get(Plant, id)   # ✅ modern way
    if plant:
        return jsonify(plant.to_dict()), 200
    return jsonify({"error": "Plant not found"}), 404

# ✅ PATCH one plant
@app.route('/plants/<int:id>', methods=['PATCH'])
def update_plant(id):
    plant = db.session.get(Plant, id)   # ✅ modern way
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    data = request.get_json()
    if "is_in_stock" in data:
        plant.is_in_stock = data["is_in_stock"]

    db.session.commit()
    return jsonify(plant.to_dict()), 200

# ✅ DELETE one plant
@app.route('/plants/<int:id>', methods=['DELETE'])
def delete_plant(id):
    plant = db.session.get(Plant, id)   # ✅ modern way
    if not plant:
        return jsonify({"error": "Plant not found"}), 404

    db.session.delete(plant)
    db.session.commit()
    return "", 204

if __name__ == '__main__':
    app.run(port=5555, debug=True)

