cut -d "      " -f1 hightemp.txt > col1_test.txt
diff col1.txt col1_test.txt

cut -d "      " -f2 hightemp.txt > col2_test.txt
diff col2.txt col2_test.txt
