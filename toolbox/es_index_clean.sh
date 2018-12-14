#!/bin/bash

date=`date "+%Y.%m.%d" --date="-1 month"`

#echo ${date}
#date "+%Y.%m.%d" --date="-10 day"

#svc=(nginx-int nginx-development nginx-preprod )

svcArray=(nginx-int
nginx-development
)

#echo ${#svcArray[@]}

for i in ${svcArray[@]};do

    index=(`curl -s -k -XGET http://localhost:9200/_cat/indices/?v|awk '{print $3}'|sed '1d'| grep $i`)
    for j in ${index[*]}
    {
    if [ "$i-$date" \> "$j" ];then
        #echo "$j"
        echo "--- curl -k -XDELETE "http://localhost:9200/$j" ---"
        curl -k -XDELETE "http://localhost:9200/$j"
    fi;
    }

done
