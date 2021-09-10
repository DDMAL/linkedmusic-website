# LinkedMusic

This is the repository for the LinkedMusic website distributed via GitHub Pages. It is a static website built using Jekyll, meaning that there is no backend presence, and the entirety of the site is stored in this repository, blog contents included. The LinkedMusic site is based on the SIMSSA website with adjustments to content and style.

## Contents

- [Local Setup](#local-setup)
- [Troubleshooting](#troubleshooting)

## Local Setup

Note: GitHub pages is not set up yet but you can run it locally following this process, skip over the GitHub pages part and use the bundle command to view at the address given in your Terminal.

You will need to download a full [Ruby development environment](https://jekyllrb.com/docs/installation/) to install Jekyll. Follow steps 1 and 2 of [these instructions](https://jekyllrb.com/docs/) after installing Ruby.

Assuming you have [Git](https://www.atlassian.com/git/tutorials/install-git) installed, open a terminal and clone the repository into any known location on your computer. The documents folder is recommended, though it is up to you. 

```
git clone git@github.com:DDMAL/linkedmusic-website.git
```

Enter the directory with `cd linkedmusic-website`, and pull from the repository to your local folder. Specifically, pull from the 'gh-pages' branch, the branch used by GitHub Pages to host the site.

```
git pull origin gh-pages
```

At this point, the site is able to be edited and run locally. Assuming steps 1 and 2 of the Jekyll documentation were followed correctly, run:

```
bundle exec jekyll serve --watch
```

The built site can then be viewed at 'localhost:4000/linkedmusic-website/'. The `--watch` option automatically checks for updates to the local files and can be immediately viewed by refreshing the page. `--watch` is not supported by Windows, thus the command above will need to be rerun after each edit.

If any changes need to be made to the 'Gemfile' at the root directory, run:

```
bundle install
```

to install any updated or newly-added gems for the build. Then, the site can be rebuilt with `bundle exec jekyll serve --watch`.

In order to build the site for production, run the following locally then push changes to GitHub (pushing changes after running "serve" will result in incorrect resolution of URLs based on site.url)

`jekyll build JEKYLL_ENV=production`

(setting ENV is the important part; for more on this see: https://mademistakes.com/mastering-jekyll/site-url-baseurl/ )

Web hosting is set up through EasyDNS.

## Troubleshooting

If you are having any difficulties with setup, or local development, please feel free to email Emily Hopkins (emily.hopkins@mcgill.ca) or use the issues tab found in this repository. 
