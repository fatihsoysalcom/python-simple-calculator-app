def add(x, y):
    """Adds two numbers"""
    return x + y

def subtract(x, y):
    """Subtracts two numbers"""
    return x - y

def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def divide(x, y):
    """Divides two numbers"""
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Basit Python Hesap Makinesi")
    print("İşlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    while True:
        choice = input("Seçiminizi yapın (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("İlk sayıyı girin: "))
                num2 = float(input("İkinci sayıyı girin: "))
            except ValueError:
                print("Geçersiz giriş. Lütfen sayı girin.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            next_calculation = input("Başka işlem yapmak ister misiniz? (evet/hayır): ")
            if next_calculation.lower() != 'evet':
                break
        else:
            print("Geçersiz giriş. Lütfen 1, 2, 3 veya 4 girin.")

if __name__ == "__main__":
    calculator()
