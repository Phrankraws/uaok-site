"""Builds the 6 BatMaine product pages for uaok-site (shared batmaine.css)."""
import html, sys, pathlib

OUT = pathlib.Path(sys.argv[1])

def esc(s): return html.escape(s, quote=True)

PAGES = [
dict(
 file="researcher.html", topic="researcher", brand=("BatMaine", "Researcher"),
 accent=("#0B7369", "#FFFFFF", "#4FD1C0", "#04211D"),
 title="BatMaineResearcher — An AI Research Team for Your Big Questions",
 desc="Four AI researchers work your question: one finds sources, one checks them, one tries to prove it wrong, one writes it up. A plain-English report with every source listed.",
 label="AI research team · Done for you",
 h1="Questions in. <em>Proven answers</em> out.",
 lede="Four AI researchers work your question. One finds sources, one checks them, one tries to prove it wrong, and one writes it up in plain English, with every source listed.",
 cta="Get a report",
 demo=[("You ask", "“Should my food truck take catering orders in Oakland?”"),
       ("Scout", "Finds <b>38 sources</b> and ranks them by how trustworthy they are"),
       ("Verifier", "Double-checks the <b>12 facts</b> the answer depends on"),
       ("Red Team", "Tries to prove the answer wrong and finds <b>3 risks</b>"),
       ("Your report", "“Yes, with a catering permit.” The cost, the steps, and what to watch, each marked <b>High</b>, <b>Medium</b> or <b>Low</b> confidence")],
 ticker=["Small businesses","Nonprofits","Grant writers","Ministries","Food trucks","Students","Big purchases","New ideas"],
 makes_label="What we research", makes_h="Big decisions, checked from every side",
 makes=[("Market research","Who your customers are, what they pay, and who you're up against."),
        ("Check before you sign","Look into a company, vendor or person before you hand over money."),
        ("Rules + permits","What licenses, permits and rules apply to your idea, in your city."),
        ("Will it work?","Pros, cons, costs and risks of a new idea before you put money in.")],
 steps=[("Tell us the question","Send a message or hop on a 15-minute call. We help you sharpen the question so the answer is useful."),
        ("The team digs in","The Scout gathers sources and sorts them: official and expert sources first, opinions last."),
        ("We try to prove it wrong","Before anything is written, the Red Team looks for the facts that would change the answer. Most research skips this step."),
        ("You get the report","A plain-English PDF: the answer up top, how sure we are, the reasons, and every source with a link.")],
 tiers=[
   dict(name="Quick Report", price="$149", was="One question · about 3 business days", fit="For one clear decision you need to make soon.",
        items=["One question, fully researched","A 4 to 6 page plain-English report","Every source listed with a link","Confidence marked on each finding","One follow-up question by message"], btn="Order a Quick Report"),
   dict(name="Deep Dive", price="$397", was="Up to 3 related questions · about 7 business days", fit="For big money decisions, new ventures and grant applications.", pick=True,
        items=["Everything in the Quick Report","Up to 3 related questions in one report","A 15 to 20 page report with a one-page summary","A 30-minute call to walk through it","Two weeks of follow-up questions"], btn="Order a Deep Dive"),
 ],
 addon=("Monthly Watch, $99/month (optional).", "We re-check your topic every month and send you what changed: new rules, new competitors, new prices."),
 rules=[("Every claim has a source.","If we can't point to where it came from, it doesn't go in the report."),
        ("We tell you how sure we are.","Each finding is marked High, Medium or Low confidence, with the reason."),
        ("We try to prove ourselves wrong.","A whole step is spent looking for evidence against the answer."),
        ("No made-up numbers.","If the facts aren't out there, the report says so instead of guessing."),
        ("Your question stays private.","We don't share your question or your report with anyone.")],
 faq=[("Is this a person or AI?","It's an AI research team run with Claude, set up and checked by UAOK before it reaches you."),
      ("Is this legal or medical advice?","No. It's research to help you decide and to ask better questions. For legal, tax or medical decisions, take the report to a professional."),
      ("What if there's no clear answer?","Then the report says so, tells you what's still unknown, and how you could find out."),
      ("Can you research a person?","Only for business reasons, like checking a contractor or a business partner, using public information.")],
 order_h="Got a big question?",
 hint="BatMaineResearcher order: which one (Quick Report or Deep Dive), and what's your question?",
 menu="BatMaineResearcher",
 card="An AI research team: sources found, checked, and challenged before a plain-English report.",
),
dict(
 file="avatar.html", topic="avatar", brand=("BatMaine", "Avatar"),
 accent=("#6A2FD6", "#FFFFFF", "#B79BFF", "#160733"),
 title="BatMaineAvatar — Done-for-You Social Posts for Your Business",
 desc="Send us your website, an idea or a few photos. We turn it into pictures, short videos and talking avatar videos, scheduled on your social media. You approve every one.",
 label="Done-for-you social posts · For businesses",
 h1="Your website in. <em>A month of posts</em> out.",
 lede="Send us your website, an idea or a few photos. We turn it into pictures, short videos and talking avatar videos for Instagram, TikTok, Facebook and LinkedIn. You approve every one.",
 cta="Get my posts",
 demo=[("You send","Your website link and 3 photos"),
       ("We pull","Your services, prices, hours and best reviews"),
       ("We make","<b>12 posts</b>: picture posts, 8-second videos, and a talking avatar video"),
       ("Calendar","Mon 9 AM Instagram + TikTok · Wed 12 PM Facebook · Fri 5 PM LinkedIn"),
       ("You","Tap <b>approve</b>, and they're scheduled")],
 ticker=["Restaurants","Food trucks","Barbers","Nail techs","Event planners","Ministries","Nonprofits","Local shops"],
 makes_label="What you get", makes_h="Posts that sound like your business",
 makes=[("Picture posts","Eye-catching pictures for your offers, menu, events and tips, with captions written in your voice."),
        ("Short videos","8-second vertical videos with your hook line big on screen, made for Reels and TikTok."),
        ("Talking avatar videos","An avatar of you, or a made-up spokesperson, speaks a 30-second script with captions."),
        ("Captions + calendar","A posting calendar and captions for each app, scheduled for you when you approve.")],
 gallery=[("avatar-media/ai-person.jpg","An AI-made woman with curly hair in a green sweater, smiling at home","1 · A made-up AI person","portrait"),
          ("avatar-media/ai-person-post.jpg","The same AI-made woman plating pasta in a bright kitchen","2 · The same face in a post","portrait"),
          ("avatar-media/ai-person-cartoon.jpg","The same woman as a 3D cartoon character with curly hair and a green sweater","3 · Now she's a cartoon character","portrait")],
 gallery_h="One face, a photo or a cartoon",
 gallery_note="She isn't a real person. We made her from a typed description, kept the same face in every post, then turned her into a cartoon character for a fun series. Your spokesperson can be you, someone made-up like her, or a mascot.",
 steps=[("Send your stuff","Your website, a few photos, or just an idea. Whatever you have."),
        ("A quick interview","How you talk, who your customers are, and anything we should never say."),
        ("See a sample first","You see the first post and the plan before the rest are made."),
        ("We schedule them","Your posts go out on your accounts on the days you pick. Or we send them as drafts for you to post.")],
 tiers=[
   dict(name="Launch Pack", price="$297", was="One time", fit="For trying it out or kicking off a new season.",
        items=["12 posts","2 short videos","1 talking avatar video","A 2-week posting calendar"], btn="Start a Launch Pack"),
   dict(name="Monthly", price="$397<small>/mo</small>", was="Cancel any time", fit="For businesses that want to show up every week.", pick=True,
        items=["20 posts a month","4 short videos a month","2 talking avatar videos a month","Scheduled for you","A monthly check-in call"], btn="Start Monthly"),
   dict(name="Growth", price="$697<small>/mo</small>", was="Cancel any time", fit="For busy brands posting every day.",
        items=["30 posts a month","8 short videos a month","4 talking avatar videos a month","“Comment a word, get a DM” setup","A monthly results report"], btn="Start Growth"),
 ],
 addon=None,
 extra_note='Want to make posts yourself, on your own Mac? See <a href="influencer.html">BatMaineInfluencer</a>, the do-it-yourself studio.',
 rules=[("You approve every post.","Nothing goes out until you say it's good."),
        ("Your accounts stay yours.","We post through a scheduling tool you control. You can turn it off any time."),
        ("Your face only with your OK.","We only make an avatar of you if you ask for one. A made-up spokesperson is brand-new, never a real person."),
        ("No surprise costs.","The price you pick covers the posts. No extra charges for the AI.")],
 faq=[("Do I need to show my face?","No. We can use a made-up spokesperson, a cartoon mascot, or no person at all."),
      ("Which apps can you post to?","Instagram, TikTok, Facebook and LinkedIn. Tell us which ones you use."),
      ("Can I change a post?","Yes. Ask for changes before you approve. Each post gets one free round of changes."),
      ("How is this different from BatMaineInfluencer?","BatMaineAvatar is done for you: we make and schedule the posts. BatMaineInfluencer is a kit you run yourself on your Mac.")],
 order_h="Ready for a month of posts?",
 hint="BatMaineAvatar order: which plan (Launch Pack, Monthly or Growth), your website, and which apps you post on?",
 menu="BatMaineAvatar",
 card="Done-for-you social posts: your website or idea becomes pictures, videos and a posting calendar.",
),
dict(
 file="crm.html", topic="crm", brand=("BatMaine", "CRM"),
 live_demo=dict(url="https://web-production-9e4b9.up.railway.app/admin/login", user="demo", password="TryIt-2026"),
 accent=("#2F45E0", "#FFFFFF", "#8FA0FF", "#0A0F33"),
 title="BatMaineCRM — Your Business Website and Customer Book in One",
 desc="A real website for your business plus a private dashboard: every lead, booking, order and payment in one place, on your phone.",
 label="Website + CRM · For small businesses",
 h1="Your website and <em>your customer book</em>, in one.",
 lede="A real website for your business, plus a private dashboard behind it. Every lead, booking, order and payment is in one place, and it works on your phone.",
 cta="Get started",
 demo=[("Visitor","Fills out your form: “Catering for 40, Saturday 6 PM”"),
       ("Website","Saves it and sends you a text right away"),
       ("CRM","New lead → Quoted → Booked → <b>Paid</b>"),
       ("Dashboard","This month: <b>$8,400</b> of your $10,000 goal")],
 ticker=["Food trucks","Kitchens","Ministries","Medical transport","Nail techs","DJs","Event planners","Contractors"],
 makes_label="What you get", makes_h="Everything behind your business, in one login",
 makes=[("Your website","Works on phones, in your colors, with your photos, menu or services and a booking or order form."),
        ("Customer book (CRM)","CRM means a customer book: every person who contacted you, what they wanted, and where the deal stands."),
        ("Get paid online","Customers pay deposits or full orders by card, right from your site."),
        ("Live dashboard","See this month's money, your goal, new leads and what needs a reply, at a glance.")],
 steps=[("A short interview","15 minutes on what you sell, who buys it, and what you want customers to do."),
        ("We build it","Your website and dashboard, usually in 1 to 2 weeks."),
        ("You look it over","Click around and tell us what to change. We fix it."),
        ("Go live + training","It goes live on your own web address, and we show you how to use it on a call.")],
 tiers=[
   dict(name="Starter", price="$997", was="One time", fit="For getting a real website and customer book fast.",
        items=["A website up to 5 pages","Contact or booking form","Your customer book (CRM)","Hooked up to your own web address","One training call"], btn="Start Starter"),
   dict(name="Business", price="$1,997", was="One time", fit="For businesses that take orders, bookings or payments.", pick=True,
        items=["Everything in Starter","Online payments by card","Text and email alerts for new leads","Live dashboard with a monthly goal","Menu, photo gallery or store page","60 days of changes"], btn="Start Business"),
 ],
 addon=("Monthly care, $49/month (optional).", "We keep it running: fixes, updates, small changes and a monthly check-in."),
 extra_note="Hosting (the computer that keeps your site online) is billed to you directly, usually $5 to $20 a month. A web address is about $12 a year.",
 rules=[("You own it.","Your website, your customer list and your data belong to you."),
        ("Private by default.","Your dashboard is behind a password. Customers only see your website."),
        ("Change your own words.","Update text, prices and photos yourself from the dashboard."),
        ("Your money goes straight to you.","Card payments go to your own account, not through us.")],
 faq=[("Do I need to know anything about tech?","No. We set it all up and show you how to use it on a call."),
      ("I don't have a web address. Is that OK?","Yes. We help you pick and buy one. It costs about $12 a year."),
      ("Can I see it before I buy?","Yes. Try the live demo at the top of this page: a sample website and the CRM behind it, filled with made-up customers. Send a message on the sample site and watch it show up in the CRM."),
      ("What happens if something breaks?","With Monthly care, we fix it. Without it, we fix it at our hourly rate.")],
 order_h="Ready for your own website and CRM?",
 hint="BatMaineCRM order: which plan (Starter or Business), your business name, and what you sell?",
 menu="BatMaineCRM",
 card="A business website plus a private customer book: leads, bookings, payments and a live dashboard.",
),
dict(
 file="text-scheduling.html", topic="text-scheduling", brand=("BatMaine", "TextScheduling"),
 accent=("#17803F", "#FFFFFF", "#5EDB8E", "#04170B"),
 title="BatMaine Text Scheduling — Clients Text a Word and Get Booked",
 desc="Clients send one word by text, Instagram DM or Facebook message, pick a time by number, reply YES, and they're on your calendar. For barbers and nail salons.",
 label="Text-to-book · Barbers + nail salons",
 h1="They text HAIRCUT. <em>They're booked.</em>",
 lede="Clients send one word by text, Instagram DM or Facebook message. They pick a time by number, reply YES, and it's on your calendar. No app to download and no phone tag.",
 cta="Get set up",
 chat=[("me","HAIRCUT"),
       ("bot","Hi! Next open times with Mike:\n1) Tue 10:00 AM\n2) Tue 2:30 PM\n3) Wed 11:00 AM\nReply with a number."),
       ("me","2"),
       ("bot","Tue 2:30 PM · Haircut $35 with Mike. Reply YES to book."),
       ("me","YES"),
       ("bot","You're booked! See you Tuesday. Reply CANCEL to cancel.")],
 ticker=["Barbers","Nail salons","Braiders","Lash techs","Brow studios","Massage","Tattoo shops","Pet groomers"],
 makes_label="What it does", makes_h="Booking that works while you're cutting",
 makes=[("Text, DM or Messenger","Clients book from whichever one they already use. One word starts it: HAIRCUT, NAILS, FADE, or your own."),
        ("Your calendar","Works with the booking calendar you already use, or a simple one we set up with your hours, services and staff."),
        ("No-show protection","Optional card on file. The fee is only charged if they no-show, by your rules."),
        ("Reminders","A reminder text the day before, so fewer people forget.")],
 steps=[("Your rules","Your hours, services, prices, staff and cancel rules."),
        ("We connect your accounts","Your own text line, Instagram, Facebook and calendar, so it all stays yours."),
        ("We test it with you","We book a pretend appointment together from your phone until it's right."),
        ("You're live","Put your word on your mirror, your bio and your cards. You get a “You're Live” guide PDF.")],
 tiers=[
   dict(name="Starter", price="$297", was="One time", fit="For a solo barber or tech.",
        items=["Booking by text, Instagram and Facebook","One booking word","Up to 2 staff","Day-before reminder texts","Works with your calendar"], btn="Start Starter"),
   dict(name="Pro", price="$497", was="One time", fit="For shops with a team and no-show problems.", pick=True,
        items=["Everything in Starter","No-show card protection","Unlimited staff","Several words (HAIRCUT, KIDS, BEARD)","A “You're Live” guide PDF"], btn="Start Pro"),
 ],
 addon=("Monthly care, $39/month (optional).", "We watch it, fix it, and make changes when your hours, prices or staff change."),
 extra_note="Texting, social media and card services bill you directly, usually $10 to $30 a month. Business texting needs a quick registration that takes about 1 to 3 weeks. We walk you through it.",
 rules=[("It runs on your accounts.","Your phone line, your social media and your calendar. Not ours."),
        ("No double booking.","It only offers times that are really open on your calendar."),
        ("Clients can opt out.","Anyone can text STOP and they won't get texts again."),
        ("Cards only by your rules.","A no-show fee is only charged under the rules you set.")],
 faq=[("Do my clients need an app?","No. They use the texting, Instagram or Facebook they already have."),
      ("What if a client wants to cancel?","They reply CANCEL. The time opens back up on your calendar."),
      ("Can I still book people myself?","Yes. Anything you add to your calendar is blocked out for the bot."),
      ("What if someone texts something else?","The message comes to you like normal, so you can answer it yourself.")],
 order_h="Ready to stop the phone tag?",
 hint="Text Scheduling order: which plan (Starter or Pro), your shop name, how many staff, and what calendar you use now?",
 menu="BatMaine Text Scheduling",
 card="Clients text or DM a word like HAIRCUT, pick a time and reply YES. Booked.",
),
dict(
 file="dj.html", topic="dj", brand=("BatMaine", "DJ"),
 accent=("#C2257A", "#FFFFFF", "#FF7AC0", "#1E0612"),
 title="BatMaine DJ App — Your Own Party App and Website",
 desc="Your own party app and website: song requests with votes, tips, shout-outs, invites with QR tickets, a photo booth and guest photos on the big screen. In your colors.",
 label="Party app + website · For DJs",
 h1="Your crowd requests. <em>You run the party.</em>",
 lede="Your own party app and website: song requests with votes, tips, shout-outs, invites with QR tickets, a photo booth and guest photos on the big screen. In your colors, with your name on it.",
 cta="See a free demo",
 lang_pair=("dj.html", "dj-es.html"),
 cta_url="https://web-production-02dc467d.up.railway.app/try",
 live_demo=dict(url="https://web-production-02dc467d.up.railway.app/try", user="demo", password="TryIt-2026",
                what="A real DJ party app with a sample party going on. Be a guest on your phone, then be the DJ."),
 demo=[("Request","“Before I Let Go” — ▲ <b>14 votes</b>"),
       ("Tip","<b>$20</b> line-jump → moved to #1"),
       ("Shout-out","“Happy 40th, Tasha!” on the big screen"),
       ("Door","QR ticket scanned → checked in"),
       ("Booking","“Wedding, June 14” → lands in your customer book")],
 ticker=["Birthdays","Weddings","Clubs","Day parties","Block parties","Reunions","Quinceañeras","Corporate events"],
 makes_label="What's inside", makes_h="Everything the party needs, from one QR code",
 makes=[("Song requests + votes","Guests search any song, request it, and tap a heart to vote it up. One vote per phone."),
        ("Paid requests + line-jumps","You set the price per party. Paid requests jump to the top of your list."),
        ("Tips","Cash App, Venmo, Zelle, or card. Every tip shows up in your DJ booth."),
        ("Shout-outs","Guests send a message for the big screen. You OK each one first."),
        ("Invites, RSVP + QR tickets","Themed invites, guests pick up to 3 songs when they RSVP, and each guest gets a personal QR ticket."),
        ("Door check-in + VIP","Scan tickets at the door with a phone camera. Sell VIP upgrades, keep a VIP list, and take table requests."),
        ("Photo booth + big screen","An iPad photo booth with fun backgrounds. Guests send photos and 15-second videos, and you pick what shows on the big screen."),
        ("Bookings + Instagram codes","A booking form that lands in your customer book, plus “comment PARTY” codes that DM followers a VIP or free-entry pass.")],
 gallery=[("dj-media/request.jpg","The guest page on a phone: now playing, song search, the vote list, shout-out and tip buttons","Guests' phones: request, vote, tip","phone"),
          ("dj-media/invite.jpg","A party invite with the date, venue and an RSVP form","The invite + RSVP","phone"),
          ("dj-media/ticket.jpg","A guest's personal QR ticket that admits 4","Each guest's QR ticket","phone"),
          ("dj-media/big-screen.jpg","The venue big screen: now playing, a scan-to-request QR code, the top 5 songs and a shout-out ticker","The big screen at the venue","wide"),
          ("dj-media/dj-booth.jpg","The DJ booth on a laptop: requests, paid requests, tips and votes counts, a list with Play, Skip and Block buttons, photo approval and shout-outs","Your DJ booth: play, skip, block, approve","wide")],
 steps=[("A free demo with your name","We make a sample of your app, with pretend tips, so you can see it before you buy."),
        ("Pick your look","We use your website, your Instagram, or a brand-new theme made for you."),
        ("We build + connect","Your own website and accounts, with tips paid to you."),
        ("Go live","You get a How It Works guide in your colors and a walk-through call.")],
 tiers=[
   dict(name="Starter", price="$199", was="Setup, then $49/month", fit="For DJs who want the party app running fast. We host it for you.",
        items=["Your own website with a booking form","Song requests, votes, tips and paid line-jumps","Shout-outs + guest photos on the big screen","Invites, RSVP, QR tickets and door check-in","iPad photo booth","Instagram “comment PARTY” codes","Hosting included"], btn="Start Starter"),
   dict(name="Pro", price="$497", was="Setup, then $69/month", fit="For DJs who book private events and want to get paid up front.", pick=True,
        items=["Everything in Starter","Gig contracts your clients sign on their phone","Deposits paid by card when they sign","Balance reminders before the party","Runs on your own accounts","How It Works guide in your colors"], btn="Go Pro"),
   dict(name="Premium", price="$997", was="Setup, then $69/month", fit="For DJs who want a full custom website, too.",
        items=["Everything in Pro","A custom website built around your brand","Extra pages: services, gallery, reviews","Connected to your own web address (like djname.com)","A walk-through call"], btn="Go Premium"),
 ],
 addon=("Not sure yet? Get a free demo.", "We make a sample of your app with your name and pretend tips, so you can try it before you buy.", "Ask for a demo"),
 extra_note="Tips, line-jumps, VIP and deposits go into your own account. Card services take their usual small fee per payment. On Pro and Premium, hosting is billed to you directly, usually $5 to $20 a month. Our sample contract is a starting point, not legal advice.",
 rules=[("Tips go straight to you.","Payments go into your own account, not through us."),
        ("Your name, your brand.","Your colors, your logo, your web address."),
        ("You control the screen.","Guest photos and shout-outs wait for your OK before they show on the big screen."),
        ("Your guest list is yours.","RSVPs and bookings belong to you.")],
 faq=[("Do guests need to download an app?","No. They scan a QR code and it opens in their phone's browser."),
      ("Does it come in Spanish?","Yes. Every page has an EN | ES button, and the sample contract comes in Spanish too."),
      ("Do I need my own website?","No. Every plan comes with one. Premium adds a custom website on your own web address."),
      ("How do contracts work?","On Pro and Premium, you send a link. Your client reads it, signs with their finger and pays the deposit right there. The date is locked once it's paid, and they get reminders before the balance is due."),
      ("Can I try it before I pay?","Yes. Ask for the free demo and we'll make one with your name on it."),
      ("What do I need at the party?","Your phone. Add an iPad for the photo booth and a TV or projector for the big screen if you want.")],
 order_h="Ready to run the party from your phone?",
 hint="BatMaine DJ App: free demo, Starter, Pro or Premium? Your DJ name and your Instagram?",
 menu="BatMaine DJ App",
 card="A DJ's own party app: requests with votes, tips, QR tickets, photo booth and the big screen.",
),
dict(
 file="kids-game.html", topic="kids-game", brand=("BatMaine", "KidsGame"),
 accent=("#F07A10", "#1E0E02", "#FFA552", "#1E0E02"),
 title="BatMaine Custom Kids Learning Game — Your Child Stars in Their Own Game",
 desc="We turn your child's photo into a cartoon host who teaches words, math, reading and money, then cheers them on in races and a toy store. Their own game, on their own website.",
 label="Custom learning game · Ages 3 to 8",
 h1="Your child is <em>the star</em> of their own learning game.",
 lede="We turn your child's photo into a cartoon host who teaches words, math, reading and money, then cheers them on in races and a toy store. Their own game, on their own website.",
 cta="Make my child's game",
 demo=[("Photo","One smiling photo of your child"),
       ("Host","A cartoon version of them, with a kid voice you pick"),
       ("Theme","Race cars, princess castle, outer space, or dinosaur jungle"),
       ("Lessons","<b>Words</b> · <b>Math</b> · <b>Reading</b> · <b>Money</b>"),
       ("Rewards","Races, prizes for their garage, and a toy store")],
 ticker=["Words","Math","Reading","Money","Races","Toy store","Prizes","Parent portal"],
 makes_label="What's inside", makes_h="Learning that feels like playing",
 makes=[("Words + reading","Sight words and short reading, read out loud by their host."),
        ("Math + money","Counting, adding, and real coins and dollar bills, with charts kids can follow."),
        ("Races + rewards","Right answers earn races, prizes for their garage, and toy store money."),
        ("Parent portal","See what they've learned, where they're stuck, and how long they played.")],
 gallery=[("kids-media/money-coins.jpg","A money question on a race track: a penny, and the question How many cents is this coin worth? with answers 25, 10 and 1 cents","Money: coin values","third"),
          ("kids-media/money-bills.jpg","A money question: three five-dollar bills and a one-dollar bill, Add up the bills! How many dollars? with answers $16, $12 and $19","Money: add up the bills","third"),
          ("kids-media/math-add.jpg","A math question on the race track's big screen: 3 cars plus 1 car, with answers 4, 6 and 5","Math: add with pictures","third")],
 gallery_h="Real questions from the game",
 gallery_note="Math and Money from the race-car theme. Each right answer moves their car down the track. Their own cartoon host asks the questions out loud (hidden here).",
 steps=[("Pick the theme + voice","Race cars, castle, space or jungle, and the voice their host talks in."),
        ("Send a photo","One clear photo of your child. Or pick a made-up cartoon kid instead."),
        ("We make the game","Their host, their theme and their own game. Usually 1 to 2 weeks."),
        ("Play anywhere","Their own web address. Works on a tablet, phone or computer, with nothing to download.")],
 tiers=[
   dict(name="One child", price="$249", was="One time", fit="For one child's own game.", pick=True,
        items=["A cartoon host made from their photo","Words, Math, Reading and Money","Races, prizes and a toy store","Their own web address","Parent portal"], btn="Make their game"),
   dict(name="Each extra child", price="$199", was="One time, per sibling", fit="For brothers, sisters and cousins.",
        items=["Their own host and theme","Their own game and web address","Same parent login for every child"], btn="Add a sibling"),
 ],
 addon=("Online + new levels, $9/month.", "Keeps your child's game online, plus new lessons and levels as we add them."),
 rules=[("Their photo is only used for their game.","We use it to make their cartoon host, and nothing else."),
        ("No ads.","No pop-ups and no ads in the game."),
        ("No strangers.","There's no chat. Races are with family and friends you invite."),
        ("Delete any time.","Ask us and we'll delete the photo and the game.")],
 faq=[("What ages is it for?","About 3 to 8. Lessons start easy and get harder as they go."),
      ("Do I have to use my child's photo?","No. Pick a made-up cartoon kid instead."),
      ("What does my child need to play?","A tablet, phone or computer with internet. Nothing to download."),
      ("Can grandparents play along?","Yes. Invite family to races from the parent portal.")],
 order_h="Ready to make your child the star?",
 hint="Kids Learning Game order: your child's first name and age, the theme (race cars, castle, space or jungle), and how many children?",
 menu="BatMaine Kids Learning Game",
 card="Your child becomes a cartoon host in their own learning game: words, math, reading and money.",
),
]

LINKS = {
 ("researcher.html","Quick Report"):"https://buy.stripe.com/8x27sL28Mclj0v2gE814407",
 ("researcher.html","Deep Dive"):"https://buy.stripe.com/5kQ7sLcNqgBz3He73y14408",
 ("researcher.html","addon"):"https://buy.stripe.com/dRmdR9fZCgBz5Pm4Vq14409",
 ("avatar.html","Launch Pack"):"https://buy.stripe.com/14A9AT3cQ8537XubjO1440a",
 ("avatar.html","Monthly"):"https://buy.stripe.com/dRm3cv8xa0CB5Pm3Rm1440b",
 ("avatar.html","Growth"):"https://buy.stripe.com/4gM6oH00E9971z6gE81440c",
 ("crm.html","Starter"):"https://buy.stripe.com/4gM00j00EfxvfpW9bG1440d",
 ("crm.html","Business"):"https://buy.stripe.com/aFa4gzcNq1GF5Pm2Ni1440e",
 ("crm.html","addon"):"https://buy.stripe.com/aFa7sLaFigBz91y3Rm1440f",
 ("text-scheduling.html","Starter"):"https://buy.stripe.com/cNi7sL4gU4SRa5CcnS1440g",
 ("text-scheduling.html","Pro"):"https://buy.stripe.com/6oU28rcNq4SRelS87C1440h",
 ("text-scheduling.html","addon"):"https://buy.stripe.com/00w00jdRufxvgu05Zu1440i",
 # DJ plans (2026-11-11): each link = setup (one time) + monthly subscription.
 # Old one-time links no longer on the page: Party App $497 6oU3cv3cQ99791ybjO1440j,
 # Full Pro $997 8x25kDcNq2KJ2Da2Ni1440k, care $49/mo 7sY6oH28M5WV91y1Je1440l.
 ("dj.html","Starter"):"https://buy.stripe.com/28E6oH8xaclj1z60Fa1440p",
 ("dj.html","Pro"):"https://buy.stripe.com/28E3cv9Beclj1z60Fa1440q",
 ("dj.html","Premium"):"https://buy.stripe.com/9B63cv28M4SRelSdrW1440r",
 ("kids-game.html","One child"):"https://buy.stripe.com/6oUeVd14I0CB4Li9bG1440m",
 ("kids-game.html","Each extra child"):"https://buy.stripe.com/aFa8wP4gU0CB2DaafK1440n",
 ("kids-game.html","addon"):"https://buy.stripe.com/4gM6oH9Beetr4LiafK1440o",
}


def lang_html(p):
    """EN | ES switch for pages that have both languages (lang_pair = (english file, spanish file))."""
    pair = p.get("lang_pair")
    if not pair:
        return ""
    es = p.get("lang") == "es"
    on = 'style="padding:7px 11px;background:var(--ink);color:var(--bg);text-decoration:none"'
    off = 'style="padding:7px 11px;color:var(--ink);text-decoration:none"'
    return (f'<nav aria-label="Language" style="display:flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;'
            f'font:700 .75rem/1 var(--mono)"><a href="{pair[0].replace(".html", "")}" hreflang="en" lang="en" {off if es else on}>EN</a>'
            f'<a href="{pair[1].replace(".html", "")}" hreflang="es" lang="es" {on if es else off}>ES</a></nav>')


def cta_html(p):
    """Top-right button. cta_url (a live demo) opens it in a new tab and blinks."""
    if p.get("cta_url"):
        return (f'<a class="btn btn-rec btn-blink" href="{p["cta_url"]}" target="_blank" rel="noopener">'
                f'<span class="dot"></span>{esc(p["cta"])}</a>')
    return f'<a class="btn btn-rec" href="#pricing"><span class="dot"></span>{esc(p["cta"])}</a>'


def live_demo_html(p):
    d = p.get("live_demo")
    if not d:
        return ""
    what = d.get("what", "A real website + CRM for a made-up business.")
    return (f'\n      <a class="btn btn-rec btn-blink" href="{d["url"]}" target="_blank" rel="noopener">▶ Try the live demo</a>'
            f'\n      <p class="fine">{esc(what)} Log in with <b>{esc(d["user"])}</b> / '
            f'<b>{esc(d["password"])}</b>. Click anything; it resets every night.</p>')


def page(p):
    a1, ai1, a2, ai2 = p["accent"]
    contact = f'/?topic={p["topic"]}#contact'
    out = []
    w = out.append
    w(f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<title>{esc(p["title"])} | UAOK</title>
<meta name="description" content="{esc(p["desc"])} From Ultimate Advancement of Knowledge (UAOK), a nonprofit." />
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
<meta property="og:title" content="{esc(p["brand"][0] + p["brand"][1])}" />
<meta property="og:description" content="{esc(p["desc"])}" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=Figtree:wght@400;500;600;700&family=JetBrains+Mono:wght@500;700&display=swap">
<link rel="stylesheet" href="batmaine.css">
<style>
:root{{--rec:{a1};--rec-ink:{ai1}}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--rec:{a2};--rec-ink:{ai2}}}}}
:root[data-theme="dark"]{{--rec:{a2};--rec-ink:{ai2}}}
</style>
</head>
<body>

<header class="wrap top">
  <div class="brand-wrap"><a class="back" href="/#ip">← UAOK Intellectual Property</a><div class="brand">{p["brand"][0]}<b>{p["brand"][1]}</b></div></div>
  <div style="display:flex;gap:10px;align-items:center">{lang_html(p)}{cta_html(p)}</div>
</header>

<main>
  <div class="wrap hero">
    <div class="left">
      <span class="label">{esc(p["label"])}</span>
      <h1>{p["h1"]}</h1>
    </div>
    <div class="right">
      <p class="lede">{esc(p["lede"])}</p>
      <div class="ctas">
        <a class="btn btn-rec" href="#pricing"><span class="dot"></span>See pricing</a>
        <a class="btn btn-ghost" href="#how">How it works</a>
      </div>{live_demo_html(p)}
    </div>
  </div>

  <div class="wrap" style="padding-bottom:clamp(48px,7vw,88px)">
''')
    if p.get("chat"):
        w('    <div class="demo" style="max-width:520px">\n      <span class="label">Example text</span>\n      <div class="chat">\n')
        for who, msg in p["chat"]:
            cls = "bubble me" if who == "me" else "bubble"
            w(f'        <span class="{cls}">{esc(msg).replace(chr(10), "<br>")}</span>\n')
        w('      </div>\n    </div>\n')
    else:
        w('    <div class="demo">\n      <span class="label">Example</span>\n')
        for k, v in p["demo"]:
            w(f'      <div class="row"><span class="k">{esc(k)}</span><span class="v">{v}</span></div>\n')
        w('    </div>\n')
    w('  </div>\n\n  <div class="ticker" aria-hidden="true"><div class="track">\n')
    for _ in range(2):
        w('    ' + "".join(f"<span>{esc(t)}</span>" for t in p["ticker"]) + "\n")
    w('  </div></div>\n\n')

    w(f'''  <section class="band">
    <div class="wrap">
      <div class="head">
        <span class="label">{esc(p["makes_label"])}</span>
        <h2>{esc(p["makes_h"])}</h2>
      </div>
      <div class="makes">
''')
    for h, d in p["makes"]:
        w(f'        <div class="make"><h3>{esc(h)}</h3><p>{esc(d)}</p></div>\n')
    w('      </div>\n    </div>\n  </section>\n\n')

    if p.get("gallery"):
        w(f'''  <section id="see">
    <div class="wrap">
      <div class="head">
        <span class="label">See it in action</span>
        <h2>{esc(p.get("gallery_h", "Real screens from the app"))}</h2>
        <p class="lede">{esc(p.get("gallery_note", "Sample party with pretend guests. Your name and colors go where you see ours."))}</p>
      </div>
      <div class="gallery">
''')
        for src, alt, cap, kind in p["gallery"]:
            w(f'        <figure class="g-{kind}"><img src="{src}" alt="{esc(alt)}" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>\n')
        w('      </div>\n    </div>\n  </section>\n\n')

    w('''  <section id="how">
    <div class="wrap">
      <div class="head">
        <span class="label">How it works</span>
        <h2>Four steps, and we do the hard part</h2>
      </div>
      <div class="steps">
''')
    for i, (h, d) in enumerate(p["steps"], 1):
        w(f'        <div class="step"><div class="n">Step<b>{i}</b></div><h3>{esc(h)}</h3><p>{esc(d)}</p></div>\n')
    w('      </div>\n    </div>\n  </section>\n\n')

    tiers_cls = "tiers" if len(p["tiers"]) == 3 else "tiers two-up"
    w(f'''  <section class="band" id="pricing">
    <div class="wrap">
      <div class="head">
        <span class="label">Pricing</span>
        <h2>Pick what fits</h2>
        <p class="lede">Pay online with a card. After you pay, we'll reach out within 1 business day to get started.</p>
      </div>
      <div class="{tiers_cls}">
''')
    for t in p["tiers"]:
        pick = t.get("pick")
        w(f'        <div class="tier{" pick" if pick else ""}">\n')
        if pick:
            w('          <span class="tag">MOST PICKED</span>\n')
        w(f'          <h3>{esc(t["name"])}</h3>\n')
        w(f'          <div><div class="price">{t["price"]}</div><div class="was">{esc(t["was"])}</div></div>\n')
        w(f'          <p class="fine">{esc(t["fit"])}</p>\n          <ul>\n')
        for it in t["items"]:
            w(f'            <li>{esc(it)}</li>\n')
        w('          </ul>\n')
        btn_cls = "btn btn-rec" if pick else "btn btn-ghost"
        dot = '<span class="dot"></span>' if pick else ""
        href = LINKS.get((p.get("links_file", p["file"]), t["name"]), contact)
        w(f'          <a class="{btn_cls}" href="{href}">{dot}{esc(t["btn"])}</a>\n        </div>\n')
    w('      </div>\n')
    if p.get("addon"):
        s, d = p["addon"][:2]
        label = p["addon"][2] if len(p["addon"]) > 2 else "Add it"
        w(f'      <div class="addon">\n        <p><strong>{esc(s)}</strong> {esc(d)}</p>\n        <a class="btn btn-ghost" href="{LINKS.get((p.get('links_file', p['file']),'addon'), contact)}">{esc(label)}</a>\n      </div>\n')
    if p.get("extra_note"):
        w(f'      <p class="note">{p["extra_note"]}</p>\n')
    w('    </div>\n  </section>\n\n')

    w('''  <section>
    <div class="wrap two">
      <div>
        <span class="label">Built to be safe</span>
        <h2>You stay in control</h2>
        <div class="rules">
''')
    for s, d in p["rules"]:
        w(f'          <div class="rule"><span class="dot"></span><p><strong>{esc(s)}</strong>{esc(d)}</p></div>\n')
    w('''        </div>
      </div>
      <div>
        <span class="label">Questions</span>
        <h2>Before you buy</h2>
        <div style="margin-top:28px">
''')
    for q, a in p["faq"]:
        w(f'          <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>\n')
    w('        </div>\n      </div>\n    </div>\n  </section>\n\n')

    name = p["brand"][0] + p["brand"][1]
    w(f'''  <section class="order" id="order">
    <div class="wrap inner">
      <span class="label">Order</span>
      <h2>{esc(p["order_h"])}</h2>
      <p class="lede">Pick your plan above and pay online with a card. We'll reach out within 1 business day to get started. Questions first? Send us a message.</p>
      <div class="ctas"><a class="btn btn-rec" href="{contact}"><span class="dot"></span>Message us</a></div>
      <p class="fine" style="color:var(--bg);opacity:.75">Or email info@uaok.org</p>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <p>{esc(p["menu"])} is a product of <a href="/">Ultimate Advancement of Knowledge (UAOK)</a>, a nonprofit that trains and employs young people.</p>
    <p>Prices are starting prices and can change. Not affiliated with Anthropic or any of the services it connects to.</p>
  </div>
</footer>
</body>
</html>
''')
    return "".join(out)


for p in PAGES:
    (OUT / p["file"]).write_text(page(p))
    print("wrote", p["file"])

# Spanish pages (_tools/pages_es.py): same layout, Spanish words
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from pages_es import CHROME_ES, PAGES_ES  # noqa: E402
for p in PAGES_ES:
    html_out = page(p)
    for en_txt, es_txt in CHROME_ES:
        html_out = html_out.replace(en_txt, es_txt)
    (OUT / p["file"]).write_text(html_out)
    print("wrote", p["file"])

# menu + card + hint data for index.html
import json
print(json.dumps([dict(file=p["file"], topic=p["topic"], menu=p["menu"], card=p["card"], hint=p["hint"]) for p in PAGES]))
