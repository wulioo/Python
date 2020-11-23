#!/bin/bash

shelpath=$(cd `dirname $0`; pwd)

echo "===============查看服务器之间是否通信================"
ping=`ping  -c 3 10.126.35.84| awk 'NR==3 {print $8}'`
if [ "${ping}" == "ms" ]; then
    echo "succed"
else
    echo "failed"
    exit 1
fi
sleep 3
echo "===============开始安装================"
tar xzvf filebeat-6.5.4-linux-x86_64.tar.gz -C ${shelpath} >/dev/null
mv ${shelpath}/filebeat-6.5.4-linux-x86_64 filebeat && cd ${shelpath}/filebeat
cat >> ./fileat.yml <<EOF
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /var/log/zdh.log
  multiline.pattern: 'Get'
  multiline.negate: true
  multiline.match: after
  multiline.flush_pattern: '------'
  fields:
    logtype: "bss"
  index.number_of_shards: 3
output.logstash:
  hosts: ["10.126.35.85:5044"]

EOF
if [ $? -eq 0 ]; then
    echo "succed"
else
    echo "failed"
    exit
fi
sleep 3
echo "===============filebeat启动================"
nohup ./filebeat -e -c fileat.yml &
