## Using the Jekyll Docker container

Link to the container: (https://github.com/envygeeks/jekyll-docker)[https://github.com/envygeeks/jekyll-docker]

## Docker Cheat Sheet

See: [https://docs.docker.com/reference/cli/docker/container/run/](https://docs.docker.com/reference/cli/docker/container/run/)

	docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Options used within this document:

* `-i`: Keep STDIN open even if not attached
* `-t`: Allocate a pseudo-TTY
* `--volume`: Bind mount a volume
* `--rm`: Automatically remove the container and its associated anonymous volumes when it exits

## Initialize a new site

```Batchfile
set site_name=my-blog
docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  -it jekyll/jekyll sh -c "chown -R jekyll /usr/gem/ && jekyll new %site_name%" && cd %site_name%
```

## Build the site (generate the HTML pages)

```Batchfile
set site_name=my-blog
docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  -it jekyll/jekyll ^
  sh -c "chown -R jekyll /usr/gem/ && cd %site_name% && jekyll build" && cd "%site_name%\_site"
```

## Run the WEB server

Add the gem `webrick`:

```Batchfile
set site_name=my-blog
docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  --publish 4000:4000 ^
  jekyll/jekyll ^
  sh -c "chown -R jekyll /usr/gem/ && cd %site_name% && bundle add webrick"
```

> See: [Jekyll serve fails on Ruby 3.0](https://github.com/jekyll/jekyll/issues/8523)

Then run the command:

```Batchfile
set site_name=my-blog
docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  --publish 4321:4000 ^
  jekyll/jekyll ^
  sh -c "chown -R jekyll /usr/gem/ && cd %site_name% && jekyll serve -w --port 4000"
```

Useful commands:

```Batchfile
docker ps -a
REM The following command returns "0.0.0.0"
docker inspect 5d33ce1b56cb | find "HostIp"
netstat -an -p TCP | find "0.0.0.0"
netstat -an -p TCP | find "4321"
```

> Note: do not use the address "`0.0.0.0`". This is a non-usable address(see: [What's the difference between 127.0.0.1 and 0.0.0.0?](https://superuser.com/questions/949428/whats-the-difference-between-127-0-0-1-and-0-0-0-0))

Then, open [http://127.0.0.1:4321/](http://127.0.0.1:4321/).




## Install a template from GitHub

Example: [The GitHub hacker theme](https://pages-themes.github.io/hacker/)



## Documentation

* https://kinsta.com/blog/jekyll-static-site/


## List of templates

* https://pages-themes.github.io/hacker/
* https://github.com/hydecorp/hydejack