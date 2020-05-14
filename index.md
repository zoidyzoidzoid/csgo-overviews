# Counter-Strike: Global Offensive map overviews

This is a collection of radar overviews, and eventually thumbnails,
in more usable formats, with scripts for easily updating them.
The scripts use [pyglet](https://warehouse.python.org/project/pyglet/) to convert 
the raw DDS files to PNG files, and then [Pillow](https://warehouse.python.org/project/Pillow/) to resize
the PNG files.

The converting stuff should work for any DDS files to PNG.

If you're just looking for image versions of the maps, go to the [Releases](https://github.com/zoidbergwill/csgo-overviews/releases)
and get the latest [`overviews.zip`](https://github.com/zoidbergwill/csgo-overviews/releases/download/0.0.1/overviews.zip)

## Updating the overviews

* Prepare the virtualenv:

```bash
  virtualenv virtualenv
  . virtualenv/bin/activate
  pip install -r requirements.txt
```

* Drop the `.dds` files from `common/Counter-Strike Global Offensive/csgo/resource/overviews` in
`csgo-overviews/overviews/raw`.

* Run the script:

```bash
  scripts/update_overviews.py
```

## Contributing

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

### Report Bugs

Report bugs using the [issue tracker](https://github.com/zoidbergwill/csgo-overviews/issues?state=open).

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug"
is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "feature"
is open to whoever wants to implement it.

### Submit Feedback

The best way to send feedback is using the [issue tracker](https://github.com/zoidbergwill/csgo-overviews/issues?state=open)

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)


## Obvious licensing stuff

All images belong to Valve.

### Welcome to GitHub Pages.
This automatic page generator is the easiest way to create beautiful pages for all of your projects. Author your page content here using GitHub Flavored Markdown, select a template crafted by a designer, and publish. After your page is generated, you can check out the new branch:

```
$ cd your_repo_root/repo_name
$ git fetch origin
$ git checkout gh-pages
```

If you're using the GitHub for Mac, simply sync your repository and you'll see the new branch.

### Designer Templates
We've crafted some handsome templates for you to use. Go ahead and continue to layouts to browse through them. You can easily go back to edit your page before publishing. After publishing your page, you can revisit the page generator and switch to another theme. Your Page content will be preserved if it remained markdown format.

### Rather Drive Stick?
If you prefer to not use the automatic generator, push a branch named `gh-pages` to your repository to create a page manually. In addition to supporting regular HTML content, GitHub Pages support Jekyll, a simple, blog aware static site generator written by our own Tom Preston-Werner. Jekyll makes it easy to create site-wide headers and footers without having to copy them across every page. It also offers intelligent blog support and other advanced templating features.

### Authors and Contributors
You can @mention a GitHub username to generate a link to their profile. The resulting `<a>` element will link to the contributor's GitHub Profile. For example: In 2007, Chris Wanstrath (@defunkt), PJ Hyett (@pjhyett), and Tom Preston-Werner (@mojombo) founded GitHub.

### Support or Contact
Having trouble with Pages? Check out the documentation at https://help.github.com/pages or contact support@github.com and we’ll help you sort it out.
