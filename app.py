from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>Dmail Python</title><script src="https://cdn.tailwindcss.com"></script><style>body{font-family:sans-serif;background:#eef2ff}.page{display:none}.page.active{display:block}</style></head>
<body>
<div class="flex"><aside class="w-[270px] bg-white min-h-screen p-4 fixed left-0 top-0 border-r"><div class="flex items-center gap-3 px-2 py-3"><div class="w-10 h-10 rounded-xl bg-gradient-to-br from-[#7c3aed] to-[#a78bfa] flex items-center justify-center text-white font-black">D</div><div><div class="font-bold text-[#4c1d95]">dmail</div><div class="text-[11px] text-gray-400">Python</div></div></div>
<nav class="mt-6 space-y-1 text-sm"><button onclick="showPage('beranda')" id="btn-beranda" class="w-full text-left px-4 py-2.5 rounded-xl bg-[#f5f3ff] font-bold text-[#4c1d95]">Beranda</button><button onclick="showPage('riwayat')" id="btn-riwayat" class="w-full text-left px-4 py-2.5 rounded-xl text-gray-500">Riwayat</button><button onclick="showPage('saldo')" id="btn-saldo" class="w-full text-left px-4 py-2.5 rounded-xl text-gray-500">Saldo</button><button onclick="showPage('profil')" id="btn-profil" class="w-full text-left px-4 py-2.5 rounded-xl text-gray-500">Profil</button></nav></aside>
<main class="ml-[270px] flex-1 p-6"><div id="beranda" class="page active"><div class="bg-white rounded-2xl p-4 flex justify-between"><h1 class="font-bold">Selamat malam, datpol</h1><span class="px-3 py-1 bg-[#f5f3ff] text-xs rounded-full text-[#4c1d95]">Python Online</span></div><div class="mt-4 bg-gradient-to-br from-[#7c3aed] to-[#4c1d95] rounded-[28px] p-6 text-white"><p class="text-xs">SALDO ANDA</p><h2 class="text-4xl font-bold mt-2">Rp0</h2></div></div><div id="riwayat" class="page"><div class="bg-white rounded-2xl p-6"><h2 class="font-bold">Riwayat</h2></div></div><div id="saldo" class="page"><div class="bg-white rounded-2xl p-6"><h2 class="font-bold">Saldo Rp0</h2></div></div><div id="profil" class="page"><div class="bg-white rounded-2xl p-6"><h2 class="font-bold">Profil datpol</h2></div></div></main></div>
<script>function showPage(id){document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('nav button').forEach(b=>b.className='w-full text-left px-4 py-2.5 rounded-xl text-gray-500');document.getElementById('btn-'+id).className='w-full text-left px-4 py-2.5 rounded-xl bg-[#f5f3ff] font-bold text-[#4c1d95]';}</script>
</body></html>
"""
@app.route("/")
def home(): return render_template_string(HTML)
if __name__=="__main__": app.run()
