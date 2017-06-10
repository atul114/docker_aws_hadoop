<?php
$a1=$_GET['usrname'];
#echo $a1;
$a2=$_GET['comment'];
#echo $a2;
#echo $a2.$a;
$myfile = fopen("/var/www/cgi-bin/nameip", "r");
$a3=fgets($myfile);
fclose($myfile);
#echo $a3;
$myfile1 = fopen("/var/www/cgi-bin/command", "w");
fwrite($myfile1,$a2);
fclose($myfile1);
#$q=exec(" sudo hive -e  '".$a2."'");
#echo $q;
#$c=" sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@".$a3." echo  |  hive -e '".$a2."'";
$c="sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@".$a3." hive -f /var/www/cgi-bin/command";
#echo $c;
echo "<pre>";
$output = shell_exec($c);
echo $output;
#$output = shell_exec("sshpass -p 'q' ssh -o StrictHostKeyChecking=no root@" +$a3+' hive -e '+$a2);
#echo "<pre>";
#echo "$output";
echo "</pre>";


?>
