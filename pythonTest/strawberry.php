<html><body>
<?php
$myfile = fopen("email.txt", "w") or die("Unable to open file!");
$txt = $_GET[email];
fwrite($myfile, $txt);
fclose($myfile);

exec("pictureTaken.py");  
?>
</body></html>