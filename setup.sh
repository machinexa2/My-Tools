read -p "Enter password: " passmepass
github_password=":""$passmepass""@"

# Clone repositories
cat README.md |  awk -F '(' '{print $2}' | awk -F ')**' '{print $1}' | sort -u | while read repository
do
	if [ ! -z "$repository" ]; then
		echo `echo "$repository"".git" | sed s/'github.com'/'machinexa2:@github.com'/g | sed s/':@'/$github_password/g`
	fi
done
