<?php

$m = new Memcached();
$m->setOption(Memcached::OPT_BINARY_PROTOCOL, true);
//$m->setSaslAuthData("felamos", "zxcvbnm");
//$m->addServer('10.10.10.190', 11211);
/*
$wordlist = file_get_contents("memforce");
$lines = explode("\n", $wordlist);

foreach($lines as $line) {
	echo "$line\n";
	$log = $m->get($line);
	var_dump($log);
}	
echo "Done!";
 */
var_dump($argv);
?>
