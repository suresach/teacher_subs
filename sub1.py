import random
teachers_abps = ["RO  " , [ "BLANK" , "9-B"   , "BLANK" , "12-C"  , "9-A"    , "BLANK"   , "11-B and C" , "9-C"],
                 "RCP  " , ["BLANK" , "9-C"   , "12-A"  , "BLANK" , "11-A"   , "BLANK"   , "BLANK"      , "BLANK" ] , 
                 "CBM  " , ["BLANK" , "SAFETY", "11-C"  , "BLANK" , "12-B"   , "10-A B C" , "11- A B C" , "BLANK"], 
                 "PD  " , [ "BLANK" , "12-B C", "BLANK" , "11-B C", "10-A"   , "BLANK"    , "BLANK"     , "10-A"], 
                 "MKM  " , [ "10-A" , "12-B"  , "BLANK" , "11-B"  , "BLANK"  , "BLANK"    , "9-C"       , "BLANK"] , 
                 "AKS  " , [ "11-C" , "12-C"  , "BLANK" , "BLANK" , "12-C"   , "BLANK"    , "BLANK"     , "BLANK"],
                 "JS  " , [  "11-A" , "BLANK" , "12-C"  , "BLANK" , "9-C"    , "11-A"     , "12-C"      , "7 - A Comm."], 
                 "Ssa  " , [ "BLANK" , "BLANK", "11-A"  , "BLANK" , "12-A"   , "BLANK"    , "10-C"      , "BLANK"] , 
                 "AKM  " , [ "12-B" , "11-B"  , "9-B"   , "BLANK" , "BLANK"  , "BLANK"    , "10-A"      , "BLANK"], 
                 "PA  " , [  "12-A" , "10-B"  , "BLANK" , "12-B"  , "BLANK"  , "11-B"     , "BLANK"     , "BLANK"]]

def sub_teach(teacher , teacher_2) :
    
    teacher = int(str(teacher))
    teacher_2 = int(str(teacher_2))
    
    for mun in range (0,7) :
        for num in range (0,8) :
            abc = random.randrange(0, 20, 2)
            
            if (teachers_abps[teacher][num] != "BLANK") :
                
                if ((teachers_abps [abc + 1][num] == "BLANK") and (teachers_abps[abc] != teachers_abps[teacher_2 - 1])) :
                    teachers_abps [abc + 1][num] = teachers_abps[abc] + teachers_abps[teacher][num]
                    
                    teachers_abps [teacher][num] = teachers_abps[abc + 1][num]
    print (teachers_abps[teacher - 1] )
    print (teachers_abps[teacher])
    
    for mun in range (0,7) :
        for num in range (0,8) :
            abc = random.randrange(0, 20, 2)
            
            if (teachers_abps[teacher_2][num] != "BLANK") :
                
                if (teachers_abps [abc + 1][num] == "BLANK") and (teachers_abps[abc] != teachers_abps[teacher - 1]) :
                    teachers_abps [abc + 1][num] = teachers_abps[abc] + teachers_abps[teacher_2][num]
                    
                    teachers_abps [teacher_2][num] = teachers_abps[abc + 1][num]
    print teachers_abps[teacher_2 - 1] 
    print teachers_abps[teacher_2]