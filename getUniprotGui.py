from pymol.Qt import QtWidgets
tb=None
def getUniprotGui(sele):
    # pymol.Qt provides the PyQt5 interface, but may support PyQt4 and/or PySide as well      
    global tb
    print("hello")
    x=cmd.get_object_list(sele)
    code=x[0].split("-")[1]
    fp = urllib.request.urlopen("https://rest.uniprot.org/uniprotkb/"+code+".txt")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    html=mystr
    soup = BeautifulSoup(html,features="html.parser")
    txt=soup.getText()
    print(txt)
    if tb == None:
        tb = QtWidgets.QTextBrowser()
    tb.setObjectName(u"textBrowser")
    tb.setText(txt)
    tb.show()
        
pymol.cmd.extend("unigui", getUniprotGui)
