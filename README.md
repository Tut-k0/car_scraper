# Auto Tempest Car Scraper

All of this is WIP currently.

### Running Instructions
```bash
pip install -r requirements.txt
```
You can either pass the parameters in the arguments, or make a config.json 
file in the src folder.
```bash
python scraper.py
# OR
python scraper.py -M Nissan -m 370z -r 300 -z 63116
```


### Issues
If this program does not run for you, make sure you have the latest version of
pyppeteer.
```bash
pip install -U git+https://github.com/pyppeteer/pyppeteer@dev
```
