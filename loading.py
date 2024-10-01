from app import app
from models import Image, db


def seed_database():
    images = [
        {'id': '1', 'url': '/static/images/1.jpg'},
        {'id': '2', 'url': '/static/images/2.jpg'},
        {'id': '3', 'url': '/static/images/3.jpg'},
        {'id': '4', 'url': '/static/images/4.jpg'},
        {'id': '5', 'url': '/static/images/5.jpg'},
        {'id': '6', 'url': '/static/images/6.jpg'},
        {'id': '7', 'url': '/static/images/7.jpg'},
        {'id': '8', 'url': '/static/images/8.jpg'},
        {'id': '9', 'url': '/static/images/9.jpg'},
        {'id': '10', 'url': '/static/images/10.jpg'},
        {'id': '11', 'url': '/static/images/11.jpg'},
        {'id': '12', 'url': '/static/images/12.jpg'},
        {'id': '13', 'url': '/static/images/13.jpg'},
        {'id': '14', 'url': '/static/images/14.jpg'},
        {'id': '15', 'url': '/static/images/15.jpg'}
    ]

    for image_data in images:
        image = Image(id=image_data['id'], url=image_data['url'])
        db.session.add(image)

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_database()