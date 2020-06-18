fileobj = open("test.csv", "r") #r, w, or a are the options
datalist = fileobj.readlines()
fileobj.close()
#print(datalist)

conflist = [ ]
for country in datalist:
    #print(country)
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    #print(pname + cname + lat + lon + conf)
    conflist.append({"pname":pname, "cname":cname, "lat":lat, "lon":lon, "conf":conf})
    
#print(conflist)
conflist.sort(key=lambda s: s['confirmed'], reverse=True)
fileout = open("test.js", "w")
fileout.write("data =" + str(conflist))
fileout.close()
