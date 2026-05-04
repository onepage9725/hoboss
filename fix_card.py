import re
with open('index.html', 'r') as f:
    text = f.read()

text = re.sub(
    r'<div class="ml-1\.5 sm:ml-2 flex-grow bg-\[#cc0000\] rounded-lg sm:rounded-xl p-5 sm:p-8 flex flex-col justify-between min-h-\[140px\] shadow-\[0_10px_30px_rgba\(204,0,0,0\.3\)\]">\s*<div class="font-serif text-3xl sm:text-4xl text-white font-bold tracking-widest text-left">公司初心</div>\s*<div class="font-sans text-sm sm:text-base tracking-\[0\.2em\] text-white/90 text-right mt-12 sm:mt-16">创新、拼搏、担当、感恩、诚 信</div>\s*</div>',
    '<div class="ml-1.5 sm:ml-2 flex-grow bg-[#cc0000] rounded-lg sm:rounded-xl p-5 sm:p-6 flex flex-col justify-between shadow-[0_10px_30px_rgba(204,0,0,0.3)]">\n                                <div class="font-serif text-3xl sm:text-4xl text-white font-bold tracking-widest text-left">公司初心</div>\n                                <div class="font-sans text-sm sm:text-base tracking-[0.2em] text-white/90 text-right mt-6 sm:mt-8">创新、拼搏、担当、感恩、诚信</div>\n                            </div>',
    text
)

with open('index.html', 'w') as f:
    f.write(text)
