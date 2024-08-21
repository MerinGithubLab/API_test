from flask import Flask,jsonify
class Product:
    def __init__(self, product_id, name, price):
        self.product_id=product_id
        self.name=name
        self.price=price

products = [
    Product(product_id=100, name="Book",price=200),
    Product(product_id=101, name="biscuit", price=110),
    Product(product_id=102, name="candy", price=5)

]
def producttojson(product:Product):
    return {
        "id":product.product_id,
        "name":product.name,
        "price":product.price

    }

#create app
app=Flask("API APP")
@app.route('/products',methods=['GET'])
def getallproducts():
    print("All products")
    productlist=[]
    for product in products:
        productlist.append(producttojson(product))
    return jsonify({"products":productlist})



#run app
if __name__ == '__main__':
    app.run(debug=True)
