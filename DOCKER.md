# Using the Docker image

## Build the images

The following images have been constructed in accordance with GitHub specifications as of November 25, 2024:
the version of Ruby is `3.3.4`.

```Batchfile
docker build --tag ubuntu-jekyll-github-ssh --progress=plain -f Dockerfile-ssh .
docker build --tag ubuntu-jekyll-github-cmd --progress=plain -f Dockerfile-cmd .
docker image ls
```

* `ubuntu-jekyll-github-ssh`: interactive container. You login using SSH.
* `ubuntu-jekyll-github-cmd`: non-interactive container. You execute commands from `docker run`.

## Run the interactive container

```Batchfile
docker run --detach ^
           --net=bridge ^
           --interactive ^
           --tty ^
           --rm ^
           --init ^
           --volume="%CD%:/srv/jekyll" ^
           --publish 4000:4000/tcp ^
           --publish 2222:22/tcp ^
           ubuntu-jekyll-github-ssh
```

The OS is configured with 2 UNIX users:

| user               | password           | MobaXterm session                         |
|--------------------|--------------------|-------------------------------------------|
| `root`             | `root`             | [root](data/ContainerUbuntuSamyRoot.moba) |
| `dev`              | `dev`              | [dev](data/ContainerUbuntuSamyDev.moba)   |

> `dev` is "_sudoer_".

SSH connexion using private SSH key:

```bash
ssh -o IdentitiesOnly=yes -o IdentityFile=data/private.key -p 2222 root@localhost
ssh -o IdentitiesOnly=yes -o IdentityFile=data/private.key -p 2222 dev@localhost
```

> Make sure that the private key file has the right permission (`chmod 600 data/private.key`).
>
> You may need to clean the host SSH configuration: `ssh-keygen -f "/home/denis/.ssh/known_hosts" -R "[localhost]:2222"`

SSH connexion using UNIX password:

```bash
ssh -o IdentitiesOnly=yes -p 2222 root@localhost
ssh -o IdentitiesOnly=yes -p 2222 dev@localhost
```

Using SCP 

From the host, download a file (stored on the container):

```bash
scp -o IdentitiesOnly=yes -o IdentityFile=data/private.key -P 2222 dev@localhost:/tmp/sftp-example-download.dump /tmp/
```

You can launch the web server by logging into the container:

```Batchfile
ssh -o IdentitiesOnly=yes -p 2222 dev@localhost
```

Then, start the server:

```bash
site_name="my-blog"
cd "/srv/jekyll/${site_name}"
bundle install
bundle update
jekyll serve -w --port 4000 &
# Optionaly
px -awx
netsat -a
curl localhost:4000
```

## Run the non-interective container

```Batchfile
SET site_name="my-blog"
docker run --net=bridge ^
           --rm ^
           --volume="%CD%:/srv/jekyll" ^
           --publish 4000:4000/tcp ^
           ubuntu-jekyll-github-cmd ^
           sh -c "ruby -v && cd '/srv/jekyll/%site_name%' && bundle install && bundle update && jekyll serve -w --port 4000"
```


