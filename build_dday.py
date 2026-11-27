import glob, os, re

candidates = [
    "d-day.html",
    "d-day-normandy.html",
    "normandy-landings.html",
    "normandy-invasion.html",
    "operation-overlord.html",
]
fname = next((c for c in candidates if os.path.exists(c)), None)
if not fname:
    matches = [
        f for f in sorted(glob.glob("*.html"))
        if any(k in f.lower() for k in ("d-day", "dday", "normandy", "overlord"))
        and "backup" not in f.lower()
    ]
    fname = matches[0] if matches else "d-day.html"

TITLE = "D-Day and the Normandy Landings: Opening the Western Front"
LEAD = (
    "Launched on June 6, 1944, Operation Overlord—known as D-Day—brought Allied land, air, and naval "
    "forces ashore along the coast of Normandy, France, marking a pivotal turning point in the liberation "
    "of Western Europe."
)

SECTIONS = [
    (
        "Planning, Deception, and Weather Decisions",
        [
            "For more than a year before the landings, Allied planners built up troops, vehicles

python3 build_white_rose.py
cd ~/ww2-archive
rm -f build_dday.py build_midway.py
git status -s
cd ~/ww2-archive

cat << 'EOF' > make_dday.py
import glob, os, re

cands = ["d-day.html", "normandy-landings.html", "d-day-normandy.html", "operation-overlord.html"]
fname = next((c for c in cands if os.path.exists(c)), None)
if not fname:
    hits = [f for f in sorted(glob.glob("*.html")) if any(k in f.lower() for k in ("d-day", "dday", "normandy", "overlord")) and "backup" not in f.lower()]
    fname = hits[0] if hits else "d-day.html"

TITLE = "D-Day and the Normandy Landings: Opening the Western Front"
LEAD = "Launched on June 6, 1944, Operation Overlord brought Allied land, air, and naval forces ashore in Normandy, France, opening a decisive Western Front in Europe."

SECTIONS = [
    ("Planning, Deception, and Weather Decisions", [
        "For over a year before June 1944, Allied planners assembled troops, vehicles, landing craft, and supplies in Britain while coordinating operations across American, British, Canadian, and other Allied forces.",
        "Choosing Normandy meant solving major logistical challenges, including building prefabricated Mulberry harbors and undersea fuel pipelines to supply armies across open beaches until major ports could be captured and cleared.",
        "Deception plans such as Operation Fortitude aimed to mislead German intelligence about the timing and primary target of the invasion, encouraging German commanders to disperse defenses along wider stretches of coast.",
        "Weather forecasting proved decisive in early June 1944. Rough seas and low clouds led General Dwight D. Eisenhower to delay the assault by a day before a short break in bad weather created a narrow window for June 6."
    ]),
    ("Airborne Drops, Naval Bombardment, and Beach Assaults", [
        "Before dawn on June 6, airborne troops dropped or landed by glider behind German coastal positions to secure key bridges, roads, and flanks while naval forces swept mines and provided gunfire support.",
        "Along five beach sectors—Utah, Omaha, Gold, Juno, and Sword—infantry, armored units, and engineers came ashore under heavy conditions against mines, obstacles, artillery, and defensive fire.",
        "Progress varied across the five beaches. Several sectors secured firm footholds on the first day, while Omaha Beach saw intense resistance and heavy casualties before Allied units pushed inland and linked up."
    ]),
    ("Securing the Beachhead and Strategic Impact", [
        "Once initial beachheads were linked, steady reinforcement and supply allowed Allied forces to expand inland despite tough fighting through Normandy's hedgerows and counterattacks.",
        "German forces struggled to shift reserves quickly and replace losses under Allied air superiority, fuel shortages, and heavy pressure on the Eastern and Italian fronts.",
        "Establishing a sustained foothold in Western Europe accelerated the liberation of France and set the stage for the Allied advance toward Germany in 1944 and 1945."
    ])
]

html = open(fname).read() if os.path.exists(fname) else "<!DOCTYPE html><html><head><title>WWII</title></head><body><article></article></body></html>"
figs = re.findall(r'<figure class="archive-figure">.*?</figure>', html, flags=re.DOTALL | re.IGNORECASE)
while len(figs) < 3:
    figs.append('<figure class="archive-figure"><img src="images/placeholder.jpg" alt="Historical archive image"><figcaption>Historical archive figure.</figcaption></figure>')
figs = figs[:3]

m = re.search(r"(<article\b[^>]*>)(.*?)(</article>)", html, flags=re.DOTALL | re.IGNORECASE)
blocks = []
for i, (h, ps) in enumerate(SECTIONS):
    paras = "\n        ".join("<p>" + p + "</p>" for p in ps)
    blocks.append("        <h2>" + h + "</h2>\n        " + figs[i] + "\n        " + paras)

inner = "\n        <h1>" + TITLE + "</h1>\n        <p>" + LEAD + "</p>\n\n" + "\n\n".join(blocks) + "\n    "
out = html[:m.start()] + m.group(1) + inner + m.group(3) + html[m.end():]
out = re.sub(r"<title>.*?</title>", "<title>" + TITLE + " | WWII History Archive</title>", out, flags=re.DOTALL | re.IGNORECASE)

open(fname, "w").write(out)
wc = len(re.findall(r"\b[\w'-]+\b", re.sub(r"<[^>]+>", " ", inner)))
print(fname, "->", wc, "words |", len(figs), "figures")
