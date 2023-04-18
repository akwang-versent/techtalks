# Docker

### 18th April 2023

Containerize your virtual environments, view changes to your application code on the fly and make your applications OS agnostic.

### Why would you want to dockerize your environment?

When you build applications, you will no doubt require a number of packages for your tools to do their job. But, what happens if your applications only requires a certain version of a package, because the new version conflicts with a version of a different package your app uses?

This is where isolation of environments comes to the rescue.

### Python venv or Docker?

Python's virutal environment works in a very similar way to Docker containers, in that they are isolated environments.
However, Python's venv only encapsulates Python dependencies, whereas Docker encapsulates an entire OS. This means that Docker has its own process space, file system, network space, etc and is more akin to a Virtual Machine than just an environment to a specific language's runtime/interpreter/

### Building your own docker image.

#### What do you need?

- Docker desktop 
- Terminal
- This repo


#### Dockerfile

Each image will require a `Dockerfile`, that defines all the commands a user could call on the command line to configure an image.

```
FROM alpine
RUN apk update && \
    apk add curl unzip nano sed

ENV PACKAGE_SOURCE=https://d3n46h3syaq3jo.cloudfront.net/b68748f5594ce2e8defceb9afe4a1b8eb74fb364/2020-05-21_AMS_CLI.zip
ENV PACKAGE_TARGET=2020-05-21_AMS_CLI.zip

RUN curl ${PACKAGE_SOURCE} -o ${PACKAGE_TARGET} \
    && unzip ${PACKAGE_TARGET} \
    && cd "./2020-05-21_AMS_CLI/Linux and Mac/" \
    && chmod u+x ./AWSManagedServices_InstallCLI.sh \
    && sh ./AWSManagedServices_InstallCLI.sh

ENTRYPOINT ["/bin/sh"]
```


#### lighttpd

Command structure
```sh
docker run --rm -t -v <home-directory>:/var/www/localhost/htdocs -p <http-port>:80 sebp/lighttpd
```


`--rm`: This removes the container when we exit the session
`-t`: Allocates a pseudo-TTY
`-v`: Bind mount a volume
`-p`: publish a container's port(s) to the host

Personal Command
```sh
docker run --rm -t -v /Users/anthonykwang/techtalks/techtalks/lighttpd:/var/www/localhost/htdocs -p 4200:80 sebp/lighttpd
```