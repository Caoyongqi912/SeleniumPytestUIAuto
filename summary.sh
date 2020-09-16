#!/usr/bin/env bash
summary_file=/path/summary.json
html_file=/path/summary.html

total=`cat ${summary_file} | grep -Po 'total[" :]+\K[^}]+'`
passed=`cat ${summary_file} | grep -Po 'passed[" :]+\K[^,]+'`
failed=`cat ${summary_file} | grep -Po 'failed[" :]+\K[^,]+'`
broken=`cat ${summary_file} | grep -Po 'broken[" :]+\K[^,]+'`


echo "<th style=\"font-family:'Arial';font-size:28px;color:#0072E3;\">Total：${total}</td>"  > $html_file
echo "<th style=\"font-family:'Arial';font-size:28px;color:#27AE60;\">Passed：${passed}</td>" >> $html_file
echo "<th style=\"font-family:'Arial';font-size:28px;color:#FF2D2D;\">Failed：${failed}</td>" >> $html_file
echo "<th style=\"font-family:'Arial';font-size:28px;color:#FF2D2D;\">Broken：${broken}</td>" >> $html_file
