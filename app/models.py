from app import db


class Player(db.Model):
    """Create a data model for the database to be set up for capturing songs

    """
    id = db.Column(db.Integer, primary_key=True)
    Value = db.Column(db.String(100), unique=False, nullable=False)
    Reactions = db.Column(db.String(100), unique=False, nullable=False)
    Composure = db.Column(db.String(100), unique=False, nullable=False)
    Age = db.Column(db.String(100), unique=False, nullable=False)
    ShortPassing = db.Column(db.String(100), unique=False, nullable=False)
    Vision = db.Column(db.String(100), unique=False, nullable=False)
    LongPassing = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        pred_repr = "<PredHist(id='%s', Value='%s', Reactions='%s', Composure='%s', Age='%s', ShortPassing='%s', Vision='%s', LongPassing='%s')>"
        return pred_repr % (self.id, self.Value, self.Reactions, self.Composure,
                            self.Age, self.ShortPassing, self.Vision, self.LongPassing)
