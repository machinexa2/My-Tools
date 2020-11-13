shopt -s expand_aliases
source ~/.bashrc
source ~/.bash_aliases
source ~/.bash_profile

CURRENT="`pwd`""/"
cat .gitignore | while read repository
do
	cd $repository && gitted #  && cd lib && cp "$CURRENT""PathFunctions.py" "PathFunctions.py"
	cd $CURRENT
done
