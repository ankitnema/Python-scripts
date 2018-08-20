#Google search python scrit
#created by 'Ankit Nema'

import webbrowser

new=2;

url='http://www.google.com/#q=';
ip=input("Query for search : ")
webbrowser.open(url+ip,new=new);
print(url)