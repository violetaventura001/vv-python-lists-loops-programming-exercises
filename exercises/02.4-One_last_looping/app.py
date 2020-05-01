my_sample_list = ['Esmeralda','Kiko','Ruth','Lebron','Pedro','Maria','Lou','Fernando','Cesco','Bart','Annie']

#Your code here:
my_sample_list[1] = "Steven" # Kiko was changed to Steven [1] indicates the index position that was changed
my_sample_list.remove("Annie") #Annie was a hard code removal
my_sample_list.insert(10, "Pepe") #Pepe was inserted into the index position 10
my_sample_list[0] ="Ruth" + my_sample_list[4]

for x in range(len(my_sample_list)-1, -1, -1):
  print(my_sample_list[x]) 
