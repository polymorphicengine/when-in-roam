#import library.writetag.server as server
import library.writetag.write as write

if __name__ == '__main__':
    #server.startDebug()
    print("HELLO")
    write.write_tag("B", "D", 3)
    print("OK")
