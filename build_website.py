"""Regenerate the static companion website from the Markdown guide (requires Pandoc)."""
from pathlib import Path
import html
import re
import subprocess

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'
DOCS.mkdir(exist_ok=True)
BUTTONS = DOCS / 'buttons'
BUTTONS.mkdir(exist_ok=True)
for slug, top, bottom, color in [
    ('join-the-indieweb','JOIN THE','INDIEWEB','#e4eddb'),
    ('indieweb','INDIE','WEB','#e4eddb'),
    ('neocities','NEOCITIES','HANDMADE WEB','#f2d775'),
    ('nekoweb','NEKOWEB','PERSONAL SITES','#e4eddb'),
    ('bear','BEAR BLOG','JUST WRITE','#f2d775'),
    ('handmade','HANDMADE','WITH HTML','#e4eddb'),
    ('nocookies','NO TRACKING','SMALL WEB','#f2d775'),
    ('rss','RSS FEEDS','READ MORE','#e4eddb'),
]:
    (BUTTONS/(slug+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="88" height="31" viewBox="0 0 88 31"><rect width="88" height="31" fill="#276345"/><rect x="2" y="2" width="84" height="27" fill="{color}" stroke="#fffef7"/><path d="M9 25V15C9 8 16 6 20 6 20 14 16 18 9 18M9 21C3 21 4 13 4 11 9 11 11 16 9 21" fill="#83b37c" stroke="#276345" stroke-width="1"/><text x="53" y="13" text-anchor="middle" font-family="monospace" font-size="8" font-weight="bold" fill="#27362b">{top}</text><text x="53" y="23" text-anchor="middle" font-family="monospace" font-size="7" font-weight="bold" fill="#27362b">{bottom}</text></svg>',encoding='utf-8')
CHAPTERS = [
    ('01-what-is-the-indieweb', 'What is the IndieWeb?', 'Own your identity, content and little corner of the internet.'),
    ('02-choose-a-platform', 'Choose your platform', 'Compare handmade sites, hosted blogs, static generators and CMSs.'),
    ('03-domains-and-hosting', 'Domains & hosting', 'Register an address, understand DNS and publish a site.'),
    ('04-learn-the-web', 'Learn the web', 'A practical roadmap for HTML, CSS, accessibility and Git.'),
    ('05-build-your-site', 'Build your personal site', 'Ideas for pages, navigation, design and your first post.'),
    ('06-publishing-and-feeds', 'Publishing & RSS feeds', 'Share your writing, follow blogs and syndicate on your own terms.'),
    ('07-indieweb-standards', 'IndieWeb standards', 'Microformats, Webmentions, IndieAuth and other optional tools.'),
    ('08-community', 'Community & connections', 'Find meetups, blogrolls, webrings and other people.'),
    ('09-care-for-your-site', 'Care for your site', 'Privacy, accessibility, backups and keeping your site alive.'),
    ('10-blogging-and-microblogging', 'Blogging & microblogging', 'Discover blogs, short notes, digital gardens and more.'),
    ('11-three-ways-to-start', 'Three ways to start', 'Compare Neocities, Nekoweb and Bear Blog.'),
    ('12-decentralized-social', 'Decentralized social media', 'Explore Mastodon, Pixelfed, Bluesky, Lemmy and open protocols.'),
    ('13-discovery', 'Discover the small web', 'Marginalia, Wiby, directories and the joy of browsing.'),
    ('14-personal-web-toolkit', 'Personal web toolkit', 'Guestbooks, web buttons, image galleries, contact forms and more.'),
]

def esc(text):
    return html.escape(text, quote=True)

def frame(title, desc, page, content, section=''):
    nav = [('index.html','Home'),('guide.html','The guide'),('resources.html','Resources'),('inspiration.html','Inspiration'),('blogroll.html','Blogroll'),('changelog.html','Site log')]
    links = ''.join(f'<li><a href="{url}"'+(' aria-current="page"' if page == url else '')+f'>{label}</a></li>' for url,label in nav)
    aside = f'''<aside class="leftbar"><section class="window"><h2>✿ site map</h2><nav aria-label="Main navigation"><ul class="site-map">{links}</ul></nav></section><section class="window"><h2>webmaster's note</h2><div class="inside"><p>A little guide for people who want a place of their own online.</p><p class="small">No accounts, analytics or frameworks.</p></div></section><section class="window"><h2>change the mood</h2><div class="inside"><button class="theme" type="button" data-toggle-theme aria-label="Switch color theme">☾</button> <small>light / dark</small></div></section><section class="window"><h2>link back?</h2><div class="inside badgecenter"><a href="index.html"><img src="buttons/join-the-indieweb.svg" width="88" height="31" alt="Join the IndieWeb"></a><p class="small">Save the button and link to this guide.</p></div></section></aside>'''
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{esc(title)} | Join the IndieWeb</title><meta name="description" content="{esc(desc)}"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="retro.css"><script src="site.js" defer></script></head>
<body><a class="skip" href="#main">Skip to content</a><div class="webpage"><header class="sitebanner"><div class="banner-art"><a class="brand" href="index.html"><img src="favicon.svg" alt=""><span>join the <strong>indieweb</strong><small>✿</small></span></a><p>a little guide to making your own corner of the internet</p></div><div class="ticker">✦ welcome, wanderer! &nbsp; · &nbsp; make a site &nbsp; · &nbsp; share a link &nbsp; · &nbsp; keep the web human ✦</div></header>
<div class="site-layout">{aside}<main id="main">{content}</main></div><footer class="foot"><div><p>handmade for the small web ♡ · CC BY 4.0</p><p><a href="https://github.com/kauz-hub/join-the-indieweb">source code</a><a href="contributing.html">contribute</a><a href="license.html">license</a><a href="https://indieweb.org/">IndieWeb wiki</a><a href="#">back to top</a></p></div></footer></div></body></html>'''

def card(i):
    slug,title,desc=CHAPTERS[i-1]
    return f'<article class="directory-entry" data-chapter><span class="num">{i:02}.</span><div><h3><a href="{slug}.html">{esc(title)}</a></h3><p>{esc(desc)}</p></div></article>'

def save(name, title, desc, body, section=''):
    (DOCS/name).write_text(frame(title, desc, name, body, section), encoding='utf-8')

home = '''<div class="home-grid"><div class="home-main"><section class="window welcome"><h1>hello, internet! ✧</h1><div class="inside"><img src="favicon.svg" class="sprout" alt=""><p>Welcome to <b>Join the IndieWeb</b>, a small guide to making a little corner of the internet your own.</p><p>Maybe you want to start a blog, make a handmade homepage, or just find interesting places outside social media. You've come to the right place.</p><p>You don't need a perfect site or a fancy framework. Start with one page and see where it takes you.</p><p class="notebox"><a href="01-what-is-the-indieweb.html">New here? Start with the basics.</a></p></div></section>
<div class="divider" aria-hidden="true">✦ · . · ✧ · . · ✦ · . · ✧ · . · ✦</div>
<section class="window"><h2>where do i start?</h2><div class="directory-list">'''+card(1)+card(11)+card(10)+card(4)+card(12)+card(13)+'''</div><div class="inside"><a href="guide.html">See all fourteen chapters</a></div></section>
<section class="window"><h2>your first hour ☘</h2><div class="inside"><p>A little checklist for your first website. Progress is saved only in your browser.</p><div class="checklist"><label><input type="checkbox" data-check="1">Choose a blog or website host.</label><label><input type="checkbox" data-check="2">Publish a short introduction.</label><label><input type="checkbox" data-check="3">Write something or share a favorite link.</label><label><input type="checkbox" data-check="4">Visit another personal website.</label><label><input type="checkbox" data-check="5">Save a backup of your work.</label></div></div></section>
<section class="window"><h2>the neighborhood</h2><div class="inside"><p>Personal sites are connected by people, not a recommendation feed. Browse a few, then make a blogroll of your own!</p><div class="button-wall"><a href="https://indieweb.org/"><img src="buttons/indieweb.svg" width="88" height="31" alt="IndieWeb"></a><a href="https://neocities.org/"><img src="buttons/neocities.svg" width="88" height="31" alt="Neocities"></a><a href="https://nekoweb.org/"><img src="buttons/nekoweb.svg" width="88" height="31" alt="Nekoweb"></a><a href="https://bearblog.dev/"><img src="buttons/bear.svg" width="88" height="31" alt="Bear Blog"></a></div><p><a href="blogroll.html">Visit the blogroll</a> · <a href="inspiration.html">See personal websites</a></p></div></section></div>
<aside class="rightbar"><section class="window"><h2>site info</h2><div class="inside"><p><b>est.</b> 2026<br><b>made with:</b> HTML + CSS<br><b>status:</b> a work in progress</p><p class="small">Read the <a href="changelog.html">site log</a>.</p></div></section><section class="window"><h2>quick links</h2><ul class="site-map"><li><a href="resources.html">Resource directory</a></li><li><a href="06-publishing-and-feeds.html">RSS and feeds</a></li><li><a href="07-indieweb-standards.html">IndieWeb standards</a></li><li><a href="14-personal-web-toolkit.html">Webmaster tools</a></li><li><a href="https://github.com/kauz-hub/join-the-indieweb">GitHub repo</a></li></ul></section><section class="window"><h2>88 × 31 club</h2><div class="inside badgecenter"><img src="buttons/handmade.svg" width="88" height="31" alt="Handmade with HTML"><img src="buttons/nocookies.svg" width="88" height="31" alt="No tracking"><img src="buttons/rss.svg" width="88" height="31" alt="Read with RSS"><p class="small">Little buttons, big web.</p></div></section><section class="window"><h2>explore!</h2><div class="inside"><p><a href="https://marginalia-search.com/">Marginalia</a><br><a href="https://wiby.me/">Wiby search</a><br><a href="https://indieblog.page/">random blog post</a></p><p class="small">Find something unexpected.</p></div></section></aside></div>'''
save('index.html','A field guide','A practical guide to making your own corner of the independent web.',home)

groups = [('Start small',[1,2,11,3]),('Make and publish',[4,5,10,6]),('Connect & explore',[7,8,12,13]),('Keep it going',[9,14])]
guide = '<div class="wrap"><header class="subhero"><p class="eyebrow">The handbook</p><h1>Explore the guide.</h1><p>Fourteen chapters, from your first homepage to feeds, decentralized networks, and the standards that connect independent sites. Read in any order.</p></header><div class="filterbox"><label for="filter">Find a chapter</label><input id="filter" type="search" data-filter placeholder="Try RSS or Bear Blog"><output data-count aria-live="polite">14 chapters</output></div><p class="no-results" data-empty hidden>No matching chapters. Try a shorter search.</p>'
for title, inds in groups:
    guide += f'<section class="group" data-group><h2>{esc(title)}</h2><div class="cards">'+''.join(card(i) for i in inds)+'</div></section>'
guide += '</div>'
save('guide.html','Guide','Browse all fourteen chapters of the IndieWeb handbook.',guide)

save('blogroll.html','Blogroll','A little collection of personal websites and directories.','''<div class="wrap reading"><article class="article"><p class="eyebrow">the neighborhood</p><h1>blogroll ✿</h1><p>A few places to wander. Follow their links, find things you love, and make your own blogroll.</p><h2>personal sites &amp; blogs</h2><ul><li><a href="https://blog.someplace-else.xyz/">someplace elsewhere</a> — personal writing and photography</li><li><a href="https://nenrikido.neocities.org/">NENRIKIDO</a> — handmade pages and a microblog</li><li><a href="https://aroma.bearblog.dev/">aroma</a> — independent blog</li><li><a href="https://birming.com/blog-inspiration">Robert Birming</a> — blogging inspiration</li><li><a href="https://byzxor.xyz/">byzxor</a> — personal writing</li><li><a href="https://angs-corner.nekoweb.org/">ang's corner</a> — handmade homepage</li></ul><h2>directories &amp; rings</h2><ul><li><a href="https://ooh.directory/">ooh.directory</a></li><li><a href="https://indieseas.net/">IndieSeas</a></li><li><a href="https://indieblog.page/">indieblog.page</a></li><li><a href="https://nenrikido.neocities.org/webrings/journalring">JournalRing</a> — explore journal-style sites</li></ul><p>More examples are on the <a href="inspiration.html">inspiration page</a>. Learn to make a <a href="08-community.html">blogroll or join a webring</a>.</p></article></div>''')
save('changelog.html','Site log','Notes about the guide and website.','''<div class="wrap reading"><article class="article"><p class="eyebrow">site diary</p><h1>site log ☘</h1><h2>November 2026</h2><p><b>Companion site redesigned.</b> A handmade homepage layout, sidebar navigation, small badges, and separate blogroll and site log pages.</p><p><b>Guide expanded.</b> Blogging, microblogging, decentralized social networks, and small-web discovery have their own chapters.</p><p><b>First version.</b> Published the initial Markdown guide, resource directory, and contribution instructions.</p><p><a href="https://github.com/kauz-hub/join-the-indieweb">See the repository for the source and history.</a></p></article></div>''')

def convert(md):
    text = md.read_text(encoding='utf-8')
    # The shared site navigation replaces the original Markdown navigation line.
    text = re.sub(r'^\[(?:Home|Back to the guide)\]\([^\n]+\n', '', text, flags=re.M)
    markup = subprocess.run(['pandoc','--from=gfm','--to=html5','--wrap=none','--no-highlight'],input=text,text=True,check=True,capture_output=True).stdout
    def replace_link(m):
        href=m[1]
        if href.startswith(('http:', 'https:', 'mailto:','#')): return m[0]
        path, _, fragment = href.partition('#')
        name=Path(path).name
        names={'README.md':'index.html','RESOURCES.md':'resources.html','INSPIRATION.md':'inspiration.html','CONTRIBUTING.md':'contributing.html','LICENSE.md':'license.html'}
        if name.endswith('.md'):
            href=names.get(name,Path(name).stem+'.html')+('#'+fragment if fragment else '')
        return f'href="{href}"'
    markup = re.sub(r'href="([^"]+)"',replace_link,markup)
    markup = markup.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    return markup

def sidebar(current):
    out='<aside class="sidebar" aria-label="Chapter navigation"><h2>In the guide</h2><a href="guide.html">All chapters</a>'
    for i,(slug,title,_) in enumerate(CHAPTERS,1):
        out += f'<a href="{slug}.html"'+(' aria-current="page"' if current==slug+'.html' else '')+f'>{i:02} · {esc(title)}</a>'
    return out+'</aside>'

for idx,(slug,title,desc) in enumerate(CHAPTERS):
    name=slug+'.html'
    article=convert(ROOT/'guides'/(slug+'.md'))
    prev = f'<a href="{CHAPTERS[idx-1][0]}.html">Previous chapter</a>' if idx else '<a href="guide.html">All chapters</a>'
    nxt = f'<a href="{CHAPTERS[idx+1][0]}.html">Next chapter</a>' if idx+1<len(CHAPTERS) else '<a href="resources.html">Resource directory</a>'
    body=f'<div class="wrap reading">{sidebar(name)}<article class="article"><p class="eyebrow">Chapter {idx+1:02} · Field guide</p>{article}<nav class="chapter-nav" aria-label="Chapter navigation">{prev}{nxt}</nav></article></div>'
    save(name,title,desc,body,'guide.html')

for md,name,title in [('RESOURCES.md','resources.html','Resource directory'),('INSPIRATION.md','inspiration.html','Personal website inspiration'),('CONTRIBUTING.md','contributing.html','Contribute'),('LICENSE.md','license.html','License')]:
    body='<div class="wrap reading">'+sidebar(name)+'<article class="article">'+convert(ROOT/md)+'</article></div>'
    save(name,title,title+' for the independent web.',body)
