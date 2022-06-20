#1. Узнайте о sparse (разряженных) файлах.
<pre>
Разрежённые файлы используются для хранения контейнеров, например:

- образов дисков виртуальных машин;

- резервных копий дисков и/или разделов, созданных спец. ПО.
</pre>
#2. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?

<pre>Права доступа всегда будут одинаковые, т.к. жесткая ссылка будет иметь тот-же инод, что и файл. При изменение прав доступа к файлу автоматически меняются права доступа всех хардлинков.</pre>

#3. Сделайте vagrant destroy на имеющийся инстанс Ubuntu. Замените содержимое Vagrantfile следующим:

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-20.04"
  config.vm.provider :virtualbox do |vb|
    lvm_experiments_disk0_path = "/tmp/lvm_experiments_disk0.vmdk"
    lvm_experiments_disk1_path = "/tmp/lvm_experiments_disk1.vmdk"
    vb.customize ['createmedium', '--filename', lvm_experiments_disk0_path, '--size', 2560]
    vb.customize ['createmedium', '--filename', lvm_experiments_disk1_path, '--size', 2560]
    vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 1, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk0_path]
    vb.customize ['storageattach', :id, '--storagectl', 'SATA Controller', '--port', 2, '--device', 0, '--type', 'hdd', '--medium', lvm_experiments_disk1_path]
  end
end

###Данная конфигурация создаст новую виртуальную машину с двумя дополнительными неразмеченными дисками по 2.5 Гб.
<pre>Сделано: создана виртуалка на убунту 20.04 с 2-мя неразмеченными жесткими дисками: sdb и sdc по 2,5Гб</pre>
#4. Используя fdisk, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.
<pre>командой sudo fdisk /dev/sdb перешел в интерактивный режим и разбил диск на 2 раздела: 1,9Гб и 652Мб</pre>
#5. Используя sfdisk, перенесите данную таблицу разделов на второй диск.
<pre>sudo sfdisk -d /dev/sdb | sudo sfdisk --force /dev/sdc</pre>
#6. Соберите mdadm RAID1 на паре разделов 2 Гб.
<pre>sudo mdadm --create --verbose /dev/md1 -l 1 -n 2 /dev/sd{b1,c1}</pre>
#7. Соберите mdadm RAID0 на второй паре маленьких разделов.
<pre>sudo mdadm --create --verbose /dev/md1 -l 0 -n 2 /dev/sd{b2,c2}</pre>
#8. Создайте 2 независимых PV на получившихся md-устройствах.
<pre>sudo pvcreate /dev/md127 /dev/md126</pre>
#9. Создайте общую volume-group на этих двух PV.
<pre>sudo vgcreate vol_grp1 /dev/md127 /dev/md126</pre>
#10. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.
<pre>sudo lvcreate -L 100M vol_grp1 /dev/md126</pre>
#11. Создайте mkfs.ext4 ФС на получившемся LV.
<pre>sudo mkfs.ext4 /dev/vol_grp1/lvol0</pre>
#12. Смонтируйте этот раздел в любую директорию, например, /tmp/new.
<pre>sudo mkdir /tmp/new | sudo mount /dev/vol_grp1/lvol0 /tmp/new</pre>
#13. Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz.
<pre>sudo wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz</pre>
#14. Прикрепите вывод lsblk.
<pre>
lsblk
NAME                         MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT

sda                         8:0    0   64G  0 disk
├─sda1                      8:1    0    1M  0 part
├─sda2                      8:2    0    1G  0 part  /boot
└─sda3                      8:3    0   63G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0 31.5G  0 lvm   /
sdb                         8:16   0  2.5G  0 disk
├─sdb1                      8:17   0  1.9G  0 part
│ └─md127                   9:127  0  1.9G  0 raid1
└─sdb2                      8:18   0  652M  0 part
  └─md126                   9:126  0  1.3G  0 raid0
    └─vol_grp1-lvol0      253:1    0  100M  0 lvm   /tmp/new
sdc                         8:32   0  2.5G  0 disk
├─sdc1                      8:33   0  1.9G  0 part
│ └─md127                   9:127  0  1.9G  0 raid1
└─sdc2                      8:34   0  652M  0 part
  └─md126                   9:126  0  1.3G  0 raid0
    └─vol_grp1-lvol0      253:1    0  100M  0 lvm   /tmp/new
</pre>

#15. Протестируйте целостность файла:
root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0

<pre>Тест целостности проходит, как в примере. Дополнительно попробовал с ключем -tv</pre>
<pre>
gzip -tv /tmp/new/test.gz
/tmp/new/test.gz:        OK
</pre>
#16. Используя pvmove, переместите содержимое PV с RAID0 на RAID1.
<pre> sudo pvmove -b /dev/md126 /dev/md127 </pre>
#17. Сделайте --fail на устройство в вашем RAID1 md.
<pre>sudo mdadm /dev/md127 --fail /dev/sdb1</pre>
#18. Подтвердите выводом dmesg, что RAID1 работает в деградированном состоянии.
<pre>dmesg |grep md127
[    3.726858] md/raid1:md127: active with 2 out of 2 mirrors
[    3.729950] md127: detected capacity change from 0 to 1997537280
[16860.068331] md/raid1:md127: Disk failure on sdb1, disabling device.
               md/raid1:md127: Operation continuing on 1 devices.</pre>
#19. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:
root@vagrant:~# gzip -t /tmp/new/test.gz
root@vagrant:~# echo $?
0
<pre>
gzip -tv /tmp/new/test.gz
/tmp/new/test.gz:        OK
</pre>
#20. Погасите тестовый хост, vagrant destroy.
<pre>
vagrant destroy
    default: Are you sure you want to destroy the 'default' VM? [y/N] y
==> default: Destroying VM and associated drives…</pre>
