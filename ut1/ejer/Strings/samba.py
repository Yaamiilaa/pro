samba = '//1.1.1.1/eoi/python'

samba_strip = samba.strip('/')
host = samba_strip.split('/')
path =  samba_strip.rsplit('/')

print(host)
print(path)