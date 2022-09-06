# cabrillorobotics.github.io

# cabrillorobotics.org

this repo holds the source and built html for the cabrilllo robotics club website

github pages looks at `/docs/`

markdown site source is located in `/src/`


## Usage

this guide assumes you are using ubuntu bare metal or ubuntu through wsl

#### install dependancies

```console
sudo apt install \
python3-venv \
python3-sphinx
```

#### Fork this repo

Create your own fork to work in

https://github.com/cabrillorobotics/cabrillorobotics.github.io/fork


#### clone your fork

make sure to replace `<CHANGEME>` with your username

```console
cd ~
git clone https://github.com/<CHANGEME>/cabrillorobotics.github.io/
```
now enter the folder the fork is located in

```console
cd ~/cabrillorobotics.github.io
```

#### setup your python virtual enviroment

```console
python3 -m venv venv 
. ./venv/bin/activate 
pip install -r requirements.txt 
```

#### edit source

inside the `/src/` folder you can find the markdown source for the site.

edit this to edit the website

**DO NOT TOUCH /docs/. YOUR CHANGES WILL BE OVERRIDDEN BY THE NEXT RENDER**

#### render source into site

```console
cd ~/cabrillorobotics.github.io
make html
```

#### commit changes and push

```console
git add --all
git commit -a -m "update website"
git push
```

#### open PR to push source to main

now open a pull request to push the source code to the main repo that the site is atually based on
(you can do this on your own)