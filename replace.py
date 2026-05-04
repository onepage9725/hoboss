import re

with open("index.html", "r") as f:
    content = f.read()

old_str = """        <!-- CTA -->
        <section class="py-24 bg-red-gradient-dark text-white text-center">
            <div class="max-w-3xl mx-auto px-4 fade-up">
                <h2 class="text-4xl md:text-5xl font-serif font-black mb-6">携手HH 共创辉煌业</h2>
                <p class="text-xl text-white/80 tracking-widest mb-10">诚邀渠道 伙伴 · 供应链合作 · 项目联合开发</p>
                
                <div class="bg-white/10 backdrop-blur border border-white/20 p-8 rounded-xl max-w-lg mx-auto">
                    <div class="text-lg mb-2">联系人：HH小助理（商务合作部）</div>
                    <div class="text-xl font-bold font-serif mb-6 flex items-center justify-center">
                        <span class="mr-3">✉️</span> hhhealthgroup@gmail.com
                    </div>
                    <button class="bg-white text-primary font-bold px-8 py-3 rounded hover:bg-gray-100 transition shadow-lg w-full">
                        立即取得联系
                    </button>
                </div>
            </div>
        </section>
    </main>"""

new_str = """        <!-- CTA -->
        <section class="py-24 bg-[#cc0000] text-white text-center relative overflow-hidden" style="background-image: linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px); background-size: 30px 30px;">
            <div class="max-w-4xl mx-auto px-4 fade-up relative z-10 py-10 text-shadow-sm">
                <h2 class="text-5xl md:text-7xl font-serif font-black mb-6 tracking-widest leading-tight">
                    携手HH<br>共创辉煌业
                </h2>
                <p class="text-base md:text-lg text-white/90 tracking-[0.2em] mb-16">诚邀渠道伙伴 · 供应链合作 · 项目联合开发</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-3xl mx-auto items-center justify-center">
                    <div>
                        <div class="text-sm text-white/80 tracking-widest mb-2 font-light">联系人</div>
                        <div class="text-lg md:text-xl font-bold tracking-widest">HH 小助理（商务合作部）</div>
                    </div>
                    <div>
                        <div class="text-sm text-white/80 tracking-widest mb-2 font-light">合作咨询邮箱</div>
                        <div class="text-lg md:text-xl font-bold tracking-wider font-sans">hhhealthgroup@gmail.com</div>
                    </div>
                </div>
            </div>
        </section>
    </main>"""

# do a soft match
start_idx = content.find("<!-- CTA -->")
end_idx = content.find("</main>", start_idx) + len("</main>")

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_str + content[end_idx:]
    with open("index.html", "w") as f:
        f.write(new_content)
    print("Replaced successfully")
else:
    print("Could not find bounds")
