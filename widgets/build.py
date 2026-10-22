# Embeds content/*.json into the widget preview page. Run: python3 build.py
import json,re,os
d=os.path.dirname(os.path.abspath(__file__)); c=os.path.join(d,"..","content")
data={"cards":json.load(open(f"{c}/ch03-flashcards.json"))["cards"],
      "problems":json.load(open(f"{c}/ch03-practice.json"))["problems"],
      "terms":json.load(open(f"{c}/ch03-glossary.json"))["terms"]}
p=os.path.join(d,"ece343-widgets.html"); s=open(p).read()
blob=json.dumps(data,ensure_ascii=False).replace("</","<\\/")
tag='<script id="content" type="application/json">'
s=re.sub(re.escape(tag)+r".*?</script>",lambda m:tag+blob+"</script>",s,count=1,flags=re.S)
open(p,"w").write(s); print("embedded",len(data["cards"]),len(data["problems"]),len(data["terms"]))
