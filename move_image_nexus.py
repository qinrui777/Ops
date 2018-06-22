#-*- coding:utf-8 -*-
import requests
import json
import os
requests.packages.urllib3.disable_warnings()
cat_url= "https://nexus-registry.yourOrg.net/v2/_catalog"


data = {
    'username':'admin',
    'password':'pass123456'
}
s = requests.Session()


s.auth = ('admin', 'pass123456')
result = s.get(cat_url,params=data,verify=False)


print type(result)
print type(result.json())
li= result.json()["repositories"]
print li

for i in li:
        if "kubernetes" in i:
                tag_url="https://nexus-registry.yourOrg.net/v2/"+i+"/tags/list"
                #tag_url="https://nexus-registry.yourOrg.net/v2/"+i+"/tags/list"
                print "************"
                print tag_url
                result = s.get(tag_url,params=data,verify=False)
                tag = result.json()["tags"]
                print tag
                for j in tag:
                        #os.system("docker pull nexus-registry.yourOrg.net/"+i+":"+j）

                        ori_image="nexus-registry.yourOrg.net/"+i+":"+j
                        os.system("cp /root/.docker/config.json.nexus   /root/.docker/config.json")
                        os.system("docker pull "+ori_image)
                        print "docker pull "+ori_image
                        harbor_image="harbor.yourOrg.net/"+i+":"+j
                        os.system("docker tag  "+ori_image + " " +harbor_image)
                        print "docker tag  "+ori_image + " " +harbor_image
                        os.system("cp /root/.docker/config.json.harbor   /root/.docker/config.json")
                        os.system("docker push "+harbor_image)
                        #os.system("docker rmi  " + ori_image)
                        #os.system("docker rmi  " + harbor_image)
                        #print "docker push "+harbor_image
