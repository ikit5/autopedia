from  flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AutolabelModel(db.Model):
    __tablename__ = "autolabels"

    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), unique=True)
    country = db.Column(db.String(100), nullable = False)
    foundation_year=db.Column(db.Integer)
    liqudation_year = db.Column(db.Integer)
    avatar_path=db.Column(db.String(100))
    models = db.relationship('AutomodelsModel', backref="producer")

    def __init__(self,label,country,f_year,l_year=None):
        self.label=label
        self.country= country
        self.foundation_year=f_year
        self.liqudation_year=l_year
        self.avatar_path=f"img/labels/{self.label}.png"

    def __repr__(self):
        return f"{self.label} was founded in {self.country} in {self.foundation_year}"


class AutomodelsModel(db.Model):
    __tablename__ = "models"

    id = db.Column(db.Integer,primary_key=True)
    label = db.Column(db.String(50), unique=True)
    prod_id = db.Column(db.Integer(),db.ForeignKey('autolabels.id'))
    start_prod_year=db.Column(db.Integer)
    end_prod_year = db.Column(db.Integer)
    lots = db.relationship('LotModel', backref="model")

    def __init__(self,label, prod_id, f_year, l_year=None):
        self.label=label
        self.prod_id=prod_id
        self.start_prod_year=f_year
        self.end_prod_year=l_year

    def __repr__(self):
        return f"{self.label} was model for {self.producer.label} and production started in {self.start_prod_year}"

class LotModel(db.Model):
    __tablename__="lot"

    id=db.Column(db.Integer, primary_key=True)
    model_id=db.Column(db.Integer(),db.ForeignKey('models.id'))
    price=db.Column(db.Integer, nullable=False)
    mileage=db.Column(db.Integer)
    prod_year=db.Column(db.Integer)
    color=db.Column(db.String)
    photo=db.Column(db.String)
    location=db.Column(db.String)

    def __init__(self,model_id,price,mileage,prod_year,color,location):
        self.model_id=model_id
        self.price=price
        self.mileage=mileage
        self.prod_year=prod_year
        self.color=color
        #self.photo=photo
        self.location=location
