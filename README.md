## Table des matières
* [Context du projet](#context-du-projet)
* [Prérequis](#prerequis)
* [Contenu de ce repository](#contenu-de-ce-repository)
* [Instructions](#instructions)
* [Changement des variables du script selon votre infrastructure](#changement-des-variables-du-script-selon-votre-infrastructure)

# Context du projet
Ce projet est une démonstration de solution qui automatise la configuration d'éléments d'une infrastructure dont la documentation est importante et stricte, mais où les procédures de changement sont homogènes et répétitives. 
<br>
Pour des raisons de sécurité, il est normal de vouloir documenter l'état d'une infrastrucrure (n° de poste affecté à un port de switch par exemple), et de contrôler chaque étape des procédures de modification de configuration. Toutes les entreprises n'ont pas forcément encore tous les outils nécessaires pour automatiser leur configuration et leur documentation.
<br>
Explication de mon context: Les prises murals sont affectés à un port du switch. Dans la documentation, une plage d'adresses IP est attribuée aux ports du switch. Ainsi, lorsque un poste utilisateur est connecté physiquement à une prise mural, elle récupère une adresse IP, mais pour que la documentation soit fixe et que l'on retrouve vite les informations réseaux des utilisateurs, nous fonctionnons par réservation DHCP. Lorsqu'un utilisateur déplace son poste ailleurs, nous devons donc modifier les documentations, la configuration du switch et du serveur DHCP. Nous devons en même temps, s'assurer que chaque étape a bien été validée.
<br>
Cette solution propose donc d'automatiser les configurations en remplissant les informations à changer sur un formulaire Web. Lors de la validation du formulaire, le lancement d'un script effectue toutes ces tâches à notre place. 

# Prerequis
•	Un serveur Linux en tant que serveur web <br><br>
(Selon votre cas)<br>
•	Un Windows Server pour la configuration DHCP<br>
•	Un switch <br>
•	Un document .csv ou .xlsx <br>

# Contenu de ce repository
Ce répertoire contient 2 dossiers: Form et Documentation.<br>
Dans le dossier Form:<br>
•	Un exemple de formulaire web (index.html)<br>
•	Le script d'automatisation en python (test.py)<br>

<br>
Dans le dossier Documentation:<br>
•	Un fichier exemple de documentation (Tableau_exemple.xlsx)<br>

# Instructions
Sur le serveur Linux:<br>
•	Installation d'Apache2: sudo apt-get install apache2 <br>

•	Activation du modules CGI <br>
1.	Editez le fichier /etc/apache2/apache.conf pour y ajouter ce bloc:<br>
<Directory "/var/www/cgi-bin"> <br>
AllowOverride None <br>
Options +ExecCGI <br>
AddHandler cgi-script .cgi .pl .py <br>
Require all granted <br> < /Directory> <br>


<br>

Sauvegardez la modification.
<br><br>
2.	Ensuite, vous devez activer le module CGI d'Apache pour pouvoir exécuter les scripts:
sudo ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/
<br><br>
- Dossier de lancement des scripts CGI (CGI-BIN).
Sur Ubuntu, la configuration par défaut d'Apache permet l'exécution des scripts CGI depuis le dossier /usr/lib/cgi-bin.
<br><br>
- Récupérez ce repository: git clone https://github.com/CindyPh7/-OC-_Project_06-automatiser-taches.git
Depuis le dossier "form":
- Copier le formulaire html dans votre répertoire apache (/var/www/votresite/index.html) ou créez/modifiez le votre. - Copier le script python dans /usr/lib/cgi-bin
(Optionel) Depuis le dossier "documentation":
- Copiez le document .xlsx là où vous souhaitez stocker la documentation, ou basez vous sur votre documentation déjà existante.
<br>

Installez le module openpyxl pour que le script python puisse lire les fichiers excels:<br>
sudo apt-get install python-openpyxl
<br>
Installez le module paramiko pour que le script python puisse se connecter en SSH:<br>
sudo apt-get install python-paramiko
# Changement des variables du script selon votre infrastructure
- VARIABLES DE LA DOCUMENTATION doc_path : Chemin + nom de la doc excel ou csv
doc_path = "/var/www/cgi-bin/tab_doc.xlsx"

- VARIABLES DU SERVEUR DHCP
""" Adresse IP du serveur DHCP a renseigner pour la connnexion SSH """
DHCP_SERV_IP = "10.50.2.10"

""" Port de connexion SSH vers le serveur """
DHCP_CONNECT_PORT= 22

""" Nom d'utilisateur du serveur pour se connecter en SSH """
Windows_Serv_username = "SERV-USERNAME"

""" Mot de passe de l'utiisateur pour la connexion SSH """
Windows_Serv_password = "PASSWORD"

""" Nom du serveur DHCP """
DHCP_SERV_NAME = "DHCP-SERV"

""" La plage DHCP dans lequel est fait le changement """
scopeID = "10.50.2.20"

