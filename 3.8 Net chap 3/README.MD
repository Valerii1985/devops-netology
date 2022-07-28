# Домашнее задание к занятию "3.8. Компьютерные сети, лекция 3"
# 1. Подключитесь к публичному маршрутизатору в интернет. Найдите маршрут к вашему публичному IP
<pre>telnet route-views.routeviews.org
Username: rviews
show ip route x.x.x.x/32
show bgp x.x.x.x/32</pre>

<pre>
route-views>show ip route 78.36.203.160
Routing entry for 78.36.200.0/21
  Known via "bgp 6447", distance 20, metric 0
  Tag 2497, type external
  Last update from 202.232.0.2 1d20h ago
  Routing Descriptor Blocks:
  * 202.232.0.2, from 202.232.0.2, 1d20h ago
      Route metric is 0, traffic share count is 1
      AS Hops 2
      Route tag 2497
      MPLS label: none
</pre>

<pre>
route-views>show bgp 78.36.203.160        
BGP routing table entry for 78.36.200.0/21, version 2358051812
Paths: (24 available, best #22, table default)
  Not advertised to any peer
  Refresh Epoch 1
  20912 3257 174 12389, (aggregated by 12389 95.167.89.10)
    212.66.96.126 from 212.66.96.126 (212.66.96.126)
      Origin IGP, localpref 100, valid, external
      Community: 3257:8070 3257:30155 3257:50001 3257:53900 3257:53902 20912:65004
      path 7FE188AD66C8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  19214 174 12389, (aggregated by 12389 95.167.89.10)
    208.74.64.40 from 208.74.64.40 (208.74.64.40)
      Origin IGP, localpref 100, valid, external
      Community: 174:21101 174:22005
      path 7FE0F21BEE00 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3267 1299 12389, (aggregated by 12389 95.167.89.10)
    194.85.40.15 from 194.85.40.15 (185.141.126.1)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE0FA4DC9A8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  1351 6939 12389, (aggregated by 12389 95.167.89.10)
    132.198.255.253 from 132.198.255.253 (132.198.255.253)
      Origin IGP, localpref 100, valid, external
      path 7FE177844130 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  20130 6939 12389, (aggregated by 12389 95.167.89.10)
    140.192.8.16 from 140.192.8.16 (140.192.8.16)
      Origin IGP, localpref 100, valid, external
      path 7FE0FCD60230 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3333 1103 12389, (aggregated by 12389 95.167.89.10)
    193.0.0.56 from 193.0.0.56 (193.0.0.56)
      Origin IGP, localpref 100, valid, external
      path 7FE0F98D6190 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3303 12389, (aggregated by 12389 95.167.89.10)
    217.192.89.50 from 217.192.89.50 (138.187.128.158)
      Origin IGP, localpref 100, valid, external
      Community: 3303:1004 3303:1006 3303:1030 3303:3056
      path 7FE14F10AA08 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  4901 6079 1299 12389, (aggregated by 12389 95.167.89.10)
    162.250.137.254 from 162.250.137.254 (162.250.137.254)
      Origin IGP, localpref 100, valid, external
      Community: 65000:10100 65000:10300 65000:10400
      path 7FE0B2E8CB10 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7018 3356 12389, (aggregated by 12389 95.167.89.10)
    12.0.1.63 from 12.0.1.63 (12.0.1.63)
      Origin IGP, localpref 100, valid, external
      Community: 7018:5000 7018:37232
      path 7FE0B0885BA8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  101 3356 12389, (aggregated by 12389 95.167.89.10)
    209.124.176.223 from 209.124.176.223 (209.124.176.223)
      Origin IGP, localpref 100, valid, external
      Community: 101:20100 101:20110 101:22100 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065
      Extended Community: RT:101:22100
      path 7FE0E7DA5658 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  49788 12552 12389, (aggregated by 12389 95.167.89.10)
    91.218.184.60 from 91.218.184.60 (91.218.184.60)
      Origin IGP, localpref 100, valid, external
      Community: 12552:12000 12552:12100 12552:12101 12552:22000
      Extended Community: 0x43:100:1
      path 7FDFFBBF8220 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  6939 12389, (aggregated by 12389 95.167.89.10)
    64.71.137.241 from 64.71.137.241 (216.218.252.164)
      Origin IGP, localpref 100, valid, external
      path 7FE12C5F17F8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  852 3356 12389, (aggregated by 12389 95.167.89.10)
    154.11.12.212 from 154.11.12.212 (96.1.209.43)
      Origin IGP, metric 0, localpref 100, valid, external
      path 7FE13736FD70 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  8283 1299 12389, (aggregated by 12389 95.167.89.10)
    94.142.247.3 from 94.142.247.3 (94.142.247.3)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 1299:30000 8283:1 8283:101 8283:102
      unknown transitive attribute: flag 0xE0 type 0x20 length 0x24
        value 0000 205B 0000 0000 0000 0001 0000 205B
              0000 0005 0000 0001 0000 205B 0000 0005
              0000 0002 
      path 7FE0B53C7C10 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  57866 3356 12389, (aggregated by 12389 95.167.89.10)
    37.139.139.17 from 37.139.139.17 (37.139.139.17)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065
      path 7FE10EFE1908 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3549 3356 12389, (aggregated by 12389 95.167.89.10)
    208.51.134.254 from 208.51.134.254 (67.16.168.191)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065 3549:2581 3549:30840
      path 7FE1767368A8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3356 12389, (aggregated by 12389 95.167.89.10)
    4.68.4.46 from 4.68.4.46 (4.69.184.201)
      Origin IGP, metric 0, localpref 100, valid, external
      Community: 3356:2 3356:22 3356:100 3356:123 3356:501 3356:901 3356:2065
      path 7FE04BAE3D00 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  53767 174 12389, (aggregated by 12389 95.167.89.10)
    162.251.163.2 from 162.251.163.2 (162.251.162.3)
      Origin IGP, localpref 100, valid, external
      Community: 174:21101 174:22005 53767:5000
      path 7FE0C0140A50 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  701 1273 12389, (aggregated by 12389 95.167.89.10)
    137.39.3.55 from 137.39.3.55 (137.39.3.55)
      Origin IGP, localpref 100, valid, external
      path 7FE0B86C82D8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  7660 2516 12389, (aggregated by 12389 95.167.89.10)
    203.181.248.168 from 203.181.248.168 (203.181.248.168)
      Origin IGP, localpref 100, valid, external
      Community: 2516:1050 7660:9001
      path 7FE11A1410E0 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3561 3910 3356 12389, (aggregated by 12389 95.167.89.10)
    206.24.210.80 from 206.24.210.80 (206.24.210.80)
      Origin IGP, localpref 100, valid, external
      path 7FE098EE1EE8 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 3
  2497 12389, (aggregated by 12389 95.167.89.10)
    202.232.0.2 from 202.232.0.2 (58.138.96.254)
      Origin IGP, localpref 100, valid, external, best
      path 7FE10D1ABF58 RPKI State valid
      rx pathid: 0, tx pathid: 0x0
  Refresh Epoch 1
  1221 4637 5511 12389, (aggregated by 12389 95.167.89.10)
    203.62.252.83 from 203.62.252.83 (203.62.252.83)
      Origin IGP, localpref 100, valid, external
      path 7FE09076E248 RPKI State valid
      rx pathid: 0, tx pathid: 0
  Refresh Epoch 1
  3257 3356 12389, (aggregated by 12389 95.167.89.10)
    89.149.178.10 from 89.149.178.10 (213.200.83.26)
      Origin IGP, metric 10, localpref 100, valid, external
      Community: 3257:8794 3257:30043 3257:50001 3257:54900 3257:54901
      path 7FE13381FFF0 RPKI State valid
      rx pathid: 0, tx pathid: 0
</pre>

# 2. Создайте dummy0 интерфейс в Ubuntu. Добавьте несколько статических маршрутов. Проверьте таблицу маршрутизации.
<pre>
sudo modprobe -v dummy numdummies=1
sudo ip addr add 192.168.1.123/24 dev dummy0
sudo ip addr add 192.168.1.150/24 dev dummy0

routel
/usr/bin/routel: 48: shift: can't shift that many
         target            gateway          source    proto    scope    dev tbl
        default           10.0.2.2       10.0.2.15     dhcp          enp0s9 
      10.0.2.0/ 24                       10.0.2.15   kernel     link enp0s9 
       10.0.2.2                          10.0.2.15     dhcp     link enp0s9 
       10.0.2.0          broadcast       10.0.2.15   kernel     link enp0s9 local
      10.0.2.15              local       10.0.2.15   kernel     host enp0s9 local
     10.0.2.255          broadcast       10.0.2.15   kernel     link enp0s9 local
      127.0.0.0          broadcast       127.0.0.1   kernel     link     lo local
     127.0.0.0/ 8            local       127.0.0.1   kernel     host     lo local
      127.0.0.1              local       127.0.0.1   kernel     host     lo local
127.255.255.255          broadcast       127.0.0.1   kernel     link     lo local
  192.168.1.123              local   192.168.1.123   kernel     host dummy0 local
  192.168.1.150              local   192.168.1.123   kernel     host dummy0 local
            ::1                                      kernel              lo 
        fe80::/ 64                                   kernel          enp0s9 
        fec0::/ 64                                       ra          enp0s9 
        default            fe80::2                       ra          enp0s9 
            ::1              local                   kernel              lo local
fe80::f0b4:d7ff:fec4:5888              local                   kernel          enp0s9 local
fec0::f0b4:d7ff:fec4:5888              local                   kernel          enp0s9 local
</pre>
# 3. Проверьте открытые TCP порты в Ubuntu, какие протоколы и приложения используют эти порты? Приведите несколько примеров.
<pre>
sudo ss -ltpn
State       Recv-Q      Send-Q           Local Address:Port            Peer Address:Port     Process                                                                                      
LISTEN      0           128                    0.0.0.0:22                   0.0.0.0:*         users:(("sshd",pid=1004,fd=3))                                                              
LISTEN      0           5                    127.0.0.1:631                  0.0.0.0:*         users:(("cupsd",pid=850,fd=7))                                                              
LISTEN      0           4096                 127.0.0.1:8125                 0.0.0.0:*         users:(("netdata",pid=980,fd=40))                                                           
LISTEN      0           4096                   0.0.0.0:19999                0.0.0.0:*         users:(("netdata",pid=980,fd=4))                                                            
LISTEN      0           4096             127.0.0.53%lo:53                   0.0.0.0:*         users:(("systemd-resolve",pid=770,fd=13))                                                   
LISTEN      0           128                       [::]:22                      [::]:*         users:(("sshd",pid=1004,fd=4))                                                              
LISTEN      0           5                        [::1]:631                     [::]:*         users:(("cupsd",pid=850,fd=6))                                                              
LISTEN      0           4096                         *:9090                       *:*         users:(("prometheus",pid=989,fd=8))                                                         
LISTEN      0           4096                         *:9100                       *:*         users:(("prometheus-node",pid=862,fd=3))                                                    
</pre>
22 порт ssh

9090 и 9100 порты используются prometheus 
# 4. Проверьте используемые UDP сокеты в Ubuntu, какие протоколы и приложения используют эти порты?
<pre>
sudo ss -lupn
State       Recv-Q      Send-Q              Local Address:Port             Peer Address:Port      Process                                         
UNCONN      0           0                         0.0.0.0:631                   0.0.0.0:*          users:(("cups-browsed",pid=916,fd=7))          
UNCONN      0           0                         0.0.0.0:36795                 0.0.0.0:*          users:(("avahi-daemon",pid=849,fd=14))         
UNCONN      0           0                       127.0.0.1:8125                  0.0.0.0:*          users:(("netdata",pid=980,fd=39))              
UNCONN      0           0                   127.0.0.53%lo:53                    0.0.0.0:*          users:(("systemd-resolve",pid=770,fd=12))      
UNCONN      0           0                10.0.2.15%enp0s9:68                    0.0.0.0:*          users:(("systemd-network",pid=741,fd=19))      
UNCONN      0           0                         0.0.0.0:5353                  0.0.0.0:*          users:(("avahi-daemon",pid=849,fd=12))         
UNCONN      0           0                            [::]:5353                     [::]:*          users:(("avahi-daemon",pid=849,fd=13))         
UNCONN      0           0                            [::]:57677                    [::]:*          users:(("avahi-daemon",pid=849,fd=15)) 
</pre>
# 5. Используя diagrams.net, создайте L3 диаграмму вашей домашней сети или любой другой сети, с которой вы работали.
https://github.com/Valerii1985/devops-netology/blob/main/3.8%20Net%20chap%203/%D0%94%D0%B8%D0%B0%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0%20%D0%B1%D0%B5%D0%B7%20%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.drawio.png