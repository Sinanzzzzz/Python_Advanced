#Write

f = open('k.txt','w')        

# f.write(string)      #format
# f.writelines(list)


# f.write("Hello\n")
# f.write("Python\n")
# OR oru line il kodukkaam

f.writelines(["Hello\n","Python\n"])

f.close()