def CheckSize(size):

    final = int

    if(size > 1000):       


        finalsize  =  size / 1000

        final = str(int(finalsize))  + "Kb"

        if (size >  1000000):

             finalse = size / 10000

             final = str(int(finalse))

             final = final[0]+"."+final[1]+final[2] +" Mb"

             if(size > 10000000):

                 finalse = size / 10000

                 final = str(int(finalse))

                 final = final[0]+final[1]+"."+final[2] +" Mb"

                 if(size > 100000000):

                     finalse = size / 10000

                     final = str(int(finalse))

                     final = final[0]+final[1]+final[2]+"."+final[4] +" Mb"

                     if(size >1000000000):

                         final = size /1000000000
                         
                         final = str(final) +" GB"


      

    return str(final)
    
    pass
