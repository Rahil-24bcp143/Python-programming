
name = input("Enter name: ")
phone = input("Enter phone number: ")
email = input("Enter email: ")

vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD"""

with open("contact.vcf", "w") as f:
    f.write(vcard)

