from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False, default=True)

    favorites: Mapped[list["FavoriteMovie"]] = relationship("FavoriteMovie", back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # Do not include password for security
        }

class FavoriteMovie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    imdb_id: Mapped[str] = mapped_column(String(20), nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="favorites")

    def serialize(self):
        return {
            "id": self.id,
            "imdb_id": self.imdb_id,
            "title": self.title,
            "user_id": self.user_id
        }
