# Vector calculus: flashcards, glossary and practice problems.
# Hand-derived derivatives are checked numerically before they are written. Run: python3 tools/make_vectors.py
import math, os, sys
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from lib import *
D=lambda s:"$$"+s+"$$"
deg=lambda x:f"{tr(x)}^\\circ"
T=["vectors"]
x_,y_,z_="\\hat{\\mathbf{x}}","\\hat{\\mathbf{y}}","\\hat{\\mathbf{z}}"
def vec(v,u=("\\mathbf{x}","\\mathbf{y}","\\mathbf{z}"),n=3):
    """TeX for a vector from its components, e.g. \\hat x 2 - \\hat y 3."""
    s=""
    for k,a in zip(u,v):
        if abs(a)<1e-12: continue
        s+=("-" if a<0 else ("+" if s else ""))+f"\\hat{{{k}}}\\,{int(round(abs(a))) if abs(a-round(a))<1e-9 else tr(abs(a),n)}"
    return s or "0"
# numerical derivative checks
h=1e-5
def grad(f,p): p=np.array(p,float); return np.array([(f(*(p+h*e))-f(*(p-h*e)))/(2*h) for e in np.eye(3)])
def div(F,p): p=np.array(p,float); return sum((F(*(p+h*e))[i]-F(*(p-h*e))[i])/(2*h) for i,e in enumerate(np.eye(3)))
def curl(F,p):
    J=np.array([(np.array(F(*(np.array(p,float)+h*e)))-np.array(F(*(np.array(p,float)-h*e))))/(2*h) for e in np.eye(3)]).T  # J[i][j]=dFi/dxj
    return np.array([J[2][1]-J[1][2],J[0][2]-J[2][0],J[1][0]-J[0][1]])
close=lambda a,b:np.allclose(a,b,atol=1e-6)

C=[
("Dot product of $\\mathbf{A}$ and $\\mathbf{B}$?",D(r"\mathbf{A}\cdot\mathbf{B}=|\mathbf{A}||\mathbf{B}|\cos\theta_{AB}=A_xB_x+A_yB_y+A_zB_z")+"It is a scalar, and zero when the vectors are perpendicular.","equation",T),
("Magnitude of the cross product, and its direction?",D(r"|\mathbf{A}\times\mathbf{B}|=|\mathbf{A}||\mathbf{B}|\sin\theta_{AB}")+"Perpendicular to both, by the right-hand rule. Zero when the vectors are parallel.","equation",T),
("Cross product in Cartesian components?",D(r"\mathbf{A}\times\mathbf{B}=\begin{vmatrix}\hat{\mathbf{x}}&\hat{\mathbf{y}}&\hat{\mathbf{z}}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}"),"equation",T),
("$\\hat{\\mathbf{x}}\\times\\hat{\\mathbf{y}}$, $\\hat{\\mathbf{r}}\\times\\hat{\\boldsymbol{\\phi}}$, $\\hat{\\mathbf{R}}\\times\\hat{\\boldsymbol{\\theta}}$?","$\\hat{\\mathbf{z}}$, $\\hat{\\mathbf{z}}$, and $\\hat{\\boldsymbol{\\phi}}$. Each set is right-handed in the order $(x,y,z)$, $(r,\\phi,z)$, $(R,\\theta,\\phi)$.","concept",T),
("Cartesian to cylindrical?",D(r"r=\sqrt{x^2+y^2},\qquad \phi=\tan^{-1}\frac{y}{x},\qquad z=z")+"Pick the quadrant of $\\phi$ from the signs of $x$ and $y$.","equation",T),
("Spherical to Cartesian?",D(r"x=R\sin\theta\cos\phi,\quad y=R\sin\theta\sin\phi,\quad z=R\cos\theta"),"equation",T),
("Ranges of $\\theta$ and $\\phi$ in spherical coordinates?","$0\\le\\theta\\le\\pi$, measured down from the $+z$ axis. $0\\le\\phi<2\\pi$, measured from the $+x$ axis in the $xy$-plane.","concept",T),
("Why can't you add $\\hat{\\mathbf{r}}$ components at two different points?","$\\hat{\\mathbf{r}}$, $\\hat{\\boldsymbol{\\phi}}$, $\\hat{\\mathbf{R}}$ and $\\hat{\\boldsymbol{\\theta}}$ point in different directions at different points. Convert to Cartesian first.","concept",T),
("Differential length in cylindrical coordinates?",D(r"d\mathbf{l}=\hat{\mathbf{r}}\,dr+\hat{\boldsymbol{\phi}}\,r\,d\phi+\hat{\mathbf{z}}\,dz"),"equation",T),
("Differential volume in cylindrical and spherical coordinates?",D(r"dV=r\,dr\,d\phi\,dz,\qquad dV=R^2\sin\theta\,dR\,d\theta\,d\phi"),"equation",T),
("Differential area on a sphere of radius $R$?",D(r"d\mathbf{s}=\hat{\mathbf{R}}\,R^2\sin\theta\,d\theta\,d\phi"),"equation",T),
("What does the gradient $\\nabla V$ tell you?","The direction in which $V$ increases fastest, with magnitude equal to that rate. It is perpendicular to surfaces of constant $V$.","concept",T),
("Gradient in Cartesian coordinates?",D(r"\nabla V=\hat{\mathbf{x}}\frac{\partial V}{\partial x}+\hat{\mathbf{y}}\frac{\partial V}{\partial y}+\hat{\mathbf{z}}\frac{\partial V}{\partial z}"),"equation",T),
("Directional derivative of $V$ along unit vector $\\hat{\\mathbf{a}}$?",D(r"\frac{dV}{dl}=\nabla V\cdot\hat{\mathbf{a}}"),"equation",T),
("What does the divergence $\\nabla\\cdot\\mathbf{A}$ measure?","Net outward flux per unit volume at a point. Positive at a source, negative at a sink, zero where flux in equals flux out.","concept",T),
("Divergence in Cartesian coordinates?",D(r"\nabla\cdot\mathbf{A}=\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}"),"equation",T),
("Divergence in cylindrical coordinates?",D(r"\nabla\cdot\mathbf{A}=\frac{1}{r}\frac{\partial(rA_r)}{\partial r}+\frac{1}{r}\frac{\partial A_\phi}{\partial\phi}+\frac{\partial A_z}{\partial z}"),"equation",T),
("Divergence theorem?",D(r"\int_V\nabla\cdot\mathbf{A}\,dV=\oint_S\mathbf{A}\cdot d\mathbf{s}"),"equation",T),
("What does the curl $\\nabla\\times\\mathbf{A}$ measure?","Circulation per unit area: how much the field swirls around a point. A small paddle wheel in the field spins about the curl's direction.","concept",T),
("Curl in Cartesian coordinates?",D(r"\nabla\times\mathbf{A}=\begin{vmatrix}\hat{\mathbf{x}}&\hat{\mathbf{y}}&\hat{\mathbf{z}}\\\partial_x&\partial_y&\partial_z\\A_x&A_y&A_z\end{vmatrix}"),"equation",T),
("Stokes's theorem?",D(r"\int_S(\nabla\times\mathbf{A})\cdot d\mathbf{s}=\oint_C\mathbf{A}\cdot d\mathbf{l}")+"$C$ bounds $S$; walk $C$ so the right-hand rule gives the direction of $d\\mathbf{s}$.","equation",T),
("Two identities that are always zero?",D(r"\nabla\times(\nabla V)=0,\qquad \nabla\cdot(\nabla\times\mathbf{A})=0"),"equation",T),
("Solenoidal versus conservative field?","Solenoidal: $\\nabla\\cdot\\mathbf{A}=0$, so $\\mathbf{A}=\\nabla\\times\\mathbf{B}$ for some $\\mathbf{B}$. Conservative (irrotational): $\\nabla\\times\\mathbf{A}=0$, so $\\mathbf{A}=\\nabla V$ and line integrals depend only on the endpoints.","concept",T),
("Laplacian of a scalar in Cartesian coordinates?",D(r"\nabla^2V=\nabla\cdot\nabla V=\frac{\partial^2V}{\partial x^2}+\frac{\partial^2V}{\partial y^2}+\frac{\partial^2V}{\partial z^2}"),"equation",T),
("Distance vector from point $P_1$ to point $P_2$?",D(r"\mathbf{R}_{12}=\mathbf{R}_2-\mathbf{R}_1=\hat{\mathbf{x}}(x_2-x_1)+\hat{\mathbf{y}}(y_2-y_1)+\hat{\mathbf{z}}(z_2-z_1)")+"Always from the first point to the second.","equation",T),
]

G=[
("Unit vector","\\hat{\\mathbf{a}}","","A vector of length one that only gives a direction: $\\hat{\\mathbf{a}}=\\mathbf{A}/|\\mathbf{A}|$.","coords",T),
("Position vector","\\mathbf{R}","\\mathrm{m}","The vector from the origin to a point: $\\mathbf{R}=\\hat{\\mathbf{x}}x+\\hat{\\mathbf{y}}y+\\hat{\\mathbf{z}}z$.","coords",T),
("Distance vector","\\mathbf{R}_{12}","\\mathrm{m}","The vector from point 1 to point 2: $\\mathbf{R}_{12}=\\mathbf{R}_2-\\mathbf{R}_1$. Used constantly in Coulomb's law and Biot–Savart.","coords",T),
("Dot product","\\mathbf{A}\\cdot\\mathbf{B}","","$|\\mathbf{A}||\\mathbf{B}|\\cos\\theta$, a scalar. It picks out the component of one vector along another.",None,T),
("Cross product","\\mathbf{A}\\times\\mathbf{B}","","A vector perpendicular to both, of length $|\\mathbf{A}||\\mathbf{B}|\\sin\\theta$, direction by the right-hand rule. Note $\\mathbf{B}\\times\\mathbf{A}=-\\mathbf{A}\\times\\mathbf{B}$.",None,T),
("Cartesian coordinates","(x,y,z)","","Three perpendicular axes with unit vectors $\\hat{\\mathbf{x}},\\hat{\\mathbf{y}},\\hat{\\mathbf{z}}$ that point the same way everywhere.","coords",T),
("Cylindrical coordinates","(r,\\phi,z)","","Radial distance $r$ from the $z$-axis, azimuth $\\phi$ from the $+x$ axis, and height $z$. Natural for wires, coax and solenoids.","coords",T),
("Spherical coordinates","(R,\\theta,\\phi)","","Distance $R$ from the origin, polar angle $\\theta$ down from $+z$, and azimuth $\\phi$. Natural for point charges and spheres.","coords",T),
("Differential length","d\\mathbf{l}","\\mathrm{m}","A tiny step along a path. Its components carry the scale factors: $r\\,d\\phi$ in cylindrical, $R\\,d\\theta$ and $R\\sin\\theta\\,d\\phi$ in spherical.",None,T),
("Differential surface","d\\mathbf{s}","\\mathrm{m^2}","A tiny patch of surface, pointing along its normal. On a closed surface the normal points outward.",None,T),
("Line integral","\\int_C\\mathbf{A}\\cdot d\\mathbf{l}","","Adds up the component of $\\mathbf{A}$ along a path. For a force it is the work done; around a closed loop it is the circulation.",None,T),
("Flux","\\int_S\\mathbf{A}\\cdot d\\mathbf{s}","","How much of a vector field passes through a surface.","divcurl",T),
("Gradient","\\nabla V","","A vector pointing toward the fastest increase of a scalar field, with magnitude equal to that rate of increase.",None,T),
("Divergence","\\nabla\\cdot\\mathbf{A}","","Net outward flux per unit volume at a point: positive at sources, negative at sinks.","divcurl",T),
("Curl","\\nabla\\times\\mathbf{A}","","Circulation per unit area at a point, pointing along the axis a tiny paddle wheel would spin around.","divcurl",T),
("Divergence theorem","","","Turns a volume integral of divergence into a flux through the closed surface: $\\int_V\\nabla\\cdot\\mathbf{A}\\,dV=\\oint_S\\mathbf{A}\\cdot d\\mathbf{s}$.","divcurl",T),
("Stokes's theorem","","","Turns a surface integral of curl into a line integral around the boundary: $\\int_S(\\nabla\\times\\mathbf{A})\\cdot d\\mathbf{s}=\\oint_C\\mathbf{A}\\cdot d\\mathbf{l}$.","divcurl",T),
("Laplacian","\\nabla^2","","The divergence of the gradient. $\\nabla^2V=0$ (Laplace's equation) holds wherever there is no charge.",None,T),
("Solenoidal field","","","A field with zero divergence everywhere, so its field lines have no beginning or end. $\\mathbf{B}$ is always solenoidal.","divcurl",T),
("Conservative field","","","A field with zero curl, so it is the gradient of a scalar and its line integrals do not depend on the path. Static $\\mathbf{E}$ is conservative.","divcurl",T),
]

P=[]
def add(**k): k.setdefault("source","original"); k.setdefault("topics",T); P.append(k)

A=np.array([2,-3,1]); B=np.array([-4,-2,5]); AB=A@B; X=np.cross(A,B); th=math.degrees(math.acos(AB/np.linalg.norm(A)/np.linalg.norm(B)))
add(difficulty=1,title="Dot and cross products",
 prompt=f"For $\\mathbf{{A}}={vec(A)}$ and $\\mathbf{{B}}={vec(B)}$, find $\\mathbf{{A}}\\cdot\\mathbf{{B}}$, $\\mathbf{{A}}\\times\\mathbf{{B}}$, and the angle between them.",
 hints=["$\\mathbf{A}\\cdot\\mathbf{B}=A_xB_x+A_yB_y+A_zB_z$.","Use the determinant for the cross product.","$\\cos\\theta=\\dfrac{\\mathbf{A}\\cdot\\mathbf{B}}{|\\mathbf{A}||\\mathbf{B}|}$."],
 steps=[D(f"\\mathbf{{A}}\\cdot\\mathbf{{B}}=(2)(-4)+(-3)(-2)+(1)(5)={AB}"),
        D(f"\\mathbf{{A}}\\times\\mathbf{{B}}={x_}[(-3)(5)-(1)(-2)]-{y_}[(2)(5)-(1)(-4)]+{z_}[(2)(-2)-(-3)(-4)]"),D(f"={vec(X)}"),
        D(f"|\\mathbf{{A}}|=\\sqrt{{14}}={tr(np.linalg.norm(A))},\\quad |\\mathbf{{B}}|=\\sqrt{{45}}={tr(np.linalg.norm(B))}"),
        D(f"\\theta=\\cos^{{-1}}\\frac{{{AB}}}{{{tr(np.linalg.norm(A))}\\cdot{tr(np.linalg.norm(B))}}}={deg(th)}")],
 answers=[{"label":r"\mathbf{A}\cdot\mathbf{B}","value":str(AB)},{"label":r"\mathbf{A}\times\mathbf{B}","value":vec(X)},{"label":r"\theta","value":deg(th)}])

P1=np.array([1,2,3]); P2=np.array([4,-2,3]); R=P2-P1
add(difficulty=1,title="Distance vector between two points",
 prompt="Find the distance vector from $P_1=(1,2,3)$ to $P_2=(4,-2,3)$, its length, and the unit vector pointing from $P_1$ to $P_2$.",
 hints=["$\\mathbf{R}_{12}=\\mathbf{R}_2-\\mathbf{R}_1$: second point minus first."],
 steps=[D(f"\\mathbf{{R}}_{{12}}=(4-1){x_}+(-2-2){y_}+(3-3){z_}={vec(R)}"),D(r"|\mathbf{R}_{12}|=\sqrt{9+16}=5"),D(f"\\hat{{\\mathbf{{R}}}}_{{12}}={vec(R/5)}")],
 answers=[{"label":r"\mathbf{R}_{12}","value":vec(R)},{"label":r"|\mathbf{R}_{12}|","value":"5"},{"label":r"\hat{\mathbf{R}}_{12}","value":vec(R/5)}],widget="coords")

x,y,z=3,4,5; r=math.hypot(x,y); ph=math.degrees(math.atan2(y,x)); Rr=math.sqrt(x*x+y*y+z*z); th=math.degrees(math.acos(z/Rr))
add(difficulty=1,title="One point in three coordinate systems",
 prompt="Express the point $P=(3,4,5)$ in cylindrical and spherical coordinates.",
 hints=["$r=\\sqrt{x^2+y^2}$, $\\phi=\\tan^{-1}(y/x)$.","$R=\\sqrt{x^2+y^2+z^2}$, $\\theta=\\cos^{-1}(z/R)$."],
 steps=[D(f"r=\\sqrt{{9+16}}=5,\\qquad \\phi=\\tan^{{-1}}\\frac{{4}}{{3}}={deg(ph)}"),"Cylindrical: $(5,\\ "+deg(ph)+",\\ 5)$.",D(f"R=\\sqrt{{9+16+25}}={tr(Rr)},\\qquad \\theta=\\cos^{{-1}}\\frac{{5}}{{{tr(Rr)}}}={deg(th)}"),"Spherical: $("+tr(Rr)+",\\ "+deg(th)+",\\ "+deg(ph)+")$."],
 answers=[{"label":r"(r,\phi,z)","value":f"(5,\\ {deg(ph)},\\ 5)"},{"label":r"(R,\theta,\phi)","value":f"({tr(Rr)},\\ {deg(th)},\\ {deg(ph)})"}],widget="coords")

R0,th0,ph0=4,60,150; t,p=math.radians(th0),math.radians(ph0); xs,ys,zs=R0*math.sin(t)*math.cos(p),R0*math.sin(t)*math.sin(p),R0*math.cos(t)
add(difficulty=1,title="Spherical to Cartesian",
 prompt="A point sits at $R=4$, $\\theta=60^\\circ$, $\\phi=150^\\circ$. Find its Cartesian coordinates and its cylindrical radius $r$.",
 hints=["$x=R\\sin\\theta\\cos\\phi$, $y=R\\sin\\theta\\sin\\phi$, $z=R\\cos\\theta$.","$r=R\\sin\\theta$."],
 steps=[D(f"x=4\\sin60^\\circ\\cos150^\\circ={tr(xs)}"),D(f"y=4\\sin60^\\circ\\sin150^\\circ={tr(ys)}"),D(f"z=4\\cos60^\\circ={tr(zs)}"),D(f"r=R\\sin\\theta={tr(R0*math.sin(t))}")],
 answers=[{"label":"(x,y,z)","value":f"({tr(xs)},\\ {tr(ys)},\\ {tr(zs)})"},{"label":"r","value":tr(R0*math.sin(t))}],widget="coords")

Av=np.array([3,-2,4]); phi=math.radians(45); Ar=Av[0]*math.cos(phi)+Av[1]*math.sin(phi); Ap=-Av[0]*math.sin(phi)+Av[1]*math.cos(phi)
add(difficulty=2,title="Vector components in cylindrical coordinates",
 prompt=f"Express $\\mathbf{{A}}={vec(Av)}$ in cylindrical components at the point $(1,1,2)$.",
 hints=["At this point $\\phi=45^\\circ$.","$A_r=A_x\\cos\\phi+A_y\\sin\\phi$ and $A_\\phi=-A_x\\sin\\phi+A_y\\cos\\phi$; $A_z$ is unchanged."],
 steps=[D(r"\phi=\tan^{-1}\frac{1}{1}=45^\circ"),D(f"A_r=3\\cos45^\\circ-2\\sin45^\\circ={tr(Ar)}"),D(f"A_\\phi=-3\\sin45^\\circ-2\\cos45^\\circ={tr(Ap)}"),D(f"\\mathbf{{A}}={vec([Ar,Ap,4],('\\mathbf{r}','\\boldsymbol{\\phi}','\\mathbf{z}'))}")],
 answers=[{"label":r"\mathbf{A}","value":vec([Ar,Ap,4],('\\mathbf{r}','\\boldsymbol{\\phi}','\\mathbf{z}'))}],widget="coords")

V=lambda x,y,z:x*x*y+3*y*z; p0=(1,2,-1); gV=np.array([2*1*2,1+3*(-1),3*2]); assert close(grad(V,p0),gV)
a=np.array([2,-1,2])/3; dd=gV@a
add(difficulty=2,title="Gradient and directional derivative",
 prompt="For $V=x^2y+3yz$, find $\\nabla V$ at $(1,2,-1)$, its magnitude, and the rate of change of $V$ in the direction of $\\hat{\\mathbf{x}}2-\\hat{\\mathbf{y}}+\\hat{\\mathbf{z}}2$.",
 hints=["$\\nabla V=\\hat{\\mathbf{x}}\\,2xy+\\hat{\\mathbf{y}}(x^2+3z)+\\hat{\\mathbf{z}}\\,3y$.","Normalize the direction vector before dotting it with $\\nabla V$."],
 steps=[D(f"\\nabla V={x_}\\,2xy+{y_}(x^2+3z)+{z_}\\,3y"),D(f"\\nabla V(1,2,-1)={vec(gV)}"),D(f"|\\nabla V|=\\sqrt{{16+4+36}}={tr(np.linalg.norm(gV))}"),D(r"\hat{\mathbf{a}}=\frac{\hat{\mathbf{x}}2-\hat{\mathbf{y}}+\hat{\mathbf{z}}2}{3}"),D(f"\\frac{{dV}}{{dl}}=\\nabla V\\cdot\\hat{{\\mathbf{{a}}}}=\\frac{{8+2+12}}{{3}}={tr(dd)}")],
 answers=[{"label":r"\nabla V","value":vec(gV)},{"label":r"|\nabla V|","value":tr(np.linalg.norm(gV))},{"label":r"dV/dl","value":tr(dd)}])

F=lambda x,y,z:(x*x*y,y*z,x*z*z); dv=2*1*1+1+2*1*1; assert close(div(F,(1,1,1)),dv)
add(difficulty=1,title="Divergence in Cartesian coordinates",
 prompt=f"Find $\\nabla\\cdot\\mathbf{{E}}$ for $\\mathbf{{E}}={x_}\\,x^2y+{y_}\\,yz+{z_}\\,xz^2$ and evaluate it at $(1,1,1)$.",
 hints=["Differentiate each component with respect to its own coordinate only."],
 steps=[D(r"\nabla\cdot\mathbf{E}=\frac{\partial(x^2y)}{\partial x}+\frac{\partial(yz)}{\partial y}+\frac{\partial(xz^2)}{\partial z}"),D(r"=2xy+z+2xz"),D(f"\\nabla\\cdot\\mathbf{{E}}(1,1,1)={dv}")],
 answers=[{"label":r"\nabla\cdot\mathbf{E}","value":"2xy+z+2xz"},{"label":r"\nabla\cdot\mathbf{E}(1,1,1)","value":str(dv)}],widget="divcurl")

F=lambda x,y,z:(math.hypot(x,y)*x,math.hypot(x,y)*y,2*z)   # r_hat r^2 + z_hat 2z
assert close(div(F,(2,0,1)),3*2+2)
add(difficulty=2,title="Divergence in cylindrical coordinates",
 prompt="Find $\\nabla\\cdot\\mathbf{A}$ for $\\mathbf{A}=\\hat{\\mathbf{r}}\\,r^2+\\hat{\\mathbf{z}}\\,2z$ and evaluate it at $r=2$.",
 hints=["$\\nabla\\cdot\\mathbf{A}=\\dfrac{1}{r}\\dfrac{\\partial(rA_r)}{\\partial r}+\\dfrac{1}{r}\\dfrac{\\partial A_\\phi}{\\partial\\phi}+\\dfrac{\\partial A_z}{\\partial z}$."],
 steps=[D(r"\frac{1}{r}\frac{\partial(r\cdot r^2)}{\partial r}=\frac{3r^2}{r}=3r"),D(r"\frac{\partial(2z)}{\partial z}=2"),D(r"\nabla\cdot\mathbf{A}=3r+2\ \Rightarrow\ 8\text{ at }r=2")],
 answers=[{"label":r"\nabla\cdot\mathbf{A}","value":"3r+2"},{"label":r"\nabla\cdot\mathbf{A}\,(r=2)","value":"8"}],widget="divcurl")

F=lambda x,y,z:(y*y,-x*z,3*x); p0=(1,2,3); cu=np.array([1-0,0-3,-3-2*2]); assert close(curl(F,p0),cu)
add(difficulty=2,title="Curl in Cartesian coordinates",
 prompt=f"Find $\\nabla\\times\\mathbf{{A}}$ for $\\mathbf{{A}}={x_}\\,y^2-{y_}\\,xz+{z_}\\,3x$ and evaluate it at $(1,2,3)$.",
 hints=["$(\\nabla\\times\\mathbf{A})_x=\\dfrac{\\partial A_z}{\\partial y}-\\dfrac{\\partial A_y}{\\partial z}$, and cycle $x\\to y\\to z$ for the others."],
 steps=[D(r"(\nabla\times\mathbf{A})_x=\frac{\partial(3x)}{\partial y}-\frac{\partial(-xz)}{\partial z}=x"),D(r"(\nabla\times\mathbf{A})_y=\frac{\partial(y^2)}{\partial z}-\frac{\partial(3x)}{\partial x}=-3"),D(r"(\nabla\times\mathbf{A})_z=\frac{\partial(-xz)}{\partial x}-\frac{\partial(y^2)}{\partial y}=-z-2y"),D(f"\\nabla\\times\\mathbf{{A}}(1,2,3)={vec(cu)}")],
 answers=[{"label":r"\nabla\times\mathbf{A}","value":f"{x_}\\,x-{y_}\\,3-{z_}(z+2y)"},{"label":r"\nabla\times\mathbf{A}(1,2,3)","value":vec(cu)}],widget="divcurl")

V=lambda x,y,z:x*x*y+z**3
lap=2*2+6*1
add(difficulty=1,title="Laplacian of a scalar",
 prompt="Find $\\nabla^2V$ for $V=x^2y+z^3$ and evaluate it at $(1,2,1)$.",
 hints=["Add the second partial derivatives in $x$, $y$ and $z$."],
 steps=[D(r"\frac{\partial^2V}{\partial x^2}=2y,\quad\frac{\partial^2V}{\partial y^2}=0,\quad\frac{\partial^2V}{\partial z^2}=6z"),D(f"\\nabla^2V=2y+6z={lap}\\ \\text{{at}}\\ (1,2,1)")],
 answers=[{"label":r"\nabla^2V","value":"2y+6z"},{"label":r"\nabla^2V(1,2,1)","value":str(lap)}])

a_,hgt=2,3; vol=2*math.pi*a_**2*hgt; side=a_*(2*math.pi*a_*hgt)
assert abs(vol-side)<1e-12
add(difficulty=2,title="Check the divergence theorem on a cylinder",
 prompt="For $\\mathbf{A}=\\hat{\\mathbf{r}}\\,r$, verify the divergence theorem over the cylinder $r\\le2$, $0\\le z\\le3$.",
 hints=["$\\nabla\\cdot\\mathbf{A}=\\dfrac{1}{r}\\dfrac{\\partial(r^2)}{\\partial r}=2$.","On the curved side $d\\mathbf{s}=\\hat{\\mathbf{r}}\\,r\\,d\\phi\\,dz$. On the flat ends $\\mathbf{A}\\cdot\\hat{\\mathbf{z}}=0$."],
 steps=[D(r"\int_V\nabla\cdot\mathbf{A}\,dV=2\cdot\pi(2)^2(3)=24\pi"),D(r"\oint_S\mathbf{A}\cdot d\mathbf{s}=\int_0^3\!\!\int_0^{2\pi}(2)(2)\,d\phi\,dz=24\pi"),f"Both sides are $24\\pi={tr(vol)}$. The ends add nothing because $\\mathbf{{A}}$ has no $z$ component."],
 answers=[{"label":r"\text{Both sides}","value":f"24\\pi={tr(vol)}"}],widget="divcurl")

a_=3; circ=2*math.pi*a_**2
add(difficulty=2,title="Check Stokes's theorem on a disk",
 prompt="For $\\mathbf{A}=\\hat{\\boldsymbol{\\phi}}\\,r$, verify Stokes's theorem on the disk $r\\le3$ in the $xy$-plane, with $d\\mathbf{s}$ along $+\\hat{\\mathbf{z}}$.",
 hints=["On the circle $r=3$, $d\\mathbf{l}=\\hat{\\boldsymbol{\\phi}}\\,r\\,d\\phi$.","$(\\nabla\\times\\mathbf{A})_z=\\dfrac{1}{r}\\dfrac{\\partial(rA_\\phi)}{\\partial r}$."],
 steps=[D(r"\oint_C\mathbf{A}\cdot d\mathbf{l}=\int_0^{2\pi}(3)(3)\,d\phi=18\pi"),D(r"\nabla\times\mathbf{A}=\hat{\mathbf{z}}\,\frac{1}{r}\frac{\partial(r^2)}{\partial r}=\hat{\mathbf{z}}\,2"),D(r"\int_S(\nabla\times\mathbf{A})\cdot d\mathbf{s}=2\cdot\pi(3)^2=18\pi"),f"Both sides are $18\\pi={tr(circ)}$."],
 answers=[{"label":r"\text{Both sides}","value":f"18\\pi={tr(circ)}"}],widget="divcurl")

F=lambda x,y,z:(y,x,0); assert close(curl(F,(0.3,0.7,0)),[0,0,0])
add(difficulty=2,title="Work along a path in a conservative field",
 prompt=f"Find $\\int\\mathbf{{F}}\\cdot d\\mathbf{{l}}$ for $\\mathbf{{F}}={x_}\\,y+{y_}\\,x$ from $(0,0,0)$ to $(1,2,0)$ along (a) the straight line $y=2x$ and (b) the parabola $y=2x^2$.",
 hints=["Check the curl first. If it is zero, the answer does not depend on the path.","$\\mathbf{F}=\\nabla(xy)$."],
 steps=[D(r"\nabla\times\mathbf{F}=\hat{\mathbf{z}}\left(\frac{\partial x}{\partial x}-\frac{\partial y}{\partial y}\right)=0"),"So $\\mathbf{F}=\\nabla V$ with $V=xy$, and"+D(r"\int\mathbf{F}\cdot d\mathbf{l}=V(1,2)-V(0,0)=2"),"Check (a) directly: $y=2x$, $dy=2dx$:"+D(r"\int_0^1(2x+2x)\,dx=2"),"Check (b): $y=2x^2$, $dy=4x\\,dx$:"+D(r"\int_0^1(2x^2+4x^2)\,dx=2")],
 answers=[{"label":r"\text{(a)}","value":"2"},{"label":r"\text{(b)}","value":"2"}],widget="divcurl")

area=2*math.pi*4*(1-math.cos(math.radians(60)))
add(difficulty=2,title="Area of a spherical cap",
 prompt="Find the area of the part of a sphere of radius $2\\ \\mathrm{m}$ with $0\\le\\theta\\le60^\\circ$.",
 hints=["$ds=R^2\\sin\\theta\\,d\\theta\\,d\\phi$."],
 steps=[D(r"A=\int_0^{2\pi}\!\!\int_0^{\pi/3}(2)^2\sin\theta\,d\theta\,d\phi"),D(r"=4(2\pi)\left[-\cos\theta\right]_0^{\pi/3}=8\pi\left(1-\tfrac12\right)=4\pi"),f"$A=4\\pi={tr(area)}\\ \\mathrm{{m^2}}$, a quarter of the full sphere."],
 answers=[{"label":"A","value":f"4\\pi={tr(area)}\\ \\mathrm{{m^2}}"}],widget="coords")

write_unit("vector-calculus","Vector calculus",C,G,P)
