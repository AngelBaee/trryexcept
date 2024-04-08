try:
    kk = open("demofile.txt")
    try:
        kk.write("blabla")
    except:
        print("issues are detected while writting")
    finally:
        kk.close()
except:
    print("issues are detected while opening the file" )            