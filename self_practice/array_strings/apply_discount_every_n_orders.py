# https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier:
  def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
    self.n = n
    self.discount = (100 - discount) / 100
    self.customer_count = 0
    self.price_map = self.calculatePriceMap(products, prices)

  def calculatePriceMap(self, products, prices):
    m = {}
    for i in range(len(products)):
      m[products[i]] = prices[i]
    return m


  def getBill(self, product: List[int], amount: List[int]) -> float:
    total = 0
    self.customer_count += 1

    for i in range(len(product)):
      price = self.price_map[product[i]]
      total += (price * amount[i])

    should_apply_discount = self.customer_count % self.n == 0
    return total * self.discount if should_apply_discount else total
