def getUniprot(sele,mode="0"):
    if mode == "0":
        x=cmd.get_object_list(sele)
        code=x[0].split("-")[1]
    else:
        x=cmd.get_object_list(sele)
        code=x[0]
    fp = urllib.request.urlopen("https://rest.uniprot.org/uniprotkb/"+code+".txt")
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    html=mystr
    soup = BeautifulSoup(html,features="html.parser") 
    print(soup.getText())   

pymol.cmd.extend("uniprot", getUniprot)
