:title: Custom Distro on okeanos@GRNET!
:slug: custom-distro-on-okeanosgrnet
:date: 2012-04-15 10:00

Την υπηρεσία Okeanos φαντάζομαι όλοι την γνωρίζετε!
Είναι ίσως ότι καλύτερο έχω δει τα τελευταία χρόνια και οι δυνατότητες είναι πολλές!

Στην τώρα φάση (alpha2), τα images που προσφέρονται είναι:

    * Windows Server 2008 R2
    * Debian base (squeeze)
    * Debian desktop (squeeze)
    * Fedora 16
    * Centos 6.0
    * Kubuntu 11.10
    * Ubuntu 11.10

Έτσι μπορείτε εύκολα να φτιάξετε ένα VM μέσα σε λίγα λεπτά, με κάποια από τα παραπάνω λειτουργικά!
Τι θα γίνει όμως και με εμάς που είμαστε κάπως παράξενοι και θέλουμε και το κάτι άλλο;! πχ… ε βρε αδερφέ, ένα Gentoo box να δοκιμάσουμε εκεί πάνω.. ένα Slackware.. ή κάποια διαφορετική έκδοση από τις παραπάνω διανομές..

Στην περίπτωση μου, θα ήθελα να τρέξω ένα gentoo.. αρχικά ψάχτηκα με το snf-image-creator και γενικότερα έψαξα να βρω ότι υπάρχει για το snf-image και το Ganeti (η λύση πάνω στην οποία είναι βασισμένο το synnefo (synnefo, okeanos, cyclades.. πολλά τα ονόματα!)

Στο ψητό.. την εγκατάσταση του Gentoo την κάνουμε με κάποιο liveCD (usb etc…). Υπάρχει βέβαια το επίσημο liveCD(iso) αλλά και το πολύ καλύτερο SystemRescueCD, με πληθώρα εργαλείων διαθέσιμα μέσα από αυτό! Επίσης με πολλά features, όπως το να φορτώνει όλο εξολοκλήρου στη RAM!

Τα παρακάτω αφορούν μηχανήματα με grub legacy. Για αυτόν τον λόγο προτείνω να φτιάξετε ένα CentOS VM.

έτσι πολύ γρήγορα προχωράμε στα παρακάτω:
συνδεόμαστε ως root στο VM με ssh κατεβάζουμε το iso (η 2.5.1 είναι η τρέχουσα έκδοση) στον φάκελο του root και στη συνέχεια προσαρτάμε το iso στο /tmp/cdrom ώστε να πάρουμε έπειτα κάποια αρχεία από αυτό.
*προσοχή, εκτελέστε τα παρακάτω σαν root*

.. code-block:: bash

   cd /root
   VERSION=$(curl -s http://sourceforge.net/projects/systemrescuecd/files/ | grep 'Download systemrescuecd-x86' | cut -d'-' -f3 | cut -d' ' -f1 | cut -d'.' -f1,2,3") && wget http://downloads.sourceforge.net/project/systemrescuecd/sysresccd-x86/$VERSION/systemrescuecd-x86-$VERSION.iso && unset VERSION
   mkdir /tmp/cdrom
   mount -o loop systemrescuecd-x86-2.5.1.iso /tmp/cdrom


στη συνέχεια, φτιάχνουμε τον φάκελο /sysrcd από τον οποίο θα φορτώσουμε το sysresccd και περνάμε μέσα τα απαραίτητα αρχεία, πλην του initram.igz το οποίο χρειάζεται και αυτό

.. code-block:: bash

  mkdir /sysrcd
  cp /tmp/cdrom/sysrcd* /tmp/cdrom/isolinux/rescue* /tmp/cdrom/isolinux/altker* /sysrcd

στη συνέχεια κατεβάζουμε το initram.igz το οποίο έχει την απαραίτητη αλλαγή για να ανιχνεύσει το σκληρό του VM μας

.. code-block:: bash

  cd /sysrcd
  wget foss.aegean.gr/~tzorvas/files/initram.igz

τέλος, προσθέτουμε στο **/boot/grub/grub.conf** τα παρακάτω και διαγράφουμε την επιλογή hiddenmenu

.. code-block:: bash

  title    SystemRescueCd-2.5.1-64bit
  root     (hd0,0)
  kernel   /sysrcd/rescue64 subdir=sysrcd setkmap=us docache
  initrd   /sysrcd/initram.igz
  title    SystemRescueCd-2.5.1-32bit
  root     (hd0,0)
  kernel   /sysrcd/rescuecd subdir=sysrcd setkmap=us docache
  initrd   /sysrcd/initram.igz

Έπειτα, συνδεόμαστε στον Okeanos και επιλέγουμε το Console στο VM μας, πατάμε reboot και διαλέγουμε την επιθυμητή έκδοση systemrescuecd που θέλουμε να ξεκινήσει!

μόλις φορτώσει, πατήστε

.. code-block:: bash
    
  net-setup eth0

επιλέξτε να πάρει αυτόματα IP από τον DHCP και στη συνέχεια βάλτε κωδικό στον root και ανοίξτε τον sshd!

.. code-block:: bash

  passwd
  /etc/init.d/sshd restart

πλέον μπορούμε να συνδεθούμε κανονικά, στην static IP που βλέπουμε και στο panel του Okeanos και να ξεκινήσουμε με την εγκατάσταση του Gentoo!

.. code-block:: bash

  ssh root@ip

Enjoy!