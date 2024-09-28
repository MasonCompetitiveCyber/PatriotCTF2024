<?php
	$pic = $_GET['pic'];
	$hash = $_GET['hash'];
	if(sha1("d0gs3cr3t5!1".$pic)==$hash){
		$imgdata = base64_encode(file_get_contents("pupper/".str_replace("\0","",$pic)));
		echo "<!DOCTYPE html>";
		echo "<html><body><h1>Here's your picture:</h1>";
		echo "<img src='data:image/png;base64,".$imgdata."'>";
		echo "</body></html>";
	}else{
		echo "<!DOCTYPE html><html><body>";
		echo "<h1>Invalid hash provided!</h1>";
		echo '<img src="assets/BAD.gif"/>';
		echo "</body></html>";
	}
?>
