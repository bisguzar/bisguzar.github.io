name: inverse
layout: true
class: center, middle, inverse
---
![Alt text](/src/img/logo.png)
.footnote[HUG Istanbul 2019]
---
## What is it and why should I be using it?
---
layout: false
.left-column[
  ## What is it?
]
.right-column[
Packer, by Hashicorp, is a command-line tool for quickly creating identical machine images for multiple platforms and environments. 

With Packer, you use a configuration file, called a template, to create a machine image containing a preconfigured operating system and software. You can then use this image to create new machines. 

You can even use a single template to orchestrate the simultaneous creation of your production, staging, and development environments.
]
---
.left-column[
  ## What is it?
  ## Why use it?
]
.right-column[
- **Super fast infrastructure deployment**

Packer images allow you to launch completely provisioned and configured machines in seconds, rather than several minutes or hours.

- **Multi-provider portability**

Because Packer creates identical images for multiple platforms, you can run production in AWS, staging/QA in a private cloud like OpenStack, and development in desktop virtualization solutions such as VMware or VirtualBox. Each environment is running an identical machine image, giving ultimate portability.

]
---
.left-column[
  ## What is it?
  ## Why use it?
]
.right-column[

- **Improved stability**

Packer installs and configures all the software for a machine at the time the image is built. If there are bugs in these scripts, they'll be caught early, rather than several minutes after a machine is launched.

- **Greater testability**

After a machine image is built, that machine image can be quickly launched and smoke tested to verify that things appear to be working. If they are, you can be confident that any other machines launched from that image will function properly.

]
---
template: inverse

## Install Packer
---
name: how

### Installing Packer

- Visit https://www.packer.io/downloads.html
- Then unzip the source 
- - for \*nix unzip to /usr/local/bin
---
template: inverse

## talk is cheap, show me the code
---
.left-column[
  ### Test Installation
]
.right-column[
Try to run **packer**

```shell
$ packer
```

successful installation will output something like

```shell
usage: packer [--version] [--help] <command> [<args>]

Available commands are:
    build       build image(s) from template
    fix         fixes templates from old versi...
    inspect     see components of a template
    push        push a template and supporting...
    validate    check that a template is valid
    version     Prints the Packer version
```

Packer installed successfully, lets create folder named ad **image** and prepare **template.json** inside it

]
???
next slide contains template.json with only builder type
---
.left-column[
  ### Test Installation
  ### Builders 1/3
]
.right-column[

###### image/template.json
```json
{
  "builders": [
    {
      "type": "digitalocean"
    }]
}
```
]
???
on next slide, we are providing details for digitalocean builder
---
.left-column[
  ### Test Installation
  ### Builders 2/3
]
.right-column[

###### image/template.json
```json
{
  "builders": [
    {
      "type": "digitalocean",
>     "ssh_username": "root",
>     "api_token": "YOUR_DIGITALOCEAN_API_TOKEN",
>     "image": "ubuntu-16-04-x64",
>     "region": "nyc1",
>     "size": "512mb"
    }]
}

```
]
???
on next slide, we are exporting api token as variable
---
.left-column[
  ### Test Installation
  ### Builders 3/3
]
.right-column[

Move API token to variables file, before moving create variables.json inside same directory with template.json

###### image/template.json
```json
{
  "digitalocean_api_token": "YOUR_DIGITALOCEAN_API_TOKEN"
}
```

Then edit template.json
###### image/template.json
```json
{
  "builders": [
    {
      "type": "digitalocean",
      "ssh_username": "root",
>     "api_token": "{{ user `digitalocean_api_token` }}",
      "image": "ubuntu-16-04-x64",
      "region": "nyc1",
      "size": "512mb"
    }]
}

```
]
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners 1/3
]
.right-column[

###### image/template.json
```json
{
  "builders": [
    {
      "type": "digitalocean",
      "ssh_username": "root",
      "api_token": "YOUR_DIGITALOCEAN_API_TOKEN",
      "image": "ubuntu-16-04-x64",
      "region": "nyc1",
      "size": "512mb"
>   }],
> "provisioners": [
>   {
>     "type": "file"
>   },
>   {
>     "type": "shell"
>   }]
}

```
]
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners 2/3
]
.right-column[

The file provisioner requires a source, which points to a local file path, and a destination, which points to an existing file path on the running machine. 

###### image/template.json

```json
{
  ...
  "provisioners": [
    {
      "type": "file",
>     "source": "configs/",
>     "destination": "/tmp"
    },
  ]
    ...
}
```
]
???
file provisioner requires **source** and **dest**

we will create these folders later
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners 3/3
]
.right-column[

Configure the shell provisioner 

###### image/template.json

```json
{
  ...
  "provisioners": [
    {
      "type": "file",
      "source": "configs/",
      "destination": "/tmp"
    },
    {
>     "type": "shell",
>     "scripts": [
>       "scripts/configureNginx.sh"
>     ]
    }]
}
```

template.json is ready for now, save and exit
]
???
in next slide, we are preparing default page for nginx
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs 1/3
]
.right-column[

Create configs/ folder inside image/ to create your Nginx configuration files

###### image/configs/index.html.new

```html
HI <b>HUG Istanbul</b>
```

template.json is ready for now, save and exit
]
???
in next slide we are preparing **route rule for nginx**
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs 2/3
]
.right-column[
###### image/configs/newDomain.conf

```dsconfig
server {
        listen 80;
        listen [::]:80;

        server_name ~^.*$;

        location / {
                root /var/www/html/newDomain;
                index index.html index.htm;
        }
}
```
]
???
in next slide we are preparing **nginx configuration**
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs 3/3
]
.right-column[
###### image/configs/nginx.conf.new

```dsconfig
user www-data;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local...]
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    ...
    }
```
]
???
in next slide we are preparing **installer script**
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs
  ### Scripts
]
.right-column[

Create scripts/ folder inside image/ and configureNginx.sh file inside scripts folder to prepare our installer script

###### image/scripts/configureNginx.sh

```bash
#!/bin/bash
# Script to install Nginx and enable on boot.

# Update your system:
apt-get update -y
apt-get upgrade -y

# Install Nginx:
apt-get install -y nginx

#Start Nginx service and enable to start on boot:
systemctl enable nginx
systemctl start nginx

# Create new 'vhost' directory for domain configuration:
mkdir /etc/nginx/vhost.d
...
```
]
???
**FFIINNIISSHHEEDD**

in next slide, **validate** packer conf
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs
  ### Scripts
  ### Validate
]
.right-column[

Everything looks like okay, but we can't trust senses. Let's pre-validate our process. Run **packer validate** to validation

```shell
$ packer validate -var-file=variables.json template.json

Output:
Template validated successfully.
```
]
???
validates successfully, **build** in next slide
---
.left-column[
  ### Test Installation
  ### Builders
  ### Provisioners
  ### Configs
  ### Scripts
  ### Validate
  ### Build
]
.right-column[

We are ready to build our image and create a snapshot on digitalocean. Run **packer build**

```shell
$ packer build -var-file=variables.json template.json
```

The output of a successful build will look similar to the following:

```shell
digitalocean output will be in this color.

==> digitalocean: Creating temporary ssh key for Droplet...
==> digitalocean: Creating Droplet...
==> digitalocean: Waiting for Droplet to become active...
==> digitalocean: Waiting for SSH to become available...
==> digitalocean: Connected to SSH!
==> digitalocean: Gracefully shutting down Droplet...
==> digitalocean: Creating snapshot: packer-1488487459
==> digitalocean: Waiting for snapshot to complete...
==> digitalocean: Destroying Droplet...
==> digitalocean: Deleting temporary ssh key...
Build 'digitalocean' finished.

==> Builds finished. The artifacts of successful builds are:
--> digitalocean: A snapshot was created: 'packer-1488487459'...
```
]

---
name: last-page-before-last-page
template: inverse

## showing code is cheap, lets see the process
---
name: last-page
template: inverse

# Thanks to HUG Istanbul

### @bugraisguzar
### github/bisguzar
### ben@bisguzar.com
