# static sites

## installing jekyll on Github pages

### 1) installing pre-requisites: ruby & jekyll

Follow instructions here (according to your Operating System) to install the requirements, which are ruby and jekyll:

https://jekyllrb.com/docs/installation/

### 2) fork a theme

Choose a jekyll theme that you like from these pages: https://jekyllrb.com/docs/themes/

Fork the theme by going to the github page, and on the top right, press "fork".

When you are prompted, be sure to change the name of the respository to something relevant to your project.

Then, clone the repo to your desktop.

```
cd Desktop
git clone [insert URL for your theme]
cd [insert name of theme folder]
```

Next, run bundle install to install the necessary jekyll packages (called "gems") in that folder.

```
bundle install
```

Finally, generate the website on your local machine:

```
bundle exec jekyll serve
```

### 3) editing pages

Open the folder of your repo on you desktop (or wherever you've saved it on your computer)

First, move all of the files (except README) in the root folder to nest permanently under the "docs" folder. You can leave the README.md file in the root (later on, you can add your own information here).

The "docs" folder is where Github looks for the HTML files to display on your site, so by moving the files there, you're making it easier for Github to generate your site later on.

Second, open the index.md file, which should now be in the "docs" folder. This file is written in markdown, and offers a handy key for markdown formatting. The top section (sandwiched by hyphens) is layout information for the page. Do not change these first three lines).

The rest you can delete to get rid of it, or keep it around for convenience, as it offers useful information on how to format markdown. I've simply "commented" it out using markdown comments, which look like this:

```
<!– –>
```

You can comment out most of that text by wrapping it with these symbols. For example, I'm commenting out the first line from the file below:

```
<!– Text can be bold, italic, ~strikethrough~ or `keyword`. –>
```

You can read a whole lot more about markdown formatting here: https://www.markdownguide.org/cheat-sheet/

Want to create new page? Create a new file for your page called PAGE-NAME.md, replacing PAGE-NAME with a meaningful filename for the page.

Add the following frontmatter to the top of the file, replacing PAGE-TITLE with the page's title and URL-PATH with a path you want for the page's URL. For example, if the base URL of your site is https://octocat.github.io and your URL-PATH is about/contact, your page will be located at https://octocat.github.io/about/contact.

```
layout: page
title: "PAGE-TITLE"
permalink: /URL-PATH
```

Below the frontmatter, add content for your page.

### 4) pushing to github pages
Add the github-pages gem to your `_config.yml` file.

```
gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugins 
```

Replace GITHUB-PAGES-VERSION with the latest supported version of the github-pages gem, which is "232" as of December 2024. Save and close the file.

Then, you'll have to build your gems once again, since you've just just added a new gem for github pages.

```
bundle install
```
For help, see "Configuring a publishing source for your GitHub Pages site": https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll

Then, go to `github.com` to your regular repository page.

On your github repo page, go to the "Settings" tab at the top. Then,
scroll down to the "Pages" tab on the left sidebar.

Then, on the main section of the page, go to the Branch heading. From the first dropdown, select "Master" or "Main," and on the second dropdown, select "docs". Finally, click save.

Congratulations!

Your website will be visible in a few minutes at the URL:

`your_username.github.io/your_repo_name`
