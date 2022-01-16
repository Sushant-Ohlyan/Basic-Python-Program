salesamount=float(input("enter sales amount"))
if salesamount<=20000:
    discountrate=10
else:
    discountrate=17.5
discount=salesamount*discountrate/100
afterdiscount=salesamount-discount
salestaxrate=float(input("enter sales tax rate(5-12%::::::)"))
salestax=afterdiscount*salestaxrate/100
netpayable=afterdiscount-salestax
print("purchace amount::",salesamount)
print("dicount offered @@@@",discountrate,"%::::",discount)
print("sales tax@@@",salestaxrate,"%::",salestax)
print("netpayable amount::",netpayable)