from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://greeneca22_db_user:Yw583pcYSvaoYM6p@drink-db.rlgxqhl.mongodb.net/?appName=drink-db"
client = MongoClient(MONGODB_URI)

db = client['budget-drink']
collection = db['drinks']

app = Flask(__name__)

# data = [
#     {
#         "name": "Carmel Machiatto",
#         "price" : 5.69,
#         "image_url": "https://cloudassets.starbucks.com/is/image/sbuxcorp/SBX20211029_CaramelMacchiato?impolicy=1by1_wide_topcrop_630&crop=180,360,1440,1440&wid=630&hei=630&qlt=85"
#       },
#     {
#         "name": "Strawberry Matcha Latte ",
#         "price" : 6.00,
#         "image_url":"https://www.butteredsideupblog.com/wp-content/uploads/2024/07/Starbucks-Iced-Matcha-Latte-with-Strawberry-Cold-Foam-5-scaled.jpg"
#
#     },
#     {
#         "name": "Taro milk tea",
#         "price" : 8.00,
#         "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuSKvDpQHZ4yOA8_JH84BSrmR6KaKqFQ-g8g&s"
#     },
#     {
#         "name": "Sunset Tea",
#         "price" : 4.00,
#         "image_url": "https://cdn.prod.website-files.com/60f21179bf9eee394dd01d05/6101627980a42525e7f1607d_SunsetTea.jpg"
#     },
#     {
#         "name": "Americano",
#         "price" : 5.00,
#         "image_url":"https://d1w7312wesee68.cloudfront.net/6iQnCMGQc_kUm3ffZQn5qGyqG_BFdIMkke-TFRr0OTM/resize:fit:720:720/plain/s3://toasttab/restaurants/restaurant-301601000000000000/menu/items/1/item-1600000000038351981_1760541329.png"
#     },
#     {
#         "name": "Vietnmese Coffee",
#         "price" : 6.50,
#         "image_url":"https://www.allrecipes.com/thmb/LlegF5NeKOTHqs9WZw5RWWwSyjU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/77768-Vietnamese-Iced-Coffee-DDMFS-4x3-62f34e1d4658433a83801c8533dbcafe.jpg"
#     }
#     ,
#     {
#         "name": "Dr. Pepper",
#         "price" : 2.00,
#         "image_url":"https://enochseagleeye.org/wp-content/uploads/2023/12/3647758998_a986319018_b.jpg"
#     }
#
# ]

@app.route("/")
def start_index():
    return render_template("index.html")
@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>Welcome to Drink Selection</em></h1></body></html>"

@app.route("/search/<budget>") #mapping
def search_drink_items(budget):
    budget = float(budget)
    result = []
    for drink in collection.find():
        if drink['price']<= budget:
            drink["_id"]=str(drink["_id"])
            result.append(drink)
    return result

app.run(host = "0.0.0.0", port = 5000)