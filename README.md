# LinkedMusic

This is the repository for the LinkedMusic website distributed via GitHub Pages. It is a static website built to run without a content management system (CMS) like Jekyll. The website contents and dependency files are stored in this repository. The formatting was adapted from the Lanyon theme, developed by Mark Otto for the Jekyll site generator.

## Contents

- [Local Setup](#local-setup)

## Local Setup

### macOS / Windows / Linux Install

Assuming you have [Git](https://www.atlassian.com/git/tutorials/install-git) installed, open a terminal and clone the repository into any known location on your computer. The documents folder is recommended, though it is up to you.

### Configuration and building site locally

```
git clone https://github.com/DDMAL/linkedmusic-website.git
```

Enter the directory with `cd linkedmusic-website`, and pull from the repository to your local folder. Specifically, pull from the 'deforested' branch, the branch used by GitHub Pages to host the site.

```
git pull origin deforested
```

At this point, the site can be edited locally. Use the VSCode "Live Server" extension to view the static website in your browser and track changes automatically. You can also copy-paste the full path of the main index.html page into your preferred browser and navigate to the desired page through the URL.