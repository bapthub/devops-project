all:
	docker compose up -d --build
run:
	docker-compose up -d --build
kill:
	docker-compose down
portainer:
	 docker run -d -p 9000:9000 --name=portainer --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
down:
	docker compose down
