fout = open('D:\other.txt','w')
str = r'''fout.write("fout = open('D:\other.txt','w')\n" + "str = r\'\'\'" + str + "\'\'\'\n" + "other = \"str = \" + str" + "\n" + str + "\n"  + "fout.close();\n" + "fin = open('D:\other.txt')\n" + "content = fin.read()\n" + "print content\n")'''
other = "str = " + str
fout.write("fout = open('D:\other.txt','w')\n" + "str = r\'\'\'" + str + "\'\'\'\n" + "other = \"str = \" + str" + "\n" + str + "\n"  + "fout.close();\n" + "fin = open('D:\other.txt')\n" + "content = fin.read()\n" + "print content\n")
fout.close();
fin = open('D:\other.txt')
content = fin.read()
print content
