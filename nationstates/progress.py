import sys
import time

def format_duration(r):
    if r >= 31536000:
        return "{y} year{yp}, {d} day{dp}, {h:02d}:{m:02d}:{s:02d}".format(
            y=int(r)//31536000,
            yp=['', 's'][int(r)//31536000 != 1],
            d=int(r%31536000)//86400,
            dp=['', 's'][int(r%31536000)//86400 != 1],
            h=int(r%86400)//3600,
            m=int(r%3600)//60,
            s=int(r%60))        
    elif r >= 86400:
        return "{d} day{dp}, {h:02d}:{m:02d}:{s:02d}".format(
            d=int(r)//86400, 
            dp=['', 's'][int(r)//86400 != 1],
            h=int(r%86400)//3600,
            m=int(r%3600)//60,
            s=int(r%60))
    else:
        return "{h:02d}:{m:02d}:{s:02d}".format(
            h=int(r%86400)//3600,
            m=int(r%3600)//60,
            s=int(r%60))            


def iterator(it, out = sys.stderr, size = 50, prefix = ""):
    count = len(it)
    start = time.time()
    def _eta(_i):
        if _i > 0:
            return (time.time() - start) * (count-_i) / _i
        else:
            return 0
    def _show(_i):
        x = int(size*_i/count)
        out.write("{prefix}[{done}{throb}{remaining}] {current}/{total} {elapsed} {eta}\r".format(
                prefix=prefix,
                done="#"*x,
                throb=["|","/","-","\\"][_i%4],
                remaining="."*(size-x),
                current=_i,
                total=count,
                elapsed=format_duration(time.time() - start),
                eta=format_duration(_eta(_i))
                ))
        out.flush()
    
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    out.write("\n")
    out.flush()
