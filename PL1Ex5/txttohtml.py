
import re 

def txttohtml(docTXT):
    dicionario = dict()
    total = 0
    with open("train.html", "w") as docHTML:
        docHTML.write("<!DOCTYPE html>\n")
        docHTML.write("<html>\n")
        docHTML.write("<head>\n")
        docHTML.write("<title>Machine Learning: datasets de treino</title>\n")
        docHTML.write("<meta charset=\"utf8\"> </meta>\n")
        docHTML.write("<link c<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" id=\"css_0\">\n")
        docHTML.write("</head>\n")
        docHTML.write("<body bgcolor=\"#B0C4DE\">\n")
        docHTML.write("<h1><center>Categorias</center></h1>\n")
        docHTML.write("<div class=\"container\"> ")
        

         
        linha = re.findall(r'([BI])-([A-Z\_]+)(\t[A-Za-z0-9]+)?', docTXT)
        dicionario = {}
        nome = ""
        nome_aux = ""
        _, cur_categoria, _ = linha[0]
        for primeiraletra, categoria, nome in linha:
            nome = nome.strip()
            if primeiraletra == 'B':
                dicionario.setdefault(cur_categoria,set())
                if nome: 
                    dicionario[cur_categoria].add(nome_aux.strip())
                    nome_aux = ""
                cur_categoria = categoria
                nome_aux = nome_aux + " " + nome 
            
            elif primeiraletra=='I':
                nome_aux = nome_aux + " " + nome
                
                
        for cat, lis in dicionario.items():
            docHTML.write("<div class=\"item\"><a href=\"{categoria}.html\">{categoria}</a><span>{total}</span></div>".format(categoria=cat, total = len(lis)))  
            with open("{categoria}.html".format(categoria=cat), "w") as f2:
                f2.write("<!DOCTYPE html>\n")
                f2.write("<html>\n")
                f2.write("<head>\n")
                f2.write("<title>{categoria}</title>\n".format(categoria=cat))
                f2.write("<meta charset=\"utf8\"> </meta>\n")
                f2.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" id=\"css_0\">\n")
                f2.write("</head>\n")
                f2.write("<body bgcolor=\"#B0C4DE\">\n")
                f2.write("<h1><center><a href=\"train.html\">{categoria}</a></center></h1>\n".format(categoria=cat))
                f2.write("<dd> ")
                
                for name in lis:
                    f2.write("<dl>{lista}</dl>".format(lista=name))
                    
                f2.write("</dd> ")
                f2.write("</body>\n")  
                f2.write("</html>\n") 

        docHTML.write("</div> ")
        docHTML.write("</body>\n")  
        docHTML.write("</html>\n")    



    print(docHTML)


with open("train.txt", encoding="utf8") as f: 
    conteudo = f.read()  
    txttohtml(conteudo)

