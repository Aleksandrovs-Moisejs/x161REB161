while True:
    result = input("Ievadi trīsstura leņķi alfa robežās no 1-89:\n")
    if 1 <= int(result) <= 89:
        print "Ļenķis ir %d grādi:" %result
        d = int(result)*3.14/180
        print "Leņķis ir %f radiāni" %d
        break;
    print "Netrāpīji robēžas mēģini vēlreiz!"
    
