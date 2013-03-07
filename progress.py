import sys
import time

def iterator(it, out = sys.stderr, size = 60, prefix = ""):
    count = len(it)
    start = time.time()
    def _eta(_i):
        if _i == 0:
            return ""
        r = (time.time() - start) * (count-_i) / _i
        if r > 86400:
            return "{d} days, {h:03d}:{m:03d}:{s:03d}".format(
                days=int(r)//86400, 
                h=int(r%86400)//3600,
                m=int(r%3600)//60,
                s=int(r%60))
        else:
            return "{h:02d}:{m:02d}:{s:02d}".format(
                h=int(r%86400)//3600,
                m=int(r%3600)//60,
                s=int(r%60))            

    def _show(_i):
        x = int(size*_i/count)
        out.write("{prefix}[{done}{throb}{remaining}] {current}/{total} {eta}\r".format(
                prefix=prefix,
                done="#"*x,
                throb=["|","/","-","\\"][_i%4],
                remaining="."*(size-x),
                current=_i,
                total=count,
                eta=_eta(_i)
                ))
        out.flush()
    
    _show(0)
    for i, item in enumerate(it):
        yield item
        _show(i+1)
    out.write("\n")
    out.flush()
