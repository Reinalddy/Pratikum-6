print (""" 
            Nama : reinalddy
            Tugas : Pemograman
""")

i =  0 
nama = []
nim =[]
tugas=[]
uts=[]
uas=[]
nilaiakhir=[]





def tambah_data () :
    while True:
        nama1=input("Nama  : ")
        nama.append(nama1)
        nim1=input("NIM   : ")
        nim.append(nim1)
        tugas1=input("Nilai Tugas : ")
        tugas.append(tugas1)
        uts1=input("Nilai UTS : ")
        uts.append(uts1)
        uas1=input("Nilai UAS : ")
        uas.append(uas1)

        nilaiakhir1=(int(tugas1)*0.30)+(int(uts1)*0.35)+(int(uas1)*0.35)
        nilaiakhir.append(nilaiakhir1)

        more=""
        while more!="y" and more!="t":
            more=input("Tambah Data(y/t) ?")
            i+=1
            if more=="t":
                break
                 

tambah_data()        










