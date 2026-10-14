from flask import Flask,render_template_string as R,request as Q,redirect as D,session as S
from datetime import datetime as T
a=Flask(__name__);a.secret_key="zhen-v2"
u={"datpol":{"p":"123456","s":0,"e":"datpol@gmail.com","r":"admin","j":0}};e={"t":0,"h":[]};K=0.20
B="""<!DOCTYPE html><html><head><meta charset=UTF-8><meta name=viewport content=\"width=device-width,initial-scale=1.0\"><title>zhen</title><script src=https://cdn.tailwindcss.com></script><link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css></head><body class=\"flex min-h-screen\" style=background:#f0f7ff><div class=\"w-64 bg-white p-4 fixed h-full\"><b>zhen-email</b><div class=mt-8><a href=/beranda class=\"block p-2\">Beranda</a><a href=/jual class=\"block p-2\">Jual Email</a><a href=/saldo class=\"block p-2\">Saldo</a><a href=/admin class=\"block p-2 bg-yellow-50\">Admin Cuan</a></div></div><div class=\"flex-1 ml-64 p-6\"><div class=flex><h2>Halo, {{ u }}</h2><span class=\"ml-auto bg-white px-4 py-1 rounded-full\">Rp{{ s }}</span><a href=/logout class=\"ml-4 text-red-500\">Keluar</a></div>{{ c|safe }}</div></body></html>"""
def P(t,c):
 if 'u' not in S:return D('/login')
 x=S['u'];d=u.get(x,{"s":0,"r":"user"});return R(B,u=x,s=d['s'],c=c)
@a.route('/')
def i():
 if 'u' not in S:return D('/login')
 return D('/beranda')
@a.route('/login',methods=['GET','POST'])
def l():
 if Q.method=='POST':
  x=Q.form['username'].strip();p=Q.form['password'].strip()
  if x in u and u[x]['p']==p:S['u']=x;return D('/beranda')
  return '<script>alert("Salah!");location="/login"</script>'
 return '<div style=display:flex;justify-content:center;align-items:center;height:100vh;background:#f0f7ff><form method=POST style=background:white;padding:40px;border-radius:24px;width:380px><h2>zhen-email Login</h2><input name=username placeholder=Username required style=width:100%;padding:12px;border:1px solid #ddd;border-radius:12px;margin:12px 0><input name=password type=password placeholder=Password required style=width:100%;padding:12px;border:1px solid #ddd;border-radius:12px;margin-bottom:20px><button style=width:100%;padding:12px;background:#2563eb;color:white;border-radius:12px> Masuk </button><p style=text-align:center;margin-top:16px><a href=/register style=color:#2563eb>Daftar Custom</a></p><p style=text-align:center;font-size:11px;color:#aaa>admin: datpol / 123456</p></form></div>'
@a.route('/register',methods=['GET','POST'])
def r():
 if Q.method=='POST':
  x=Q.form['username'].strip();p=Q.form['password'].strip();m=Q.form['email'].strip()
  if x in u:return '<script>alert("Dipake");location="/register"</script>'
  u[x]={"p":p,"s":0,"e":m,"r":"user","j":0};S['u']=x;return D('/beranda')
 return '<div style=display:flex;justify-content:center;align-items:center;height:100vh;background:#f0f7ff><form method=POST style=background:white;padding:40px;border-radius:24px;width:380px><h2>Daftar Akun Baru</h2><input name=username placeholder="Username bebas" required style=width:100%;padding:12px;border:1px solid #ddd;border-radius:12px;margin:12px 0><input name=email placeholder=Email required style=width:100%;padding:12px;border:1px solid #ddd;border-radius:12px;margin-bottom:12px><input name=password type=password placeholder=Password required style=width:100%;padding:12px;border:1px solid #ddd;border-radius:12px;margin-bottom:20px><button style=width:100%;padding:12px;background:#2563eb;color:white;border-radius:12px>Daftar</button></form></div>'
@a.route('/beranda')
def b():
 if 'u' not in S:return D('/login')
 d=u[S['u']];c=f'<div class=bg-blue-600 style=background:linear-gradient(135deg,#3b82f6,#1d4ed8);padding:24px;border-radius:24px;color:white><p>TOTAL SALDO</p><h1 style=font-size:32px;font-weight:bold>Rp{d["s"]}</h1><div style=margin-top:16px><a href=/saldo style=background:white;color:#2563eb;padding:8px 20px;border-radius:999px>Tarik</a><a href=/jual style=background:rgba(255,255,255,0.2);color:white;padding:8px 20px;border-radius:999px;margin-left:8px>Jual Email</a></div></div><div class="bg-white rounded-2xl p-5 mt-6"><h3>Cuan Admin: Rp{e["t"]}</h3><p style=font-size:12px;color:#888>Setiap jual email Rp1000, kamu dapet Rp{int(1000*K)} (20%)</p></div>'
 return P("Beranda",c)
@a.route('/jual',methods=['GET','POST'])
def j():
 if 'u' not in S:return D('/login')
 if Q.method=='POST':
  h=int(Q.form.get('harga',1000));m=[x for x in Q.form.get('list_email','').split('\n') if x.strip()!=''];n=len(m) if m else 1;x=S['u'];t=h*n;ca=int(t*K);cu=t-ca;u[x]['s']+=cu;u[x]['j']+=n;e['t']+=ca;e['h'].append({"u":x,"n":n,"c":ca,"w":T.now().strftime("%d/%m %H:%M")});return f'<script>alert("Berhasil {n} email! Kamu Rp{cu} Admin Rp{ca}");location="/beranda"</script>'
 c='<div class="bg-white rounded-2xl p-6"><h3>Jual Email</h3><form method=POST><textarea name=list_email required placeholder="budi@gmail.com|pass" style=width:100%;height:160px;border:1px solid #ddd;border-radius:12px;padding:12px;margin-top:12px></textarea><input type=number name=harga value=1000 style=width:100%;padding:12px;border:1px solid #ddd;border-radius:999px;margin-top:12px><button style=width:100%;padding:12px;background:#2563eb;color:white;border-radius:999px;margin-top:12px>Jual & Cuan</button></form></div>'
 return P("Jual",c)
@a.route('/saldo')
def s():
 if 'u' not in S:return D('/login')
 return P("Saldo",'<div class="bg-white rounded-2xl p-6 max-w-md"><h3>Tarik ke DANA</h3><button onclick=alert("Dikirim!") style=width:100%;padding:12px;background:#2563eb;color:white;border-radius:999px;margin-top:12px>Ajukan</button></div>')
@a.route('/admin')
def ad():
 if 'u' not in S:return D('/login')
 if u[S['u']]['r']!='admin':return "Bukan admin! Login datpol / 123456"
 h="".join([f"<tr><td>{x['w']}</td><td>{x['u']}</td><td>{x['n']}</td><td>+Rp{x['c']}</td></tr>" for x in e['h']]);return P("Admin",f'<div class="bg-white rounded-2xl p-6"><h3>Admin Cuan: Rp{e["t"]}</h3><table>{h}</table></div>')
@a.route('/logout')
def o():S.pop('u',None);return D('/login')
