
NAME=$(openssl rand -hex 6)
echo $NAME
curl --request POST http://localhost:5000/api/timeline_post -d 'name='"$NAME"'&email=test@test.com&content=Test Content!'
LNAME=$(curl http://localhost:5000/api/timeline_post|jq .'timelineposts[0].name')
echo $LNAME
if [ "$LNAME"=="$NAME" ];
then 
	echo successfully added!
else 
	echo LNAME
	echo NAME
fi

#while true 
	#do
		#curl -X "DELETE" 'http://localhost:5000/api/timeline_post'
	#done
