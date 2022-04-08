from app import db
from datetime import datetime


class OTS(db.Model):
    ots_id = db.Column(db.String(250), primary_key=True)
    ots_content = db.Column(db.String(5000), nullable=False)
    ots_key2 = db.Column(db.String(250), unique=True, nullable=False)
    ots_date_fin = db.Column(db.DateTime(), default=datetime.utcnow, nullable=False)

    def __init__(self, ots_id: str, ots_content: str, ots_key2: str, ots_date_fin: datetime):
        self.ots_id = ots_id
        self.ots_content = ots_content
        self.ots_key2 = ots_key2
        self.ots_date_fin =ots_date_fin

    def __repr__(self):
        return f'OTS(ots_id={self.ots_id}, date de fin={self.ots_date_fin})'
