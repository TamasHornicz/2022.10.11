import math

testtömeg = int(input("Írja be a testtömegét: "))

magassag = int(input("Írja be a magasságát(cm): "))

magassag2 = magassag/100

magassag3 = magassag2*magassag2

TTI = testtömeg/magassag3

if(TTI < 18):
    print("Vékony alkat vagy.")
elif(18 <= TTI <=25 ):
    print("Normális alkatod van.")
else:
    print("Túlsúlyos vagy.")
