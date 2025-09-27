from app import app, db
from models import Plant

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create sample plants
    plants = [
        Plant(
            name="Aloe Vera",
            image="https://example.com/aloe.jpg",
            price=10,
            is_in_stock=True
        ),
        Plant(
            name="Snake Plant",
            image="https://example.com/snake.jpg",
            price=15,
            is_in_stock=False
        ),
        Plant(
            name="Peace Lily",
            image="https://example.com/peace.jpg",
            price=20,
            is_in_stock=True
        )
    ]

    # Add and commit
    db.session.add_all(plants)
    db.session.commit()

    print("✅ Database seeded with sample plants!")
