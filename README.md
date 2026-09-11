# Cabrillo Robotics Club Website

Source for [cabrillorobotics.org](http://cabrillorobotics.org/).

## Getting Started

These instructions are for Ubuntu. For other OS view the [installation
guide](https://jekyllrb.com/docs/installation/).

1. Install Ruby and other prerequisites.

    ```console
    $ sudo apt-get install ruby-full build-essential zlib1g-dev ruby-bundler
    ```

1. Install the necessary dependencies locally

    ```console
    $ bundle config set --local path .bundle
    $ bundle install
    ```
    
## Deploy Locally

1. To deploy the site on a local server to see live changes as you develop, run
   the following in the root directory of this repository.

    ```console
    $ bundle exec jekyll s
    ```

1. Follow the link provided following the `Server address:` qualifier. Should
   look something like the following:

    http://localhost:4000 

1. Save the content then refresh the page with `ctrl-shift-r` to see live
   changes (reload the current page, ignoring cached content).

## Deploy

1. GitHub actions will build and deploy the pages upon push to this branch.

## Resources

* [Github Pages](https://pages.github.com/)
* [Jekyll](https://jekyllrb.com/)
* [Bulma](https://bulma.io/documentation/)