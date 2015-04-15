# Counter-Strike: Global Offensive map overviews

This is a collection of radar overviews, and eventually thumbnails,
in more usable formats, with scripts for easily updating them.

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
