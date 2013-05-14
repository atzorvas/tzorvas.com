:title: Gentoo guest inside KVM host
:slug: gentoo-guest-inside-kvm-host
:date: 2012-04-15 03:00

Αφού καταφέραμε στο `προηγούμενο <http://83.212.120.35:8000/posts/custom-distro-on-okeanosgrnet/>`_
 post να μπούμε με το systemrescuecd σε live περιβάλλον, έχουμε κάθε άνεση για να συνεχίσουμε στην εγκατάσταση του Gentoo!

Ακολουθώντας λοιπόν τις οδηγίες στο `Gentoo Handbook <http://www.gentoo.org/doc/en/handbook/>`_

θα πρέπει να προσέξουμε στα βήματα για το χτίσιμο του πυρήνα και για την εγκατάσταση του Grub.

σημαντικό:
march=native!
εγώ που το δοκίμασα πάνω στο VM μέσα στο chrooted περιβάλλον του gentoo μου επέλεγε -march=pentium-m και μέσα στο systemRescueCD μου επέλεγε -march=core2. Η σωστή επιλογή είναι -march=core2 και από κει και πέρα χρησιμοποιείστε αν θέλετε και τα υπόλοιπα options που παίρνει ο gcc το από το τεστ με -march=native. (σε πρόσφατο VM η επιλογή ήταν march=amdfam10. πάντα να τρέχετε το παρακάτω script για να σιγουρεύετε την επιλογή του march)

κάντε τις δοκιμές σας με αυτό εδώ:
**-march=native**

.. code-block:: bash

	echo 'int main(){return 0;}' > test.c && gcc -v -Q -march=native -O2 test.c -o test && rm test.c test

**Kernel:**

θα χρειαστούμε στο .config μας τα παρακάτω. φροντίστε να τα επιλέξετε κατά τη διάρκεια του make menuconfig αλλιώς μπείτε ξανά στο make menuconfig, επιλέξτε τα και ξανακάντε make τον kernel.

.. code-block:: bash
	
	#initrd
	CONFIG_BLK_DEV_INITRD=y
	#virtio related
	CONFIG_NET_9P_VIRTIO=m
	CONFIG_VIRTIO_BLK=y
	CONFIG_VIRTIO_NET=m
	CONFIG_VIRTIO_CONSOLE=y
	CONFIG_HW_RANDOM_VIRTIO=y
	CONFIG_VIRTIO=y
	CONFIG_VIRTIO_RING=y
	CONFIG_VIRTIO_PCI=y
	CONFIG_VIRTIO_BALLOON=m
	CONFIG_VIRTIO_MMIO=m
	#virtio disk
	CONFIG_ATA_PIIX=y
	CONFIG_PATA_OLDPIIX=y
	CONFIG_I2C_PIIX4=y

παραθέτω εδώ και το αποτέλεσμα για το lspci -n για όποιον ενδιαφέρεται

.. code-block:: bash

	00:00.0 0600: 8086:1237 (rev 02)
	00:01.0 0601: 8086:7000
	00:01.1 0101: 8086:7010
	00:01.2 0c03: 8086:7020 (rev 01)
	00:01.3 0680: 8086:7113 (rev 03)
	00:02.0 0300: 1013:00b8
	00:03.0 0200: 1af4:1000
	00:04.0 0100: 1af4:1001

για όσους ακολουθήσουν την μέθοδο για manual kernel, θα πρέπει να φτιάξουν και ένα initrd. αυτό θα γίνει με τη βοήθεια του genkernel
(προσοχή, από το genkernel θα φτιάξουμε μόνο το initrd)

.. code-block:: bash

	echo "MODULES_KVM=\"virtio virtio_balloon virtio_ring virtio_pci virtio_blk virtio_net\"" >> /etc/genkernel.conf
	sed -i 's/'HWOPTS=\''/'HWOPTS=\'virtio\ '/g' /usr/share/genkernel/defaults/initrd.defaults
	sed -i '/'\$\{DEVICES\}'/ i\
	        # virtio devices \
	        DEVICES="$DEVICES /dev/vd*"' /usr/share/genkernel/defaults/initrd.scripts

και τέλος φτιάχνουμε το initrd μας. (θα το περάσει κατευθείαν μέσα στο /boot/initramfs-genkernel-KERNELNAME

.. code-block:: bash

	genkernel ramdisk

επίσης αλλάζουμε το grub.conf σε κάτι αντίστοιχο του παρακάτω
/boot/grub/grub.conf

.. code-block:: bash

	title Gentoo Linux Hardened 3.2.2-hardened-r1
	root (hd0,0)
	kernel /boot/KERNEL_IMAGE doload=virtio,virtio_blk root=/dev/ram0 real_root=/dev/vda3 init=/linuxrc
	initrd /boot/INITRAMFS_IMAGE

(με ένα απλό ls -l /boot μπορούμε να δούμε την ονομασία του initramfs μέσα στο /boot)

Επίσης εδώ να σημειώσω πως εγώ ακολούθησα τα βήματα ξανά για να έχω και το systemrescuecd στον δίσκο (post), γιατί αλλιώς αν κάτι στραβώσει θα πρέπει να κάνω destroy το VM!

 

**Grub:**

.. code-block:: bash	

	echo "(hd0) /dev/vda" > /boot/grub/device.map

στη συνέχεια κάνουμε το grub-install όπως το αναφέρει στο handbook.

And .. we are ready..
Enjoy!