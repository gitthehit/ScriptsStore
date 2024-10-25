import time
inner = 500
for n in range(inner+1):
    loading = round(n/inner*100)
    print(f"loading {loading}%",end='\r')
    time.sleep(0.02)
print('\n'+time.ctime())
