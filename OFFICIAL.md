# Using an official Jekyll image

```Batchfile
set site_name=my-blog

docker pull jekyll/jekyll
docker image ls

docker run --rm ^
  --volume="%CD%:/srv/jekyll" ^
  --publish 4000:4000 ^
  jekyll/jekyll ^
  sh -c "ruby -v && cd '/srv/jekyll/%site_name%' && bundle install && bundle update && jekyll serve --host 0.0.0.0 --watch --port 4000"
```

> Please, make sure to set the option `--host 0.0.0.0`, otherwise the HTTP server will not be accessible from the host.

Then, open [http://127.0.0.1:4000/](http://127.0.0.1:4000/).
