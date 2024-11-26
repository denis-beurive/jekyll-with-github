# Jekyll with GitHub

## Generate the "Gemfile" that matches the GitHub environment for Jekyll

The Python script below retrieves the GitHub Pages dependency versions and generates the 'Gemfile' based on the specified versions:

```python
import requests
from typing import Final, Dict, List
from requests import Response
import json


URL: Final[str] = 'https://pages.github.com/versions.json'

response: Final[Response] = requests.get(URL)

if response.status_code != 200:
    print("ERROR: cannot fetch {}".format(URL))
    exit(1)

data: Dict[str, str] = json.loads(response.text)
plugins: List[str] = []
deps: List[str] = []

for key, value in data.items():
    if key.startswith('jekyll-'):
        if key == 'jekyll-github-metadata':
            continue
        plugins.append("gem '{}', '{}'".format(key, value))
    else:
        if key == "ruby":
            continue
        deps.append("gem '{}', '{}'".format(key, value))

print("source 'https://rubygems.org'\n")
print("{}\n\n".format("\n".join(deps)))
print("group :jekyll_plugins do")
print("{}".format("\n".join( map(lambda x: "  {}".format(x), plugins))))
print("end\n")
print("gem 'webrick'")
print("gem 'rexml'")
```

Usage: just run the script.

As of November 25, 2024, the generated 'Gemfile' is as follows:

```
source 'https://rubygems.org'

gem 'jekyll', '3.10.0'
gem 'kramdown', '2.4.0'
gem 'kramdown-parser-gfm', '1.1.0'
gem 'liquid', '4.0.4'
gem 'rouge', '3.30.0'
gem 'github-pages-health-check', '1.18.2'
gem 'jemoji', '0.13.0'
gem 'minima', '2.5.1'
gem 'github-pages', '232'
gem 'html-pipeline', '2.14.3'
gem 'sass', '3.7.4'
gem 'safe_yaml', '1.0.5'
gem 'nokogiri', '1.16.7'

group :jekyll_plugins do
  gem 'jekyll-sass-converter', '1.5.2'
  gem 'jekyll-commonmark-ghpages', '0.5.1'
  gem 'jekyll-redirect-from', '0.16.0'
  gem 'jekyll-sitemap', '1.4.0'
  gem 'jekyll-feed', '0.17.0'
  gem 'jekyll-gist', '1.5.0'
  gem 'jekyll-paginate', '1.1.0'
  gem 'jekyll-coffeescript', '1.2.2'
  gem 'jekyll-seo-tag', '2.8.0'
  gem 'jekyll-avatar', '0.8.0'
  gem 'jekyll-remote-theme', '0.4.3'
  gem 'jekyll-include-cache', '0.2.1'
  gem 'jekyll-mentions', '1.6.0'
  gem 'jekyll-relative-links', '0.6.1'
  gem 'jekyll-optional-front-matter', '0.3.2'
  gem 'jekyll-readme-index', '0.3.0'
  gem 'jekyll-default-layout', '0.1.5'
  gem 'jekyll-titles-from-headings', '0.5.3'
  gem 'jekyll-swiss', '1.0.0'
  gem 'jekyll-theme-primer', '0.6.0'
  gem 'jekyll-theme-architect', '0.2.0'
  gem 'jekyll-theme-cayman', '0.2.0'
  gem 'jekyll-theme-dinky', '0.2.0'
  gem 'jekyll-theme-hacker', '0.2.0'
  gem 'jekyll-theme-leap-day', '0.2.0'
  gem 'jekyll-theme-merlot', '0.2.0'
  gem 'jekyll-theme-midnight', '0.2.0'
  gem 'jekyll-theme-minimal', '0.2.0'
  gem 'jekyll-theme-modernist', '0.2.0'
  gem 'jekyll-theme-slate', '0.2.0'
  gem 'jekyll-theme-tactile', '0.2.0'
  gem 'jekyll-theme-time-machine', '0.2.0'
end

gem 'webrick'
gem 'rexml'
```

## Start the Jekyll WEB server

```Batchfile
set site_name=my-blog

docker pull jekyll/jekyll
docker image ls

docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  --publish 4000:4000 ^
  jekyll/jekyll ^
  sh -c "ruby -v; cd /srv/jekyll; ls && cd '%site_name%' && bundle install && bundle update && jekyll serve -w --port 4000 --no-watch"
```

Then, open [http://127.0.0.1:4000/](http://127.0.0.1:4000/).

Useful commands:

```Batchfile
docker ps -a
REM The following command returns "0.0.0.0"
docker inspect 5d33ce1b56cb | find "HostIp"
netstat -an -p TCP | find "0.0.0.0"
netstat -an -p TCP | find "4000"
```

> Please note that it is not possible to access the WEB page if we choose to use the Ruby image `ruby:3.4-rc`:
>
> ```Batchfile
> set site_name=Personal
> 
> docker pull ruby:3.4-rc
> docker image ls
> docker run --rm ^
>   --volume="%CD%:/srv/jekyll" ^
>   --publish 4000:4000 ^
>   ruby ^
>  sh -c "ruby -v; cd /srv/jekyll; ls && cd '%site_name%' && bundle install && bundle update && jekyll serve -w --port 4000 --no-watch"
> ```

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
* Link to the container: (https://github.com/envygeeks/jekyll-docker)[https://github.com/envygeeks/jekyll-docker]

