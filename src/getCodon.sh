i=0

while [ $i -lt 100 ]
do
	i=`expr $i + 1`
	echo Iteration $i
	python getCodon.py

done
