def maker():
    file = open("result.txt","r")
    result = file.read()
    
    html_base ="<html><head><title>Result</title></head><body bgcolor='#ffffff'><pre style='font-size:20;'>{}</pre></body></html>".format(result)
    
    file = open("result.html","w")
    file.write(html_base)
    file.close

    file.close()
    
maker()