from app.extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Integer, nullable=True)
    review = db.Column(db.Text, nullable=True)
    read_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, book_id):
        return cls.query.get(book_id)

    @classmethod
    def search(cls, keyword):
        search_pattern = f"%{keyword}%"
        return cls.query.filter(cls.title.like(search_pattern)).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
