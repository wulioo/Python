#!/bin/bash

filebeat=`ps -ef | grep filebeat | awk 'NR==2{print $2}'|wc -l`
pid=`ps -ef | grep filebeat | awk 'NR==2{print $2}'`
now_day=`date '+%d'`
now_month=`date '+%Y%m'`


# -------关闭filebeat进程----------
if [ "${filebeat}" == "1" ];then
      killall filebeat
      echo "kill filebeat scucceed"
fi

# -------替换fileat.yml里面的（月份,日期）
sed  -i 's/runtime\/log\/[0-9]\{6\}\/[0-9]\{2\}.log/runtime\/log\/'${now_month}'\/'${now_day}.log'/g' /usr/local/filebeat/fileat.yml

echo "--------重启filebeat进程----------"
cd /usr/local/filebeat/ && nohup ./filebeat -e -c fileat.yml &
