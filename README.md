# tor-country
A script to manually set the exit country for [Tor](https://www.torproject.org).

Let's say you are developing or operating a highly distributed application Continent or Global level with POPs (Point of Presence) and/or CDN providing services optimized per each region because of regulation compliance, as a feature per se, etc. There are two practical options for testing out such an infrastructure, either by using proxies or using Tor.

With vanilla Tor, though, you can't pick and choose the exit node unless you tell the software what country to use to exit the Onion, which is what this script is useful for.

### WARNING

The Tor Project devs don't like the idea of users changing entry/exit nodes.

> We recommend you do not use these — they are intended for testing and may disappear in future versions. 
> You get the best security that Tor can provide when you leave the route selection to Tor; overriding the entry / exit nodes can mess up your anonymity in ways we don't understand. 
> 
> [Tor FAQ](https://www.torproject.org/docs/faq.html.en#ChooseEntryExit)

### DISCLAIMER

Use this script if you know what you are doing and at your own risk.

# Set up

- Rename *template-config.ini* to *config.ini*
- Fill in the path information in *config.ini*
- Make *main.py* executable.

```bash
chmod u+x ./main.py
```
# Usage

You must pass in a valid country code, like this:

```bash
./main.py ca
```
or, if you want to have more than one country, like this:

```bash
./main.py ca gb de
```

Launch Tor.

# See
- https://www.torproject.org/docs/faq.html.en#ChooseEntryExit
- https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
- https://www.torproject.org/docs/faq.html.en#torrc
