from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)   # limit length for efficiency
    image = db.Column(db.String(255), nullable=False)  # allow longer URLs
    price = db.Column(db.Float, nullable=False)        # price fits better as Float
    is_in_stock = db.Column(db.Boolean, default=True, nullable=False)

    def to_dict(self):
        """Serialize Plant object to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image,
            "price": self.price,
            "is_in_stock": self.is_in_stock
        }
