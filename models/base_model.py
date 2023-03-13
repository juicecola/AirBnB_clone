#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class that defines common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at'
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of the BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute update_at with current datetime"""
        self.update_at = datetime.now()

    def to_dict(self):
        """Return a dict containing all key/value of __dict__ of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

