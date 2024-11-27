# Jekyll with GitHub

## Using the official jekyll Docker image

1. Generate a "`Gemfile`" from the GitHub specifications.
2. Replace the "`Gemfile`" from your site by the one previously generated.
3. Start the Jekyll WEB server.

### Generate the "Gemfile" that matches the GitHub environment for Jekyll

This Python script retrieves the GitHub Pages dependency versions and generates the 'Gemfile' based on the specified versions:
[jekyll-github.py](jekyll-github.py)

    python jekyll-github.py gemfile

As of November 25, 2024 the generated "`Gemfile`" is as follows: [Gemfile](data/gemfile-20241125)

### Replace the Gemfile by the new one

Replace "[my-blog/Gemfile](my-blog/Gemfile)" by the one you've previouly generated (for example [data/gemfile-20241125](data/gemfile-20241125)).

### Start the Jekyll WEB server

```Batchfile
set site_name=my-blog

docker pull jekyll/jekyll
docker image ls

docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  --publish 4000:4000 ^
  jekyll/jekyll ^
  sh -c "ruby -v && cd /srv/jekyll && cd '%site_name%' && bundle install && bundle update && jekyll serve -w --port 4000"
```

Then, open [http://127.0.0.1:4000/](http://127.0.0.1:4000/).

## Useful commands:

```Batchfile
docker ps -a
REM The following command returns "0.0.0.0"
docker inspect 5d33ce1b56cb | find "HostIp"
netstat -an -p TCP | find "0.0.0.0"
netstat -an -p TCP | find "4000"
```

## Docker Cheat Sheet

See: [https://docs.docker.com/reference/cli/docker/container/run/](https://docs.docker.com/reference/cli/docker/container/run/)

  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Options used within this document:

* `-i`: Keep STDIN open even if not attached
* `-t`: Allocate a pseudo-TTY
* `--volume`: Bind mount a volume
* `--rm`: Automatically remove the container and its associated anonymous volumes when it exits

## Links

* [GitHub page Dependency versions](https://pages.github.com/versions/)
* https://kinsta.com/blog/jekyll-static-site/
* Link to the official Jekyll containers: (https://github.com/envygeeks/jekyll-docker)[https://github.com/envygeeks/jekyll-docker]

