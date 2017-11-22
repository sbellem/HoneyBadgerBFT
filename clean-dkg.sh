for i in `seq 1 4`
do
	rm -f node$i/*.log
       	rm -f node$i/keys.out
	rm -f node$1/*.param
	ls -al node$i
done
