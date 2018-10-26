#!/bin/bash

date=`date "+%Y.%m.%d" --date="-1 month"`
echo ${date}

#svc=(nginx-int nginx-development nginx-preprod )

svcArray=(nginx-int
nginx-development
int03-integration-order
int02-coupon
int03-coupon
)

echo ${#svcArray[@]}

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