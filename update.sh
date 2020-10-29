shopt -s expand_aliases
source /root/.bash_aliases
current="`pwd`""/"
cat .gitignore | while read repository
do
	cd $repository && gitted #  && cd lib && cp "$current""PathFunctions.py" "PathFunctions.py"
	cd $current
done
