input=open("input.txt")
inpF=input.read()
input.close()
output=open("output.txt","w",)
output.write(inpF)
output.close()
