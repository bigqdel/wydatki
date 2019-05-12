import sys  
import os
import PySimpleGUI  as sg  
import xml.etree.ElementTree as ET  
from PIL import Image
import numpy
import datetime
from lxml import etree
import lxml.html


 
dane_xml ="wydatki.xml"  
dane_xml_xsd="wydatki.xsd"
dane_xml_xsl="wydatki.xsl"
dane_xml_xsl2="wydatki2.xsl"
xml_dodaj=[]
Kolumny = ["DataDodania","Rachunek","Kategoria",'Kwota','Data','Plik']
data_zakupu=str


def validate(xml_path: str, xsd_path: str) -> bool:#######Walidacja #####

    xmlschema_plik = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_plik)

    xml_plik = etree.parse(xml_path)
    result = xmlschema.validate(xml_plik)

    return result
def html(xml_path: str, xsl_path: str):###### transformata do html#####

    xls_plik = etree.parse(xsl_path)
    xsl_transformer= etree.XSLT(xls_plik)

    xml_plik = etree.parse(xml_path)
    result = xsl_transformer(xml_plik)

    return result



def dodaj(form_output):####### "Dodawanie kolejnego wiersza "######
    lista=form_output
    tree = ET.parse((dane_xml))  
    root = tree.getroot()

   
    Wydatek= ET.Element('Wydatek')
    DataDodania=ET.SubElement(Wydatek,'DataDodania')
    DataDodania.text =lista[0]
    Rachunek=ET.SubElement(Wydatek,'Rachunek')
    Rachunek.text=lista[1]
    Kategoria=ET.SubElement(Wydatek,'Kategoria')
    Kategoria.text=lista[2]
    Waluta=ET.SubElement(Wydatek,'Waluta')
    Waluta.text='PLN'
    Kwota=ET.SubElement(Wydatek,'Kwota')
    Kwota.text=lista[3]
    Data=ET.SubElement(Wydatek,'Data')
    Data.text=lista[4]
    Plik=ET.SubElement(Wydatek,'Plik')
    Plik.text=lista[5]
    root.append(Wydatek)
    tree.write(dane_xml)

    """
def usun():
    print('test')
    tree = ET.parse((dane_xml))  
    root = tree.getroot()
    """
def make_table(dodaj_button):### rysowanie "tabelki"########
    xml_kwota=[]
    xml_datadodania=[]
    xml_rachunek=[]
    xml_kategoria=[]
    xml_data=[]
    xml_plik=[]
    kolumna=6
    wiersz=0
    
    
    tree = ET.parse((dane_xml))  
    root = tree.getroot()
    for wydatek in root.findall('Wydatek'):
        
        wiersz=wiersz+1
        xml_data.append(wydatek.find('Data').text)
        xml_plik.append(wydatek.find('Plik').text)
        xml_datadodania.append(wydatek.find('DataDodania').text)  
        xml_kwota.append(wydatek.find('Kwota').text)
        xml_kategoria.append(wydatek.find('Kategoria').text)
        xml_rachunek.append(wydatek.find('Rachunek').text)
        
    data = [[j for j in range(kolumna)] for i in range(wiersz)]
    
    for i in range(0,wiersz):
        data[i] = [xml_datadodania[i],xml_rachunek[i],xml_kategoria[i],xml_kwota[i],xml_data[i],xml_plik[i]]
        
    return data   
 

data = make_table(0)
#################### walidacja xml 
if validate(dane_xml, dane_xml_xsd):
    print('xml zgodny z xsd :)')
    OK='XML zgodny z XSD'
else:
     print('niezgodny z xsd :(')
     OK='XML nie zgodny z XSD'
###############################


# ###wypluwamy XML - moze wyjdzie ladnie#######
sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0, 0))
###layout dla tabelki
wylistowanie = [
                  [sg.Text(OK)],
                  [sg.T('Ostatnie wpisy'),sg.Button('Pokaż Plik')],
                  [sg.Table(values=data[0:][:], headings=Kolumny, 
                        auto_size_columns=False, display_row_numbers=False, justification='center',  alternating_row_color='blue', key='table',row_colors=None,background_color=None,text_color=None)]
                  
                       
               ]  
              

##### dodawania nowego wpisu
dodajwpis = [            
            [sg.Text("Rodzaj rachunku", size=(15, 1)),sg.InputCombo(['Paragon','Faktura'],key='rachunek',size=(15, 1))],
            [sg.Text("Kategoria", size=(15, 1)),sg.InputCombo(['Jedzenie','Samochód','Rozrywka','Rachunki'],key='kategoria',size=(15, 1))],
            [sg.Text("Kwota", size=(15, 1)),sg.Input('00.00',key='kwota',size=(17, 1))],
            [sg.Text("Podaj Date", size=(15, 1)),sg.CalendarButton('Data',key='data',target='temp2'),sg.Input('pusty',key='temp2',visible=False)],
            [sg.Text("Dodaj Załącznik", size=(15, 1)),sg.FileBrowse(button_text='Wybierz',target='temp',key='plik',file_types=(("zdjecie","*.jpg"),))],
            [sg.Button('Dodaj'),sg.Button('Exit', button_color=('gray60', 'red')),sg.Button('Eksport')],
            [sg.Input('pusty',key='temp',visible=False)],
            
            [sg.Frame('',wylistowanie)]
            ]  


#okno start 
window = sg.Window('Wydatki',no_titlebar=True,grab_anywhere=True,).Layout(dodajwpis)


  
    


while True:                 # Główna Pętla  
  event, values = window.Read()  
  
  
  if event is None or event == 'Exit':  
      break  
  if event == 'Dodaj':  
       
      print(values['temp2'],"#######",values['temp'])
      if  (values['temp2'] or values['temp']) == 'pusty':
          sg.Popup("uzupelnij dane powyzej")

      else:
        im=Image.open(values['temp'])
        plik_png=datetime.datetime.today().strftime("%Y-%m-%d %H%M%S")+'.png'
        im.save(plik_png,"PNG")
        xml_dodaj=[str(datetime.datetime.today()).split()[0],values['rachunek'],values['kategoria'],values['kwota'],values['temp2'].split()[0],plik_png]
        dodaj(xml_dodaj)
        data=make_table(0)
        window.FindElement('table').Update(values = data) 
      
      
     
  if event == "Eksport":  
      
      
      html(dane_xml,dane_xml_xsl2).write("eksportlista.html",pretty_print=True)
      html(dane_xml, dane_xml_xsl).write("eksportabela.html", pretty_print=True)
      
  if event =='Pokaż Plik':
      
      ktorywiersz=(values['table'])
      if len(ktorywiersz) !=0:
          sgimage=data[ktorywiersz[0]][5]
          plotno= [
            [sg.Image(filename=sgimage, key='image',size=(1080,600))]
            ]
          obrazek = sg.Window('Skan',size=(None,None),force_toplevel=False).Layout(plotno)
          event, values = obrazek.Read()    
          obrazek.Close()
      
      else:
          sg.Popup("wybierz wiersz z tabeli")
      
      
      

     
window.Close()


