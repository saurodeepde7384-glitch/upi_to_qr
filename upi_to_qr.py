import qrcode
# qrcode LIBRARY - TO GENERATE QR CODE ( pip install qrcode )
# pillow LIBRARY INSTALLED TO SHOW THE IMAGE (pip install pillow)
import time
# time LIBRARY - TO INTRODUCE DELAY 
print()
print()
print("~~~~~~~~~~~~~    UPI TO  QR  GENERATOR   ~~~~~~~~~~~~~~~~~")
print()
print()
def gen_qr():
    upi_id = input("Enter your upi id: ")

    # FORMAT OF UPI URL IS (upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR). 
    time.sleep(1)
    upi_url = f"upi://pay?pa={upi_id}"
    print("Generating your UPI QR code...")
    time.sleep(2)

    # .make FUNCTION TO GENERATE THE QR
    upi_qr= qrcode.make(upi_url)
    print("Here is your UPI QR code:")
    time.sleep(1)

    # .show FUNCTION TO DISPLAY THE QR CODE
    upi_qr.show()

while True:
    x= input("Do you want to generate UPI QR code? (yes/no): ").strip().lower()
    if x == 'yes'or x == 'y':
        gen_qr()
        
    elif x == 'no' or x=='n':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
