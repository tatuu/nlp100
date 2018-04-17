cut -f1 hightemp.txt > col1_test.txt
diff -u col1.txt col1_test.txt

cut -f2 hightemp.txt > col2_test.txt
diff -u col2.txt col2_test.txt
