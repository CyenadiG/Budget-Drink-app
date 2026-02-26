from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://greeneca22_db_user:Yw583pcYSvaoYM6p@drink-db.rlgxqhl.mongodb.net/?appName=drink-db"
client = MongoClient(MONGODB_URI)

db = client['budget-drink']
collection = db['drinks']


#collection.insert_one({"name":"Carmel Machiatto", "price" :5.69 , "image_url" :"https://cloudassets.starbucks.com/is/image/sbuxcorp/SBX20211029_CaramelMacchiato?impolicy=1by1_wide_topcrop_630&crop=180,360,1440,1440&wid=630&hei=630&qlt=85"})
#collection.insert_one({"name":"Strawberry Matcha Latte", "price" : 6.00 , "image_url" :"https://www.butteredsideupblog.com/wp-content/uploads/2024/07/Starbucks-Iced-Matcha-Latte-with-Strawberry-Cold-Foam-5-scaled.jpg"})
#collection.insert_one({"name":"Taro milk tea", "price" :8.00 , "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuSKvDpQHZ4yOA8_JH84BSrmR6KaKqFQ-g8g&s"})
#collection.insert_one({"name": "Sunset Tea", "price" : 4.00, "image_url": "https://cdn.prod.website-files.com/60f21179bf9eee394dd01d05/6101627980a42525e7f1607d_SunsetTea.jpg"})
#collection.insert_one({"name": "Americano","price" : 5.00 , "image_url":"https://d1w7312wesee68.cloudfront.net/6iQnCMGQc_kUm3ffZQn5qGyqG_BFdIMkke-TFRr0OTM/resize:fit:720:720/plain/s3://toasttab/restaurants/restaurant-301601000000000000/menu/items/1/item-1600000000038351981_1760541329.png"})
#collection.insert_one({"name": "Vietnmese Coffee", "price" : 6.50 , "image_url":"https://www.allrecipes.com/thmb/LlegF5NeKOTHqs9WZw5RWWwSyjU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/77768-Vietnamese-Iced-Coffee-DDMFS-4x3-62f34e1d4658433a83801c8533dbcafe.jpg"})
#collection.insert_one({"name": "Dr. Pepper", "price" : 2.00 , "image_url":"https://enochseagleeye.org/wp-content/uploads/2023/12/3647758998_a986319018_b.jpg"})

for d in collection.find():
    print(d)
