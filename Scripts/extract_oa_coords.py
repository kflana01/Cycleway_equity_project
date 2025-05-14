from lxml import etree
from pykml import parser

kml_file_path = '/Users/karen/Cycleway_equity_project/Data sources/5.3 Census data/Output_Areas_(December_2021)_Boundaries_EW_BFE_(V9).kml'
Borough_list = ("Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden", "Croydon", "City of London", "Ealing", "Enfield", "Greenwich", "Hackney",
                "Hammersmith and Fulham", "Haringey", "Harrow", "Havering", "Hillingdon", "Hounslow", "Islington", "Kensington and Chelsea",
                "Kingston upon Thames", "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge", "Richmond upon Thames", "Southwark", "Sutton",
                "Tower Hamlets", "Waltham Forest", "Wandsworth", "Westminster")



for borough in Borough_list:
    print("borough", borough)
# parse the input file into an object tree
    with open(kml_file_path) as f:
        tree = parser.parse(f)

# get a reference to the "Document.Folder" node
        folder = tree.getroot().Document.Folder

# iterate through all "Document.Folder.Placemark" nodes and find and remove all nodes
# which contain child node "name" with content "ZONE"

        for pm in folder.Placemark:

            data = {item.get("name"): item.text for item in pm.ExtendedData.SchemaData.SimpleData}
            index = data["LSOA21NM"].find(borough)
            if (index == -1):
                parent = pm.getparent()
                parent.remove(pm)

# convert the object tree into a string and write it into an output file
        with open('/Users/karen/Cycleway_equity_project/Data sources/7.2.1 Census data/'+borough+'.kml', 'wb') as output:
            output.write(etree.tostring(folder, pretty_print=True))
    f.close()