from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserInteraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def get_by_user_id(user_id):
        return UserInteraction.query.filter_by(user_id=user_id).all()
