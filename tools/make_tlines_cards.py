import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import roman
D=lambda s:"$$"+s+"$$"
G=[
("Transmission line","","","A pair of conductors that guides an electromagnetic wave from a source to a load. Treat a connection as a line, not a wire, when its length is a noticeable fraction of a wavelength (rule of thumb: $\\ell>\\lambda/10$).","waves"),
("Lumped-element model","R',\\,L',\\,G',\\,C'","","Splits the line into short sections of length $\\Delta z$, each with series resistance $R'\\Delta z$ and inductance $L'\\Delta z$ and shunt conductance $G'\\Delta z$ and capacitance $C'\\Delta z$. Letting $\\Delta z\\to0$ gives the telegrapher's equations.","params"),
("Telegrapher's equations","","","The pair of equations from KVL and KCL on one lumped section:"+D(r"-\frac{\partial v}{\partial z}=R'i+L'\frac{\partial i}{\partial t},\qquad -\frac{\partial i}{\partial z}=G'v+C'\frac{\partial v}{\partial t}"),None),
("Phasor","\\tilde V","\\mathrm{V}","A complex number holding a sinusoid's amplitude and phase: $v(t)=\\mathrm{Re}\\{\\tilde V e^{j\\omega t}\\}$.",None),
("Propagation constant","\\gamma=\\alpha+j\\beta","\\mathrm{m}^{-1}","Its real part sets attenuation and its imaginary part sets the phase change per meter."+D(r"\gamma=\sqrt{(R'+j\omega L')(G'+j\omega C')}"),"params"),
("Attenuation constant","\\alpha","\\mathrm{Np/m}","How fast the amplitude decays: a wave falls as $e^{-\\alpha z}$. Multiply by $8.686$ to get dB/m. Zero on a lossless line.","params"),
("Phase constant","\\beta","\\mathrm{rad/m}","Phase change per meter of travel: $\\beta=\\dfrac{2\\pi}{\\lambda}=\\dfrac{\\omega}{u_p}$. On a lossless line $\\beta=\\omega\\sqrt{L'C'}$.","params"),
("Phase velocity","u_p","\\mathrm{m/s}","Speed of a point of constant phase: $u_p=\\dfrac{\\omega}{\\beta}=\\dfrac{1}{\\sqrt{L'C'}}$ on a lossless line, or $\\dfrac{c}{\\sqrt{\\varepsilon_r}}$ in a non-magnetic dielectric.","calc"),
("Velocity factor","u_p/c","","Phase velocity as a fraction of $c$. Solid-polyethylene coax is about $0.66$.","bounce"),
("Characteristic impedance","Z_0","\\Omega","Ratio of voltage to current for a single traveling wave. It is not a resistance you can measure with an ohmmeter."+D(r"Z_0=\sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}}\;\xrightarrow{\text{lossless}}\;\sqrt{\frac{L'}{C'}}"),"params"),
("Reflection coefficient","\\Gamma","","Ratio of reflected to incident voltage. $|\\Gamma|\\le1$ for passive loads."+D(r"\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0},\qquad \Gamma(d)=\Gamma_Le^{-j2\beta d}"),"waves"),
("Transmission coefficient","\\tau","","Ratio of load voltage to incident voltage: $\\tau=1+\\Gamma_L$.","calc"),
("Standing wave","","","The pattern formed when incident and reflected waves add. $|V(z)|$ no longer depends on time; its maxima and minima sit $\\lambda/2$ apart.","waves"),
("VSWR","S","","Voltage standing wave ratio. It ranges from $1$ (matched) to $\\infty$ (open, short, or pure reactance)."+D(r"S=\frac{|V|_{max}}{|V|_{min}}=\frac{1+|\Gamma|}{1-|\Gamma|}"),"waves"),
("Return loss","RL","\\mathrm{dB}","$RL=-20\\log_{10}|\\Gamma|$. Larger means better matched; a VNA shows it as $-|S_{11}|$ in dB.","calc"),
("Input impedance","Z_{in}","\\Omega","Impedance seen looking into a line of length $\\ell$:"+D(r"Z_{in}=Z_0\,\frac{Z_L+jZ_0\tan\beta\ell}{Z_0+jZ_L\tan\beta\ell}"),"calc"),
("Half-wave line","\\lambda/2","","A line $\\lambda/2$ long (or any multiple) repeats the load: $Z_{in}=Z_L$.","smith"),
("Quarter-wave transformer","\\lambda/4","","A $\\lambda/4$ section of impedance $Z_1$ turns $Z_L$ into $\\dfrac{Z_1^2}{Z_L}$. Choosing $Z_1=\\sqrt{Z_0R_L}$ matches a real load.","calc"),
("Shorted stub","","","A line ending in a short: $Z_{in}=jZ_0\\tan\\beta\\ell$. It can make any pure reactance.","smith"),
("Open stub","","","A line ending in an open: $Z_{in}=-jZ_0\\cot\\beta\\ell$. It can make any pure reactance.","smith"),
("Impedance matching","","","Adding a network between source and load so the line sees $Z_0$ and no power is reflected.","stub"),
("Smith chart","","","A plot of the $\\Gamma$ plane with circles of constant normalized resistance and reactance. Moving along a lossless line rotates a point around the center.","smith"),
("Normalized impedance","z=Z/Z_0","","Impedance divided by $Z_0$, used on the Smith chart:"+D(r"z=\frac{1+\Gamma}{1-\Gamma}"),"smith"),
("Admittance","Y=1/Z","\\mathrm{S}","Reciprocal of impedance; $G$ is conductance and $B$ is susceptance. On the Smith chart, $y$ sits diametrically opposite $z$.","smith"),
("Wavelengths toward generator","WTG","\\lambda","The outer Smith chart scale. Moving from the load toward the source is clockwise; one full turn is $\\lambda/2$.","smith"),
("Single-stub tuner","","","A matching network with a shunt (or series) stub a distance $d$ from the load. $d$ brings the admittance onto $g=1$, and the stub cancels the leftover susceptance.","stub"),
("Transient","","","The time-domain response right after a source switches on, before the line settles to steady state.","bounce"),
("One-way delay","T","\\mathrm{s}","Time for a wave to travel the line once: $T=\\dfrac{\\ell}{u_p}$.","bounce"),
("Bounce (lattice) diagram","","","A space–time drawing of each wave bouncing between source and load. Each segment carries its voltage; the voltage at a point is the sum of the segments that have reached it.","bounce"),
("Source reflection coefficient","\\Gamma_s","","Applied to each wave that returns to the source:"+D(r"\Gamma_s=\frac{R_s-Z_0}{R_s+Z_0}"),"bounce"),
("Vector network analyzer","VNA","","An instrument that measures reflection ($S_{11}$) and transmission ($S_{21}$) versus frequency, shown as magnitude, phase, or on a Smith chart.",None),
]
def tags(spec,n):
    """Expand {"tline":"1-9,19"} into a 1-based index -> topic list."""
    out={}
    for t,r in spec.items():
        for part in r.split(","):
            a,_,b=part.partition("-")
            for i in range(int(a),int(b or a)+1): out.setdefault(i,[]).append(t)
    assert sorted(out)==list(range(1,n+1)), sorted(set(range(1,n+1))-set(out))
    return out
GT=tags({"tline":"1-10,16-17,19-20","reflection":"11-15,31","matching":"18,21,26","smith":"22-25","transients":"27-30"},len(G))
glossary=[{"term":t,"symbol":s,"units":u,"definition":d,"widget":w,"topics":GT[i+1]} for i,(t,s,u,d,w) in enumerate(G)]
C=[
("When must you treat a connection as a transmission line instead of a simple wire?","When its length is a significant fraction of a wavelength, roughly $\\ell>\\lambda/10$. Then voltage and current change along the line.","concept"),
("What four per-unit-length parameters describe a line?","$R'$ (Ω/m), $L'$ (H/m), $G'$ (S/m), and $C'$ (F/m)","concept"),
("Write $\\gamma$ in terms of $R',L',G',C'$.",D(r"\gamma=\alpha+j\beta=\sqrt{(R'+j\omega L')(G'+j\omega C')}"),"equation"),
("Write $Z_0$ in terms of $R',L',G',C'$.",D(r"Z_0=\sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}}")+"Lossless: $Z_0=\\sqrt{\\dfrac{L'}{C'}}$","equation"),
("Lossless line: $\\beta$ and $u_p$?",D(r"\beta=\omega\sqrt{L'C'},\qquad u_p=\frac{1}{\sqrt{L'C'}}=\frac{\omega}{\beta}"),"equation"),
("What does $\\alpha$ tell you, and how do you convert it to dB/m?","The amplitude decays as $e^{-\\alpha z}$. In dB/m: $8.686\\,\\alpha$ with $\\alpha$ in Np/m.","concept"),
("Phase velocity in a non-magnetic dielectric with $\\varepsilon_r$?",D(r"u_p=\frac{c}{\sqrt{\varepsilon_r}}"),"equation"),
("General phasor voltage on a lossless line?",D(r"V(z)=V_0^+e^{-j\beta z}+V_0^-e^{j\beta z}"),"equation"),
("General phasor current on a lossless line?",D(r"I(z)=\frac{V_0^+}{Z_0}e^{-j\beta z}-\frac{V_0^-}{Z_0}e^{j\beta z}")+"Note the minus sign on the reflected term.","equation"),
("$\\Gamma_L$ in terms of $Z_L$ and $Z_0$?",D(r"\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0}=\frac{z_L-1}{z_L+1}"),"equation"),
("$\\Gamma_L$ for a matched load, a short, and an open?","Matched: $0$. Short: $-1$. Open: $+1$.","concept"),
("A purely reactive load gives what $|\\Gamma_L|$ and VSWR?","$|\\Gamma_L|=1$ and $\\mathrm{VSWR}=\\infty$. All power reflects.","concept"),
("VSWR in terms of $|\\Gamma|$?",D(r"S=\frac{1+|\Gamma|}{1-|\Gamma|}"),"equation"),
("$|\\Gamma|$ in terms of VSWR?",D(r"|\Gamma|=\frac{S-1}{S+1}"),"equation"),
("How far apart are adjacent voltage maxima on a standing wave?","$\\lambda/2$. A maximum and the nearest minimum are $\\lambda/4$ apart.","concept"),
("Where is the first voltage maximum from the load?",D(r"d_{max}=\frac{\theta_\Gamma}{4\pi}\lambda")+"Add $\\lambda/2$ if negative. $\\theta_\\Gamma$ is the phase of $\\Gamma_L$.","equation"),
("Line impedance at a voltage maximum and at a voltage minimum?","At $V_{max}$: $Z_0S$ (real). At $V_{min}$: $\\dfrac{Z_0}{S}$ (real).","concept"),
("Transmission coefficient $\\tau$?","$\\tau=1+\\Gamma_L$, so $V_L=\\tau V_0^+$.","equation"),
("Input impedance of a lossless line of length $\\ell$?",D(r"Z_{in}=Z_0\,\frac{Z_L+jZ_0\tan\beta\ell}{Z_0+jZ_L\tan\beta\ell}"),"equation"),
("$\\Gamma$ at distance $d$ from the load?",D(r"\Gamma(d)=\Gamma_Le^{-j2\beta d}"),"equation"),
("Input impedance of a shorted stub?",D(r"Z_{in}=jZ_0\tan\beta\ell"),"equation"),
("Input impedance of an open stub?",D(r"Z_{in}=-jZ_0\cot\beta\ell"),"equation"),
("What does a $\\lambda/2$ line do to a load?","Repeats it: $Z_{in}=Z_L$.","concept"),
("What does a $\\lambda/4$ line do to a load?","Inverts it:"+D(r"Z_{in}=\frac{Z_0^2}{Z_L}")+"A short looks open, and an open looks short.","concept"),
("A capacitor at the end of a $\\lambda/4$ line looks like…?","An inductor.","concept"),
("Quarter-wave transformer impedance to match $R_L$ to $Z_0$?",D(r"Z_1=\sqrt{Z_0R_L}"),"equation"),
("Can a quarter-wave transformer match a complex load directly?","No. First move to a voltage maximum or minimum, where the impedance is real, then insert the transformer.","concept"),
("Time-average power delivered to the load on a lossless line?",D(r"P_{av}=\frac{|V_0^+|^2}{2Z_0}\left(1-|\Gamma_L|^2\right)"),"equation"),
("If $Z_s=Z_0$, what is $|V_0^+|$?","$\\dfrac{V_s}{2}$, whatever the load.","concept"),
("On a Smith chart, which way do you rotate moving toward the generator?","Clockwise. One full turn is $\\lambda/2$.","concept"),
("Where are the short, the open, and the matched point on a Smith chart?","Short: far left ($\\Gamma=-1$). Open: far right ($\\Gamma=+1$). Match: center ($\\Gamma=0$).","concept"),
("How do you find $y$ from $z$ on the Smith chart?","Reflect through the center: a $180^\\circ$ rotation, which is $\\lambda/4$ on the WTG scale.","concept"),
("What does a circle centered on the middle of the Smith chart represent?","Constant $|\\Gamma|$, so constant VSWR. Moving along a lossless line keeps you on it.","concept"),
("Upper half of the Smith chart: inductive or capacitive?","Upper half is inductive ($+jx$); lower half is capacitive ($-jx$).","concept"),
("Shunt-stub matching: which circle must the line bring $y$ onto?","The $g=1$ circle. The stub then cancels the susceptance $\\pm jb$.","concept"),
("Shorted stub admittance?",D(r"y=-j\cot\beta\ell"),"equation"),
("Open stub admittance?",D(r"y=+j\tan\beta\ell"),"equation"),
("Why are shunt stubs more common than series stubs?","They attach in parallel without cutting the line, which is easy in microstrip and coax.","concept"),
("One-way transit time on a line?",D(r"T=\frac{\ell}{u_p}"),"equation"),
("First wave launched when a step source switches on?",D(r"V_1^+=V_s\,\frac{Z_0}{R_s+Z_0}"),"equation"),
("$\\Gamma_s$ for a source with internal resistance $R_s$?",D(r"\Gamma_s=\frac{R_s-Z_0}{R_s+Z_0}"),"equation"),
("Steady-state voltage after all reflections die out?","The DC voltage divider:"+D(r"V_\infty=V_s\,\frac{R_L}{R_s+R_L}"),"concept"),
("In a bounce diagram, when does the load voltage first change?","At $t=T$, when the first wave arrives. It jumps to $V_1^+(1+\\Gamma_L)$.","concept"),
("When does the source-end voltage change after $t=0$?","Only at $t=2T,\\ 4T,\\ 6T,\\dots$, when reflected waves return.","concept"),
("What does a VNA's $S_{11}$ measure?","The reflection coefficient at port 1 versus frequency. $|S_{11}|$ in dB is the negative of the return loss.","concept"),
("Why calibrate a VNA with open, short, and load standards?","To remove the effect of the cables and connectors so the measured $\\Gamma$ is that of the device alone.","concept"),
]
CT=tags({"tline":"1-9,19,21-25,28-29","reflection":"10-18,20,45-46","matching":"26-27,35-38","smith":"30-34","transients":"39-44"},len(C))
n={}
cards=[]
for i,(f,b,k) in enumerate(C):
    t=CT[i+1]; n[t[0]]=n.get(t[0],0)+1
    cards.append({"id":f"card-{t[0]}-{n[t[0]]:02d}","front":f,"back":b,"kind":k,"topics":t})
fmt="Text with inline TeX in $...$ and display TeX in $$...$$. Glossary symbol and units fields are TeX without delimiters."
json.dump(roman({"unit":"Transmission lines","format":fmt,"cards":cards}),open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","content","transmission-lines","flashcards.json"),"w"),ensure_ascii=False,indent=1)
json.dump(roman({"unit":"Transmission lines","format":fmt,"terms":glossary}),open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","content","transmission-lines","glossary.json"),"w"),ensure_ascii=False,indent=1)
print(len(cards),len(glossary))
