with open('index.html', 'r') as f:
    text = f.read()

import re
old_html = r'''                        <!-- Bottom Bar -->
                        <div class="w-full relative mt-auto flex items-stretch pt-4">
                            <!-- Thin red line -->
                            <div class="w-1\.5 bg-\[#cc0000\] flex-shrink-0"></div>
                            <!-- Main red box -->
                            <div class="ml-1\.5 sm:ml-2 flex-grow bg-\[#cc0000\] rounded-lg sm:rounded-xl p-5 sm:p-8 flex flex-col justify-between min-h-\[140px\] shadow-\[0_10px_30px_rgba\(204,0,0,0\.3\)\]">
                                <div class="font-serif text-3xl sm:text-4xl text-white font-bold tracking-widest text-left">公司初心</div>
                                <div class="font-sans text-sm sm:text-base tracking-\[0\.2em\] text-white/90 text-right mt-12 sm:mt-16">创新、拼搏、担当、感恩、诚 信</div>
                            </div>
                        </div>'''

new_html = '''                        <!-- Bottom Bar -->
                        <div class="w-full relative mt-auto flex items-stretch pt-12">
                            <!-- Thin red line -->
                            <div class="w-2 bg-[#b5221d] flex-shrink-0"></div>
                            <!-- Main red box -->
                            <div class="ml-3 sm:ml-4 flex-grow bg-[#b5221d] rounded-2xl p-8 sm:p-10 flex flex-col justify-between h-[180px] sm:h-[220px] shadow-[0_20px_40px_rgba(181,34,29,0.3)]">
                                <div class="font-serif text-4xl sm:text-5xl text-white font-black tracking-widest text-left drop-shadow-sm">公司初心</div>
                                <div class="font-sans text-base sm:text-lg tracking-[0.25em] text-white/95 text-right mt-auto drop-shadow-sm">创新、拼搏、担当、感恩、诚信</div>
                            </div>
                        </div>'''

text = re.sub(old_html, new_html, text)

with open('index.html', 'w') as f:
    f.write(text)
