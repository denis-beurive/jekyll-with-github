# Jekyll with GitHub

## Introduction

This page demonstrates how to utilize a Docker container to run Jekyll on a Windows host.

We leverage both the official Jekyll image and a custom-built image.

The official Jekyll image offers convenience, but it might not always include the precise Ruby version you require. On the other hand, opting for a custom-built image involves a bit more effort but ensures you can use the exact Ruby version you need.

Whichever solution you choose, the procedure remains consistent when focusing on Jekyll:

1. Generate a `Gemfile` based on the GitHub specifications.  
2. Replace your site's existing `Gemfile` with the newly generated one.  
3. Launch the Jekyll web server.  

> Kindly note that the command lines provided in this document are tailored for Windows Command Prompt (CMS/DOS).
> Adapting them for BASH is a simple task.

## Generate the "Gemfile" that matches the GitHub environment for Jekyll

This Python script retrieves the GitHub Pages dependency versions and generates the 'Gemfile' based on the specified versions:
[jekyll-github.py](jekyll-github.py)

    python jekyll-github.py

As of November 25, 2024 the generated "`Gemfile`" is as follows: [Gemfile](data/gemfile-20241125)

## Replace the Gemfile by the new one

Replace "[my-blog/Gemfile](my-blog/Gemfile)" by the one you've previouly generated (for example [data/gemfile-20241125](data/gemfile-20241125)).

## Start the Jekyll WEB server

* [using an official Docker image](OFFICIAL.md)
* [using a custon Docker image](CUSTOM.md)

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
* Link to the official Jekyll containers: (https://github.com/envygeeks/jekyll-docker)[https://github.com/envygeeks/jekyll-docker]

