def main():
    products = []
    file_name = "urunler.txt"

    try:/
        with open(file_name, "r", encoding="utf-8") as file:
           for line in file:

                if not line.strip():
                    continue


                try:
                    name, price_str = line.strip().split(",", 1)

                    product = {
                        'name': name.strip(),
                        'price': float(price_str.strip())
                    }
                    products.append(product)
                except ValueError as e:
                    print(f"Satır formatı hatalı: '{line.strip()}'. Hata: {e}")

    except FileNotFoundError:
        print(f"'{file_name}' dosyası bulunamadı!")
        return


    products_sorted = sorted(products, key=lambda x: x['price'], reverse=True)


    print("\nÜrünler, fiyatlara göre büyükten küçüğe sıralanmıştır:")
    for product in products_sorted:
        print(f"Ürün: {product['name']} - Fiyat: {product['price']:.2f}")


if __name__ == "__main__":
    main()