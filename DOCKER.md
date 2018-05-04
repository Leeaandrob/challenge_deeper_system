# Running a dev environment in docker

### Docker instalation:
- Ubuntu (https://docs.docker.com/install/linux/docker-ce/ubuntu/)
- Windows (https://docs.docker.com/docker-for-windows/install/)
- Mac (https://docs.docker.com/docker-for-mac/install/)
- Debian (https://docs.docker.com/install/linux/docker-ce/debian/)
- Centos (https://docs.docker.com/install/linux/docker-ce/centos/)
- Fedora (https://docs.docker.com/install/linux/docker-ce/fedora/)

## Development

Run `docker-compose up` and develop away!

Everything is working as always, except if you change dependencies in requirements.txt`

In that case, you need to re-run `docker-compose up --build`

### Logs

*It's possible to see the outlog come from the container split by service*

- docker-compose logs -f **name_container**

for example:

- docker-compose logs -f portal
- docker-compose logs -f db
- docker-compose logs -f mongo
- docker-compose logs -f parity
