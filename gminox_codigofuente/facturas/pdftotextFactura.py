from pathlib import Path
import sqlite3
from sqlite3 import Error
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTImage, LTFigure
from gminox.settings import NombreDB
import sys
import re

sys.path.insert(1,'..')

def sql_connection():
    try:
        con = sqlite3.connect(NombreDB)
        return con
    except Error: 
        print(Error)


def pdf2txtCompra(pdfname, txtname):
    btxt=False
    con=sql_connection()
    cursorObj = con.cursor()
    ListaDB = []
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
        cont=0
        #print("pdf2txt %s..." % pdfname) # informa por consola del nombre de archivo
    
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
                        linealist = re.split(":| |\n",spagetxt)
                        linealist = listToStringSpace(linealist).replace("$"," ").split(" ")
                        #print(linealist)
                        #print(cont)
                        if(cont==1):
                            NombreEmpresa=spagetxt
                            ListaDB.append(NombreEmpresa)
                            #print(NombreEmpresa)
                        if("77.842.710-9" in linealist):
                            Empresa1="SANCHEZ E HIJAS METALMECANICA LTDA"
                            #print("Comprado por:",Empresa1)
                        if("76.285.508-9" in linealist):
                            Empresa2="METALMECANICA DIVISION LASER GMINOX S.B. LIMITADA"
                            #print("comprado por:",Empresa2)
                        if("Nº" in linealist):
                            i=linealist.index("Nº")+1
                            Folio=str(linealist[i])
                            ListaDB.append(Folio)
                            #print("Nº:",Folio)
                        if("Emision" in linealist):
                            FechaEmision=listToStringSpace(linealist[2:-1])
                            #print("Fecha:",FechaEmision)
                        if("MONTO" and "EXENTO" in linealist):
                            i=linealist.index("EXENTO")+1
                            if(linealist[i]!=""):
                                MontoExento = int(listToString(linealist[i]).replace(".",""))
                                ListaDB.append(MontoExento)
                                cursorObj.execute('''INSERT INTO Factura(name,id,total) VALUES(?, ?, ?)''', ListaDB)
                                con.commit() 
                                #print("MontoExento:",MontoExento)  
                        if("MONTO" and "NETO" in linealist):
                            j=linealist.index("NETO")+1
                            MontoNeto = int(listToString(linealist[j]).replace(".",""))
                            ListaDB.append(MontoNeto)
                            #print("Neto: ",MontoNeto)
                        if("I.V.A." in linealist):
                            k=linealist.index("I.V.A.")+3
                            MontoIva = int(listToString(linealist[k]).replace(".",""))
                            #print("IVA: ",MontoIva)
                            ListaDB.append(MontoIva)
                            total=MontoNeto+MontoIva
                            #print("total: ",total)
                            ListaDB.append(total)
                        cont+=1
                elif isinstance(lt_obj, LTFigure):
                    #print("LTFigure, pte implementar!")
                    spagetxt=""
            ncount+=1
        cursorObj.execute('''INSERT INTO facturas_facturacompragminox(Proveedor,NumeroFactura,Monto,Iva,Total) VALUES(?, ?, ?,?,?)''', ListaDB)
        con.commit()
        #print("end")
        fptxt.closed
        fp.closed
    except Exception as e:
        print("Error: %s" % (e))        
    return btxt

def pdf2txtVenta(pdfname, txtname):
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
        lineaNeto = 0
        LineaIva = 0
        LineaFolio = 0
        ncount=0
        cont=0
        i=0
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
                        linealist = re.split(":| |\n",spagetxt)
                        linealist = listToStringSpace(linealist).replace("$"," ").split(" ")
                        #print(linealist)
                        #print(cont)
                        if("77.842.710-"  in linealist):
                            Empresa1="SANCHEZ E HIJAS METALMECANICA LTDA"
                            print("Vendido por:",Empresa1)
                        if("76.285.508-" in linealist):
                            Empresa2="METALMECANICA DIVISION LASER GMINOX S.B."
                            print("vendido por:",Empresa2)
                        if("FACTURA" in linealist and "ELECTRONICA" in linealist):
                            LineaFolio = cont+1
                        if(LineaFolio == cont and cont != 0):
                            Folio = linealist[0].replace("Nº","")
                            print("Folio:",Folio)
                        if("Emision" in linealist):
                            FechaEmision=listToStringSpace(linealist[2:-1])
                            print("Fecha:",FechaEmision)
                        if("MONTO" in linealist and "NETO" in linealist):
                            lineaNeto = cont+8
                        if(lineaNeto == cont and cont!= 0):
                            MontoNeto = int(listToString(linealist[0].replace(".","")))
                            print("Monto Neto:",MontoNeto)    
                        if("I.V.A." in linealist):
                            LineaIva = cont+8
                        if(LineaIva == cont and cont != 0):
                            MontoIva = int(listToString(linealist[0].replace(".","")))
                            print("MontoIva:",MontoIva)
                            print("Total:",MontoNeto+MontoIva)
                        if("SEÑOR(ES)" in linealist and "R.U.T." in linealist):
                            i = linealist.index("SEÑOR(ES)")+1
                            j = linealist.index("R.U.T.")
                            NombreEmpresa = listToStringSpace(linealist[i:j])
                            print("Vendido a:",NombreEmpresa)
                        cont+=1
                elif isinstance(lt_obj, LTFigure):
                    print("LTFigure, pte implementar!")
                    spagetxt=""
            ncount+=1
    
        print("end")
        fptxt.closed
        fp.closed
    except Exception as e:
        print("Error: %s" % (e))        
    return btxt

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