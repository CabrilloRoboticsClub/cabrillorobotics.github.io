# Cabrillo Robotics Club Website
Source for [cabrillorobotics.org](http://cabrillorobotics.org/).

## Getting Started
### Install Jekyll
These instructions are for Ubuntu. For other OS view the [installation guide](https://jekyllrb.com/docs/installation/).

1. Install Ruby and other prerequisites.
    ```sh
    sudo apt-get install ruby-full build-essential zlib1g-dev
    ```
2. Avoid installing RubyGems packages (called gems) as the root user. 
    ```sh
    echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

3. Install Jekyll and Bundler.
    ```sh
    gem install jekyll bundler
    ```

### Deploy Locally
1. To deploy the site on a local server to see live changes as you develop, run the following in the root directory of this repository.
    ```sh
    bundle exec jekyll s
    ```
2. If `zsh: command not found: bundle` or similar error, re-source the `bashrc`.
    ```sh
    source ~/.bashrc
    ```
3. Follow the link provided following the`Server address:` qualifier. Should look something like the following. 
    ```sh
    Server address: http://127.0.0.1:4000
    ```
4. Save the content then refresh the page with `ctrl-shift-r` to see live changes (reload the current page, ignoring cached content).

### Deploy
1. GitHub actions will build and deploy the pages upon push to this branch.

## Resources
* [Github Pages](https://pages.github.com/)
* [Jekyll](https://jekyllrb.com/)
* [Bulma](https://bulma.io/documentation/)