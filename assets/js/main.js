const y=document.getElementById('year');if(y)y.textContent=new Date().getFullYear();const m=document.querySelector('.menu'),n=document.querySelector('nav');if(m&&n)m.addEventListener('click',()=>{const open=n.classList.toggle('open');m.setAttribute('aria-expanded',String(open));});const f=document.getElementById('enquiry');if(f)f.addEventListener('submit',e=>{e.preventDefault();const d=new FormData(f);const lines=['Hello VOIZON, I would like to enquire.','Name: '+d.get('name'),'Business: '+(d.get('business')||'Not provided'),'Email: '+d.get('email'),'Phone: '+(d.get('phone')||'Not provided'),'Country / market: '+(d.get('country')||'Not provided'),'Preferred contact: '+(d.get('preferred')||'Not specified'),'Service: '+d.get('service'),'Budget / currency: '+(d.get('budget')||'Not decided'),'Details: '+d.get('message')];const url='https://wa.me/919567497943?text='+encodeURIComponent(lines.join('\n'));window.open(url,'_blank','noopener');});
const params=new URLSearchParams(window.location.search);const serviceParam=params.get('service');const serviceSelect=document.querySelector('#enquiry select[name="service"]');if(serviceParam&&serviceSelect){const match=[...serviceSelect.options].find(o=>o.text.toLowerCase()===serviceParam.toLowerCase());if(match)serviceSelect.value=match.value;else{const opt=document.createElement('option');opt.textContent=serviceParam;opt.value=serviceParam;opt.selected=true;serviceSelect.insertBefore(opt,serviceSelect.firstChild);}}

/* Persistent enquiry options: available on every website page */
(function(){
 const path=window.location.pathname.split('/').pop()||'index.html';
 const pageTitle=(document.querySelector('main .pagehero h1')?.innerText||document.title.split('|')[0]).replace(/\s+/g,' ').trim();
 const isService=/seo|ads|social-media|marketing|lead-generation|email|analytics|branding|design|video|presentation|web-development|ecommerce|web-applications|wordpress|ui-ux|it-consulting|automation|maintenance|strategy/i.test(path);
 const subject=isService?pageTitle:'a project';
 const box=document.createElement('div');
 box.className='floating-contact';
 box.setAttribute('aria-label','Contact VOIZON');
 const waText='Hello VOIZON, I would like to discuss '+subject+'. Please share the next steps.';
 const wa='https://wa.me/919567497943?text='+encodeURIComponent(waText);
 const contact='contact.html'+(isService?'?service='+encodeURIComponent(subject):'');
 box.innerHTML='<a class="contact-float" href="'+contact+'"><span class="float-icon">✉</span><span>Contact Us</span></a><a class="whatsapp-float" href="'+wa+'" target="_blank" rel="noopener noreferrer"><span class="float-icon">◉</span><span>WhatsApp Us</span></a>';
 document.body.appendChild(box);
})();
