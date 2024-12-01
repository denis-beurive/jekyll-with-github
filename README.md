# Jekyll with GitHub

## Introduction

This page demonstrates how to utilize a Docker container to run Jekyll on a Windows host.

We leverage both the official Jekyll image and a custom-built image.

The official Jekyll image offers convenience, but it might not always include the precise Ruby version you require. On the other hand, opting for a custom-built image involves a bit more effort but ensures you can use the exact Ruby version you need.

Whichever solution you choose, the procedure remains consistent when focusing on Jekyll:

1. Generate a `Gemfile` based on the GitHub specifications.  
2. Replace your site's existing `Gemfile` with the newly generated one.  
3. Launch the Jekyll web server.  

> Kindly note that the command lines provided in this document are tailored for Windows Command Prompt (CMD/DOS).
> Adapting them for BASH is a simple task.

## Using Jekyll to generate the site from a template

For this demonstration, we utilize the following Jekyll theme: [hacker](https://github.com/pages-themes/hacker). Simply download the ZIP file containing the theme and extract its contents. The "[hacker-theme](hacker-theme)" directory holds the extracted files.

The previously outlined three-step procedure is elaborated in detail below.

### 1. Generate the "Gemfile" that matches the GitHub environment for Jekyll

This Python script retrieves the GitHub Pages dependency versions and generates the 'Gemfile' based on the specified versions:
[jekyll-github.py](jekyll-github.py)

    python jekyll-github.py

As of November 25, 2024 the generated "`Gemfile`" is as follows: [Gemfile](data/gemfile-20241125)

### 2. Replace the Gemfile by the new one

Replace "[my-blog/Gemfile](my-blog/Gemfile)" by the one you've previouly generated (for example [data/gemfile-20241125](data/gemfile-20241125)).

### 3. Start the Jekyll WEB server

* [using an official Docker image](OFFICIAL.md)
* [using a custon Docker image](CUSTOM.md)

## Pushing the site on GitHub

After successfully testing the site locally, you can proceed to push it to GitHub. To accomplish this, simply follow the steps outlined below.

From : [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)

We suppose that you've already created a GitHub repository.

1. Add "#" to the beginning of the line that starts with gem "`jekyll`" to comment out this line.

2. Add the github-pages gem by editing the line starting with # gem "github-pages". Change this line to: `gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugins`

> Replace `GITHUB-PAGES-VERSION` with the latest supported version of the github-pages gem. You can find this version here: "[Dependency versions](https://pages.github.com/versions/)."

Therefore, the content of the file "`Gemfile`" becomes: [Gemfile](https://github.com/denis-beurive/jekyll-site/blob/master/Gemfile)

> "[Gemfile](data/gemfile-20241125)" for local tests _vs_ "[Gemfile](https://github.com/denis-beurive/jekyll-site/blob/master/Gemfile)" for GitHub.

3. Add configuration to the file `_config.yml`:

```
repository: denis-beurive/jekyll-with-github
```

> Thus the content of the file `_config.yml` becomes:
> 
> ```
> repository: denis-beurive/jekyll-with-github
> title: Hacker theme
> description: Hacker is a theme for GitHub Pages.
> show_downloads: true
> google_analytics:
> theme: jekyll-theme-hacker
> ```

4. At this stage, thoroughly test your site locally once more.

5. Once satisfied, push the site to GitHub. (see: [denis-beurive/jekyll-with-github](https://github.com/denis-beurive/jekyll-site/tree/master)).

6. Next, configure your repository to instruct GitHub to generate the site using the Jekyll theme:

![](data/kekyll-activate.png)

7. Allow GitHub some time to process the site. Once completed, you will observe the following:

![](data/kekyll-activate-done.png)

## Troubleshooting

### Useful commands:

```Batchfile
docker ps -a
REM The following command returns "0.0.0.0"
docker inspect 5d33ce1b56cb | find "HostIp"
netstat -an -p TCP | find "0.0.0.0"
netstat -an -p TCP | find "4000"
```

### Docker Cheat Sheet

See: [https://docs.docker.com/reference/cli/docker/container/run/](https://docs.docker.com/reference/cli/docker/container/run/)

  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Options used within this document:

* `-i`: Keep STDIN open even if not attached
* `-t`: Allocate a pseudo-TTY
* `--volume`: Bind mount a volume
* `--rm`: Automatically remove the container and its associated anonymous volumes when it exits

### Links

* [GitHub page Dependency versions](https://pages.github.com/versions/)
* Link to the official Jekyll containers: (https://github.com/envygeeks/jekyll-docker)[https://github.com/envygeeks/jekyll-docker]

