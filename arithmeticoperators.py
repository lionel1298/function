#given an exlusive price and VAT and tax provided by the user calculate 
# the VAT amount then return the inclusive price 
exclusive_price=51.80
VAT_tax =0.16
VAT_amount=0
inclusive_price=0
VAT_amount=exclusive_price*VAT_tax
inclusive_price=exclusive_price+VAT_amount
print(inclusive_price)
#given an inclusive price and tax provided by the user calculate the VAT amount and exclusive price
inclusiveprice=60.087999999
VATtax=0.16
exclusiveprice=0
VATamount=inclusiveprice*VATtax
exclusiveprice=inclusiveprice-VATamount
print(exclusiveprice)
#functions
#block of code executed when you called in the global space
#def key word

def calculate_VAT(exclusive_price, VAT_tax):
    VAT_amount=0
    inclusive_price=0
    VAT_amount=exclusive_price*VAT_tax
    inclusive_price=exclusive_price+VAT_amount
    print(inclusive_price)
def userinput():
    excl=float(input("enter exclusive price"))
    vat_tax=float(input("enter the VAT tax"))
    calculate_VAT(excl,vat_tax)


userinput()






