from app import db


class PhoneNumbers(db.Model):
    __tablename__ = "phone_numbers"
    code = db.Column("code", db.Integer, primary_key=True)
    begin = db.Column("begin", db.BigInteger, primary_key=True)
    end = db.Column("end", db.BigInteger, primary_key=True)
    amount = db.Column("amount", db.BigInteger, nullable=False)
    mobile_operator = db.Column("operator", db.Text)
    region = db.Column("region", db.Text)


class MovedNumbers(db.Model):
    __tablename__ = "moved_numbers"
    number = db.Column("number", db.BigInteger, primary_key=True)
    mobile_operator = db.Column("operator", db.Text, nullable=False)
