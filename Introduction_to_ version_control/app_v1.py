def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total


def apply_discount(total):
    discount_rate = 0.10
    return total - (total * discount_rate)


def main():
    prices = [10, 20, 30]
    total = calculate_total(prices)
    final_amount = apply_discount(total)

    print("Total before discount:", total)
    print("Final amount:", final_amount)


if __name__ == "__main__":
    main()
