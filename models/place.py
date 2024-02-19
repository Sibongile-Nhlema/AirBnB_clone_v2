#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models import type_of_storage
from models.review import Review
from models.amenities import Amenities


class Place(BaseModel):
    """A place to stay"""

    if type_of_storage == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        amenity_ids = []

        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='place'
            )
        amenities = relationship(
                'Amenity',
                secondary=place_amenity,
                viewonly=False,
                back_populates="place_amenities"
            )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id
            equal to the current Place.id. It's the FileStorage
            relationship between Place and Review.

            """

            from models import storage

            all_reviews = storage.all(Review)
            reviews = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            ''' returns a list of the amenities '''
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            '''Adds amenity ids to attr '''
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
