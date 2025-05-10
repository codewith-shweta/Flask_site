from flask import Flask , render_template , session, url_for,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'Shwet_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Uncommented for tracking modifications
# Initialize database
db = SQLAlchemy(app)

# Create db model 
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=50), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=15), nullable=False, unique=True)
    description = db.Column(db.String(length=1023), nullable=False, unique=True)


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', '{self.barcode}')"

# Create func to return string to add something
# def __repr__(self):
#     return '<Name %r>' % self.id

@app.route('/')
@app.route('/home')
def home_page():  
    return render_template('index.html')

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

@app.route('/services')
def services_page():
    return render_template('services.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        Item.query.delete()
        db.session.commit()


        if not Item.query.first():
            item1 = Item(name="Phone", price=500, barcode="123456789012", description="Smartphone")
            item2 = Item(name="Laptop", price=900, barcode="987654321098", description="Gaming Laptop")
            item3 = Item(name="Keyboard", price=300, barcode="112233445566", description="Mechanical Keyboard")
            item4 = Item(name ="Headphones", price=800, barcode= "2323398561",description="Noise cancelling Headphones")
            item5 = Item(name="Smart watch", price=700, barcode="459386565",description="Tracker SmartWatch")
            item6 = Item(name="Camera", price=1300, barcode= "095674834", description = "Digital camera")
            db.session.add_all([item1,item2,item3,item4,item5,item6])
            db.session.commit()

    app.run(debug=True)  

