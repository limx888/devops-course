持续集成和交付及其工具
===============================================



### debian, ubuntu安装java8



1. 添加webupd8team Java PPA(Personal Package Archives) repository到系统里;

```
$ vim /etc/apt/sources.list.d/java-8-debian.list

deb <http://ppa.launchpad.net/webupd8team/java/ubuntu> trusty main
deb-src <http://ppa.launchpad.net/webupd8team/java/ubuntu> trusty main
```

2. 安装之前导入GPG key;
```
$ apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
```

假如出现错误提示：
Error:
Executing: /tmp/apt-key-gpghome.iKAAqs0hjL/gpg.1.sh --keyserver keyserver.ubuntu.com --recv-keys EEA14886
gpg: failed to start the dirmngr '/usr/bin/dirmngr': No such file or directory
gpg: connecting dirmngr at '/tmp/apt-key-gpghome.iKAAqs0hjL/S.dirmngr' failed: No such file or directory

dirmngr
提示没有dirmngr，安装dirmngr：
```
$ apt-get install software-properties-common dirmngr

$ apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886

3.apt-get update;

$ apt-get update
```

3. 安装java8
```
$ apt-get install oracle-java8-installer
```

5. 验证安装
```
$ java -version
```

6. 将java8设置为默认的java环境；
```
$ apt-get install oracle-java8-set-default  这一步也可以不做
```


### 安装jenkins步骤

```
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
```


