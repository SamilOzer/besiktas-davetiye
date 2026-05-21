import sys, os

with open('qrcode.min.js', 'r', encoding='utf-8') as f:
    qr_lib = f.read()

with open('jsqr.min.js', 'r', encoding='utf-8') as f:
    jsqr_lib = f.read()

# ── INDEX.HTML ──────────────────────────────────────────────────────────────
index = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="BB Davetiye">
<meta name="theme-color" content="#00c4b8">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-512.png">
<title>Besiktas Belediyesi - Davetiye Yonetimi</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script>""" + qr_lib + """</script>
<style>
:root{--bg:#060e0e;--sf:#0d1c1c;--sf2:#122222;--brd:#1a3232;--ac:#00c4b8;--ac2:#00e8d8;--tx:#eefafa;--mt:#5a8888;--ok:#4ade80;--er:#f87171;--wn:#fb923c;--r:14px;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg);color:var(--tx);font-family:Inter,sans-serif;min-height:100vh;}
header{background:linear-gradient(135deg,#060e0e,#0d2020);border-bottom:1px solid var(--brd);padding:16px 20px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;}
.logo-area{display:flex;align-items:center;gap:12px;}
.logo-badge{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,var(--ac),#009990);display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:800;color:#fff;flex-shrink:0;}
.logo-text h1{font-size:15px;font-weight:700;}
.logo-text p{font-size:11px;color:var(--mt);margin-top:1px;}
.nav-links{display:flex;gap:8px;}
.nav-btn{padding:8px 14px;border-radius:9px;font-size:12px;font-weight:600;cursor:pointer;border:none;transition:all .2s;text-decoration:none;display:inline-flex;align-items:center;gap:6px;}
.nav-btn.primary{background:var(--ac);color:#fff;}.nav-btn.primary:hover{background:var(--ac2);transform:translateY(-1px);}
.nav-btn.secondary{background:var(--sf2);color:var(--tx);border:1px solid var(--brd);}.nav-btn.secondary:hover{border-color:var(--ac);color:var(--ac);}
.stats-bar{display:flex;gap:12px;padding:18px 20px 0;flex-wrap:wrap;}
.stat-card{background:var(--sf);border:1px solid var(--brd);border-radius:var(--r);padding:14px 16px;flex:1;min-width:110px;display:flex;align-items:center;gap:12px;transition:border-color .2s;}
.stat-card:hover{border-color:var(--ac);}
.stat-icon{font-size:22px;}.stat-val{font-size:22px;font-weight:800;}.stat-label{font-size:11px;color:var(--mt);margin-top:1px;}
main{padding:18px 20px;display:grid;grid-template-columns:360px 1fr;gap:18px;}
@media(max-width:780px){main{grid-template-columns:1fr;}}
.panel{background:var(--sf);border:1px solid var(--brd);border-radius:var(--r);padding:20px;}
.panel-title{font-size:14px;font-weight:700;margin-bottom:16px;display:flex;align-items:center;gap:8px;color:var(--ac);}
.field{margin-bottom:13px;}
.field label{display:block;font-size:10px;font-weight:600;color:var(--mt);margin-bottom:5px;text-transform:uppercase;letter-spacing:.5px;}
.field input,.field select{width:100%;padding:11px 13px;background:var(--bg);border:1px solid var(--brd);border-radius:9px;color:var(--tx);font-size:14px;font-family:Inter,sans-serif;transition:border-color .2s;outline:none;}
.field input:focus,.field select:focus{border-color:var(--ac);box-shadow:0 0 0 3px rgba(0,196,184,.1);}
.field select option{background:var(--sf2);}
.row2{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
.btn-create{width:100%;padding:13px;background:linear-gradient(135deg,var(--ac),#009990);color:#fff;border:none;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;transition:all .2s;margin-top:4px;display:flex;align-items:center;justify-content:center;gap:8px;}
.btn-create:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,196,184,.3);}
.btn-create:active{transform:scale(.97);}
/* QR POPUP */
.qr-preview{display:none;position:fixed;inset:0;background:rgba(0,0,0,.85);backdrop-filter:blur(8px);z-index:1000;align-items:center;justify-content:center;padding:16px;}
.qr-preview.open{display:flex;}
.qr-card{background:var(--sf);border:1px solid var(--brd);border-radius:20px;padding:24px 20px;max-width:360px;width:100%;text-align:center;animation:popIn .3s cubic-bezier(.34,1.56,.64,1);}
@keyframes popIn{from{opacity:0;transform:scale(.85)}to{opacity:1;transform:scale(1)}}
.qr-card h2{font-size:17px;font-weight:700;margin-bottom:3px;}
.qr-card .qr-sub{color:var(--mt);font-size:12px;margin-bottom:6px;}
.qr-role{display:inline-block;padding:3px 12px;border-radius:20px;background:rgba(0,196,184,.15);color:var(--ac);font-size:11px;font-weight:600;margin-bottom:14px;}
#qr-container{background:#fff;padding:12px;border-radius:10px;display:inline-block;margin-bottom:12px;min-width:180px;min-height:180px;}
#qr-container canvas,#qr-container img{display:block !important;}
.pin-box{background:var(--bg);border:1px solid var(--brd);border-radius:10px;padding:10px 14px;margin-bottom:14px;}
.pin-label{font-size:10px;color:var(--mt);text-transform:uppercase;letter-spacing:.5px;margin-bottom:4px;}
.pin-code{font-size:28px;font-weight:800;letter-spacing:8px;color:var(--ac);font-family:monospace;}
.qr-actions{display:flex;gap:8px;justify-content:center;}
.qr-btn{padding:10px 16px;border-radius:9px;font-size:13px;font-weight:600;cursor:pointer;border:none;transition:all .2s;}
.qr-btn.dl{background:var(--ac);color:#fff;}.qr-btn.dl:hover{background:var(--ac2);}
.qr-btn.cls{background:var(--sf2);color:var(--tx);border:1px solid var(--brd);}.qr-btn.cls:hover{border-color:var(--er);color:var(--er);}
/* LIST */
.list-panel{background:var(--sf);border:1px solid var(--brd);border-radius:var(--r);overflow:hidden;}
.list-header{padding:14px 18px;border-bottom:1px solid var(--brd);display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap;}
.list-header-title{font-size:14px;font-weight:700;}
.search-box{padding:8px 13px;background:var(--bg);border:1px solid var(--brd);border-radius:8px;color:var(--tx);font-size:13px;font-family:Inter,sans-serif;outline:none;width:190px;transition:border-color .2s;}
.search-box:focus{border-color:var(--ac);}
table{width:100%;border-collapse:collapse;}
th{padding:10px 14px;text-align:left;font-size:10px;font-weight:600;color:var(--mt);text-transform:uppercase;letter-spacing:.6px;border-bottom:1px solid var(--brd);background:var(--bg);}
td{padding:12px 14px;font-size:13px;border-bottom:1px solid rgba(26,50,50,.5);vertical-align:middle;}
tr:last-child td{border-bottom:none;}
tr:hover td{background:rgba(0,196,184,.03);}
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:20px;font-size:11px;font-weight:600;}
.badge.checked{background:rgba(74,222,128,.12);color:var(--ok);}.badge.pending{background:rgba(0,196,184,.12);color:var(--ac);}
.badge.vip{background:rgba(168,85,247,.15);color:#c084fc;}.badge.press{background:rgba(56,189,248,.15);color:#7dd3fc;}
.badge.staff{background:rgba(251,146,60,.15);color:var(--wn);}.badge.guest{background:rgba(148,163,184,.15);color:#94a3b8;}
.pin-cell{font-family:monospace;font-weight:700;color:var(--ac);letter-spacing:3px;font-size:14px;}
.action-btns{display:flex;gap:5px;}
.action-btn{padding:5px 10px;border-radius:7px;font-size:11px;font-weight:600;cursor:pointer;border:none;transition:all .2s;}
.action-btn.show{background:rgba(0,196,184,.1);color:var(--ac);border:1px solid rgba(0,196,184,.2);}.action-btn.show:hover{background:rgba(0,196,184,.2);}
.action-btn.del{background:rgba(248,113,113,.1);color:var(--er);border:1px solid rgba(248,113,113,.2);}.action-btn.del:hover{background:rgba(248,113,113,.2);}
.empty-state{text-align:center;padding:50px 20px;color:var(--mt);}
.empty-icon{font-size:44px;margin-bottom:10px;}
.toast{position:fixed;bottom:24px;right:16px;left:16px;max-width:360px;margin:0 auto;z-index:9999;background:var(--sf2);border:1px solid var(--brd);border-radius:11px;padding:12px 16px;font-size:13px;font-weight:500;display:flex;align-items:center;gap:8px;transform:translateY(100px);opacity:0;transition:all .4s cubic-bezier(.34,1.56,.64,1);}
.toast.show{transform:translateY(0);opacity:1;}.toast.success{border-color:var(--ok);}.toast.error{border-color:var(--er);}
@media(max-width:600px){th:nth-child(2),td:nth-child(2){display:none;}.stats-bar{gap:8px;}.stat-val{font-size:18px;}}
</style>
</head>
<body>
<header>
  <div class="logo-area">
    <div class="logo-badge">BB</div>
    <div class="logo-text">
      <h1>Besiktas Belediyesi</h1>
      <p>Davetiye Yonetim - Lansman 2026</p>
    </div>
  </div>
  <div class="nav-links">
    <a href="scanner.html" class="nav-btn secondary">&#128247; Kapi Kontrol</a>
    <button class="nav-btn primary" onclick="exportCSV()">&#8595; Disari Aktar</button>
  </div>
</header>

<div class="stats-bar">
  <div class="stat-card"><div class="stat-icon">&#127903;</div><div><div class="stat-val" id="stat-total">0</div><div class="stat-label">Toplam</div></div></div>
  <div class="stat-card"><div class="stat-icon">&#10003;</div><div><div class="stat-val" id="stat-checked">0</div><div class="stat-label">Girdi</div></div></div>
  <div class="stat-card"><div class="stat-icon">&#9200;</div><div><div class="stat-val" id="stat-pending">0</div><div class="stat-label">Bekliyor</div></div></div>
  <div class="stat-card"><div class="stat-icon">&#128081;</div><div><div class="stat-val" id="stat-vip">0</div><div class="stat-label">VIP</div></div></div>
</div>

<main>
  <div class="panel">
    <div class="panel-title">&#10022; Yeni Davetiye Olustur</div>
    <div class="field"><label>Ad Soyad *</label><input type="text" id="f-name" placeholder="Ornek: Ahmet Yilmaz"></div>
    <div class="field"><label>Kurum / Unvan</label><input type="text" id="f-org" placeholder="Ornek: Belediye Baskani"></div>
    <div class="row2">
      <div class="field"><label>Davetli Tipi</label>
        <select id="f-type">
          <option value="VIP">VIP</option>
          <option value="Basin">Basin</option>
          <option value="Personel">Personel</option>
          <option value="Misafir" selected>Misafir</option>
        </select>
      </div>
      <div class="field"><label>Masa / Alan</label><input type="text" id="f-seat" placeholder="A-12"></div>
    </div>
    <div class="field"><label>E-posta</label><input type="email" id="f-email" placeholder="ornek@mail.com"></div>
    <div class="field"><label>Telefon</label><input type="tel" id="f-phone" placeholder="+90 5XX XXX XX XX"></div>
    <button class="btn-create" onclick="createInvite()">&#10024; Davetiye Olustur ve QR Goster</button>
  </div>

  <div class="list-panel">
    <div class="list-header">
      <div class="list-header-title">&#128203; Davetli Listesi</div>
      <input class="search-box" type="text" placeholder="&#128269; Isim ara..." oninput="filterGuests(this.value)">
    </div>
    <div id="table-wrapper">
      <div class="empty-state"><div class="empty-icon">&#127914;</div><p>Henuz davetiye olusturulmadi.</p></div>
    </div>
  </div>
</main>

<div class="qr-preview" id="qr-popup">
  <div class="qr-card">
    <h2 id="qr-name">-</h2>
    <p class="qr-sub" id="qr-org">-</p>
    <span class="qr-role" id="qr-role">-</span><br>
    <div id="qr-container"></div>
    <div class="pin-box">
      <div class="pin-label">Manuel Giris PIN Kodu</div>
      <div class="pin-code" id="qr-pin">------</div>
    </div>
    <div class="qr-actions">
      <button class="qr-btn dl" onclick="downloadQR()">&#8595; Indir</button>
      <button class="qr-btn cls" onclick="closeQR()">&#10005; Kapat</button>
    </div>
  </div>
</div>
<div class="toast" id="toast"></div>

<script>
var guests=JSON.parse(localStorage.getItem('bb_guests')||'[]');
var currentQRGuest=null;
function save(){localStorage.setItem('bb_guests',JSON.stringify(guests));}
function uid(){return 'BBD-'+Date.now().toString(36).toUpperCase()+'-'+Math.random().toString(36).substr(2,4).toUpperCase();}
function genPin(){return Math.floor(100000+Math.random()*900000).toString();}
function typeClass(t){return({VIP:'vip',Basin:'press',Personel:'staff',Misafir:'guest'})[t]||'guest';}
function typeLabel(t){return({VIP:'VIP',Basin:'Basin',Personel:'Personel',Misafir:'Misafir'})[t]||t;}
function toast(msg,type){
  type=type||'success';
  var el=document.getElementById('toast');
  el.className='toast '+type;
  el.innerHTML=(type==='success'?'&#10003; ':'&#10007; ')+msg;
  el.classList.add('show');
  setTimeout(function(){el.classList.remove('show');},3000);
}
function updateStats(){
  document.getElementById('stat-total').textContent=guests.length;
  document.getElementById('stat-checked').textContent=guests.filter(function(g){return g.checked;}).length;
  document.getElementById('stat-pending').textContent=guests.filter(function(g){return !g.checked;}).length;
  document.getElementById('stat-vip').textContent=guests.filter(function(g){return g.type==='VIP';}).length;
}
function renderTable(list){
  var wrap=document.getElementById('table-wrapper');
  if(!list.length){wrap.innerHTML='<div class="empty-state"><div class="empty-icon">&#128269;</div><p>Sonuc bulunamadi.</p></div>';return;}
  var rows=list.map(function(g){return '<tr>'
    +'<td><strong>'+g.name+'</strong></td>'
    +'<td style="color:var(--mt)">'+(g.org||'-')+'</td>'
    +'<td><span class="badge '+typeClass(g.type)+'">'+typeLabel(g.type)+'</span></td>'
    +'<td class="pin-cell">'+(g.pin||'------')+'</td>'
    +'<td><span class="badge '+(g.checked?'checked':'pending')+'">'+(g.checked?'Girdi':'Bekliyor')+'</span></td>'
    +'<td><div class="action-btns">'
    +'<button class="action-btn show" onclick="showQR(\''+g.id+'\')">QR</button>'
    +'<button class="action-btn del" onclick="deleteGuest(\''+g.id+'\')">Sil</button>'
    +'</div></td></tr>';}).join('');
  wrap.innerHTML='<table><thead><tr><th>Ad Soyad</th><th>Kurum</th><th>Tip</th><th>PIN</th><th>Durum</th><th>Islem</th></tr></thead><tbody>'+rows+'</tbody></table>';
}
function filterGuests(q){
  var t=q.toLowerCase();
  renderTable(guests.filter(function(g){return g.name.toLowerCase().indexOf(t)>=0||(g.org||'').toLowerCase().indexOf(t)>=0;}));
}
function createInvite(){
  var name=document.getElementById('f-name').value.trim();
  if(!name){toast('Ad Soyad zorunludur!','error');return;}
  var guest={
    id:uid(),pin:genPin(),name:name,
    org:document.getElementById('f-org').value.trim(),
    type:document.getElementById('f-type').value,
    seat:document.getElementById('f-seat').value.trim(),
    email:document.getElementById('f-email').value.trim(),
    phone:document.getElementById('f-phone').value.trim(),
    checked:false,createdAt:new Date().toISOString()
  };
  guests.unshift(guest);save();updateStats();renderTable(guests);
  ['f-name','f-org','f-seat','f-email','f-phone'].forEach(function(id){document.getElementById(id).value='';});
  toast(name+' icin davetiye olusturuldu!');
  showQR(guest.id);
}
function showQR(id){
  var g=guests.find(function(x){return x.id===id;});
  if(!g)return;
  currentQRGuest=g;
  document.getElementById('qr-name').textContent=g.name;
  document.getElementById('qr-org').textContent=g.org||'Besiktas Belediyesi Lansman 2026';
  document.getElementById('qr-role').textContent=typeLabel(g.type);
  document.getElementById('qr-pin').textContent=g.pin||'------';
  var container=document.getElementById('qr-container');
  container.innerHTML='';
  try{
    var payload=JSON.stringify({id:g.id,pin:g.pin,name:g.name,type:g.type});
    new QRCode(container,{text:payload,width:180,height:180,colorDark:'#000000',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel.H});
  }catch(e){container.innerHTML='<p style="color:red;padding:20px;font-size:12px">QR Hatasi: '+e.message+'</p>';}
  document.getElementById('qr-popup').classList.add('open');
}
function closeQR(){document.getElementById('qr-popup').classList.remove('open');}
function downloadQR(){
  var canvas=document.querySelector('#qr-container canvas');
  if(!canvas){toast('QR gorsel bulunamadi','error');return;}
  var link=document.createElement('a');
  link.download='davetiye-'+(currentQRGuest?currentQRGuest.pin:'qr')+'.png';
  link.href=canvas.toDataURL();link.click();
}
function deleteGuest(id){
  if(!confirm('Bu davetiyeyi silmek istediginizden emin misiniz?'))return;
  guests=guests.filter(function(g){return g.id!==id;});
  save();updateStats();renderTable(guests);
  toast('Davetiye silindi.','error');
}
function exportCSV(){
  if(!guests.length){toast('Davetli yok.','error');return;}
  var h=['ID','PIN','Ad Soyad','Kurum','Tip','Masa','E-posta','Telefon','Durum','Tarih'];
  var r=guests.map(function(g){return[g.id,g.pin,g.name,g.org,g.type,g.seat,g.email,g.phone,g.checked?'Girdi':'Bekliyor',g.createdAt];});
  var csv=[h].concat(r).map(function(row){return row.map(function(c){return'"'+(c||'')+'"';}).join(',');}).join('\\n');
  var blob=new Blob(['\\ufeff'+csv],{type:'text/csv;charset=utf-8'});
  var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='davetliler.csv';a.click();
  toast('CSV indirildi!');
}
document.getElementById('qr-popup').addEventListener('click',function(e){if(e.target===this)closeQR();});
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').catch(function(){});}
updateStats();renderTable(guests);
</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index)
print('index.html written:', len(index), 'bytes')

# ── SCANNER.HTML ─────────────────────────────────────────────────────────────
scanner = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0,viewport-fit=cover">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Kapi Kontrol">
<meta name="theme-color" content="#060e0e">
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-512.png">
<title>Besiktas Belediyesi - Kapi Kontrol</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<script>""" + jsqr_lib + """</script>
<style>
:root{--bg:#060e0e;--sf:#0d1c1c;--sf2:#122222;--brd:#1a3232;--ac:#00c4b8;--ac2:#00e8d8;--tx:#eefafa;--mt:#5a8888;--ok:#4ade80;--er:#f87171;--wn:#fb923c;--r:14px;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg);color:var(--tx);font-family:Inter,sans-serif;min-height:100vh;display:flex;flex-direction:column;}
header{background:linear-gradient(135deg,#060e0e,#0d2020);border-bottom:1px solid var(--brd);padding:14px 18px;display:flex;align-items:center;justify-content:space-between;gap:8px;}
.logo-area{display:flex;align-items:center;gap:10px;}
.logo-badge{width:40px;height:40px;border-radius:9px;background:linear-gradient(135deg,var(--ac),#009990);display:flex;align-items:center;justify-content:center;font-size:15px;font-weight:800;color:#fff;flex-shrink:0;}
.logo-text h1{font-size:14px;font-weight:700;}.logo-text p{font-size:10px;color:var(--mt);margin-top:1px;}
.live-clock{font-size:17px;font-weight:700;color:var(--ac);font-variant-numeric:tabular-nums;}
.back-btn{padding:7px 12px;border-radius:8px;font-size:11px;font-weight:600;cursor:pointer;border:1px solid var(--brd);background:var(--sf2);color:var(--tx);text-decoration:none;transition:all .2s;white-space:nowrap;}
.back-btn:hover{border-color:var(--ac);color:var(--ac);}
.mini-stats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:14px 16px 0;}
.mini-stat{background:var(--sf);border:1px solid var(--brd);border-radius:10px;padding:12px;text-align:center;}
.mini-stat .val{font-size:22px;font-weight:800;}.mini-stat .lbl{font-size:10px;color:var(--mt);margin-top:2px;}
.mini-stat.ok .val{color:var(--ok);}.mini-stat.fail .val{color:var(--er);}.mini-stat.dup .val{color:var(--wn);}
.scan-area{padding:14px 16px;display:flex;flex-direction:column;gap:12px;flex:1;}
.scan-btn{width:100%;padding:22px 16px;background:linear-gradient(135deg,var(--ac),#009990);color:#fff;border:none;border-radius:14px;font-size:17px;font-weight:800;cursor:pointer;transition:all .2s;display:flex;align-items:center;justify-content:center;gap:10px;box-shadow:0 6px 20px rgba(0,196,184,.25);}
.scan-btn:active{transform:scale(.97);}
.scan-btn .icon{font-size:26px;}
#qr-file-input{display:none;}
.manual-section{background:var(--sf);border:1px solid var(--brd);border-radius:var(--r);padding:16px;}
.manual-title{font-size:11px;font-weight:700;color:var(--mt);text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px;}
.manual-row{display:flex;gap:8px;}
.manual-input{flex:1;padding:11px 13px;background:var(--bg);border:1px solid var(--brd);border-radius:9px;color:var(--tx);font-size:14px;font-family:Inter,sans-serif;outline:none;transition:border-color .2s;}
.manual-input:focus{border-color:var(--ac);}
.manual-go{padding:11px 16px;background:var(--ac);color:#fff;border:none;border-radius:9px;font-size:13px;font-weight:700;cursor:pointer;white-space:nowrap;transition:all .2s;}
.manual-go:active{background:var(--ac2);}
.result-card{background:var(--sf);border:2px solid var(--brd);border-radius:var(--r);padding:22px 18px;display:flex;flex-direction:column;align-items:center;text-align:center;min-height:170px;justify-content:center;transition:all .35s;}
.result-card.success{border-color:var(--ok);background:rgba(74,222,128,.05);}
.result-card.error{border-color:var(--er);background:rgba(248,113,113,.05);}
.result-card.warning{border-color:var(--wn);background:rgba(251,146,60,.05);}
.result-icon{font-size:50px;margin-bottom:10px;line-height:1;}
.result-status{font-size:19px;font-weight:800;margin-bottom:4px;}
.result-card.success .result-status{color:var(--ok);}.result-card.error .result-status{color:var(--er);}.result-card.warning .result-status{color:var(--wn);}
.result-desc{font-size:13px;color:var(--mt);}
.guest-info{margin-top:14px;width:100%;background:var(--bg);border-radius:9px;padding:12px;text-align:left;}
.guest-info-row{display:flex;justify-content:space-between;align-items:center;padding:5px 0;font-size:12px;border-bottom:1px solid var(--brd);}
.guest-info-row:last-child{border-bottom:none;}
.guest-info-row .lbl{color:var(--mt);}.guest-info-row .val{font-weight:600;}
.badge{display:inline-flex;align-items:center;gap:4px;padding:2px 9px;border-radius:20px;font-size:10px;font-weight:600;}
.badge.vip{background:rgba(168,85,247,.15);color:#c084fc;}.badge.press{background:rgba(56,189,248,.15);color:#7dd3fc;}
.badge.staff{background:rgba(251,146,60,.15);color:var(--wn);}.badge.guest{background:rgba(148,163,184,.15);color:#94a3b8;}
.log-panel{background:var(--sf);border:1px solid var(--brd);border-radius:var(--r);overflow:hidden;}
.log-header{padding:12px 16px;border-bottom:1px solid var(--brd);display:flex;justify-content:space-between;align-items:center;}
.log-header h3{font-size:12px;font-weight:700;}
.log-clear{font-size:11px;color:var(--mt);cursor:pointer;background:none;border:none;font-family:Inter,sans-serif;}
.log-clear:hover{color:var(--er);}
.log-list{max-height:200px;overflow-y:auto;}
.log-item{padding:9px 14px;border-bottom:1px solid rgba(26,50,50,.4);display:flex;align-items:center;gap:9px;font-size:12px;}
.log-item:last-child{border-bottom:none;}
.log-dot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}
.log-dot.ok{background:var(--ok);}.log-dot.fail{background:var(--er);}.log-dot.dup{background:var(--wn);}
.log-name{font-weight:600;flex:1;}.log-time{color:var(--mt);white-space:nowrap;}
.log-empty{text-align:center;padding:24px;color:var(--mt);font-size:12px;}
.processing{display:none;position:fixed;inset:0;background:rgba(0,0,0,.75);backdrop-filter:blur(4px);z-index:999;align-items:center;justify-content:center;flex-direction:column;gap:14px;}
.processing.show{display:flex;}
.spinner{width:44px;height:44px;border:4px solid var(--brd);border-top-color:var(--ac);border-radius:50%;animation:spin .8s linear infinite;}
@keyframes spin{to{transform:rotate(360deg)}}
.processing p{color:var(--tx);font-size:13px;font-weight:600;}
@keyframes pulse-border{0%,100%{box-shadow:0 0 0 0 rgba(0,196,184,.4)}50%{box-shadow:0 0 0 12px rgba(0,196,184,0)}}
.result-card.pulse{animation:pulse-border .8s ease-out;}
@media(min-width:700px){.scan-area{display:grid;grid-template-columns:1fr 1fr;padding:20px 30px;gap:16px;}.scan-area>*:first-child,.scan-area>*:nth-child(2){grid-column:1/3;}.mini-stats{padding:20px 30px 0;}}
</style>
</head>
<body>
<header>
  <div class="logo-area">
    <div class="logo-badge">BB</div>
    <div class="logo-text"><h1>Besiktas Belediyesi</h1><p>Kapi Kontrol - Lansman 2026</p></div>
  </div>
  <div class="live-clock" id="clock">--:--</div>
  <a href="index.html" class="back-btn">&#8592; Yonetim</a>
</header>

<div class="mini-stats">
  <div class="mini-stat ok"><div class="val" id="ms-ok">0</div><div class="lbl">&#10003; Kabul</div></div>
  <div class="mini-stat fail"><div class="val" id="ms-fail">0</div><div class="lbl">&#10007; Red</div></div>
  <div class="mini-stat dup"><div class="val" id="ms-dup">0</div><div class="lbl">&#9888; Mukerrer</div></div>
</div>

<div class="scan-area">
  <div class="result-card" id="result-card">
    <div class="result-icon" id="res-icon">&#128247;</div>
    <div class="result-status" id="res-status">Hazir</div>
    <div class="result-desc" id="res-desc">Asagidaki butona basin ve QR kodu fotograflayin.</div>
    <div id="guest-info-box"></div>
  </div>

  <button class="scan-btn" onclick="openCamera()">
    <span class="icon">&#128247;</span>
    Kamera ile QR Oku
  </button>
  <input type="file" id="qr-file-input" accept="image/*" capture="environment">

  <div class="manual-section">
    <div class="manual-title">PIN Kodu ile Manuel Giris</div>
    <div class="manual-row">
      <input class="manual-input" type="text" id="manual-id" placeholder="6 haneli PIN veya davetiye no" maxlength="30">
      <button class="manual-go" onclick="checkManual()">Kontrol</button>
    </div>
  </div>

  <div class="log-panel">
    <div class="log-header">
      <h3>&#128203; Giris Kaydi</h3>
      <button class="log-clear" onclick="clearLog()">Temizle</button>
    </div>
    <div class="log-list" id="log-list"><div class="log-empty">Henuz kayit yok.</div></div>
  </div>
</div>

<div class="processing" id="processing"><div class="spinner"></div><p>QR kod okunuyor...</p></div>

<script>
var counters={ok:0,fail:0,dup:0};
var sessionLog=[];
setInterval(function(){document.getElementById('clock').textContent=new Date().toLocaleTimeString('tr-TR');},1000);
function getGuests(){return JSON.parse(localStorage.getItem('bb_guests')||'[]');}
function saveGuests(list){localStorage.setItem('bb_guests',JSON.stringify(list));}
function typeClass(t){return({VIP:'vip',Basin:'press',Personel:'staff',Misafir:'guest'})[t]||'guest';}
function typeLabel(t){return({VIP:'VIP',Basin:'Basin',Personel:'Personel',Misafir:'Misafir'})[t]||t;}
function updateCounters(){
  document.getElementById('ms-ok').textContent=counters.ok;
  document.getElementById('ms-fail').textContent=counters.fail;
  document.getElementById('ms-dup').textContent=counters.dup;
}
function addLog(type,name,detail){
  sessionLog.unshift({type:type,name:name,detail:detail,time:new Date().toLocaleTimeString('tr-TR')});
  var list=document.getElementById('log-list');
  list.innerHTML=sessionLog.slice(0,30).map(function(l){
    return '<div class="log-item"><div class="log-dot '+l.type+'"></div><div class="log-name">'+l.name+'</div><span style="font-size:11px;color:var(--mt)">'+l.detail+'</span><span class="log-time">'+l.time+'</span></div>';
  }).join('');
}
function clearLog(){sessionLog=[];document.getElementById('log-list').innerHTML='<div class="log-empty">Henuz kayit yok.</div>';}
function showResult(type,icon,status,desc,guest){
  var card=document.getElementById('result-card');
  card.className='result-card '+type;
  document.getElementById('res-icon').textContent=icon;
  document.getElementById('res-status').textContent=status;
  document.getElementById('res-desc').textContent=desc;
  var box=document.getElementById('guest-info-box');
  if(guest){
    box.innerHTML='<div class="guest-info">'
      +'<div class="guest-info-row"><span class="lbl">Ad Soyad</span><span class="val">'+guest.name+'</span></div>'
      +'<div class="guest-info-row"><span class="lbl">Kurum</span><span class="val">'+(guest.org||'-')+'</span></div>'
      +'<div class="guest-info-row"><span class="lbl">Tip</span><span class="val"><span class="badge '+typeClass(guest.type)+'">'+typeLabel(guest.type)+'</span></span></div>'
      +'<div class="guest-info-row"><span class="lbl">Masa</span><span class="val">'+(guest.seat||'-')+'</span></div>'
      +'<div class="guest-info-row"><span class="lbl">PIN</span><span class="val" style="color:var(--ac);font-family:monospace;letter-spacing:3px">'+(guest.pin||'-')+'</span></div>'
      +'</div>';
  }else{box.innerHTML='';}
  setTimeout(function(){card.classList.add('pulse');setTimeout(function(){card.classList.remove('pulse');},1000);},10);
}
function processCode(raw){
  var payload;
  try{payload=JSON.parse(raw);}catch(e){payload={id:raw.trim(),pin:raw.trim()};}
  var id=payload.id;
  var pin=payload.pin||payload.id;
  var guests=getGuests();
  var idx=-1;
  // Try to find by ID first, then by PIN
  idx=guests.findIndex(function(g){return g.id===id;});
  if(idx===-1) idx=guests.findIndex(function(g){return g.pin===pin;});
  if(idx===-1){
    counters.fail++;updateCounters();
    showResult('error','\\u274C','GECERSIZ DAVETIYE','Bu QR kod veya PIN sistemde kayitli degil!',null);
    addLog('fail',id,'Kayitsiz');
    playBeep('fail');return;
  }
  var guest=guests[idx];
  if(guest.checked){
    counters.dup++;updateCounters();
    showResult('warning','\\u26A0\\uFE0F','MUKERRER GIRIS','Bu davetiye daha once kullanildi! ('+( guest.checkedAt||'-')+')',guest);
    addLog('dup',guest.name,'Daha once kullanildi');
    playBeep('dup');return;
  }
  guests[idx].checked=true;
  guests[idx].checkedAt=new Date().toLocaleTimeString('tr-TR');
  saveGuests(guests);
  counters.ok++;updateCounters();
  showResult('success','\\u2705','HOS GELDINIZ!','Giris onaylandi. Iyi eglenceler!',guest);
  addLog('ok',guest.name,typeLabel(guest.type));
  playBeep('ok');
}
function openCamera(){document.getElementById('qr-file-input').click();}
document.getElementById('qr-file-input').addEventListener('change',function(event){
  var file=event.target.files[0];
  if(!file)return;
  document.getElementById('processing').classList.add('show');
  var reader=new FileReader();
  reader.onload=function(e){
    var img=new Image();
    img.onload=function(){
      var canvas=document.createElement('canvas');
      var maxDim=1024;
      var w=img.width,h=img.height;
      if(w>maxDim||h>maxDim){if(w>h){h=Math.round(h*maxDim/w);w=maxDim;}else{w=Math.round(w*maxDim/h);h=maxDim;}}
      canvas.width=w;canvas.height=h;
      var ctx=canvas.getContext('2d');
      ctx.drawImage(img,0,0,w,h);
      var imageData=ctx.getImageData(0,0,w,h);
      document.getElementById('processing').classList.remove('show');
      var code=jsQR(imageData.data,imageData.width,imageData.height,{inversionAttempts:'dontInvert'});
      if(code){processCode(code.data);}
      else{showResult('error','\\uD83D\\uDD0D','QR Okunamadi','Fotografı net cekin, QR kod tamamen gorunsun.',null);}
      event.target.value='';
    };
    img.src=e.target.result;
  };
  reader.readAsDataURL(file);
});
function checkManual(){
  var val=document.getElementById('manual-id').value.trim();
  if(!val)return;
  processCode(val);
  document.getElementById('manual-id').value='';
}
function playBeep(type){
  try{
    var ctx=new(window.AudioContext||window.webkitAudioContext)();
    var osc=ctx.createOscillator();
    var gain=ctx.createGain();
    osc.connect(gain);gain.connect(ctx.destination);
    if(type==='ok'){osc.frequency.value=880;gain.gain.value=0.3;}
    else if(type==='fail'){osc.frequency.value=220;gain.gain.value=0.4;}
    else{osc.frequency.value=440;gain.gain.value=0.2;}
    osc.start();
    gain.gain.exponentialRampToValueAtTime(0.001,ctx.currentTime+0.4);
    osc.stop(ctx.currentTime+0.4);
  }catch(e){}
}
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').catch(function(){});}
</script>
</body>
</html>"""

with open('scanner.html', 'w', encoding='utf-8') as f:
    f.write(scanner)
print('scanner.html written:', len(scanner), 'bytes')
print('ALL DONE')
