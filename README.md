# w251_trm
#get broker running
docker run --name mosq-broker -p 1883:1883 -v /home/trmetz/hw3:/hw3 --network hw03 -ti broker-image mosquitto

#get forwarder running
docker run --name forwarder --network hw03 -v /home/trmetz/hw3:/hw3 -ti forwarder-image sh

#get opencv face processor running
docker run -e DISPLAY=$DISPLAY --privileged --name fd1 --net host -v /home/trmetz/hw3:/hw3 -ti fd

#from cloud, start cloud broker running
docker run --name broker --network hw03-cloud -p 1883:1883 -ti broker-image mosquitto

#from cloud, start cloud processor running
docker run --name cloud_processor -v /root/w251_trm:/hw3 --privilged --network hw03-cloud -ti cloud-processor-image bash
#within that cloud processor,
s3fs s3-trm /hw3/mybucket -o passwd_file=/hw3/.cos_creds -o sigv2 -o use_path_request_style -o url=https://s3.us-east.objectstorage.softlayer.net

#ssh to get to IBM VSI that is running two containers for pictures
ssh root@169.62.39.215 -i .ssh/id_rsa

when jetson  stops - restart the opencv python program - that times out with broker
