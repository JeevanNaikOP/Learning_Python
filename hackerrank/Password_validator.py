x=input()

y,z=0,0

for i in (x):

   if i.isdigit():

      y+=1

   if(i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='&' or i=='*'):

      z+=1 

if y>=2 and z>=2 and len(x)>7:

   print('Strong')

else:

   print('Weak')   

      
