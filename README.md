# mongodb-client

docker build --tag mongodb-client .

docker images

docker tag ac212ea452fe imsrv01/mongodb-client

docker push imsrv01/mongodb-client


Can be access from node 

imsrv01@gke-standard-cluster-1-default-pool-73728ea7-fq89 ~ $ curl -X POST 'http://127.0.0.1:30268/star' -d '{"name":"rudra", "distance":"33"}' -H "Content-Type:application/json" -k
{
  "result": {
    "distance": "33",
    "name": "rudra"
  }
}

imsrv01@gke-standard-cluster-1-default-pool-73728ea7-fq89 ~ $ curl -X POST 'http://127.0.0.1:30268/star' -d '{"name":"Tara", "distance":"55"}' -H "Content-Type:application/json" -k
{
  "result": {
    "distance": "55",
    "name": "Tara"
  }
}

imsrv01@gke-standard-cluster-1-default-pool-73728ea7-fq89 ~ $ curl 'http://127.0.0.1:30268/star' -k
{
  "result": [
    {
      "distance": "33",
      "name": "rudra"
    },
    {
      "distance": "55",
      "name": "Tara"
    }
  ]
}
