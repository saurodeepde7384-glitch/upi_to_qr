# UPI QR Code Generator

A simple Python tool to generate UPI payment QR codes instantly using the qrcode library.
Just enter your UPI ID, and the script creates a QR code that can be scanned for payments.

# Features

Generate UPI QR codes with your UPI ID

Displays the generated QR code image

Loop mode — create multiple QR codes without restarting the script

Clean & simple CLI based interaction

# Requirements

Make sure you have Python installed, then install the dependencies:

pip3 install qrcode
pip3 install pillow

# How to Run

Clone / Download the project

Open terminal in the project folder

Run the script:

python your_script_name.py


Follow the prompt:

Do you want to generate UPI QR code? (yes/no): yes
Enter your upi id: yourname@upi


The QR code will open as an image.
Scan it using any UPI app like PhonePe, Google Pay, Paytm, etc.

# Code Explanation

qrcode → Generates QR code images

pillow → Displays generated QR code

time → Adds delay for better user experience

# Notes

Currently, the script uses only the UPI ID (pa field).

If needed, you can add name (pn), amount (am) etc. later in the format:

upi://pay?pa={upi_id}&pn={Name}&am={Amount}&cu=INR

# Contributing

Feel free to fork and enhance:

Add name & amount fields

Save QR codes as image files

Build GUI using Tkinter / PyQt

Create a web version

# License

This project is open-source and free to use.
