from pathlib import Path
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTImage, LTFigure
import sys
import re

sys.path.insert(1,'..')

#pdf ="2263 QUATTRO.pdf"
pdf= "2643 WOR TECNOLOGIA LTDA.pdf"
txt = "auxiliar.txt"

def pdf2txt(pdfname, txtname):
    btxt=False
    try:
        fp = open(pdfname, 'rb')    
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
    
        laparams.char_margin = 1.0
        laparams.word_margin = 1.0
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)    
        ncount=0
        print("pdf2txt %s..." % pdfname) # informa por consola del nombre de archivo
    
        # abre archivo de texto para la salida
        fptxt = open(txtname, "w")
        # recorre el documento procesando cada página
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            # recorre la página procesando cada objeto
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    spagetxt = lt_obj.get_text().strip() + " "
                    if(spagetxt!=""):
                        btxt=True
                        fptxt.write(spagetxt)
                        #print(spagetxt)
                        #print(spagetxt.split(" "))
                        linealist = re.split(":| |\n|,",spagetxt)#convierte el string en una lista que separa las palabras por ":" " " "\n" y ","
                        linealist = listToStringSpace(linealist).replace("$"," ").split(" ")#aquí se eliminan los $ de la cadena
                        linealist = [i for i in linealist if i ] #elimina espacios en blanco de la lista
                        #print(linealist)
                        if("lunes" in linealist or "Lunes" in linealist):
                            FechaEmision = listToStringSpace(linealist)
                            print("Fecha de emision:",FechaEmision)
                        if("martes" in linealist or "Martes" in linealist):
                            FechaEmision = listToStringSpace(linealist)
                            print("Fecha de emision:",FechaEmision)
                        if("miercoles" in linealist or "Miercoles" in linealist or "miércoles" in linealist or "Miércoles" in linealist):
                            FechaEmision = listToStringSpace(linealist)
                            print("Fecha de emision:",FechaEmision)
                        if("jueves" in linealist or "Jueves" in linealist):
                            FechaEmision = listToStringSpace(linealist)
                            print("Fecha de emision:",FechaEmision)
                        if("viernes" in linealist or "Viernes" in linealist):
                            FechaEmision = listToStringSpace(linealist)
                            print("Fecha de emision:",FechaEmision)
                    spagetxt=""
            ncount+=1
    
        print("end")
        fptxt.closed
        fp.closed
    except Exception as e:
        print("Error: %s" % (e))        
    return btxt

def ExtraerInfoCotizacion(txtname):
    algo = False
    fptxt = open(txtname,'r')
    linea = fptxt.readline()
    lineaDesc=0
    lineaNeto=0
    lineaIva=0
    cont = 0
    total = 0
    while linea != "":
        linea = fptxt.readline() #devuelve un string de una linea del txt
        linealist = re.split(":|\n|",linea) #el string se convierte en una lista que separa las palabras por saltos de linea y ":"
        palabra = listToString(linealist) #
        palabra = palabra.replace("\n","")
        #print("palabra es ",palabra)
        separado = palabra.split(" ") #se separa la lista x los espacios
        separado = [i for i in separado if i ]
        #print(linealist)
        #print(separado)
        if("NOMBRE" in separado):       #se extrae el nombre del cliente
            if("DIRECCION" in separado):
                i=separado.index("NOMBRE")+1
                j=separado.index("DIRECCION")
                nombre= separado[i:j]
                nombrestr = " ".join(nombre)
                print(nombrestr)
            else:
                i=separado.index("NOMBRE")+1
                nombre = separado[i:]
                nombrestr = " ".join(nombre)
                print(nombrestr)
        if("DESC" in separado):     #descuento de la cotizacion
            lineaDesc= cont+5
            #print("LineaDescuento",lineaDesc)
        if(lineaDesc!= 0 and "NETO" in separado): 
            lineaNeto = cont+5
            #print("LineaNeto:",lineaNeto)
        elif("NETO" in separado):
            lineaNeto = cont+4
            #print("LineaNeto:",lineaNeto)
        if(lineaDesc!= 0 and "IVA" in separado):
            lineaIva = cont+6
            #print("LineaIva:",lineaIva)
        elif("IVA" in separado):
            lineaIva = cont+5
            print("LineaIva=",lineaIva)
        cont= cont+1
        if(lineaDesc == cont):
            descuento = int(separado[0].replace(".", "").replace("$",""))
            print("Descuento=",descuento)
        if(lineaNeto == cont):
            neto = int(separado[0].replace(".",""))
            print("neto =",neto)
        if(lineaIva == cont):
            valoriva = int(separado[0].replace(".",""))
            print("iva =",valoriva)
            total = valoriva+neto
            print("total = ",total)
        
        
            
    fptxt.close()
    return algo

def listToString(s):  
    
    # inicizaliza un string vacío
    str1 = ""  
    
    for ele in s:  
        str1 += ele

    return str1

def listToStringSpace(s):  
    
    # inicizaliza un string vacío
    str1 = ""  
    
    for ele in s:  
        str1 += ele + ' '

    return str1   

variable = pdf2txt(pdf,txt)
variable = ExtraerInfoCotizacion(txt)