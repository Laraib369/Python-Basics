for i in range (2,21):
    with open(f"tables/multiplication_table_of_{i}.txt","w") as f:
        for j in range(21):
            f.write(f"{i}x{j} ={i*j}")
            if (j!= 20) :
               f.write("\n")
   
