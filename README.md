# LinkedMusic

This is the repository for the LinkedMusic website distributed via GitHub Pages. It is a static website built to run without a content management system (CMS) like Jekyll. The website contents and dependency files are stored in this repository. The formatting was adapted from the Lanyon theme, developed by Mark Otto for the Jekyll site generator.

To view the old version using Forestry CMS, consult the 'old-forestry-website' branch.

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
git pull origin main
```

At this point, the site can be edited locally. Use the VSCode "Live Server" extension to view the static website in your browser and track changes automatically. You can also copy-paste the full path of the main index.html page into your preferred browser and navigate to the desired page through the URL.


## Updating Citations Locally

In order to update citations on the website, you will need access to the lab's Zotero collections. Once there, inside the LinkedMusic and SIMSSA folders, there are subfolders for _References_ and _Publications_, respectively.

To create an export, right click on the desired subfolder and select the option **Create Bibliography from Collection...**. At this point, make sure you have installed _SIMSSA's Chicago Manual of Style 17th edition_ inside the **Manage Styles...** popup. Then, set _Output Mode_ to **Bibliography** and _Output Method_ to **Save as HTML**. Select ok, and name the file one of
```
  <[SIMSSA/LinkedMusic]>_<[references/publications]>.html
```
depending on which folder you are exporting. Then, save it inside the `zotero_export/` folder within this directory.

_NOTE: make sure your generated HTML file contains all of the content you want displayed for the given page, old and new. Once the script is run, the existing page content will be **replaced** with the contents of your generated file, so include previous content you want to keep as well as any new modifications._ 

Next, run the `html_parser.py` script at the top level of this directory (works on Python 3.7, have not checked others). You will be prompted to input text based on which type of citations you would like to update, one of the three or all. The changes will be reflected in the `content.json` files in each of the specified folders, which are dynamically displayed in the static pages. Open any modified pages locally to ensure they display correctly before pushing to this repository.

_There is another GitHub Actions script called github_html_parser.py that was used in an attempt to automatically update the citation markdown files when zotero_export/ files are updated and pushed to the repo. It is currently deprecated._


