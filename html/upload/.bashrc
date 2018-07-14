# .bashrc
# User specific aliases and functions
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
JAVA_HOME=/usr/java/jdk1.7.0_79
HIVE_PREFIX=/hive
PATH=$JAVA_HOME/bin:$HIVE_PREFIX/bin:$PATH
export PATH