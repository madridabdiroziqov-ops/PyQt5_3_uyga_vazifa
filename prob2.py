def total_price(products: list) -> float | str:
    total = 0
    for product in products:
        if product["price"] < 0 and product["count"] < 0:
            return "Xato ma'lumot"
        
        total+=product["price"] * product["count"]
    return total
    

print(total_price([
    {"name": "Non", "price": 2500, "count": 4},
    {"name": "Sut", "price": 8000, "count": 1}
]))
# Output: 18000.0

print(total_price([
    {"name": "Kola", "price": 10000, "count": 0},
    {"name": "Fanta", "price": 9000, "count": 3}
]))
# Output: 27000.0
