from lxml import etree 
import xml.etree.ElementTree as ET
import requests

xml_file= "./Font/calculation_view.xml"


#Pegando a árvore do xml
tree = etree.parse(xml_file)

#Extraindo a raiz do XML
root = tree.getroot()
print("Raiz: ",root)

# Abra um arquivo Markdown para escrita
markdown_file = open("output.md", "w")

# Escreva o título do documento
markdown_file.write("# Documentação da View \n\n")

#print("Exibindo todos os nós")
#filtro = "*"
#for child in root.iter(filtro):
#    print(child.tag, child.text)

#Realizando uma iteração : retornando todos os filhos (diretos ou não)

print("Tabelas fontes da view")
filter = "DataSource"
#for child in root.iter(filter):
#    print(child.tag, child.text)

for i, item in enumerate(root.findall("dataSources/DataSource")):
    print("{}: {}".format(i, item.attrib["id"]))
    var_id = "{}: {}".format(i, item.attrib["id"])
    markdown_file.write("\n")
    markdown_file.write("{}\n".format(var_id))

nsmap = {
  'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

#Exibindo o Output de Cada Nó

for i, item in enumerate(root.findall("calculationViews/calculationView")):
    print("\n")
    print("Calculation Node")
    markdown_file.write("## Calculation Node\n")

    print("{}:{}: ".format(i, item.attrib["id"]), item.attrib[ f"{{{nsmap['xsi']}}}type" ],)
    var_attrib = "{}:{}: ".format(i, item.attrib["id"]), item.attrib[ f"{{{nsmap['xsi']}}}type" ]
    markdown_file.write("{}\n".format(var_attrib))


    #se o nó for do tipo JOIN
    if item.attrib[ f"{{{nsmap['xsi']}}}type" ] == "Calculation:JoinView":
        print("Ordem do Join: {} ".format(item.attrib["joinOrder" ] ))
        var_ordem_j = "{}".format(item.attrib["joinOrder" ] )
        markdown_file.write("{}\n".format(var_ordem_j))

        print("Tipo do Join: {} ".format(item.attrib["joinType" ] ))
        var_tipo_j = "{}".format(item.attrib["joinOrder" ] )
        markdown_file.write("{}\n".format(var_tipo_j))

        print("Campos no Join:")

        var_campo_j = "{}".format(item.attrib["joinOrder" ] )
        markdown_file.write("{}\n".format(var_campo_j))

        for atb in item.findall("viewAttributes/viewAttribute"):
            print(atb.attrib["id"])
            var_atb_id = atb.attrib["id"]
            markdown_file.write("{}\n".format(var_atb_id))

        print("Nós inseridos no Join")
        markdown_file.write("Nós inseridos no Join")

        for ipt in item.findall("input"):
            print(ipt.attrib["node"])
            var_inp_id = ipt.attrib["node"]
            markdown_file.write("{}\n".format(var_inp_id))

        print("Conexão do Join")
        markdown_file.write("Conexão do Join")

        for con in item.findall("joinAttribute"):
            print(con.attrib["name"])
            var_con_id = con.attrib["name"]
            markdown_file.write("{}\n".format(var_con_id))
    else:
        print("Node Output")
        markdown_file.write("Node Output")

        for atb, item in enumerate(root.findall("calculationViews/calculationView/viewAttributes/viewAttribute")):
           print("  {}: {}".format(atb, item.attrib["id"]))
           var_node_id = "  {}: {}".format(atb, item.attrib["id"])
           markdown_file.write("{}\n".format(var_node_id))

        print(" Campos calculados")  
        markdown_file.write(" Campos calculados")

        for calc, item in enumerate(root.findall("calculationViews/calculationView/calculatedViewAttributes/calculatedViewAttribute")):
            print("     {}: {} {}".format(calc, item.attrib["id"], item.attrib["datatype"]))
            var_calc = "     {}: {} {}".format(calc, item.attrib["id"], item.attrib["datatype"])
            markdown_file.write("{}\n".format(var_calc))

        formula = item.find('formula').text
        print("         Formula do campo: ",formula)
        var_form = "         Formula do campo: ",formula
        markdown_file.write("{}\n".format(var_form))

# Feche o arquivo Markdown
markdown_file.close()