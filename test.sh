##curl -F file=@<path to a file> 0.0.0.0:5050/upload
curl -F file=@/home/driver220v/Pictures/doc123.txt 0.0.0.0:8000/upload
##curl -X GET 0.0.0.0:5050/size?<size of a file>
curl -X GET 0.0.0.0:8000/size?file=doc123.txt
##curl -X GET 0.0.0.0:5050/download?<file you want toi download> -o <where you want to store your file>
curl -X GET 0.0.0.0:8000/download?file=doc123.txt -o download_file.txt


