# PySitemap

Simple sitemap generator with Python 3

## Description
This is simple and easy sitemap generator written in python which can help you easily create sitemap of your website for SEO and other purposes.

## Options
Simply you can run with thisthis command and program will create sitemap.xml with links from url option
```
python main.py --url="https://www.finstead.com"
```

If you want the search to include all subdomains like docs.finstead.com
```
python main.py --url="https://www.finstead.com" --domain="finstead.com"
```

If you want custome path for sitemap file you can add `--output` option like below
```
python main.py --url="https://www.finstead.com" --output="/custom/path/sitemap.xml"
```

By default program will print parsing urls in console, but if you want to run siletnly you can add `--no-verbose` option.
```
python main.py --url="https://www.finstead.com" --output="/custom/path/sitemap.xml" --no-verbose
```

If you want to restrict some urls from being visited by crawler you can exclude them with regex pattern using `--exclude` option. Below code will exclude `png` or `jpg` files.
```
python main.py --url="https://www.finstead.com" --output="/custom/path/sitemap.xml" --exclude="\.jpg|\.png"
```