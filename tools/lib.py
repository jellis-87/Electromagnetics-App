import numpy as np, math, cmath
c=299792458.0
def G(zl,z0): return (zl-z0)/(zl+z0)
def zin(zl,z0,l):
    if zl==np.inf: return -1j*z0/np.tan(2*np.pi*l)
    t=np.tan(2*np.pi*l); return z0*(zl+1j*z0*t)/(z0+1j*zl*t)
def vswr(g): g=abs(g); return (1+g)/(1-g)
def r(x,n=3):
    if x==0: return "0"
    d=n-int(math.floor(math.log10(abs(x))))-1
    v=round(x,max(d,0)); s=f"{v:.{max(d,0)}f}"
    return s.replace("-","−")
def fc(z,n=3):
    re,im=z.real,z.imag
    return f"{r(re,n)} {'−' if im<0 else '+'} j{r(abs(im),n)}"
def fp(z,n=3): return f"{r(abs(z),n)}∠{r(math.degrees(cmath.phase(z)),n)}°"
def eng(v,u,n=3):
    if v==0: return "0 "+u
    for k,p in [(1e9,'G'),(1e6,'M'),(1e3,'k'),(1,''),(1e-3,'m'),(1e-6,'µ'),(1e-9,'n'),(1e-12,'p')]:
        if abs(v)>=k*0.9995: return f"{r(v/k,n)} {p}{u}"
    return f"{v:.3e} {u}"
def roots(f,a=0,b=0.5,N=400001):
    d=np.linspace(a,b,N); v=f(d); i=np.where(np.diff(np.sign(v))!=0)[0]
    out=[]
    for k in i:
        lo,hi=d[k],d[k+1]
        for _ in range(60):
            m=(lo+hi)/2
            if np.sign(f(np.array([m]))[0])==np.sign(f(np.array([lo]))[0]): lo=m
            else: hi=m
        out.append((lo+hi)/2)
    return out
def shunt_stub(zl,z0):
    """returns list of (d, b, l_short, l_open) with normalized y(d)=1+jb"""
    gl=G(zl,z0)
    y=lambda d:(1-gl*np.exp(-4j*np.pi*d))/(1+gl*np.exp(-4j*np.pi*d))
    res=[]
    for d in roots(lambda d:y(d).real-1):
        b=y(d).imag
        ls=math.atan2(1,b)/(2*math.pi)
        lo=math.atan(-b)
        if lo<0: lo+=math.pi
        res.append((d,b,ls,lo/(2*math.pi)))
    return res
def series_pts(zl,z0):
    gl=G(zl,z0)
    z=lambda d:(1+gl*np.exp(-4j*np.pi*d))/(1-gl*np.exp(-4j*np.pi*d))
    return [(d,z(d).imag) for d in roots(lambda d:z(d).real-1)]
def bounce(Vs,Rs,Z0,RL,T,K=12):
    GL=1 if RL==np.inf else (RL-Z0)/(RL+Z0); Gs=(Rs-Z0)/(Rs+Z0); V1=Vs*Z0/(Rs+Z0)
    A=[V1*GL**math.ceil(k/2)*Gs**(k//2) for k in range(K)]
    return GL,Gs,V1,A
def vstep(A,x,t,T):
    v=0
    for k,a in enumerate(A):
        tk=k*T+(x*T if k%2==0 else (1-x)*T)
        if t>=tk-1e-15: v+=a
    return v

# ---- TeX formatters ----
def tr(x,n=3): return r(x,n).replace("−","-")
def tc(z,n=3):
    re_,im=z.real,z.imag
    return f"{tr(re_,n)} {'-' if im<0 else '+'} j{tr(abs(im),n)}"
def tp(z,n=3): return f"{tr(abs(z),n)}\\angle {tr(math.degrees(cmath.phase(z)),n)}^\\circ"
def teng(v,u,n=3):
    s=eng(v,u,n)
    num,unit=s.split(" ",1)
    unit=unit.replace("µ","\\mu ").replace("Ω","\\Omega")
    return f"{num.replace('−','-')}\\ \\mathrm{{{unit}}}"

# Upright text subscripts (Z_{in} -> Z_{\mathrm{in}}) in every string of a content tree

import re as _re
_SUBS=_re.compile(r'_\{(in|stub|max|min|av|load|avail|shunt|dB)\}')
def roman(o):
    if isinstance(o,str): return _SUBS.sub(lambda m:'_{\\mathrm{'+m.group(1)+'}}',o)
    if isinstance(o,list): return [roman(x) for x in o]
    if isinstance(o,dict): return {k:roman(v) for k,v in o.items()}
    return o
