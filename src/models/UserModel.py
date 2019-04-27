# src/models/UserModel.py
from . import db, BaseModel


class UserModel(BaseModel):

    """ Student Model """
    __abstract__ = True

    name = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=True) 
    email = db.Column(db.String(128), unique=True, nullable=False)
    phonenumber = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_role_name = db.Column(db.Integer, nullable=False)
    user_role_value = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get("name")
        self.title = data.get("title")
        self.email = data.get("email")
        self.phonenumber = data.get("phonenumber")
        self.user_role_name = data.get("user_role_name")
        self.user_role_value = data.get("user_role_value")
        self.password = self.__generate_hash(data.get('password'))

    def __str__(self):
        return "<id: {}>".format(self.id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    #CRUD Operations
    @staticmethod
    def get_by_email(value):
        return UserModel.query.filter_by(email=value).order_by(UserModel.created_at.desc()).first()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(value)
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()