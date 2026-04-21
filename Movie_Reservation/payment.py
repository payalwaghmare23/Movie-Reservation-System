
def process_payment(amount):
    
    print("\n Payment Section")
    print(f"Total Amount: ₹{amount}")

    print("\nSelect Payment Method:")
    print("1. UPI")
    print("2. Card")
    print("3. Cash")

    choice = input("Enter choice: ")

    if choice == "1":
        upi = input("Enter UPI ID: ")
        print("Processing UPI payment...")
    
    elif choice == "2":
        card = input("Enter Card Number: ")
        print("Processing Card payment...")
    
    elif choice == "3":
        print("Cash will be collected at counter")
    
    else:
        return False

    print("Payment Successful ")
    return True