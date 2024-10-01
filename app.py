from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from models import Image, db

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)


@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])


@app.route('/images/<int:image_id>', methods=['POST'])
def update_rating(image_id):
    image = Image.query.get_or_404(image_id)
    data = request.get_json()
    if 'rating' in data:
        image.rating = data['rating']
        db.session.commit()
        return jsonify(image.to_dict()), 200
    return jsonify({"error": "Invalid data"}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
