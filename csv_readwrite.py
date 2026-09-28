# # CSV READ

# import csv

# f=open("data.csv","r")

# content = csv.reader(f)

# for row in content:
#     print(row)
    
# f.close()

# CSV Write
import csv

f=open("data.csv","w",newline="")

content = [
    ["title","author","place"],
    ["book1","john","ekm"],
    ["book2","sam","tvm"]
]
writer = csv.writer(f)
writer.writerows(content)   # OR for row in content:
                            #       writer.writerow(row)

f.close()