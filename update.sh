shopt -s expand_aliases
source /root/.bash_aliases
current="`pwd`""/"
cat .gitignore | while read repository
do
	cd $repository && gitted # && cd lib && cp "$current""Skipper.py" "Skipper.py"
	cd $current
done
