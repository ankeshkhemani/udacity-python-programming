import webbrowser
import time
total_breaks = 3
break_count = 0
break_delay = 10
print "this program started on %s" % time.ctime()
while(break_count < total_breaks):
    time.sleep(break_delay)
    webbrowser.open("http://www.rainymood.com/")
    break_count = break_count+1
