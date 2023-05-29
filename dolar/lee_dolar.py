ent = open("dolar.txt")
sal = open("dolar1.txt", "w")
for linea in ent:
    linea = linea.rstrip("\n")
    lista = linea.split("\t")
    st1 = lista[0]
    st2 = lista[1]
    if st2 != '':
        st1_s = st1.replace(".", "-")
        st2_s = st2.replace(".","")
        st2_s = st2_s.replace(",", ".")
        sal.write(st1_s+" "+st2_s+"\n")
sal.close()


