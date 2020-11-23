#! bin/bash

sudo cat > /etc/hosts << EOF 
# Host Database
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
##
127.0.0.1 localhost
255.255.255.255 broadcasthost
::1             localhost
159.138.133.209 bss.kwvpn.com 
159.138.133.209 bss.kuai500app.com 
159.138.133.209 bss.kuaiapp.net.cn 
159.138.133.209 bss.kuai500.net 
159.138.133.209 bss.huabotech.com.cn 
159.138.133.209 static.kwvpn.com 
159.138.133.209 static.kuai500app.com 
159.138.133.209 static.kuaiapp.net.cn 
159.138.133.209 static.kuai500.net 
159.138.133.209 static.huabotech.com.cn
EOF
