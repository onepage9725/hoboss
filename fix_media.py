import re

with open("index.html", "r") as f:
    content = f.read()

# Fix space typo in 公司初心
content = content.replace("感恩、诚 信", "感恩、诚信")

# Recreate the exact grid HTML to be safe
start_str = '<!-- Grid -->'
end_str = '</section>'

start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx)

new_grid = """<!-- Grid -->
                <div class="grid grid-cols-2 lg:grid-cols-4 bg-[#0a0a0a] border border-[#222] fade-up">
                    <!-- Item 1 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b border-r border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-4xl sm:text-5xl md:text-6xl text-primary font-serif font-black mb-4 sm:mb-6">2025</div>
                        <div class="text-sm sm:text-lg md:text-xl text-white font-bold mb-2 sm:mb-3 tracking-widest">光明日报</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider">企业勇上奖 · 头条报道</div>
                    </div>
                    <!-- Item 2 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b lg:border-r border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-4xl sm:text-5xl md:text-6xl text-primary font-serif font-black mb-4 sm:mb-6">2025</div>
                        <div class="text-sm sm:text-lg md:text-xl text-white font-bold mb-2 sm:mb-3 tracking-widest">星洲日报</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider">头条特别报道</div>
                    </div>
                    <!-- Item 3 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b border-r border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-4xl sm:text-5xl md:text-6xl text-primary font-serif font-black mb-4 sm:mb-6">2025</div>
                        <div class="text-sm sm:text-lg md:text-xl text-white font-bold mb-2 sm:mb-3 tracking-widest">星洲日报</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider">慈善公益专题报道</div>
                    </div>
                    <!-- Item 4 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-4xl sm:text-5xl md:text-6xl text-primary font-serif font-black mb-4 sm:mb-6">2025</div>
                        <div class="text-sm sm:text-lg md:text-xl text-white font-bold mb-2 sm:mb-3 tracking-widest">光明日报</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider">企业荣誉专题报道</div>
                    </div>
                    
                    <!-- Item 5 -->
                    <div class="bg-primary py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b lg:border-b-0 border-r border-[#0a0a0a] transition hover:brightness-110">
                        <div class="text-5xl sm:text-6xl md:text-7xl text-white font-serif font-black mb-3 sm:mb-4">2</div>
                        <div class="text-xs sm:text-sm md:text-base text-white tracking-widest font-bold mt-2">届慈善跑</div>
                    </div>
                    <!-- Item 6 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-b lg:border-b-0 lg:border-r border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-5xl sm:text-6xl md:text-7xl text-primary font-serif font-black mb-3 sm:mb-4">1</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider mt-2">项吉尼斯世界纪录</div>
                    </div>
                    <!-- Item 7 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-r border-[#0a0a0a] transition hover:bg-[#222]">
                        <div class="text-5xl sm:text-6xl md:text-7xl text-primary font-serif font-black mb-3 sm:mb-4">4</div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider mt-2">大主流媒体报道</div>
                    </div>
                    <!-- Item 8 -->
                    <div class="bg-[#1a1a1a] py-10 px-3 sm:py-14 sm:px-6 text-center flex flex-col justify-center border-transparent transition hover:bg-[#222]">
                        <div class="text-4xl sm:text-5xl md:text-6xl text-primary font-serif font-black mb-3 sm:mb-4">RM10<span class="text-2xl sm:text-3xl md:text-4xl">万+</span></div>
                        <div class="text-[10px] sm:text-xs md:text-sm text-gray-400 tracking-wider mt-2">慈善捐款总额</div>
                    </div>
                </div>
            </div>
        """

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_grid + content[end_idx:]
    with open("index.html", "w") as f:
        f.write(content)
    print("Replaced Media Grid gracefully")
else:
    print("Could not find boundaries")
