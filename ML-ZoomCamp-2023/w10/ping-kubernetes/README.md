```bash
docker build -t ping:001 .

docker run -it --rm -p 9696:9696 ping:001 
```