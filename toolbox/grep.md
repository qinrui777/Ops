ps aux|grep '[o]ms'




`$ ps -ef| grep docker`


```
    0    88     1   0 Wed04PM ??         0:00.02 /Library/PrivilegedHelperTools/com.docker.vmnetd
  510   629   571   0 Wed04PM ??         0:01.43 /Applications/Docker.app/Contents/MacOS/com.docker.supervisor -watchdog fd:0
  510   635   629   0 Wed04PM ??         0:00.12 com.docker.osxfs serve --address fd:3 --connect vms/0/connect --control fd:4 --log-destination asl
  510   636   629   0 Wed04PM ??         0:03.06 com.docker.vpnkit --ethernet fd:3 --port fd:4 --introspection fd:5 --diagnostics fd:6 --vsock-path vms/0/connect --host-names host.docker.internal,docker.for.mac.host.internal,docker.for.mac.localhost --gateway-names gateway.docker.internal,docker.for.mac.gateway.internal,docker.for.mac.http.internal --vm-names docker-for-desktop --listen-backlog 32 --mtu 1500 --allowed-bind-addresses 0.0.0.0 --http /Users/ruqin/Library/Group Containers/group.com.docker/http_proxy.json --dhcp /Users/ruqin/Library/Group Containers/group.com.docker/dhcp.json --port-max-idle-time 300 --max-connections 2000 --gateway-ip 192.168.65.1 --host-ip 192.168.65.2 --lowest-ip 192.168.65.3 --highest-ip 192.168.65.254 --log-destination asl
  510   637   629   0 Wed04PM ??         0:02.18 com.docker.driver.amd64-linux -addr fd:3 -debug
  510   643   637   0 Wed04PM ??        14:02.41 com.docker.hyperkit -A -u -F vms/0/hyperkit.pid -c 4 -m 2048M -s 0:0,hostbridge -s 31,lpc -s 1:0,virtio-vpnkit,path=s50,uuid=99760b23-a6a5-452d-8726-e7a490c182c7 -U 16943701-e00a-4122-ae27-67644f80f7c6 -s 2:0,ahci-hd,file:///Users/ruqin/Library/Containers/com.docker.docker/Data/vms/0/Docker.qcow2?sync=os&buffered=1,format=qcow,qcow-config=discard=true;compact_after_unmaps=262144;keep_erased=262144;runtime_asserts=false -s 3,virtio-sock,guest_cid=3,path=vms/0,guest_forwards=2376;1525 -s 4,ahci-cd,/Applications/Docker.app/Contents/Resources/linuxkit/docker-for-mac.iso -s 5,ahci-cd,vms/0/config.iso -s 6,virtio-rnd -s 7,virtio-9p,path=s51,tag=port -l com1,autopty=vms/0/tty,log=vms/0/console-ring -f bootrom,/Applications/Docker.app/Contents/Resources/uefi/UEFI.fd,,
  510  2755   426   0  5:08PM ttys000    0:00.00 **grep docker**  
```

或者 `ps -ef| grep docker | grep -v grep `


`$ ps -ef| grep [d]ocker`  
```
    0    88     1   0 Wed04PM ??         0:00.02 /Library/PrivilegedHelperTools/com.docker.vmnetd
  510   629   571   0 Wed04PM ??         0:01.43 /Applications/Docker.app/Contents/MacOS/com.docker.supervisor -watchdog fd:0
  510   635   629   0 Wed04PM ??         0:00.12 com.docker.osxfs serve --address fd:3 --connect vms/0/connect --control fd:4 --log-destination asl
  510   636   629   0 Wed04PM ??         0:03.06 com.docker.vpnkit --ethernet fd:3 --port fd:4 --introspection fd:5 --diagnostics fd:6 --vsock-path vms/0/connect --host-names host.docker.internal,docker.for.mac.host.internal,docker.for.mac.localhost --gateway-names gateway.docker.internal,docker.for.mac.gateway.internal,docker.for.mac.http.internal --vm-names docker-for-desktop --listen-backlog 32 --mtu 1500 --allowed-bind-addresses 0.0.0.0 --http /Users/ruqin/Library/Group Containers/group.com.docker/http_proxy.json --dhcp /Users/ruqin/Library/Group Containers/group.com.docker/dhcp.json --port-max-idle-time 300 --max-connections 2000 --gateway-ip 192.168.65.1 --host-ip 192.168.65.2 --lowest-ip 192.168.65.3 --highest-ip 192.168.65.254 --log-destination asl
  510   637   629   0 Wed04PM ??         0:02.18 com.docker.driver.amd64-linux -addr fd:3 -debug
  510   643   637   0 Wed04PM ??        14:02.82 com.docker.hyperkit -A -u -F vms/0/hyperkit.pid -c 4 -m 2048M -s 0:0,hostbridge -s 31,lpc -s 1:0,virtio-vpnkit,path=s50,uuid=99760b23-a6a5-452d-8726-e7a490c182c7 -U 16943701-e00a-4122-ae27-67644f80f7c6 -s 2:0,ahci-hd,file:///Users/ruqin/Library/Containers/com.docker.docker/Data/vms/0/Docker.qcow2?sync=os&buffered=1,format=qcow,qcow-config=discard=true;compact_after_unmaps=262144;keep_erased=262144;runtime_asserts=false -s 3,virtio-sock,guest_cid=3,path=vms/0,guest_forwards=2376;1525 -s 4,ahci-cd,/Applications/Docker.app/Contents/Resources/linuxkit/docker-for-mac.iso -s 5,ahci-cd,vms/0/config.iso -s 6,virtio-rnd -s 7,virtio-9p,path=s51,tag=port -l com1,autopty=vms/0/tty,log=vms/0/console-ring -f bootrom,/Applications/Docker.app/Contents/Resources/uefi/UEFI.fd,,
```
